import logging
from typing import Any, Tuple, Optional, List, Dict
from ..models.farmer import FarmerProfile
from ..models.scheme import (
    EligibilityRule,
    RuleEvaluationResult,
    CriterionStatus,
    SchemeStatus,
    SchemeRecord,
    SchemeMatchResult,
    RuleOperator
)

logger = logging.getLogger(__name__)

def get_nested_field_value(data: Dict[str, Any], path: str) -> Tuple[bool, Any]:
    """
    Safely retrieves a value from a nested dictionary using dot notation (e.g. 'location.district').
    Returns (found, value).
    """
    parts = path.split(".")
    current = data
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif hasattr(current, part):
            current = getattr(current, part)
        else:
            return False, None
    return True, current

class EligibilityEngine:
    """
    Transparent, deterministic, auditable rule-evaluation engine for Krishi Mitra Phase 2.
    Supports equality, inequality, numeric boundaries, allowed values, AND/OR composite logic,
    missing field detection, and official verification flags.
    Zero use of arbitrary eval(). All logic is deterministic and reproducible.
    """

    @classmethod
    def evaluate_rule(cls, rule: EligibilityRule, profile: FarmerProfile) -> RuleEvaluationResult:
        # Handle composite sub-rules (OR / AND compound rules)
        if rule.sub_rules and len(rule.sub_rules) > 0:
            sub_results: List[RuleEvaluationResult] = []
            for sub_r in rule.sub_rules:
                sub_results.append(cls.evaluate_rule(sub_r, profile))

            if rule.logical_operator == "OR" or rule.operator == RuleOperator.OR_CONDITIONS:
                # OR logic: Satisfied if any sub-rule is satisfied
                any_sat = any(r.status == CriterionStatus.SATISFIED for r in sub_results)
                all_unsat = all(r.status == CriterionStatus.NOT_SATISFIED for r in sub_results)
                any_unknown = any(r.status == CriterionStatus.UNKNOWN for r in sub_results)
                any_verify = any(r.status == CriterionStatus.NEEDS_VERIFICATION for r in sub_results)

                if any_sat:
                    status = CriterionStatus.SATISFIED
                    reason = "At least one condition in the alternate criteria was satisfied."
                    reason_kn = "ಪರ್ಯಾಯ ಮಾನದಂಡಗಳಲ್ಲಿ ಕನಿಷ್ಠ ಒಂದು ಷರತ್ತು ಪೂರೈಸಲಾಗಿದೆ."
                elif all_unsat:
                    status = CriterionStatus.NOT_SATISFIED
                    reason = "None of the alternative conditions were satisfied."
                    reason_kn = "ಯಾವುದೇ ಪರ್ಯಾಯ ಮಾನದಂಡಗಳು ಪೂರೈಸಲಾಗಿಲ್ಲ."
                elif any_unknown:
                    status = CriterionStatus.UNKNOWN
                    reason = "Information is missing for evaluating alternative conditions."
                    reason_kn = "ಪರ್ಯಾಯ ಮಾನದಂಡಗಳ ಪರಿಶೀಲನೆಗೆ ಅಗತ್ಯ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ."
                else:
                    status = CriterionStatus.NEEDS_VERIFICATION
                    reason = "Requires official verification of alternative conditions."
                    reason_kn = "ಪರ್ಯಾಯ ಮಾನದಂಡಗಳ ಅಧಿಕೃತ ಪರಿಶೀಲನೆ ಅಗತ್ಯವಿದೆ."

            else:
                # AND logic (default): Satisfied if all sub-rules are satisfied
                all_sat = all(r.status == CriterionStatus.SATISFIED for r in sub_results)
                any_unsat = any(r.status == CriterionStatus.NOT_SATISFIED for r in sub_results)
                any_unknown = any(r.status == CriterionStatus.UNKNOWN for r in sub_results)

                if any_unsat:
                    status = CriterionStatus.NOT_SATISFIED
                    reason = "At least one required condition in the group was not satisfied."
                    reason_kn = "ಗುಂಪಿನ ಕನಿಷ್ಠ ಒಂದು ಕಡ್ಡಾಯ ಷರತ್ತು ಪೂರೈಸಲಾಗಿಲ್ಲ."
                elif any_unknown:
                    status = CriterionStatus.UNKNOWN
                    reason = "Missing information for some conditions in the group."
                    reason_kn = "ಗುಂಪಿನ ಕೆಲವು ಮಾನದಂಡಗಳಿಗೆ ಮಾಹಿತಿ ಅಗತ್ಯವಿದೆ."
                elif all_sat:
                    status = CriterionStatus.SATISFIED
                    reason = "All required conditions in the group were satisfied."
                    reason_kn = "ಗುಂಪಿನ ಎಲ್ಲಾ ಕಡ್ಡಾಯ ಮಾನದಂಡಗಳು ಪೂರೈಸಲಾಗಿವೆ."
                else:
                    status = CriterionStatus.NEEDS_VERIFICATION
                    reason = "Requires official verification for conditions in the group."
                    reason_kn = "ಗುಂಪಿನ ಮಾನದಂಡಗಳ ಅಧಿಕೃತ ಪರಿಶೀಲನೆ ಬಾಕಿ ಇದೆ."

            return RuleEvaluationResult(
                rule_id=rule.rule_id,
                description=rule.description,
                description_kn=rule.description_kn,
                field=rule.field,
                status=status,
                expected_value=rule.expected_value,
                actual_value=[r.actual_value for r in sub_results],
                is_mandatory=rule.is_mandatory,
                source_reference=rule.source_reference,
                reason=reason,
                reason_kn=reason_kn,
                clarification_question=rule.clarification_question,
                clarification_question_kn=rule.clarification_question_kn,
                why_needed=rule.why_needed,
                why_needed_kn=rule.why_needed_kn,
                sub_evaluations=sub_results
            )

        # Standard atomic rule evaluation
        profile_dict = profile.model_dump()
        found, actual_value = get_nested_field_value(profile_dict, rule.field)

        # 1. Missing / Unknown Value Check
        if not found or actual_value is None or actual_value == [] or actual_value == "":
            return RuleEvaluationResult(
                rule_id=rule.rule_id,
                description=rule.description,
                description_kn=rule.description_kn,
                field=rule.field,
                status=CriterionStatus.UNKNOWN,
                expected_value=rule.expected_value,
                actual_value=None,
                is_mandatory=rule.is_mandatory,
                source_reference=rule.source_reference,
                reason=f"Field '{rule.field}' is not yet provided by the farmer.",
                reason_kn=f"'{rule.description_kn or rule.field}' ಮಾಹಿತಿಯನ್ನು ಇನ್ನೂ ಒದಗಿಸಿಲ್ಲ.",
                clarification_question=rule.clarification_question,
                clarification_question_kn=rule.clarification_question_kn,
                why_needed=rule.why_needed,
                why_needed_kn=rule.why_needed_kn
            )

        # 2. Check if rule is unverified or requires official verification
        if rule.verification_status == "unverified":
            return RuleEvaluationResult(
                rule_id=rule.rule_id,
                description=rule.description,
                description_kn=rule.description_kn,
                field=rule.field,
                status=CriterionStatus.NEEDS_VERIFICATION,
                expected_value=rule.expected_value,
                actual_value=actual_value,
                is_mandatory=rule.is_mandatory,
                source_reference=rule.source_reference,
                reason=f"This criterion requires official offline document verification.",
                reason_kn="ಈ ಮಾನದಂಡಕ್ಕೆ ಅಧಿಕೃತ ಇಲಾಖಾ ದಾಖಲೆಗಳ ಪರಿಶೀಲನೆ ಅಗತ್ಯವಿದೆ.",
                clarification_question=rule.clarification_question,
                clarification_question_kn=rule.clarification_question_kn,
                why_needed=rule.why_needed,
                why_needed_kn=rule.why_needed_kn
            )

        # 3. Deterministic Operator evaluation
        op = rule.operator
        exp = rule.expected_value
        is_satisfied = False
        reason = ""
        reason_kn = ""

        try:
            if op == RuleOperator.EQUALS:
                if isinstance(actual_value, str) and isinstance(exp, str):
                    is_satisfied = actual_value.strip().lower() == exp.strip().lower()
                else:
                    is_satisfied = actual_value == exp
                reason = f"Value '{actual_value}' {'matches' if is_satisfied else 'does not match'} required '{exp}'."
                reason_kn = f"ಮೌಲ್ಯ '{actual_value}' ಅಗತ್ಯವಿರುವ '{exp}' ಗೆ {'ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ' if is_satisfied else 'ಹೊಂದಿಕೆಯಾಗುವುದಿಲ್ಲ'}."

            elif op == RuleOperator.NOT_EQUALS:
                if isinstance(actual_value, str) and isinstance(exp, str):
                    is_satisfied = actual_value.strip().lower() != exp.strip().lower()
                else:
                    is_satisfied = actual_value != exp
                reason = f"Value '{actual_value}' {'does not equal' if is_satisfied else 'equals excluded'} '{exp}'."
                reason_kn = f"ಮೌಲ್ಯ '{actual_value}' ಹೊರಗಿಡಲಾದ '{exp}' ಗೆ {'ಹೊಂದಿಕೆಯಾಗುವುದಿಲ್ಲ' if is_satisfied else 'ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ'}."

            elif op == RuleOperator.IN:
                if isinstance(exp, list):
                    lowered_exp = [str(x).strip().lower() for x in exp]
                    is_satisfied = str(actual_value).strip().lower() in lowered_exp
                    reason = f"Value '{actual_value}' {'is allowed' if is_satisfied else 'is not in allowed list'}."
                    reason_kn = f"ಮೌಲ್ಯ '{actual_value}' ಅನುಮೋದಿತ ಪಟ್ಟಿಯಲ್ಲಿದೆ." if is_satisfied else f"ಮೌಲ್ಯ '{actual_value}' ಅನುಮೋದಿತ ಪಟ್ಟಿಯಲ್ಲಿಲ್ಲ."
                else:
                    is_satisfied = actual_value in exp
                    reason = f"Value '{actual_value}' in {exp}: {is_satisfied}"

            elif op == RuleOperator.NOT_IN:
                if isinstance(exp, list):
                    lowered_exp = [str(x).strip().lower() for x in exp]
                    is_satisfied = str(actual_value).strip().lower() not in lowered_exp
                    reason = f"Value '{actual_value}' {'is not in' if is_satisfied else 'is in'} excluded list."
                    reason_kn = f"ಮೌಲ್ಯ '{actual_value}' ಹೊರಗಿಡಲಾದ ಪಟ್ಟಿಯಲ್ಲಿಲ್ಲ." if is_satisfied else f"ಮೌಲ್ಯ '{actual_value}' ಹೊರಗಿಡಲಾದ ಪಟ್ಟಿಯಲ್ಲಿದೆ."
                else:
                    is_satisfied = actual_value not in exp

            elif op == RuleOperator.GREATER_THAN:
                act_num = float(actual_value)
                exp_num = float(exp)
                is_satisfied = act_num > exp_num
                reason = f"Value {act_num} {'is greater than' if is_satisfied else 'is not greater than'} required {exp_num}."
                reason_kn = f"{act_num} ಅಗತ್ಯವಿರುವ {exp_num} ಗಿಂತ {'ಹೆಚ್ಚಾಗಿದೆ' if is_satisfied else 'ಹೆಚ್ಚಾಗಿಲ್ಲ'}."

            elif op == RuleOperator.GREATER_THAN_OR_EQUAL:
                act_num = float(actual_value)
                exp_num = float(exp)
                is_satisfied = act_num >= exp_num
                reason = f"Value {act_num} {'meets minimum requirement of' if is_satisfied else 'is below minimum of'} {exp_num}."
                reason_kn = f"{act_num} ಕನಿಷ್ಠ ಅಗತ್ಯವಿರುವ {exp_num} ಗೆ {'ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ' if is_satisfied else 'ಕಡಿಮೆಯಾಗಿದೆ'}."

            elif op == RuleOperator.LESS_THAN:
                act_num = float(actual_value)
                exp_num = float(exp)
                is_satisfied = act_num < exp_num
                reason = f"Value {act_num} {'is below upper limit of' if is_satisfied else 'exceeds limit of'} {exp_num}."
                reason_kn = f"{act_num} ನಿಗದಿತ ಗರಿಷ್ಠ {exp_num} ಗಿಂತ {'ಕಡಿಮೆಯಾಗಿದೆ' if is_satisfied else 'ಹೆಚ್ಚಾಗಿದೆ'}."

            elif op == RuleOperator.LESS_THAN_OR_EQUAL:
                act_num = float(actual_value)
                exp_num = float(exp)
                is_satisfied = act_num <= exp_num
                reason = f"Value {act_num} {'is within maximum threshold of' if is_satisfied else 'exceeds maximum threshold of'} {exp_num}."
                reason_kn = f"{act_num} ಗರಿಷ್ಠ ಮಿತಿ {exp_num} ರ {'ಒಳಗಿದೆ' if is_satisfied else 'ಮೀರಿದೆ'}."

            elif op == RuleOperator.BETWEEN:
                act_num = float(actual_value)
                if isinstance(exp, list) and len(exp) == 2:
                    low_val = float(exp[0])
                    high_val = float(exp[1])
                    is_satisfied = low_val <= act_num <= high_val
                    reason = f"Value {act_num} {'is within range' if is_satisfied else 'is outside range'} [{low_val}, {high_val}]."
                    reason_kn = f"{act_num} ನಿಗದಿತ ವ್ಯಾಪ್ತಿ [{low_val}, {high_val}] ರ {'ಒಳಗಿದೆ' if is_satisfied else 'ಹೊರಗಿದೆ'}."
                else:
                    is_satisfied = False
                    reason = f"Invalid expected range format: {exp}"

            elif op == RuleOperator.EXISTS:
                is_satisfied = actual_value is not None and actual_value != "" and actual_value != []
                reason = f"Field {'is present' if is_satisfied else 'is missing'}."
                reason_kn = f"ವಿವರಗಳು {'ಲಭ್ಯವಿವೆ' if is_satisfied else 'ಲಭ್ಯವಿಲ್ಲ'}."

            elif op == RuleOperator.ANY_OF:
                lowered_exp = [str(x).strip().lower() for x in (exp if isinstance(exp, list) else [exp])]
                if isinstance(actual_value, list):
                    lowered_act = [str(x).strip().lower() for x in actual_value]
                    common = set(lowered_act).intersection(set(lowered_exp))
                    is_satisfied = len(common) > 0
                    reason = f"Found matching items: {list(common)}" if is_satisfied else f"No items in {actual_value} match required {exp}."
                    reason_kn = f"ಹೊಂದಿಕೆಯಾಗುವ ಬೆಳೆ/ವಿವರ: {list(common)}" if is_satisfied else f"ಯಾವುದೇ ಬೆಳೆ ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ."
                else:
                    is_satisfied = str(actual_value).strip().lower() in lowered_exp
                    reason = f"Value '{actual_value}' matches one of allowed options." if is_satisfied else f"'{actual_value}' does not match allowed options."
                    reason_kn = f"'{actual_value}' ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ." if is_satisfied else f"'{actual_value}' ಹೊಂದಿಕೆಯಾಗುವುದಿಲ್ಲ."

            elif op == RuleOperator.ALL_OF:
                lowered_exp = [str(x).strip().lower() for x in (exp if isinstance(exp, list) else [exp])]
                if isinstance(actual_value, list):
                    lowered_act = set([str(x).strip().lower() for x in actual_value])
                    is_satisfied = set(lowered_exp).issubset(lowered_act)
                    reason = f"All required items present." if is_satisfied else f"Missing required items from {exp}."
                    reason_kn = f"ಎಲ್ಲಾ ಕಡ್ಡಾಯ ಅಂಶಗಳು ಲಭ್ಯವಿವೆ." if is_satisfied else f"ಅಗತ್ಯವಿರುವ ಕೆಲವು ಅಂಶಗಳು ಲಭ್ಯವಿಲ್ಲ."
                else:
                    is_satisfied = False
                    reason = f"Expected list for ALL_OF, got {type(actual_value)}."

        except Exception as e:
            logger.error(f"Rule evaluation exception for rule {rule.rule_id}: {e}")
            return RuleEvaluationResult(
                rule_id=rule.rule_id,
                description=rule.description,
                description_kn=rule.description_kn,
                field=rule.field,
                status=CriterionStatus.NOT_SATISFIED,
                expected_value=rule.expected_value,
                actual_value=actual_value,
                is_mandatory=rule.is_mandatory,
                source_reference=rule.source_reference,
                reason=f"Rule evaluation error: {str(e)}",
                reason_kn=f"ನಿಯಮ ಪರಿಶೀಲನಾ ದೋಷ: {str(e)}",
                clarification_question=rule.clarification_question,
                clarification_question_kn=rule.clarification_question_kn,
                why_needed=rule.why_needed,
                why_needed_kn=rule.why_needed_kn
            )

        status = CriterionStatus.SATISFIED if is_satisfied else CriterionStatus.NOT_SATISFIED
        return RuleEvaluationResult(
            rule_id=rule.rule_id,
            description=rule.description,
            description_kn=rule.description_kn,
            field=rule.field,
            status=status,
            expected_value=rule.expected_value,
            actual_value=actual_value,
            is_mandatory=rule.is_mandatory,
            source_reference=rule.source_reference,
            reason=reason,
            reason_kn=reason_kn,
            clarification_question=rule.clarification_question,
            clarification_question_kn=rule.clarification_question_kn,
            why_needed=rule.why_needed,
            why_needed_kn=rule.why_needed_kn
        )

    @classmethod
    def evaluate_scheme(cls, scheme: SchemeRecord, profile: FarmerProfile) -> SchemeMatchResult:
        satisfied = []
        unsatisfied = []
        unknown = []
        needs_verification = []

        for rule in scheme.eligibility_rules:
            res = cls.evaluate_rule(rule, profile)
            if res.status == CriterionStatus.SATISFIED:
                satisfied.append(res)
            elif res.status == CriterionStatus.NOT_SATISFIED:
                unsatisfied.append(res)
            elif res.status == CriterionStatus.UNKNOWN:
                unknown.append(res)
            elif res.status == CriterionStatus.NEEDS_VERIFICATION:
                needs_verification.append(res)

        mandatory_unsatisfied = [r for r in unsatisfied if r.is_mandatory]
        mandatory_unknown = [r for r in unknown if r.is_mandatory]
        mandatory_needs_verification = [r for r in needs_verification if r.is_mandatory]

        total_rules = len(scheme.eligibility_rules)
        score = (len(satisfied) / total_rules) if total_rules > 0 else 0.0

        if mandatory_unsatisfied:
            status = SchemeStatus.NOT_SUITABLE_BASED_ON_KNOWN_RULES
            reasons = [r.description for r in mandatory_unsatisfied]
            reasons_kn = [r.description_kn or r.description for r in mandatory_unsatisfied]
            match_reason = f"Does not meet mandatory criteria: {'; '.join(reasons)}."
            match_reason_kn = f"ಕಡ್ಡಾಯ ಮಾನದಂಡಗಳನ್ನು ಪೂರೈಸುತ್ತಿಲ್ಲ: {'; '.join(reasons_kn)}."
            next_q = None
            next_q_kn = None
        elif mandatory_unknown:
            status = SchemeStatus.INSUFFICIENT_INFORMATION
            missing_fields = [r.field for r in mandatory_unknown]
            match_reason = f"Potentially matches, but requires information on: {', '.join(missing_fields)}."
            match_reason_kn = f"ಹೊಂದಿಕೆಯಾಗುವ ಸಾಧ್ಯತೆಯಿದೆ, ಆದರೆ ಈ ಕೆಳಗಿನ ಮಾಹಿತಿಯನ್ನು ದೃಢೀಕರಿಸಬೇಕು: {', '.join(missing_fields)}."
            first_unknown = mandatory_unknown[0]
            next_q = first_unknown.clarification_question or f"Could you specify your {first_unknown.field}?"
            next_q_kn = first_unknown.clarification_question_kn or f"ದಯವಿಟ್ಟು ನಿಮ್ಮ {first_unknown.description_kn or first_unknown.field} ಬಗ್ಗೆ ತಿಳಿಸುವಿರಾ?"
        elif mandatory_needs_verification:
            status = SchemeStatus.REQUIRES_OFFICIAL_VERIFICATION
            match_reason = f"Meets known digital criteria, but final eligibility requires official authority inspection."
            match_reason_kn = f"ಡಿಜಿಟಲ್ ಮಾನದಂಡಗಳು ಹೊಂದಿಕೆಯಾಗಿವೆ, ಅಂತಿಮ ಅನುಮೋದನೆಗೆ ಕೃಷಿ ಅಧಿಕಾರಿಯ ಪರಿಶೀಲನೆ ಅಗತ್ಯವಿದೆ."
            next_q = None
            next_q_kn = None
        else:
            status = SchemeStatus.POTENTIALLY_SUITABLE
            match_reason = f"Meets all {len(satisfied)} known mandatory criteria for this scheme."
            match_reason_kn = f"ಈ ಯೋಜನೆಯ ಎಲ್ಲಾ {len(satisfied)} ಕಡ್ಡಾಯ ಮಾನದಂಡಗಳನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಪೂರೈಸಿದೆ."
            next_q = None
            next_q_kn = None

        return SchemeMatchResult(
            scheme=scheme,
            evaluation_status=status,
            score=round(score, 2),
            satisfied_rules=satisfied,
            unsatisfied_rules=unsatisfied,
            unknown_rules=unknown,
            needs_verification_rules=needs_verification,
            match_reason=match_reason,
            match_reason_kn=match_reason_kn,
            next_clarification_question=next_q,
            next_clarification_question_kn=next_q_kn
        )
