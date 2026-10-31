import pytest
from app.models.farmer import FarmerProfile, Location, LandArea
from app.models.scheme import (
    EligibilityRule,
    RuleOperator,
    CriterionStatus,
    SchemeStatus,
    SchemeRecord
)
from app.services.eligibility_engine import EligibilityEngine
from app.services.scheme_source_service import SchemeSourceService

def test_rule_operator_greater_than():
    rule = EligibilityRule(
        rule_id="test_land_gt",
        description="Land must be greater than 0",
        field="land_area.value_acres",
        operator=RuleOperator.GREATER_THAN,
        expected_value=0,
        is_mandatory=True
    )
    profile = FarmerProfile(land_area=LandArea(value_acres=3.0))
    res = EligibilityEngine.evaluate_rule(rule, profile)
    assert res.status == CriterionStatus.SATISFIED

    # Zero land fails
    profile_zero = FarmerProfile(land_area=LandArea(value_acres=0.0))
    res_zero = EligibilityEngine.evaluate_rule(rule, profile_zero)
    assert res_zero.status == CriterionStatus.NOT_SATISFIED

def test_missing_field_returns_unknown():
    rule = EligibilityRule(
        rule_id="test_missing_district",
        description="District must be Shivamogga",
        field="location.district",
        operator=RuleOperator.EQUALS,
        expected_value="Shivamogga",
        is_mandatory=True
    )
    profile = FarmerProfile()  # district is None
    res = EligibilityEngine.evaluate_rule(rule, profile)
    # Must NOT silently pass or fail; must be UNKNOWN
    assert res.status == CriterionStatus.UNKNOWN

def test_pm_kisan_eligible_profile():
    pm_kisan = SchemeSourceService.get_by_id("pm-kisan")
    assert pm_kisan is not None

    profile = FarmerProfile(
        location=Location(state="Karnataka", district="Shivamogga"),
        land_area=LandArea(value=3.0, unit="acre", value_acres=3.0),
        crops=["arecanut"],
        ownership="owned",
        assistance_needs=["subsidy", "income_support"]
    )

    match_res = EligibilityEngine.evaluate_scheme(pm_kisan, profile)
    assert match_res.evaluation_status == SchemeStatus.POTENTIALLY_SUITABLE
    assert len(match_res.unsatisfied_rules) == 0

def test_pm_kisan_tenant_fails_mandatory_ownership():
    pm_kisan = SchemeSourceService.get_by_id("pm-kisan")
    assert pm_kisan is not None

    # Tenant farmer does not qualify for PM-KISAN central landholding requirement
    profile = FarmerProfile(
        location=Location(state="Karnataka", district="Shivamogga"),
        land_area=LandArea(value_acres=3.0),
        crops=["arecanut"],
        ownership="tenant"
    )

    match_res = EligibilityEngine.evaluate_scheme(pm_kisan, profile)
    assert match_res.evaluation_status == SchemeStatus.NOT_SUITABLE_BASED_ON_KNOWN_RULES
    failed_rule_ids = [r.rule_id for r in match_res.unsatisfied_rules]
    assert "pmk_ownership" in failed_rule_ids

def test_demonstration_scheme_identification():
    demo_scheme = SchemeSourceService.get_by_id("demo-micro-irrigation")
    assert demo_scheme is not None
    assert demo_scheme.scheme_type == "demonstration"
    assert "DEMONSTRATION ONLY" in demo_scheme.description

    # Test landholding threshold rule (> 12.5 acres fails)
    profile_large = FarmerProfile(
        location=Location(state="Karnataka", district="Hassan"),
        land_area=LandArea(value_acres=15.0),
        crops=["arecanut"]
    )
    res = EligibilityEngine.evaluate_scheme(demo_scheme, profile_large)
    assert res.evaluation_status == SchemeStatus.NOT_SUITABLE_BASED_ON_KNOWN_RULES
