from typing import Optional, List, Dict, Any, Union
from enum import Enum
from pydantic import BaseModel, Field

class RuleOperator(str, Enum):
    EQUALS = "equals"
    NOT_EQUALS = "not_equals"
    IN = "in"
    NOT_IN = "not_in"
    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    GREATER_THAN_OR_EQUAL = "greater_than_or_equal"
    LESS_THAN_OR_EQUAL = "less_than_or_equal"
    BETWEEN = "between"
    EXISTS = "exists"
    ALL_OF = "all_of"
    ANY_OF = "any_of"
    OR_CONDITIONS = "or_conditions"

class CriterionStatus(str, Enum):
    SATISFIED = "SATISFIED"
    NOT_SATISFIED = "NOT_SATISFIED"
    UNKNOWN = "UNKNOWN"
    NEEDS_VERIFICATION = "NEEDS_VERIFICATION"

class SchemeStatus(str, Enum):
    POTENTIALLY_SUITABLE = "POTENTIALLY_SUITABLE"
    NOT_SUITABLE_BASED_ON_KNOWN_RULES = "NOT_SUITABLE_BASED_ON_KNOWN_RULES"
    INSUFFICIENT_INFORMATION = "INSUFFICIENT_INFORMATION"
    REQUIRES_OFFICIAL_VERIFICATION = "REQUIRES_OFFICIAL_VERIFICATION"

class EligibilityRule(BaseModel):
    rule_id: str
    description: str
    description_kn: Optional[str] = None
    field: str
    operator: RuleOperator
    expected_value: Any
    is_mandatory: bool = True
    source_reference: Optional[str] = None
    verification_status: str = "verified"  # verified, unverified, synthetic
    clarification_question: Optional[str] = None
    clarification_question_kn: Optional[str] = None
    why_needed: Optional[str] = None
    why_needed_kn: Optional[str] = None
    sub_rules: Optional[List['EligibilityRule']] = None
    logical_operator: str = "AND"  # "AND" or "OR"

class RuleEvaluationResult(BaseModel):
    rule_id: str
    description: str
    description_kn: Optional[str] = None
    field: str
    status: CriterionStatus
    expected_value: Any
    actual_value: Any
    is_mandatory: bool
    source_reference: Optional[str] = None
    reason: str
    reason_kn: Optional[str] = None
    clarification_question: Optional[str] = None
    clarification_question_kn: Optional[str] = None
    why_needed: Optional[str] = None
    why_needed_kn: Optional[str] = None
    sub_evaluations: Optional[List['RuleEvaluationResult']] = None

class SchemeRecord(BaseModel):
    id: str
    name: str
    name_kn: Optional[str] = None
    official_abbreviation: Optional[str] = None
    government_level: str = "central"  # central, karnataka
    scheme_type: str  # real, demonstration
    category: str
    category_kn: Optional[str] = None
    assistance_type: Optional[str] = None
    status_label: Optional[str] = None
    status_label_kn: Optional[str] = None
    description: str
    description_kn: Optional[str] = None
    benefits: List[str] = Field(default_factory=list)
    benefits_kn: List[str] = Field(default_factory=list)
    eligibility_rules: List[EligibilityRule] = Field(default_factory=list)
    required_documents: List[str] = Field(default_factory=list)
    required_documents_kn: List[str] = Field(default_factory=list)
    optional_documents: List[str] = Field(default_factory=list)
    optional_documents_kn: List[str] = Field(default_factory=list)
    application_steps: List[str] = Field(default_factory=list)
    application_steps_kn: List[str] = Field(default_factory=list)
    official_source_url: Optional[str] = None
    issuing_authority: Optional[str] = None
    verification_authority: Optional[str] = None
    last_verified_at: Optional[str] = None
    verification_status: str = "verified"  # verified, unverified, synthetic
    applicable_locations: List[str] = Field(default_factory=list)
    supported_crops: List[str] = Field(default_factory=list)
    notes: List[str] = Field(default_factory=list)
    notes_kn: List[str] = Field(default_factory=list)

class SchemeMatchResult(BaseModel):
    scheme: SchemeRecord
    evaluation_status: SchemeStatus
    score: float = 0.0
    satisfied_rules: List[RuleEvaluationResult] = Field(default_factory=list)
    unsatisfied_rules: List[RuleEvaluationResult] = Field(default_factory=list)
    unknown_rules: List[RuleEvaluationResult] = Field(default_factory=list)
    needs_verification_rules: List[RuleEvaluationResult] = Field(default_factory=list)
    match_reason: str
    match_reason_kn: Optional[str] = None
    next_clarification_question: Optional[str] = None
    next_clarification_question_kn: Optional[str] = None

# Scheme Comparison Models
class SchemeComparisonItem(BaseModel):
    scheme_id: str
    name: str
    name_kn: Optional[str] = None
    government_level: Optional[str] = "central"
    scheme_type: str
    category: str
    category_kn: Optional[str] = None
    assistance_type: Optional[str] = None
    purpose: str
    purpose_kn: Optional[str] = None
    target_beneficiaries: str
    target_beneficiaries_kn: Optional[str] = None
    key_eligibility: List[str]
    key_eligibility_kn: List[str]
    benefits_summary: List[str]
    benefits_summary_kn: List[str]
    required_documents: List[str]
    required_documents_kn: List[str]
    application_mode: str
    application_mode_kn: Optional[str] = None
    official_url: Optional[str] = None
    verification_status: str
    status_label: Optional[str] = None
    status_label_kn: Optional[str] = None
    application_steps: List[str] = Field(default_factory=list)
    application_steps_kn: List[str] = Field(default_factory=list)
    issuing_authority: Optional[str] = None
    verification_authority: Optional[str] = None

class SchemeComparisonResponse(BaseModel):
    schemes: List[SchemeComparisonItem]
    comparison_matrix: Dict[str, Dict[str, Any]]
    disclaimer: str
    disclaimer_kn: str

# Readiness Checklist Models
class ChecklistItem(BaseModel):
    item_id: str
    title: str
    title_kn: Optional[str] = None
    category: str  # "document", "prerequisite", "official_check"
    is_mandatory: bool = True
    is_completed: bool = False
    evidence_found: Optional[str] = None
    help_text: Optional[str] = None
    help_text_kn: Optional[str] = None

class SchemeReadinessChecklist(BaseModel):
    scheme_id: str
    scheme_name: str
    scheme_name_kn: Optional[str] = None
    scheme_type: str
    official_source_url: Optional[str] = None
    completion_percentage: int
    mandatory_ready_count: int
    mandatory_total_count: int
    items: List[ChecklistItem]
    next_steps: List[str]
    next_steps_kn: List[str]
    disclaimer: str
    disclaimer_kn: str
