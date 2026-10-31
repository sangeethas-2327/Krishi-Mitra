import pytest
from app.models.farmer import FarmerProfile, Location, LandArea, IrrigationInfo
from app.models.scheme import (
    EligibilityRule,
    RuleOperator,
    CriterionStatus,
    SchemeStatus,
    SchemeRecord
)
from app.services.eligibility_engine import EligibilityEngine
from app.services.scheme_source_service import SchemeSourceService
from app.services.scheme_comparison import SchemeComparisonService
from app.services.checklist_service import ChecklistService

def test_compound_or_rules_evaluation():
    # Rule with sub-rules evaluated with OR logic
    or_rule = EligibilityRule(
        rule_id="compound_or_crop",
        description="Either grows arecanut or coffee",
        field="crops",
        operator=RuleOperator.OR_CONDITIONS,
        expected_value=["arecanut", "coffee"],
        logical_operator="OR",
        sub_rules=[
            EligibilityRule(
                rule_id="sub_areca",
                description="Grows arecanut",
                field="crops",
                operator=RuleOperator.ANY_OF,
                expected_value=["arecanut"],
                is_mandatory=True
            ),
            EligibilityRule(
                rule_id="sub_coffee",
                description="Grows coffee",
                field="crops",
                operator=RuleOperator.ANY_OF,
                expected_value=["coffee"],
                is_mandatory=True
            )
        ]
    )

    # Profile with arecanut only -> should satisfy OR rule
    p1 = FarmerProfile(crops=["arecanut"])
    res1 = EligibilityEngine.evaluate_rule(or_rule, p1)
    assert res1.status == CriterionStatus.SATISFIED

    # Profile with paddy only -> should fail OR rule
    p2 = FarmerProfile(crops=["paddy"])
    res2 = EligibilityEngine.evaluate_rule(or_rule, p2)
    assert res2.status == CriterionStatus.NOT_SATISFIED

def test_between_operator():
    rule = EligibilityRule(
        rule_id="land_between_1_and_10",
        description="Land must be between 1.0 and 10.0 acres",
        field="land_area.value_acres",
        operator=RuleOperator.BETWEEN,
        expected_value=[1.0, 10.0],
        is_mandatory=True
    )

    p_in = FarmerProfile(land_area=LandArea(value_acres=5.0))
    res_in = EligibilityEngine.evaluate_rule(rule, p_in)
    assert res_in.status == CriterionStatus.SATISFIED

    p_out = FarmerProfile(land_area=LandArea(value_acres=15.0))
    res_out = EligibilityEngine.evaluate_rule(rule, p_out)
    assert res_out.status == CriterionStatus.NOT_SATISFIED

def test_unverified_rule_requires_official_verification():
    unverified_rule = EligibilityRule(
        rule_id="rule_caste_survey",
        description="Official revenue department caste certificate required",
        field="additional_details.caste_certificate_verified",
        operator=RuleOperator.EQUALS,
        expected_value=True,
        is_mandatory=True,
        verification_status="unverified"
    )

    p = FarmerProfile(additional_details={"caste_certificate_verified": True})
    res = EligibilityEngine.evaluate_rule(unverified_rule, p)
    assert res.status == CriterionStatus.NEEDS_VERIFICATION

def test_optional_rule_failure_does_not_block_qualification():
    scheme = SchemeSourceService.get_by_id("pm-kisan")
    assert scheme is not None

    # Farmer has 3 acres, owned, Karnataka, but is_income_tax_payer is unstated/unknown
    profile = FarmerProfile(
        location=Location(state="Karnataka", district="Shivamogga"),
        land_area=LandArea(value_acres=3.0),
        crops=["arecanut"],
        ownership="owned"
    )

    # Optional rule (exclusion check) unknown should NOT block POTENTIALLY_SUITABLE
    match_res = EligibilityEngine.evaluate_scheme(scheme, profile)
    assert match_res.evaluation_status == SchemeStatus.POTENTIALLY_SUITABLE

def test_scheme_comparison_service():
    resp = SchemeComparisonService.compare_schemes(["pm-kisan", "pmfby", "demo-micro-irrigation"])

    assert len(resp.schemes) == 3
    ids = [s.scheme_id for s in resp.schemes]
    assert "pm-kisan" in ids
    assert "pmfby" in ids
    assert "demo-micro-irrigation" in ids

    # Check matrix
    assert "purpose" in resp.comparison_matrix
    assert "required_documents" in resp.comparison_matrix
    assert "verification_status" in resp.comparison_matrix
    assert "pm-kisan" in resp.comparison_matrix["purpose"]

    # Factual disclaimer present
    assert len(resp.disclaimer) > 0
    assert len(resp.disclaimer_kn) > 0

def test_application_readiness_checklist_generation():
    pm_kisan = SchemeSourceService.get_by_id("pm-kisan")
    assert pm_kisan is not None

    checklist = ChecklistService.generate_checklist(pm_kisan)
    assert checklist.scheme_id == "pm-kisan"
    assert len(checklist.items) >= 4

    # Check mandatory items
    mandatory_items = [it for it in checklist.items if it.is_mandatory]
    assert len(mandatory_items) >= 4

    # Prerequisite item present
    has_ekyc = any(it.item_id == "pre_ekyc" for it in checklist.items)
    assert has_ekyc is True

    # Disclaimer on no actual application submission
    assert "does NOT submit applications" in checklist.disclaimer

def test_real_vs_fictional_scheme_separation():
    schemes = SchemeSourceService.get_all()
    real_schemes = [s for s in schemes if s.scheme_type == "real"]
    demo_schemes = [s for s in schemes if s.scheme_type == "demonstration"]

    assert len(real_schemes) >= 50
    real_ids = set(s.id for s in real_schemes)
    assert "pm-kisan" in real_ids
    assert "pmfby" in real_ids

    assert len(demo_schemes) == 3
    demo_ids = set(s.id for s in demo_schemes)
    assert "demo-micro-irrigation" in demo_ids
    assert "demo-equipment-assistance" in demo_ids
    assert "demo-soil-improvement" in demo_ids

    # Real schemes MUST have official portals and verified status
    for rs in real_schemes:
        assert rs.official_source_url is not None
        assert rs.verification_status == "verified"
        assert rs.last_verified_at is not None

    # Demo schemes MUST be clearly flagged
    for ds in demo_schemes:
        assert ds.official_source_url is None
        assert ds.verification_status == "synthetic"
        assert "DEMONSTRATION ONLY" in ds.description

