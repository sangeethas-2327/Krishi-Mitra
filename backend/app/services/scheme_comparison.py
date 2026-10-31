import logging
from typing import List, Dict, Any, Optional
from ..models.scheme import SchemeRecord, SchemeComparisonItem, SchemeComparisonResponse
from .scheme_source_service import SchemeSourceService

logger = logging.getLogger(__name__)

class SchemeComparisonService:
    """
    Compares selected agricultural schemes on factual, verified dimensions:
    Purpose, eligibility conditions, benefits, required documents, application process, and official verification status.
    Only factual, verifiable information is presented; synthetic demo schemes are clearly highlighted.
    """

    @classmethod
    def compare_schemes(cls, scheme_ids: List[str]) -> SchemeComparisonResponse:
        all_schemes = SchemeSourceService.load_schemes()
        scheme_map = {s.id: s for s in all_schemes}

        selected: List[SchemeRecord] = []
        for sid in scheme_ids:
            if sid in scheme_map:
                selected.append(scheme_map[sid])

        if not selected:
            # Fallback: take top 2 schemes
            selected = all_schemes[:2]

        items: List[SchemeComparisonItem] = []
        matrix: Dict[str, Dict[str, Any]] = {
            "purpose": {},
            "target_beneficiaries": {},
            "scheme_type": {},
            "benefits": {},
            "eligibility_rules": {},
            "required_documents": {},
            "application_process": {},
            "official_portal": {},
            "verification_status": {}
        }

        for s in selected:
            is_real = s.scheme_type == "real"
            
            # Key eligibility summary
            elig_summary = [r.description for r in s.eligibility_rules if r.is_mandatory]
            elig_summary_kn = [r.description_kn or r.description for r in s.eligibility_rules if r.is_mandatory]

            # Purpose and Target
            if s.id == "pm-kisan":
                target_en = "Landholding farmer families with cultivable land in their names."
                target_kn = "ತಮ್ಮ ಹೆಸರಿನಲ್ಲಿ ಸಾಗುವಳಿ ಭೂಹಿಡುವಳಿ ಹೊಂದಿರುವ ಎಲ್ಲಾ ರೈತ ಕುಟುಂಬಗಳು."
                app_mode_en = "Online self-registration at pmkisan.gov.in or via Grama One / CSC."
                app_mode_kn = "pmkisan.gov.in ನಲ್ಲಿ ನೇರ ಆನ್‌ಲೈನ್ ನೋಂದಣಿ ಅಥವಾ ಗ್ರಾಮ ಒನ್ / CSC ಮೂಲಕ."
            elif s.id == "pmfby":
                target_en = "All farmers (loanee, non-loanee, tenant, sharecropper) growing notified crops."
                target_kn = "ಅಧಿಸೂಚಿತ ಬೆಳೆ ಬೆಳೆಯುವ ಎಲ್ಲಾ ರೈತರು (ಸ್ವಂತ ಮತ್ತು ಗುತ್ತಿಗೆ/ಪಾಲುದಾರಿಕೆ ರೈತರು)."
                app_mode_en = "Bank branch (for loanee) or Samrakshane portal / Grama One (for non-loanee)."
                app_mode_kn = "ಬೆಳೆ ಸಾಲ ಪಡೆದ ಬ್ಯಾಂಕ್ ಮೂಲಕ ಅಥವಾ ಸಂರಕ್ಷಣೆ ಪೋರ್ಟಲ್ / ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರದ ಮೂಲಕ."
            elif s.scheme_type == "demonstration":
                target_en = "[DEMONSTRATION] Demonstration test scenario for farmers."
                target_kn = "[ಪ್ರಾಯೋಗಿಕ] ಪರೀಕ್ಷಾರ್ಥ ಮಾದರಿ ರೈತರು."
                app_mode_en = "Demonstration execution only (No statutory submission)."
                app_mode_kn = "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಪರೀಕ್ಷಾರ್ಥ ಉದ್ದೇಶಕ್ಕೆ ಮಾತ್ರ (ಯಾವುದೇ ಅರ್ಜಿ ಸಲ್ಲಿಕೆ ಇಲ್ಲ)."
            else:
                loc_str = ", ".join(s.applicable_locations) if s.applicable_locations else "Karnataka / All India"
                crops_str = ", ".join(s.supported_crops) if s.supported_crops else "All crops"
                target_en = f"Eligible farmers in {loc_str} ({crops_str})."
                target_kn = f"{loc_str} ವ್ಯಾಪ್ತಿಯಲ್ಲಿ {crops_str} ಬೆಳೆಯುವ ರೈತರು."

                if s.application_steps:
                    app_mode_en = s.application_steps[0]
                    app_mode_kn = s.application_steps_kn[0] if s.application_steps_kn else s.application_steps[0]
                elif s.official_source_url:
                    app_mode_en = f"Online application via official portal: {s.official_source_url}"
                    app_mode_kn = f"ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ: {s.official_source_url}"
                else:
                    app_mode_en = "Visit local Raitha Samparka Kendra (RSK) or Taluk Department Office."
                    app_mode_kn = "ಸ್ಥಳೀಯ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK) ಅಥವಾ ತಾಲೂಕು ಇಲಾಖಾ ಕಚೇರಿಗೆ ಭೇಟಿ ನೀಡಿ."

            comp_item = SchemeComparisonItem(
                scheme_id=s.id,
                name=s.name,
                name_kn=s.name_kn,
                government_level=s.government_level or "central",
                scheme_type=s.scheme_type,
                category=s.category,
                category_kn=s.category_kn,
                assistance_type=s.assistance_type,
                purpose=s.description,
                purpose_kn=s.description_kn,
                target_beneficiaries=target_en,
                target_beneficiaries_kn=target_kn,
                key_eligibility=elig_summary,
                key_eligibility_kn=elig_summary_kn,
                benefits_summary=s.benefits,
                benefits_summary_kn=s.benefits_kn,
                required_documents=s.required_documents,
                required_documents_kn=s.required_documents_kn,
                application_mode=app_mode_en,
                application_mode_kn=app_mode_kn,
                official_url=s.official_source_url,
                verification_status=s.verification_status,
                status_label=s.status_label,
                status_label_kn=s.status_label_kn,
                application_steps=s.application_steps,
                application_steps_kn=s.application_steps_kn,
                issuing_authority=s.issuing_authority,
                verification_authority=s.verification_authority
            )
            items.append(comp_item)

            matrix["purpose"][s.id] = s.description
            matrix["target_beneficiaries"][s.id] = target_en
            matrix["scheme_type"][s.id] = "Official Government Scheme" if is_real else "Fictional Demonstration Simulation"
            matrix["benefits"][s.id] = s.benefits
            matrix["eligibility_rules"][s.id] = elig_summary
            matrix["required_documents"][s.id] = s.required_documents
            matrix["application_process"][s.id] = app_mode_en
            matrix["official_portal"][s.id] = s.official_source_url or "None (Simulated Scheme)"
            matrix["verification_status"][s.id] = f"Verified ({s.last_verified_at})" if is_real else "Synthetic / Demonstration Only"

        disclaimer_en = (
            "Comparison is based strictly on verified public government guidelines and synthetic simulation specifications. "
            "Fictional demonstration schemes are clearly flagged and must not be treated as real government benefits."
        )
        disclaimer_kn = (
            "ಈ ಹೋಲಿಕೆಯು ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಮಾರ್ಗಸೂಚಿಗಳು ಮತ್ತು ಪ್ರಾಯೋಗಿಕ ಸಿಮ್ಯುಲೇಶನ್ ಆಧಾರಿತವಾಗಿದೆ. "
            "ಪ್ರಾಯೋಗಿಕ ಯೋಜನೆಗಳನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಗುರುತಿಸಲಾಗಿದೆ ಮತ್ತು ಅವುಗಳು ಅಧಿಕೃತ ಪ್ರಯೋಜನಗಳಲ್ಲ."
        )

        return SchemeComparisonResponse(
            schemes=items,
            comparison_matrix=matrix,
            disclaimer=disclaimer_en,
            disclaimer_kn=disclaimer_kn
        )

