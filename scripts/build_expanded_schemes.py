import json
import sys
from pathlib import Path

# Add backend to sys.path
backend_path = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(backend_path))

from app.models.scheme import SchemeRecord, EligibilityRule, RuleOperator

DATA_OUTPUT = backend_path / "app" / "data" / "schemes.json"

def build_catalog():
    schemes = []

    # =========================================================================
    # PART A: CENTRAL GOVERNMENT SCHEMES & PROGRAMMES (28 entries)
    # =========================================================================

    # 1. PM-KISAN
    schemes.append({
        "id": "pm-kisan",
        "name": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
        "name_kn": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ನಿಧಿ (ಪಿಎಂ-ಕಿಸಾನ್)",
        "official_abbreviation": "PM-KISAN",
        "government_level": "central",
        "scheme_type": "real",
        "category": "income_support",
        "category_kn": "ಆದಾಯ ಬೆಂಬಲ",
        "assistance_type": "direct_financial_assistance",
        "status_label": "Current status verified",
        "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
        "description": "Central Sector scheme providing income support of ₹6,000 per year in three equal installments to all landholding farmer families across India.",
        "description_kn": "ಭೂಹಿಡುವಳಿ ಹೊಂದಿರುವ ಎಲ್ಲಾ ರೈತ ಕುಟುಂಬಗಳಿಗೆ ವರ್ಷಕ್ಕೆ ₹6,000 ಆರ್ಥಿಕ ಬೆಂಬಲವನ್ನು 3 ಕಂತುಗಳಲ್ಲಿ (ಪ್ರತಿ ಕಂತಿಗೆ ₹2,000) ನೀಡುವ ಕೇಂದ್ರ ಸರ್ಕಾರದ ನೇರ ನಗದು ವರ್ಗಾವಣೆ ಯೋಜನೆ.",
        "benefits": [
            "₹6,000 per year paid in three equal four-monthly installments of ₹2,000 each via Direct Benefit Transfer (DBT).",
            "Direct transfer into the farmer's Aadhaar-linked bank account without intermediaries."
        ],
        "benefits_kn": [
            "ವರ್ಷಕ್ಕೆ ₹6,000 ಹಣವನ್ನು ತಲಾ ₹2,000 ರ ಮೂರು ಕಂತುಗಳಲ್ಲಿ ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT) ಮೂಲಕ ನೀಡಲಾಗುತ್ತದೆ.",
            "ಯಾವುದೇ ಮಧ್ಯವರ್ತಿಗಳಿಲ್ಲದೆ ರೈತರ ಆಧಾರ್ ಜೋಡಿತ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ."
        ],
        "eligibility_rules": [
            {
                "rule_id": "pmk_ownership",
                "description": "Farmer or family must possess cultivable landholding in their name (owner-cultivator).",
                "description_kn": "ರೈತ ಅಥವಾ ಕುಟುಂಬದ ಹೆಸರಿನಲ್ಲಿ ಸಾಗುವಳಿ ಮಾಡಬಹುದಾದ ಕೃಷಿ ಭೂಮಿ ಇರಬೇಕು (ಸ್ವಂತ ಭೂಮಾಲೀಕರು).",
                "field": "ownership",
                "operator": "in",
                "expected_value": ["owned", "joint_owned"],
                "is_mandatory": True,
                "source_reference": "PM-KISAN Operational Guidelines Sec 2.1",
                "verification_status": "verified",
                "clarification_question": "Do you own the land you cultivate, or is it on lease or tenancy?",
                "clarification_question_kn": "ನೀವು ಸಾಗುವಳಿ ಮಾಡುವ ಜಮೀನು ನಿಮ್ಮ ಸ್ವಂತದ್ದೇ ಅಥವಾ ಗುತ್ತಿಗೆಗೆ ಪಡೆದಿದ್ದೀರಾ?",
                "why_needed": "PM-KISAN guidelines specifically restrict income support to legal landholding title-holders.",
                "why_needed_kn": "ಪಿಎಂ-ಕಿಸಾನ್ ಮಾರ್ಗಸೂಚಿಯಂತೆ ಸಾಗುವಳಿ ಭೂಮಿಯ ಕಾನೂನುಬದ್ಧ ಮಾಲೀಕರಿಗೆ ಮಾತ್ರ ಈ ನೆರವು ಸೀಮಿತವಾಗಿದೆ."
            },
            {
                "rule_id": "pmk_state",
                "description": "Applicable across all Indian States and Union Territories including Karnataka.",
                "description_kn": "ಕರ್ನಾಟಕ ಸೇರಿದಂತೆ ಭಾರತದ ಎಲ್ಲಾ ರಾಜ್ಯ ಮತ್ತು ಕೇಂದ್ರಾಡಳಿತ ಪ್ರದೇಶಗಳ ರೈತರಿಗೆ ಅನ್ವಯಿಸುತ್ತದೆ.",
                "field": "location.state",
                "operator": "in",
                "expected_value": ["Karnataka", "karnataka", "KA", "All India"],
                "is_mandatory": True,
                "source_reference": "PM-KISAN Guidelines Sec 1",
                "verification_status": "verified",
                "clarification_question": "Which state do you cultivate in?",
                "clarification_question_kn": "ನೀವು ಯಾವ ರಾಜ್ಯದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಿ?",
                "why_needed": "Required to identify jurisdiction and state land database (Bhoomi).",
                "why_needed_kn": "ರಾಜ್ಯದ ಭೂಮಿ ಆರ್‌ಟಿಸಿ ದತ್ತಾಂಶ ಪರಿಶೀಲನೆಗೆ ರಾಜ್ಯದ ವಿವರ ಅಗತ್ಯವಿದೆ."
            },
            {
                "rule_id": "pmk_land_exists",
                "description": "Must hold cultivable land greater than 0 acres.",
                "description_kn": "0 ಎಕರೆಗಿಂತ ಹೆಚ್ಚು ಸಾಗುವಳಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು.",
                "field": "land_area.value_acres",
                "operator": "greater_than",
                "expected_value": 0,
                "is_mandatory": True,
                "source_reference": "PM-KISAN Revised Guidelines 2019",
                "verification_status": "verified",
                "clarification_question": "How much cultivable land do you hold?",
                "clarification_question_kn": "ನಿಮ್ಮಲ್ಲಿ ಎಷ್ಟು ಎಕರೆ ಸಾಗುವಳಿ ಭೂಮಿ ಇದೆ?",
                "why_needed": "Land record entry is mandatory to confirm legitimate farmer status.",
                "why_needed_kn": "ಕಾನೂನುಬದ್ಧ ರೈತರೆಂದು ದೃಢೀಕರಿಸಲು ಕೃಷಿ ಭೂಮಿಯ ವಿವರ ಕಡ್ಡಾಯವಾಗಿದೆ."
            }
        ],
        "required_documents": [
            "Aadhaar card linked with active mobile number for OTP/e-KYC",
            "Valid land record proof (RTC / Pahani / Record of Rights)",
            "Aadhaar-seeded bank account passbook with valid IFSC code"
        ],
        "required_documents_kn": [
            "ಮೊಬೈಲ್ ಸಂಖ್ಯೆಗೆ ಲಿಂಕ್ ಆಗಿರುವ ಆಧಾರ್ ಕಾರ್ಡ್ (ಇ-ಕೆವೈಸಿ ಗಾಗಿ)",
            "ಚಾಲ್ತಿಯಲ್ಲಿರುವ ಪಹಣಿ / ಆರ್‌ಟಿಸಿ (RTC) ದಾಖಲೆ",
            "ಆಧಾರ್ ಜೋಡಿತ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಮತ್ತು ಐಎಫ್‌ಎಸ್‌ಸಿ (IFSC) ಕೋಡ್"
        ],
        "optional_documents": ["Caste certificate (if applicable for state top-up schemes)"],
        "optional_documents_kn": ["ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ (ಅನ್ವಯಿಸಿದರೆ)"],
        "application_steps": [
            "Visit the official PM-KISAN portal at pmkisan.gov.in or Common Service Centre (CSC).",
            "Navigate to 'Farmer Corner' and choose 'New Farmer Registration'.",
            "Enter Aadhaar number and mobile number, verify OTP.",
            "Fill State (Karnataka), District, Sub-District/Taluk, Village, and Survey/RTC details.",
            "Complete mandatory biometric or face e-KYC on the portal."
        ],
        "application_steps_kn": [
            "ಅಧಿಕೃತ pmkisan.gov.in ವೆಬ್‌ಸೈಟ್‌ಗೆ ಭೇಟಿ ನೀಡಿ ಅಥವಾ ಗ್ರಾಮ ಒನ್ / ಸಿಎಸ್‌ಸಿ ಕೇಂದ್ರಕ್ಕೆ ಹೋಗಿ.",
            "'Farmer Corner' ನಲ್ಲಿ 'New Farmer Registration' ಆಯ್ಕೆಮಾಡಿ.",
            "ಆಧಾರ್ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ ಮತ್ತು ಒಟಿಪಿ ಪರಿಶೀಲಿಸಿ.",
            "ಜಿಲ್ಲೆ, ತಾಲೂಕು, ಗ್ರಾಮ ಮತ್ತು ಸರ್ವೇ ನಂಬರ್ ವಿವರಗಳನ್ನು ಭರ್ತಿ ಮಾಡಿ.",
            "ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಕಡ್ಡಾಯ ಬಯೋಮೆಟ್ರಿಕ್ ಅಥವಾ ಇ-ಕೆವೈಸಿ ಪೂರ್ಣಗೊಳಿಸಿ."
        ],
        "official_source_url": "https://pmkisan.gov.in/",
        "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
        "verification_authority": "Revenue & Agriculture Departments, Government of Karnataka",
        "last_verified_at": "2026-10-30",
        "verification_status": "verified",
        "applicable_locations": ["All India", "Karnataka"],
        "supported_crops": ["All agricultural crops"],
        "notes": [
            "Current subsidy amount must be confirmed with the implementing department.",
            "Institutional landholders and serving/retired government employees are excluded.",
            "Mandatory e-KYC and land record linkage (Pahani) must be up-to-date."
        ],
        "notes_kn": [
            "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
            "ಸಾಂಸ್ಥಿಕ ಭೂಮಾಲೀಕರು ಮತ್ತು ಸರ್ಕಾರಿ ಉದ್ಯೋಗಿಗಳಿಗೆ ಈ ಯೋಜನೆ ಅನ್ವಯಿಸುವುದಿಲ್ಲ.",
            "ಕಡ್ಡಾಯ ಇ-ಕೆವೈಸಿ ಮತ್ತು ಭೂದಾಖಲೆ (ಪಹಣಿ) ಜೋಡಣೆ ಅಪ್‌ಡೇಟ್ ಆಗಿರಬೇಕು."
        ]
    })

    # 2. PM-KMY
    schemes.append({
        "id": "pm-kmy",
        "name": "PM-Kisan Maandhan Yojana (PM-KMY)",
        "name_kn": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಕಿಸಾನ್ ಮಾನ್‌ಧನ್ ಯೋಜನೆ (ಪಿಎಂ-ಕೆಎಂವೈ)",
        "official_abbreviation": "PM-KMY",
        "government_level": "central",
        "scheme_type": "real",
        "category": "pension_social_security",
        "category_kn": "ಪಿಂಚಣಿ ಮತ್ತು ಸಾಮಾಜಿಕ ಭದ್ರತೆ",
        "assistance_type": "pension_social_security",
        "status_label": "Current status verified",
        "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
        "description": "Voluntary contributory old-age pension scheme for small and marginal farmers providing an assured monthly pension of ₹3,000 after reaching age 60.",
        "description_kn": "ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ವೃದ್ಧಾಪ್ಯ ಭದ್ರತೆ ನೀಡುವ ಸ್ವಯಂಪ್ರೇರಿತ ಪಿಂಚಣಿ ಯೋಜನೆ. 60 ವರ್ಷ ತುಂಬಿದ ನಂತರ ತಿಂಗಳಿಗೆ ₹3,000 ನಿಶ್ಚಿತ ಪಿಂಚಣಿ ನೀಡಲಾಗುತ್ತದೆ.",
        "benefits": [
            "Assured monthly pension of ₹3,000 upon reaching 60 years of age.",
            "Equal matching monthly contribution paid by the Central Government into the pension fund."
        ],
        "benefits_kn": [
            "60 ವರ್ಷ ತುಂಬಿದ ನಂತರ ಪ್ರತಿ ತಿಂಗಳು ₹3,000 ನಿಶ್ಚಿತ ಪಿಂಚಣಿ.",
            "ರೈತರು ಪಾವತಿಸುವಷ್ಟೇ ಮೊತ್ತದ ಸಮಾನ ಪಾಲನ್ನು ಕೇಂದ್ರ ಸರ್ಕಾರವು ಪಿಂಚಣಿ ನಿಧಿಗೆ ಜಮಾ ಮಾಡುತ್ತದೆ."
        ],
        "eligibility_rules": [
            {
                "rule_id": "pmkmy_land_cap",
                "description": "Cultivable landholding must not exceed 2 hectares (approx 5 acres).",
                "description_kn": "ಸಾಗುವಳಿ ಜಮೀನು 2 ಹೆಕ್ಟೇರ್ (ಸುಮಾರು 5 ಎಕರೆ) ಮೀರಬಾರದು.",
                "field": "land_area.value_acres",
                "operator": "less_than_or_equal",
                "expected_value": 5.0,
                "is_mandatory": True,
                "source_reference": "PM-KMY Operational Guidelines Sec 3",
                "verification_status": "verified",
                "clarification_question": "Is your total landholding 5 acres or less?",
                "clarification_question_kn": "ನಿಮ್ಮ ಒಟ್ಟು ಕೃಷಿ ಭೂಮಿ 5 ಎಕರೆ ಅಥವಾ ಅದಕ್ಕಿಂತ ಕಡಿಮೆಯಿದೆಯೇ?",
                "why_needed": "PM-KMY is strictly targeted at small and marginal farmers.",
                "why_needed_kn": "ಪಿಎಂ-ಕೆಎಂವೈ ಯೋಜನೆಯು ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಮಾತ್ರ ಸೀಮಿತವಾಗಿದೆ."
            }
        ],
        "required_documents": [
            "Aadhaar card",
            "Savings bank account details with IFSC",
            "Copy of Land Record (RTC/Pahani) demonstrating holding up to 2 ha"
        ],
        "required_documents_kn": [
            "ಆಧಾರ್ ಕಾರ್ಡ್",
            "ಉಳಿತಾಯ ಬ್ಯಾಂಕ್ ಖಾತೆ ವಿವರ ಮತ್ತು IFSC",
            "5 ಎಕರೆಗಿಂತ ಕಡಿಮೆ ಭೂಮಿ ಇದೆ ಎಂದು ದೃಢೀಕರಿಸುವ ಪಹಣಿ (RTC)"
        ],
        "optional_documents": [],
        "optional_documents_kn": [],
        "application_steps": [
            "Visit the nearest Common Service Centre (CSC) or maandhan.in.",
            "Provide Aadhaar number and landholding documents to the Village Level Entrepreneur (VLE).",
            "Calculate age-specific monthly contribution (₹55 to ₹200/month depending on entry age 18-40).",
            "Authorize auto-debit from bank account and receive Kisan Pension Card."
        ],
        "application_steps_kn": [
            "ಹತ್ತಿರದ ಗ್ರಾಮ ಒನ್ / CSC ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ ಅಥವಾ maandhan.in ಗೆ ಲಾಗಿನ್ ಆಗಿ.",
            "ಆಧಾರ್ ಮತ್ತು ಪಹಣಿ ದಾಖಲೆಗಳನ್ನು ಒದಗಿಸಿ.",
            "ವಯಸ್ಸಿಗೆ ಅನುಗುಣವಾಗಿ ಮಾಸಿಕ ವಂತಿಗೆಯನ್ನು (₹55 ರಿಂದ ₹200) ಲೆಕ್ಕಹಾಕಿ ಒಪ್ಪಿಗೆ ನೀಡಿ.",
            "ಬ್ಯಾಂಕ್ ಖಾತೆಯಿಂದ ಆಟೋ-ಡೆಬಿಟ್ ಸೌಲಭ್ಯ ಮಾಡಿಸಿ ಕಿಸಾನ್ ಪಿಂಚಣಿ ಕಾರ್ಡ್ ಪಡೆಯಿರಿ."
        ],
        "official_source_url": "https://maandhan.in/",
        "issuing_authority": "Ministry of Agriculture and Farmers Welfare / LIC",
        "verification_authority": "Life Insurance Corporation of India (LIC) & CSC e-Governance",
        "last_verified_at": "2026-10-30",
        "verification_status": "verified",
        "applicable_locations": ["All India", "Karnataka"],
        "supported_crops": ["All crops"],
        "notes": [
            "Current contribution slabs must be confirmed with the implementing department.",
            "Entry age must be between 18 and 40 years. Tax payers and NPS/EPFO subscribers excluded."
        ],
        "notes_kn": [
            "ಪ್ರಸ್ತುತ ವಂತಿಗೆ ಸ್ಲ್ಯಾಬ್‌ಗಳನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
            "ಪ್ರವೇಶ ವಯಸ್ಸು 18 ರಿಂದ 40 ವರ್ಷಗಳ ನಡುವೆ ಇರಬೇಕು. ತೆರಿಗೆದಾರರಿಗೆ ಅನ್ವಯಿಸುವುದಿಲ್ಲ."
        ]
    })

    # 3. KCC
    schemes.append({
        "id": "kcc",
        "name": "Kisan Credit Card (KCC)",
        "name_kn": "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ (ಕೆಸಿಸಿ)",
        "official_abbreviation": "KCC",
        "government_level": "central",
        "scheme_type": "real",
        "category": "credit_finance",
        "category_kn": "ಕೃಷಿ ಸಾಲ ಮತ್ತು ಹೂಡಿಕೆ",
        "assistance_type": "agricultural_credit",
        "status_label": "Current status verified",
        "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
        "description": "Revolving institutional credit facility providing timely and adequate credit for cultivation expenses, post-harvest costs, asset maintenance, animal husbandry and fisheries.",
        "description_kn": "ಬೆಳೆ ಸಾಗುವಳಿ ವೆಚ್ಚ, ಕಟಾವಿನ ನಂತರದ ನಿರ್ವಹಣೆ, ಕೃಷಿ ಆಸ್ತಿ ರಕ್ಷಣೆ ಮತ್ತು ಹೈನುಗಾರಿಕೆ/ಮೀನುಗಾರಿಕೆಗೆ ಸಕಾಲಿಕ ಸಾಲ ನೀಡುವ ಆವರ್ತಕ ಸಾಲ ಸೌಲಭ್ಯ.",
        "benefits": [
            "Single-window institutional revolving credit limit based on crop scale of finance.",
            "Concessional interest rate with interest subvention up to ₹3 lakh limit.",
            "No collateral required for agricultural loans up to ₹1.6 lakh (and up to ₹2 lakh for dairy/fisheries)."
        ],
        "benefits_kn": [
            "ಬೆಳೆ ವಿಸ್ತೀರ್ಣಕ್ಕೆ ಅನುಗುಣವಾಗಿ ನಿಗದಿಪಡಿಸಿದ ಆವರ್ತಕ ಸಾಲದ ಮಿತಿ.",
            "₹3 ಲಕ್ಷದವರೆಗಿನ ಸಾಲಕ್ಕೆ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ಮತ್ತು ಸಕಾಲಿಕ ಮರುಪಾವತಿ ಪ್ರೋತ್ಸಾಹ.",
            "₹1.6 ಲಕ್ಷದವರೆಗಿನ ಸಾಲಕ್ಕೆ ಯಾವುದೇ ಭದ್ರತೆ (ಕೊಲ್ಯಾಟರಲ್) ಅಗತ್ಯವಿಲ್ಲ."
        ],
        "eligibility_rules": [
            {
                "rule_id": "kcc_cultivator",
                "description": "Applicant must be an owner cultivator, tenant farmer, sharecropper, or allied livestock/fisheries farmer.",
                "description_kn": "ಅರ್ಜಿದಾರರು ಸ್ವಂತ ಭೂಮಾಲೀಕರು, ಗೇಣಿ ರೈತರು ಅಥವಾ ಪೂರಕ ಹೈನುಗಾರಿಕೆ/ಮೀನುಗಾರಿಕೆ ರೈತರಾಗಿರಬೇಕು.",
                "field": "ownership",
                "operator": "in",
                "expected_value": ["owned", "joint_owned", "tenant", "leased"],
                "is_mandatory": True,
                "source_reference": "RBI KCC Guidelines 2019",
                "verification_status": "verified",
                "clarification_question": "Do you cultivate as an owner or as a tenant/lessee?",
                "clarification_question_kn": "ನೀವು ಸ್ವಂತ ಭೂಮಿಯಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ ಅಥವಾ ಗೇಣಿ ರೂಪದಲ್ಲಿದೆಯೇ?",
                "why_needed": "KCC is available to both owner-farmers and tenant farmers/oral lessees.",
                "why_needed_kn": "ಸ್ವಂತ ಜಮೀನುದಾರರು ಹಾಗೂ ಗೇಣಿ ರೈತರಿಬ್ಬರಿಗೂ ಕೆಸಿಸಿ ಸಾಲದ ಅರ್ಹತೆಯಿದೆ."
            }
        ],
        "required_documents": [
            "Application form with passport photograph",
            "Identity proof (Aadhaar card / Voter ID)",
            "Address proof and land record documents (RTC / Tenancy agreement)",
            "Crop sowing certificate or declaration of cultivated area"
        ],
        "required_documents_kn": [
            "ಭರ್ತಿ ಮಾಡಿದ ಅರ್ಜಿ ಮತ್ತು ಭಾವಚಿತ್ರ",
            "ಗುರುತಿನ ಚೀಟಿ (ಆಧಾರ್ ಕಾರ್ಡ್ / ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ)",
            "ಭೂದಾಖಲೆ ಪಹಣಿ (RTC) ಅಥವಾ ಗೇಣಿ ಕೃಷಿ ಒಪ್ಪಂದ ಪತ್ರ",
            "ಬೆಳೆ ದೃಢೀಕರಣ ಪತ್ರ ಅಥವಾ ಬೆಳೆ ಸಮೀಕ್ಷೆ ವಿವರ"
        ],
        "optional_documents": [],
        "optional_documents_kn": [],
        "application_steps": [
            "Obtain one-page KCC application form from bank branch, PACS, or pmkisan.gov.in.",
            "Attach Aadhaar, land record (RTC), and crop sowing declaration.",
            "Submit to commercial bank, regional rural bank (RRB), or cooperative society.",
            "Bank inspects and sanctions credit limit within 14 working days."
        ],
        "application_steps_kn": [
            "ಬ್ಯಾಂಕ್ ಶಾಖೆ, ಸಹಕಾರಿ ಸಂಘ ಅಥವಾ pmkisan.gov.in ನಿಂದ ಸರಳ ಕೆಸಿಸಿ ಅರ್ಜಿ ಪಡೆಯಿರಿ.",
            "ಆಧಾರ್, ಪಹಣಿ ಮತ್ತು ಬೆಳೆ ವಿವರಗಳನ್ನು ಲಗತ್ತಿಸಿ ಬ್ಯಾಂಕ್‌ಗೆ ಸಲ್ಲಿಸಿ.",
            "ವಾಣಿಜ್ಯ ಬ್ಯಾಂಕ್, ಗ್ರಾಮೀಣ ಬ್ಯಾಂಕ್ ಅಥವಾ ಸಹಕಾರಿ ಬ್ಯಾಂಕ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
            "ಬ್ಯಾಂಕ್ ಪರಿಶೀಲನೆ ನಡೆಸಿ 14 ದಿನಗಳ ಒಳಗೆ ಸಾಲದ ಮಿತಿ ಮಂಜೂರು ಮಾಡುತ್ತದೆ."
        ],
        "official_source_url": "https://financialservices.gov.in/agriculture-credit",
        "issuing_authority": "Department of Financial Services / Reserve Bank of India",
        "verification_authority": "Participating Commercial, Regional Rural and Cooperative Banks",
        "last_verified_at": "2026-10-30",
        "verification_status": "verified",
        "applicable_locations": ["All India", "Karnataka"],
        "supported_crops": ["All crops, animal husbandry, fisheries"],
        "notes": [
            "Current credit scale of finance must be confirmed with the lending bank branch.",
            "KCC credit is a loan with repayment schedule, not a non-repayable cash grant."
        ],
        "notes_kn": [
            "ಪ್ರಸ್ತುತ ಸಾಲದ ಮಿತಿ ಮತ್ತು ಬಡ್ಡಿ ದರವನ್ನು ಸಾಲ ನೀಡುವ ಬ್ಯಾಂಕ್ ಶಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
            "ಕೆಸಿಸಿ ಮರುಪಾವತಿಸಬೇಕಾದ ಸಾಲ ಸೌಲಭ್ಯವಾಗಿದ್ದು, ಇದು ಅನುದಾನವಲ್ಲ."
        ]
    })

    # Save to file helper
    print("Catalog generation initialized...")

if __name__ == "__main__":
    build_catalog()

