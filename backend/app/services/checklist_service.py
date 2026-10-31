import logging
from typing import Optional, List
from ..models.scheme import SchemeRecord, SchemeReadinessChecklist, ChecklistItem
from ..models.farmer import FarmerProfile

logger = logging.getLogger(__name__)

class ChecklistService:
    """
    Generates structured, scheme-specific application readiness checklists.
    Identifies mandatory and optional documents, prerequisites, and pending items.
    Explicitly clarifies that Krishi Mitra does not submit applications.
    """

    @classmethod
    def generate_checklist(
        cls,
        scheme: SchemeRecord,
        profile: Optional[FarmerProfile] = None
    ) -> SchemeReadinessChecklist:
        items: List[ChecklistItem] = []

        # 1. Mandatory Documents
        for idx, doc in enumerate(scheme.required_documents):
            doc_kn = scheme.required_documents_kn[idx] if idx < len(scheme.required_documents_kn) else None
            item_id = f"doc_req_{idx+1}"

            # Check if farmer profile already has evidence
            is_completed = False
            evidence = None
            if profile:
                confirmed = profile.confirmed_fields
                if "Aadhaar" in doc and "aadhaar_linked" in profile.additional_details:
                    is_completed = True
                    evidence = "Aadhaar status noted from conversation."
                elif ("RTC" in doc or "Pahani" in doc) and profile.ownership == "owned":
                    # Partially ready
                    evidence = "Ownership stated as owner-cultivator."

            items.append(ChecklistItem(
                item_id=item_id,
                title=doc,
                title_kn=doc_kn,
                category="document",
                is_mandatory=True,
                is_completed=is_completed,
                evidence_found=evidence,
                help_text=f"Must be original or attested copy as required by {scheme.name}.",
                help_text_kn=f"{scheme.name_kn or scheme.name} ನಿಯಮಾವಳಿಯಂತೆ ಅಗತ್ಯ ದಾಖಲೆ ಪ್ರತಿ."
            ))

        # 2. Optional Documents
        for idx, opt_doc in enumerate(scheme.optional_documents or []):
            opt_kn = scheme.optional_documents_kn[idx] if idx < len(scheme.optional_documents_kn or []) else None
            items.append(ChecklistItem(
                item_id=f"doc_opt_{idx+1}",
                title=opt_doc,
                title_kn=opt_kn,
                category="document",
                is_mandatory=False,
                is_completed=False,
                help_text="Optional: may help secure enhanced subsidy or expedited approval.",
                help_text_kn="ಐಚ್ಛಿಕ: ಹೆಚ್ಚುವರಿ ರಿಯಾಯಿತಿ ಅಥವಾ ತ್ವರಿತ ಪರಿಶೀಲನೆಗೆ ಸಹಾಯಕ."
            ))

        # 3. Scheme-specific Prerequisites
        if scheme.id == "pm-kisan":
            items.append(ChecklistItem(
                item_id="pre_ekyc",
                title="Mandatory e-KYC (Aadhaar OTP or Biometric)",
                title_kn="ಕಡ್ಡಾಯ e-KYC ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ (ಆಧಾರ್ OTP ಅಥವಾ ಬಯೋಮೆಟ್ರಿಕ್)",
                category="prerequisite",
                is_mandatory=True,
                is_completed=False,
                help_text="Can be completed online at pmkisan.gov.in or nearest CSC center.",
                help_text_kn="pmkisan.gov.in ನಲ್ಲಿ ನೇರವಾಗಿ ಅಥವಾ ಸಿಎಸ್‌ಸಿ ಕೇಂದ್ರದಲ್ಲಿ ಮಾಡಿಸಬಹುದು."
            ))
            items.append(ChecklistItem(
                item_id="pre_bhoomi",
                title="Karnataka Bhoomi RTC Land Record matching Aadhaar name",
                title_kn="ಭೂಮಿ ಆರ್‌ಟಿಸಿ ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್‌ನಲ್ಲಿ ಹೆಸರು ಹೊಂದಾಣಿಕೆ",
                category="prerequisite",
                is_mandatory=True,
                is_completed=False,
                help_text="Name on land RTC must match name in Aadhaar database.",
                help_text_kn="ಪಹಣಿ ಮತ್ತು ಆಧಾರ್‌ನಲ್ಲಿ ಹೆಸರು ಒಂದೇ ರೀತಿ ಇರಬೇಕು."
            ))
        elif scheme.id == "pmfby":
            items.append(ChecklistItem(
                item_id="pre_samrakshane",
                title="Village Notified Crop Cut-off Date Verification",
                title_kn="ಗ್ರಾಮದ ಅಧಿಸೂಚಿತ ಬೆಳೆ ಮತ್ತು ಕೊನೆಯ ದಿನಾಂಕ ಪರಿಶೀಲನೆ",
                category="prerequisite",
                is_mandatory=True,
                is_completed=False,
                help_text="Verify seasonal cut-off date on samrakshane.karnataka.gov.in.",
                help_text_kn="ಸಂರಕ್ಷಣೆ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಕೊನೆಯ ದಿನಾಂಕ ಮುಗಿಯುವ ಮುನ್ನ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು."
            ))
        elif scheme.id == "demo-micro-irrigation":
            items.append(ChecklistItem(
                item_id="pre_water",
                title="Active Borewell / Well Electricity RR Number Verification",
                title_kn="ಕೊಳವೆಬಾವಿ / ಬಾವಿಯ ವಿದ್ಯುತ್ ಆರ್‌ಆರ್ ಸಂಖ್ಯೆ ದೃಢೀಕರಣ",
                category="prerequisite",
                is_mandatory=True,
                is_completed=bool(profile and profile.additional_details.get("water_source_available")),
                help_text="Required for official drip irrigation site verification.",
                help_text_kn="ಹನಿ ನೀರಾವರಿ ಸ್ಥಳ ಪರಿಶೀಲನೆಗೆ ವಿದ್ಯುತ್ ಬಿಲ್ ಅಥವಾ ಆರ್‌ಆರ್ ಸಂಖ್ಯೆ ಅಗತ್ಯ."
            ))

        # Compute stats
        mandatory_items = [it for it in items if it.is_mandatory]
        mandatory_total = len(mandatory_items)
        mandatory_ready = len([it for it in mandatory_items if it.is_completed])
        pct = int((mandatory_ready / mandatory_total) * 100) if mandatory_total > 0 else 0

        next_steps_en = [
            f"1. Gather all mandatory documents listed in the checklist above.",
            f"2. Visit the designated portal ({scheme.official_source_url or 'Taluk Agricultural Office'}) or your local Grama One / Raitha Samparka Kendra.",
            f"3. Submit physical copies for official document verification and obtain an acknowledgement receipt."
        ]
        next_steps_kn = [
            f"1. ಮೇಲಿನ ಸಿದ್ಧತಾ ಪಟ್ಟಿಯಲ್ಲಿರುವ ಎಲ್ಲಾ ಕಡ್ಡಾಯ ದಾಖಲೆಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿಕೊಳ್ಳಿ.",
            f"2. ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ({scheme.official_source_url or 'ತಾಲೂಕು ಕೃಷಿ ಇಲಾಖೆ'}) ಅಥವಾ ಗ್ರಾಮ ಒನ್ / ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.",
            f"3. ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಸ್ವೀಕೃತಿ ರಶೀದಿಯನ್ನು (Acknowledgement Receipt) ಪಡೆದುಕೊಳ್ಳಿ."
        ]

        disclaimer_en = (
            "NOTICE: Krishi Mitra is an AI preparatory guidance system. It does NOT submit applications or collect personal documents. "
            "Final application submission must be performed on official government portals or at authorized citizen service centers."
        )
        disclaimer_kn = (
            "ಗಮನಿಸಿ: ಕೃಷಿ ಮಿತ್ರ ಕೇವಲ ಅರ್ಜಿ ಪೂರ್ವ ಸಿದ್ಧತಾ ಮಾರ್ಗದರ್ಶಿಯಾಗಿದೆ. ಇದು ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್‌ಗಳಲ್ಲಿ ಅರ್ಜಿಯನ್ನು ಸಲ್ಲಿಸುವುದಿಲ್ಲ. "
            "ಅಧಿಕೃತ ಅರ್ಜಿ ಸಲ್ಲಿಕೆ ಸಂಬಂಧಪಟ್ಟ ಇಲಾಖಾ ವೆಬ್‌ಸೈಟ್ ಅಥವಾ ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರಗಳಲ್ಲಿ ಮಾತ್ರ ನಡೆಯುತ್ತದೆ."
        )

        return SchemeReadinessChecklist(
            scheme_id=scheme.id,
            scheme_name=scheme.name,
            scheme_name_kn=scheme.name_kn,
            scheme_type=scheme.scheme_type,
            official_source_url=scheme.official_source_url,
            completion_percentage=pct,
            mandatory_ready_count=mandatory_ready,
            mandatory_total_count=mandatory_total,
            items=items,
            next_steps=next_steps_en,
            next_steps_kn=next_steps_kn,
            disclaimer=disclaimer_en,
            disclaimer_kn=disclaimer_kn
        )

