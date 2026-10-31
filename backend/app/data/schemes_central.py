from app.models.scheme import SchemeRecord, EligibilityRule, RuleOperator

def make_rule(rule_id, desc, desc_kn, field, operator, expected_value, mandatory=True, ref=None, status='verified', q=None, q_kn=None, why=None, why_kn=None):
    return {
        'rule_id': rule_id,
        'description': desc,
        'description_kn': desc_kn,
        'field': field,
        'operator': operator,
        'expected_value': expected_value,
        'is_mandatory': mandatory,
        'source_reference': ref,
        'verification_status': status,
        'clarification_question': q,
        'clarification_question_kn': q_kn,
        'why_needed': why,
        'why_needed_kn': why_kn
    }

def get_central_schemes():
    return [
        # 1. PM-KISAN
        {
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
                "₹6,000 per year paid in three equal four-monthly installments of ₹2,000 each.",
                "Direct Benefit Transfer (DBT) directly into the farmer's Aadhaar-linked bank account without intermediaries."
            ],
            "benefits_kn": [
                "ವರ್ಷಕ್ಕೆ ₹6,000 ಹಣವನ್ನು ತಲಾ ₹2,000 ರ ಮೂರು ಕಂತುಗಳಲ್ಲಿ (ಪ್ರತಿ 4 ತಿಂಗಳಿಗೊಮ್ಮೆ) ನೀಡಲಾಗುತ್ತದೆ.",
                "ಯಾವುದೇ ಮಧ್ಯವರ್ತಿಗಳಿಲ್ಲದೆ ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT) ಮೂಲಕ ರೈತರ ಆಧಾರ್ ಜೋಡಿತ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "eligibility_rules": [
                make_rule("pmk_ownership", "Farmer or family must possess cultivable landholding in their name (owner-cultivator).", "ರೈತ ಅಥವಾ ಕುಟುಂಬದ ಹೆಸರಿನಲ್ಲಿ ಸಾಗುವಳಿ ಮಾಡಬಹುದಾದ ಕೃಷಿ ಭೂಮಿ ಇರಬೇಕು (ಸ್ವಂತ ಭೂಮಾಲೀಕರು).", "ownership", "in", ["owned", "joint_owned"], True, "PM-KISAN Operational Guidelines Sec 2.1", "verified", "Do you own the land you cultivate, or is it on lease or tenancy?", "ನೀವು ಸಾಗುವಳಿ ಮಾಡುವ ಜಮೀನು ನಿಮ್ಮ ಸ್ವಂತದ್ದೇ ಅಥವಾ ಗುತ್ತಿಗೆಗೆ ಪಡೆದಿದ್ದೀರಾ?", "PM-KISAN guidelines specifically restrict income support to legal landholding title-holders.", "ಪಿಎಂ-ಕಿಸಾನ್ ಮಾರ್ಗಸೂಚಿಯಂತೆ ಸಾಗುವಳಿ ಭೂಮಿಯ ಕಾನೂನುಬದ್ಧ ಮಾಲೀಕರಿಗೆ ಮಾತ್ರ ಈ ನೆರವು ಸೀಮಿತವಾಗಿದೆ."),
                make_rule("pmk_state", "Applicable across all Indian States and Union Territories including Karnataka.", "ಕರ್ನಾಟಕ ಸೇರಿದಂತೆ ಭಾರತದ ಎಲ್ಲಾ ರಾಜ್ಯ ಮತ್ತು ಕೇಂದ್ರಾಡಳಿತ ಪ್ರದೇಶಗಳ ರೈತರಿಗೆ ಅನ್ವಯಿಸುತ್ತದೆ.", "location.state", "in", ["Karnataka", "karnataka", "KA", "All India"], True, "PM-KISAN Guidelines Sec 1", "verified", "Which state do you cultivate in?", "ನೀವು ಯಾವ ರಾಜ್ಯದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಿ?", "Required to identify jurisdiction and state land database (Bhoomi).", "ರಾಜ್ಯದ ಭೂಮಿ ಆರ್‌ಟಿಸಿ ದತ್ತಾಂಶ ಪರಿಶೀಲನೆಗೆ ರಾಜ್ಯದ ವಿವರ ಅಗತ್ಯವಿದೆ."),
                make_rule("pmk_land_exists", "Must hold cultivable land greater than 0 acres.", "0 ಎಕರೆಗಿಂತ ಹೆಚ್ಚು ಸಾಗುವಳಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು.", "land_area.value_acres", "greater_than", 0, True, "PM-KISAN Revised Guidelines 2019", "verified", "How much cultivable land do you hold?", "ನಿಮ್ಮಲ್ಲಿ ಎಷ್ಟು ಎಕರೆ ಸಾಗುವಳಿ ಭೂಮಿ ಇದೆ?", "Land record entry is mandatory to confirm legitimate farmer status.", "ಕಾನೂನುಬದ್ಧ ರೈತರೆಂದು ದೃಢೀಕರಿಸಲು ಕೃಷಿ ಭೂಮಿಯ ವಿವರ ಕಡ್ಡಾಯವಾಗಿದೆ.")
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
                "Institutional landholders, income-tax payers, and government employees are excluded."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಸಾಂಸ್ಥಿಕ ಭೂಮಾಲೀಕರು, ತೆರಿಗೆದಾರರು ಮತ್ತು ಸರ್ಕಾರಿ ಉದ್ಯೋಗಿಗಳಿಗೆ ಈ ಯೋಜನೆ ಅನ್ವಯಿಸುವುದಿಲ್ಲ."
            ]
        },

        # 2. PM-KMY
        {
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
            "description": "Voluntary contributory old-age pension for small and marginal farmers. Eligible subscribers receive an assured ₹3,000 monthly pension after turning 60 with matching central contribution.",
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
                make_rule("pmkmy_land_cap", "Cultivable landholding must not exceed 2 hectares (approx 5 acres).", "ಸಾಗುವಳಿ ಜಮೀನು 2 ಹೆಕ್ಟೇರ್ (ಸುಮಾರು 5 ಎಕರೆ) ಮೀರಬಾರದು.", "land_area.value_acres", "less_than_or_equal", 5.0, True, "PM-KMY Operational Guidelines Sec 3", "verified", "Is your total landholding 5 acres or less?", "ನಿಮ್ಮ ಒಟ್ಟು ಕೃಷಿ ಭೂಮಿ 5 ಎಕರೆ ಅಥವಾ ಅದಕ್ಕಿಂತ ಕಡಿಮೆಯಿದೆಯೇ?", "PM-KMY is strictly targeted at small and marginal farmers.", "ಪಿಎಂ-ಕೆಎಂವೈ ಯೋಜನೆಯು ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಮಾತ್ರ ಸೀಮಿತವಾಗಿದೆ.")
            ],
            "required_documents": [
                "Aadhaar card",
                "Savings bank account details with IFSC",
                "Land Record (RTC/Pahani) demonstrating holding up to 2 ha"
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
                "Provide Aadhaar and landholding documents to the operator.",
                "Calculate age-specific monthly contribution (₹55 to ₹200/month depending on entry age 18-40).",
                "Authorize auto-debit and obtain Kisan Pension Card."
            ],
            "application_steps_kn": [
                "ಹತ್ತಿರದ ಗ್ರಾಮ ಒನ್ / CSC ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ ಅಥವಾ maandhan.in ಗೆ ಲಾಗಿನ್ ಆಗಿ.",
                "ಆಧಾರ್ ಮತ್ತು ಪಹಣಿ ದಾಖಲೆಗಳನ್ನು ಒದಗಿಸಿ.",
                "ವಯಸ್ಸಿಗೆ ಅನುಗುಣವಾಗಿ ಮಾಸಿಕ ವಂತಿಗೆಯನ್ನು ಲೆಕ್ಕಹಾಕಿ ಒಪ್ಪಿಗೆ ನೀಡಿ.",
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
                "Current subsidy amount must be confirmed with the implementing department.",
                "Entry age is generally 18–40 years. Farmers covered by statutory social-security schemes and income-tax payers are excluded."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಪ್ರವೇಶ ವಯಸ್ಸು 18 ರಿಂದ 40 ವರ್ಷಗಳ ನಡುವೆ ಇರಬೇಕು. ತೆರಿಗೆದಾರರು ಮತ್ತು ಸಾಮಾಜಿಕ ಭದ್ರತಾ ಚಂದಾದಾರರಿಗೆ ಅನ್ವಯಿಸುವುದಿಲ್ಲ."
            ]
        },

        # 3. KCC
        {
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
            "description": "Revolving credit facility for cultivation expenses, post-harvest costs, produce marketing, household maintenance, and animal husbandry/fisheries working capital.",
            "description_kn": "ಬೆಳೆ ಸಾಗುವಳಿ ವೆಚ್ಚ, ಕಟಾವಿನ ನಂತರದ ನಿರ್ವಹಣೆ, ಕೃಷಿ ಆಸ್ತಿ ರಕ್ಷಣೆ ಮತ್ತು ಹೈನುಗಾರಿಕೆ/ಮೀನುಗಾರಿಕೆಗೆ ಸಕಾಲಿಕ ಸಾಲ ನೀಡುವ ಆವರ್ತಕ ಸಾಲ ಸೌಲಭ್ಯ.",
            "benefits": [
                "Single-window institutional revolving credit limit based on crop scale of finance.",
                "Concessional interest rate with interest subvention up to ₹3 lakh limit.",
                "Collateral-free agricultural loans up to ₹1.6 lakh (and up to ₹2 lakh for dairy/fisheries)."
            ],
            "benefits_kn": [
                "ಬೆಳೆ ವಿಸ್ತೀರ್ಣಕ್ಕೆ ಅನುಗುಣವಾಗಿ ನಿಗದಿಪಡಿಸಿದ ಆವರ್ತಕ ಸಾಲದ ಮಿತಿ.",
                "₹3 ಲಕ್ಷದವರೆಗಿನ ಸಾಲಕ್ಕೆ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ಮತ್ತು ಸಕಾಲಿಕ ಮರುಪಾವತಿ ಪ್ರೋತ್ಸಾಹ.",
                "₹1.6 ಲಕ್ಷದವರೆಗಿನ ಸಾಲಕ್ಕೆ ಯಾವುದೇ ಭದ್ರತೆ (ಕೊಲ್ಯಾಟರಲ್) ಅಗತ್ಯವಿಲ್ಲ."
            ],
            "eligibility_rules": [
                make_rule("kcc_cultivator", "Applicant must be an owner cultivator, tenant farmer, sharecropper, or allied livestock/fisheries farmer.", "ಅರ್ಜಿದಾರರು ಸ್ವಂತ ಭೂಮಾಲೀಕರು, ಗೇಣಿ ರೈತರು ಅಥವಾ ಪೂರಕ ಹೈನುಗಾರಿಕೆ/ಮೀನುಗಾರಿಕೆ ರೈತರಾಗಿರಬೇಕು.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "RBI KCC Guidelines 2019", "verified", "Do you cultivate as an owner or as a tenant/lessee?", "ನೀವು ಸ್ವಂತ ಭೂಮಿಯಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ ಅಥವಾ ಗೇಣಿ ರೂಪದಲ್ಲಿದೆಯೇ?", "KCC is available to both owner-farmers and tenant farmers/oral lessees.", "ಸ್ವಂತ ಜಮೀನುದಾರರು ಹಾಗೂ ಗೇಣಿ ರೈತರಿಬ್ಬರಿಗೂ ಕೆಸಿಸಿ ಸಾಲದ ಅರ್ಹತೆಯಿದೆ.")
            ],
            "required_documents": [
                "Application form with passport photograph",
                "Identity and address proof (Aadhaar / Voter ID)",
                "Land record documents (RTC / Tenancy agreement)",
                "Crop sowing declaration"
            ],
            "required_documents_kn": [
                "ಭರ್ತಿ ಮಾಡಿದ ಅರ್ಜಿ ಮತ್ತು ಭಾವಚಿತ್ರ",
                "ಗುರುತಿನ ಮತ್ತು ವಿಳಾಸ ಚೀಟಿ (ಆಧಾರ್ ಕಾರ್ಡ್)",
                "ಭೂದಾಖಲೆ ಪಹಣಿ (RTC) ಅಥವಾ ಗೇಣಿ ಕೃಷಿ ಒಪ್ಪಂದ ಪತ್ರ",
                "ಬೆಳೆ ದೃಢೀಕರಣ ಪತ್ರ ಅಥವಾ ಬೆಳೆ ಸಮೀಕ್ಷೆ ವಿವರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Obtain KCC application from participating commercial, regional rural or cooperative bank.",
                "Submit with land/tenancy records and crop details.",
                "Bank assesses scale of finance and sanctions credit limit within 14 working days."
            ],
            "application_steps_kn": [
                "ವಾಣಿಜ್ಯ ಬ್ಯಾಂಕ್, ಗ್ರಾಮೀಣ ಬ್ಯಾಂಕ್ ಅಥವಾ ಸಹಕಾರಿ ಬ್ಯಾಂಕ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಪಹಣಿ ಮತ್ತು ಬೆಳೆ ವಿವರಗಳನ್ನು ಲಗತ್ತಿಸಿ ಸಲ್ಲಿಸಿ.",
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
                "Current credit limit and interest terms must be confirmed with the lending bank branch.",
                "KCC is a credit facility, not a grant."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಾಲದ ಮಿತಿ ಮತ್ತು ಬಡ್ಡಿ ದರವನ್ನು ಸಾಲ ನೀಡುವ ಬ್ಯಾಂಕ್ ಶಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಕೆಸಿಸಿ ಮರುಪಾವತಿಸಬೇಕಾದ ಸಾಲ ಸೌಲಭ್ಯವಾಗಿದ್ದು, ಇದು ಅನುದಾನವಲ್ಲ."
            ]
        },

        # 4. MISS
        {
            "id": "miss",
            "name": "Modified Interest Subvention Scheme (MISS)",
            "name_kn": "ಮಾರ್ಪಡಿಸಿದ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ಯೋಜನೆ (ಎಂಐಎಸ್‌ಎಸ್)",
            "official_abbreviation": "MISS",
            "government_level": "central",
            "scheme_type": "real",
            "category": "credit_finance",
            "category_kn": "ಕೃಷಿ ಸಾಲ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ",
            "assistance_type": "agricultural_credit",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Provides interest relief on eligible short-term agricultural crop loans up to ₹3 lakh through KCC lending, with additional prompt-repayment incentive reducing effective borrowing cost.",
            "description_kn": "ಕೆಸಿಸಿ ಮೂಲಕ ಪಡೆದ ₹3 ಲಕ್ಷದವರೆಗಿನ ಅಲ್ಪಾವಧಿ ಬೆಳೆ ಸಾಲಕ್ಕೆ ಕೇಂದ್ರ ಸರ್ಕಾರದ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ಮತ್ತು ಸಕಾಲಿಕ ಮರುಪಾವತಿಗೆ ಹೆಚ್ಚುವರಿ ಪ್ರೋತ್ಸಾಹಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Standard 1.5% interest subvention to lending institutions on short-term crop loans up to ₹3 lakh.",
                "Additional 3% Prompt Repayment Incentive (PRI) for farmers who repay on time, bringing net interest down to 4%."
            ],
            "benefits_kn": [
                "₹3 ಲಕ್ಷದವರೆಗಿನ ಅಲ್ಪಾವಧಿ ಬೆಳೆ ಸಾಲಕ್ಕೆ ಶೇ 1.5 ಬಡ್ಡಿ ಸಹಾಯಧನ.",
                "ಸಕಾಲದಲ್ಲಿ ಸಾಲ ಮರುಪಾವತಿಸುವ ರೈತರಿಗೆ ಶೇ 3 ರಷ್ಟು ಹೆಚ್ಚುವರಿ ಪ್ರೋತ್ಸಾಹಧನ, ಪರಿಣಾಮವಾಗಿ ನಿವ್ವಳ ಬಡ್ಡಿ ಶೇ 4 ಕ್ಕೆ ಇಳಿಕೆಯಾಗುತ್ತದೆ."
            ],
            "eligibility_rules": [
                make_rule("miss_crop_loan", "Applicant must hold an active short-term crop loan through a participating bank or cooperative.", "ಅರ್ಜಿದಾರರು ಮಾನ್ಯತೆ ಪಡೆದ ಬ್ಯಾಂಕ್ ಅಥವಾ ಸಹಕಾರಿ ಸಂಘದಲ್ಲಿ ಸಕ್ರಿಯ ಅಲ್ಪಾವಧಿ ಬೆಳೆ ಸಾಲ ಹೊಂದಿರಬೇಕು.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "DA&FW MISS Guidelines", "verified", "Do you hold an active agricultural crop loan?", "ನೀವು ಸಕ್ರಿಯ ಕೃಷಿ ಬೆಳೆ ಸಾಲ ಹೊಂದಿದ್ದೀರಾ?", "Benefit depends on loan purpose and repayment within stipulated due date.", "ಸಾಲದ ಉದ್ದೇಶ ಮತ್ತು ನಿಗದಿತ ದಿನಾಂಕದೊಳಗೆ ಮರುಪಾವತಿ ಮಾಡುವುದರ ಮೇಲೆ ಇದು ಅವಲಂಬಿತವಾಗಿದೆ.")
            ],
            "required_documents": [
                "Active KCC loan account documents",
                "Prompt repayment acknowledgement from lender",
                "Land cultivation certificate"
            ],
            "required_documents_kn": [
                "ಸಕ್ರಿಯ ಕೆಸಿಸಿ ಸಾಲ ಖಾತೆ ದಾಖಲೆ",
                "ಬ್ಯಾಂಕ್ ಮರುಪಾವತಿ ರಶೀದಿ",
                "ಸಾಗುವಳಿ ದೃಢೀಕರಣ ಪತ್ರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Apply automatically through the bank that issues the crop loan/KCC.",
                "Repay the crop loan on or before the notified due date.",
                "The lending bank credits the prompt repayment incentive directly to the account."
            ],
            "application_steps_kn": [
                "ಕೆಸಿಸಿ ಸಾಲ ನೀಡಿದ ಬ್ಯಾಂಕ್ ಮೂಲಕವೇ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅನ್ವಯವಾಗುತ್ತದೆ.",
                "ನಿಗದಿತ ಗಡುವಿನೊಳಗೆ ಬೆಳೆ ಸಾಲವನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಮರುಪಾವತಿಸಿ.",
                "ಬ್ಯಾಂಕ್ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ಮೊತ್ತವನ್ನು ನೇರವಾಗಿ ನಿಮ್ಮ ಖಾತೆಗೆ ಜಮೆ ಮಾಡುತ್ತದೆ."
            ],
            "official_source_url": "https://financialservices.gov.in/agriculture-credit",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare / RBI / NABARD",
            "verification_authority": "Lending Banks and Primary Agricultural Credit Societies",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Notified seasonal crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Benefit is linked to timely loan repayment within the financial year. Overdue loans lose the incentive."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಗಡುವು ಮೀರಿದ ಸಾಲಗಳಿಗೆ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ಸೌಲಭ್ಯ ರದ್ದಾಗುತ್ತದೆ."
            ]
        },

        # 5. AIF
        {
            "id": "aif",
            "name": "Agriculture Infrastructure Fund (AIF)",
            "name_kn": "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ನಿಧಿ (ಎಐಎಫ್)",
            "official_abbreviation": "AIF",
            "government_level": "central",
            "scheme_type": "real",
            "category": "credit_finance",
            "category_kn": "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ನಿಧಿ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Medium/long-term financing facility for post-harvest management infrastructure and community farming assets with 3% interest subvention on loans up to ₹2 crore for up to 7 years.",
            "description_kn": "ಕಟಾವಿನ ನಂತರದ ಸಂಸ್ಕರಣೆ, ಗೋದಾಮು, ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್ ಮತ್ತು ಸಮುದಾಯ ಕೃಷಿ ಆಸ್ತಿ ನಿರ್ಮಾಣಕ್ಕೆ ₹2 ಕೋಟಿವರೆಗಿನ ಸಾಲಕ್ಕೆ ಶೇ 3 ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "3% per annum interest subvention on bank term loans up to ₹2 crore for up to 7 years.",
                "Credit guarantee coverage under CGTMSE for loans up to ₹2 crore without collateral."
            ],
            "benefits_kn": [
                "₹2 ಕೋಟಿವರೆಗಿನ ಬ್ಯಾಂಕ್ ಸಾಲಕ್ಕೆ ವಾರ್ಷಿಕ ಶೇ 3 ಬಡ್ಡಿ ರಿಯಾಯಿತಿ (7 ವರ್ಷಗಳವರೆಗೆ).",
                "₹2 ಕೋಟಿವರೆಗಿನ ಸಾಲಕ್ಕೆ ಸಿಜಿಟಿಎಂಎಸ್‌ಇ ಅಡಿಯಲ್ಲಿ ಕ್ರೆಡಿಟ್ ಗ್ಯಾರಂಟಿ ರಕ್ಷಣೆ."
            ],
            "eligibility_rules": [
                make_rule("aif_entity", "Applicant must be an individual farmer, FPO, PACS, SHG, cooperative, or agri-entrepreneur undertaking post-harvest infrastructure.", "ಅರ್ಜಿದಾರರು ರೈತರು, ಎಫ್‌ಪಿಒ, ಪಿಎಸಿಎಸ್, ಸ್ವಸಹಾಯ ಗುಂಪು ಅಥವಾ ಕೃಷಿ ಉದ್ಯಮಿಯಾಗಿರಬೇಕು.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "AIF Guidelines Sec 4", "verified", "Are you establishing post-harvest storage or processing infrastructure?", "ನೀವು ಕಟಾವಿನ ನಂತರದ ಗೋದಾಮು ಅಥವಾ ಸಂಸ್ಕರಣಾ ಮೂಲಸೌಕರ್ಯ ನಿರ್ಮಿಸುತ್ತಿದ್ದೀರಾ?", "The lender must appraise project viability and eligibility.", "ಬ್ಯಾಂಕ್ ಯೋಜನೆಯ ಕಾರ್ಯಸಾಧ್ಯತೆಯನ್ನು ಪರಿಶೀಲಿಸುವುದು ಕಡ್ಡಾಯವಾಗಿದೆ.")
            ],
            "required_documents": [
                "Detailed Project Report (DPR)",
                "Land ownership or registered lease agreement for project site",
                "Entity registration / KYC documents",
                "Bank loan sanction letter"
            ],
            "required_documents_kn": [
                "ವಿವರವಾದ ಯೋಜನಾ ವರದಿ (DPR)",
                "ಯೋಜನಾ ಜಾಗದ ಮಾಲೀಕತ್ವ ಅಥವಾ ನೋಂದಾಯಿತ ಗುತ್ತಿಗೆ ಪತ್ರ",
                "ಕೆವೈಸಿ ಮತ್ತು ಸಂಸ್ಥೆ ನೋಂದಣಿ ದಾಖಲೆಗಳು",
                "ಬ್ಯಾಂಕ್ ಸಾಲ ಮಂಜೂರಾತಿ ಪತ್ರ"
            ],
            "optional_documents": ["Pollution / local body trade license (where required)"],
            "optional_documents_kn": ["ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಯ ಪರವಾನಗಿ"],
            "application_steps": [
                "Prepare project report for eligible infrastructure (warehouse, cold chain, packhouse).",
                "Register and submit online application at agriinfra.dac.gov.in.",
                "Ministry verifies online eligibility and routes to selected commercial/cooperative bank.",
                "Bank sanctions loan and disburses with interest subvention."
            ],
            "application_steps_kn": [
                "ಅರ್ಹ ಯೋಜನೆಗೆ (ಗೋದಾಮು, ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್) ಡಿಪಿಆರ್ ಸಿದ್ಧಪಡಿಸಿ.",
                "agriinfra.dac.gov.in ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಕೇಂದ್ರ ಕೃಷಿ ಸಚಿವಾಲಯ ಪರಿಶೀಲಿಸಿ ಆಯ್ಕೆ ಮಾಡಿದ ಬ್ಯಾಂಕ್‌ಗೆ ರವಾನಿಸುತ್ತದೆ.",
                "ಬ್ಯಾಂಕ್ ಸಾಲ ಮಂಜೂರು ಮಾಡಿ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ಸೌಲಭ್ಯ ನೀಡುತ್ತದೆ."
            ],
            "official_source_url": "https://agriinfra.dac.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "National Implementation Management Unit (NIMU) / Lending Banks",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["All horticultural and agricultural commodities"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Credit-linked support, not an unrestricted grant for individual spending."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ಸಾಲ ಆಧಾರಿತ ಬಡ್ಡಿ ರಿಯಾಯಿತಿ ಯೋಜನೆಯಾಗಿದ್ದು ನೇರ ನಗದು ಅನುದಾನವಲ್ಲ."
            ]
        },

        # 6. PMFBY
        {
            "id": "pmfby",
            "name": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
            "name_kn": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಫಸಲ್ ಬಿಮಾ ಯೋಜನೆ (ಪಿಎಂಎಫ್‌ಬಿವೈ)",
            "official_abbreviation": "PMFBY",
            "government_level": "central",
            "scheme_type": "real",
            "category": "crop_insurance",
            "category_kn": "ಬೆಳೆ ವಿಮೆ",
            "assistance_type": "crop_insurance",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Comprehensive yield-based crop insurance scheme covering non-preventable natural risks from pre-sowing to post-harvest for notified crops.",
            "description_kn": "ಬಿತ್ತನೆಯಿಂದ ಕಟಾವಿನ ನಂತರದವರೆಗೆ ಹವಾಮಾನ ವೈಪರೀತ್ಯ, ರೋಗಬಾಧೆ ಹಾಗೂ ನೈಸರ್ಗಿಕ ವಿಕೋಪಗಳಿಂದ ಉಂಟಾಗುವ ಬೆಳೆ ನಷ್ಟಕ್ಕೆ ಪರಿಹಾರ ನೀಡುವ ರಾಷ್ಟ್ರೀಯ ಬೆಳೆ ವಿಮೆ ಯೋಜನೆ.",
            "benefits": [
                "Uniform low premium rates: 2.0% for Kharif food grains/oilseeds, 1.5% for Rabi crops, and 5.0% for annual commercial/horticultural crops.",
                "Balance actuarial premium subsidized equally by Central and State Governments.",
                "Coverage for prevented sowing, mid-season adversity, post-harvest losses, and localized calamities."
            ],
            "benefits_kn": [
                "ರೈತರಿಗೆ ಅತ್ಯಂತ ಕಡಿಮೆ ಪ್ರೀಮಿಯಂ ದರ: ಮುಂಗಾರಿಗೆ ಶೇ 2.0, ಹಿಂಗಾರಿಗೆ ಶೇ 1.5 ಮತ್ತು ತೋಟಗಾರಿಕೆಗೆ ಶೇ 5.0.",
                "ಉಳಿದ ಪ್ರೀಮಿಯಂ ಮೊತ್ತವನ್ನು ಕೇಂದ್ರ ಮತ್ತು ರಾಜ್ಯ ಸರ್ಕಾರಗಳು ಸಮಾನವಾಗಿ ಭರಿಸುತ್ತವೆ.",
                "ಬಿತ್ತನೆ ವಿಫಲತೆ, ಕಟಾವಿನ ನಂತರದ ನಷ್ಟ ಹಾಗೂ ಸ್ಥಳೀಯ ವಿಕೋಪಗಳಿಗೆ ಪರಿಹಾರ ದೊರೆಯುತ್ತದೆ."
            ],
            "eligibility_rules": [
                make_rule("pmfby_notified_crop", "Crop must be notified in the relevant district/taluk insurance unit for the current season.", "ಪ್ರಸ್ತುತ ಹಂಗಾಮಿಗೆ ನಿಮ್ಮ ತಾಲೂಕು/ಗ್ರಾಮ ಪಂಚಾಯಿತಿಯಲ್ಲಿ ಬೆಳೆಯು ಅಧಿಸೂಚಿತವಾಗಿರಬೇಕು.", "crops", "any_of", ["paddy", "arecanut", "sugarcane", "maize", "ragi", "groundnut", "cotton", "bhatta", "adike", "kabbu", "jola", "cotton", "pulses", "soybean"], True, "PMFBY Revamped Guidelines 2020", "verified", "Which crops are you cultivating this season?", "ಈ ಹಂಗಾಮಿನಲ್ಲಿ ನೀವು ಯಾವ ಬೆಳೆಗಳನ್ನು ಬೆಳೆಯುತ್ತಿದ್ದೀರಿ?", "Insurance coverage applies exclusively to crops notified in the gazette for that insurance unit.", "ಅಧಿಸೂಚಿತ ವಿಮಾ ಘಟಕದಲ್ಲಿ ಗೆಜೆಟ್ ಅಧಿಸೂಚನೆ ಹೊರಡಿಸಿದ ಬೆಳೆಗಳಿಗೆ ಮಾತ್ರ ವಿಮೆ ಅನ್ವಯಿಸುತ್ತದೆ."),
                make_rule("pmfby_cultivator", "Open to all cultivators including owner-farmers, tenant farmers, and sharecroppers with insurable interest.", "ಸ್ವಂತ ಜಮೀನುದಾರರು, ಗೇಣಿ ರೈತರು ಮತ್ತು ಪಾಲುದಾರರು ಸೇರಿದಂತೆ ಬೆಳೆ ಹಾನಿಯ ಹೊಣೆಗಾರಿಕೆ ಹೊಂದಿರುವ ಎಲ್ಲರಿಗೂ ಮುಕ್ತವಾಗಿದೆ.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "PMFBY Guidelines Sec 3.1", "verified", "What is your land ownership or tenancy arrangement?", "ನಿಮ್ಮ ಭೂ ಮಾಲೀಕತ್ವ ಅಥವಾ ಗೇಣಿ ವ್ಯವಸ್ಥೆ ಹೇಗಿದೆ?", "Tenant farmers and sharecroppers are fully eligible if state-accepted cultivation proof is provided.", "ಗೇಣಿ ಕೃಷಿ ದೃಢೀಕರಣ ಪತ್ರ ಒದಗಿಸಿದರೆ ಗೇಣಿ ರೈತರಿಗೂ ಬೆಳೆ ವಿಮೆ ಲಭ್ಯವಿರುತ್ತದೆ.")
            ],
            "required_documents": [
                "Aadhaar card of the farmer",
                "Land Record Pahani (RTC) with crop entry or tenancy agreement",
                "Bank passbook copy with clear account and IFSC details",
                "Crop Sowing Certificate / Declaration"
            ],
            "required_documents_kn": [
                "ರೈತರ ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಚಾಲ್ತಿಯಲ್ಲಿರುವ ಪಹಣಿ (RTC) ಅಥವಾ ಗೇಣಿ ಒಪ್ಪಂದ ಪತ್ರ",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಜೆರಾಕ್ಸ್ (IFSC ಕೋಡ್ ಸಮೇತ)",
                "ಬೆಳೆ ದೃಢೀಕರಣ ಪತ್ರ / ಬೆಳೆ ಸಮೀಕ್ಷೆ ವಿವರ"
            ],
            "optional_documents": ["Crop loss intimation within 72 hours for localized calamities"],
            "optional_documents_kn": ["ಸ್ಥಳೀಯ ವಿಕೋಪದ ಸಂದರ್ಭದಲ್ಲಿ 72 ಗಂಟೆಯೊಳಗೆ ಬೆಳೆ ನಷ್ಟ ವರದಿ"],
            "application_steps": [
                "Check notification cutoff dates for your crop and district at pmfby.gov.in or Samrakshane.",
                "Visit bank branch, PACS, CSC, or register directly on the PMFBY portal.",
                "Pay farmer share of premium (1.5% to 5%) before the seasonal deadline.",
                "Obtain and preserve policy receipt and application acknowledgement."
            ],
            "application_steps_kn": [
                "pmfby.gov.in ಅಥವಾ ಸಂರಕ್ಷಣೆ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಕೊನೆಯ ದಿನಾಂಕ ಪರಿಶೀಲಿಸಿ.",
                "ಬ್ಯಾಂಕ್, ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರಿ ಸಂಘ ಅಥವಾ ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.",
                "ನಿಗದಿತ ಕಟ್-ಆಫ್ ದಿನಾಂಕದೊಳಗೆ ಪ್ರೀಮಿಯಂ ಮೊತ್ತ ಪಾವತಿಸಿ.",
                "ವಿಮಾ ರಸೀದಿ ಮತ್ತು ಅರ್ಜಿ ಸ್ವೀಕೃತಿ ಪತ್ರವನ್ನು ಸುರಕ್ಷಿತವಾಗಿಟ್ಟುಕೊಳ್ಳಿ."
            ],
            "official_source_url": "https://pmfby.gov.in/",
            "issuing_authority": "Ministry of Agriculture & Farmers Welfare / Government of Karnataka",
            "verification_authority": "Department of Agriculture / Empanelled General Insurance Companies",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Paddy", "Arecanut", "Maize", "Ragi", "Groundnut", "Sugarcane", "Cotton", "Pulses"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Enrolment is voluntary. Crop loss claims must be reported within 72 hours via Crop Insurance App or helpline."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಬೆಳೆ ನಷ್ಟ ಸಂಭವಿಸಿದಲ್ಲಿ 72 ಗಂಟೆಗಳ ಒಳಗೆ ಕ್ರಾಪ್ ಇನ್ಶೂರೆನ್ಸ್ ಆ್ಯಪ್ ಅಥವಾ ಟೋಲ್ ಫ್ರೀ ಸಂಖ್ಯೆ ಮೂಲಕ ಮಾಹಿತಿ ನೀಡುವುದು ಕಡ್ಡಾಯ."
            ]
        },

        # 7. RWBCIS
        {
            "id": "rwbcis",
            "name": "Restructured Weather Based Crop Insurance Scheme (RWBCIS)",
            "name_kn": "ಹವಾಮಾನ ಆಧಾರಿತ ಬೆಳೆ ವಿಮೆ ಯೋಜನೆ (ಆರ್‌ಡಬ್ಲ್ಯೂಬಿಸಿಐಎಸ್)",
            "official_abbreviation": "RWBCIS",
            "government_level": "central",
            "scheme_type": "real",
            "category": "crop_insurance",
            "category_kn": "ಹವಾಮಾನ ಆಧಾರಿತ ಬೆಳೆ ವಿಮೆ",
            "assistance_type": "crop_insurance",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Weather-index insurance that pays according to pre-defined weather triggers such as rainfall, temperature, humidity or wind during specified crop stages.",
            "description_kn": "ಮಳೆ ಕೊರತೆ, ಅತಿಯಾದ ಉಷ್ಣಾಂಶ, ಆರ್ದ್ರತೆ ಅಥವಾ ಬಿರುಗಾಳಿಯಂತಹ ಹವಾಮಾನ ಮಾನದಂಡಗಳ ಆಧಾರದ ಮೇಲೆ ಪೂರ್ವನಿರ್ಧರಿತ ಹಂತಗಳಲ್ಲಿ ಪರಿಹಾರ ಒದಗಿಸುವ ಹವಾಮಾನ ಆಧಾರಿತ ಬೆಳೆ ವಿಮೆ.",
            "benefits": [
                "Fast, objective settlement based on automatic weather station (AWS) data without waiting for crop-cutting experiments.",
                "Covers adverse weather deviations for sensitive commercial and horticultural crops."
            ],
            "benefits_kn": [
                "ಬೆಳೆ ಕಟಾವು ಪ್ರಯೋಗಗಳಿಗೆ ಕಾಯದೆ ಹವಾಮಾನ ಮಾಪನ ಕೇಂದ್ರದ (AWS) ದತ್ತಾಂಶದ ಆಧಾರದ ಮೇಲೆ ಶೀಘ್ರ ಪರಿಹಾರ ಪಾವತಿ.",
                "ಹವಾಮಾನ ವೈಪರೀತ್ಯಗಳಿಗೆ ಸೂಕ್ಷ್ಮವಾಗಿರುವ ವಾಣಿಜ್ಯ ಮತ್ತು ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳಿಗೆ ರಕ್ಷಣೆ."
            ],
            "eligibility_rules": [
                make_rule("rwbcis_notified_area", "Applicant must cultivate notified horticultural or commercial crops within reference weather station jurisdiction.", "ಅರ್ಜಿದಾರರು ಮಾನ್ಯತೆ ಪಡೆದ ಹವಾಮಾನ ಕೇಂದ್ರದ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಅಧಿಸೂಚಿತ ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳನ್ನು ಬೆಳೆಯುತ್ತಿರಬೇಕು.", "crops", "any_of", ["arecanut", "pepper", "mango", "pomegranate", "banana", "grapes", "adike", "mavina", "bale"], True, "RWBCIS Guidelines", "verified", "Do you cultivate notified horticultural/plantation crops in the notified block?", "ನೀವು ಅಧಿಸೂಚಿತ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ತೋಟಗಾರಿಕಾ ಬೆಳೆ ಬೆಳೆಯುತ್ತಿದ್ದೀರಾ?", "Triggers are strictly mapped to designated Reference Weather Stations (RWS).", "ಹವಾಮಾನ ಮಾನದಂಡಗಳು ನಿರ್ದಿಷ್ಟ ಹವಾಮಾನ ಕೇಂದ್ರಗಳಿಗೆ ಜೋಡಣೆಯಾಗಿರುತ್ತವೆ.")
            ],
            "required_documents": [
                "Aadhaar card",
                "Land Pahani (RTC) showing perennial or notified crop entry",
                "Bank passbook details with IFSC code"
            ],
            "required_documents_kn": [
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ತೋಟಗಾರಿಕಾ ಬೆಳೆ ನಮೂದಾಗಿರುವ ಪಹಣಿ (RTC)",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ವಿವರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Check notification for your district and horticultural crop.",
                "Enrol via Samrakshane portal, bank, or authorised insurer before cut-off date.",
                "Claims are automatically calculated based on AWS weather trigger deviations."
            ],
            "application_steps_kn": [
                "ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ತೋಟಗಾರಿಕಾ ಬೆಳೆ ಅಧಿಸೂಚನೆ ಪರಿಶೀಲಿಸಿ.",
                "ಸಂರಕ್ಷಣೆ ಪೋರ್ಟಲ್ ಅಥವಾ ಬ್ಯಾಂಕ್ ಮೂಲಕ ಕಟ್-ಆಫ್ ದಿನಾಂಕದೊಳಗೆ ನೋಂದಾಯಿಸಿ.",
                "ಹವಾಮಾನ ವ್ಯತ್ಯಾಸವಾದಾಗ ಪರಿಹಾರವು ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://pmfby.gov.in/",
            "issuing_authority": "Ministry of Agriculture & Farmers Welfare / Horticulture Dept",
            "verification_authority": "Karnataka State Natural Disaster Monitoring Centre (KSNDMC) / Insurers",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Arecanut", "Mango", "Pomegranate", "Banana", "Grapes", "Pepper"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Unlike conventional yield insurance, settlement is based on recorded weather parameters and notified thresholds."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ಹವಾಮಾನ ಕೇಂದ್ರದ ಅಂಕಿಅಂಶಗಳ ಆಧಾರದ ಮೇಲೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ."
            ]
        },

        # 8. PM-AASHA
        {
            "id": "pm-aasha",
            "name": "Pradhan Mantri Annadata Aay Sanraksan Abhiyan (PM-AASHA)",
            "name_kn": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಅನ್ನದಾತ ಆಯ ಸಂರಕ್ಷಣಾ ಅಭಿಯಾನ (ಪಿಎಂ-ಆಶಾ)",
            "official_abbreviation": "PM-AASHA",
            "government_level": "central",
            "scheme_type": "real",
            "category": "procurement_price_support",
            "category_kn": "ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ",
            "assistance_type": "procurement_price_support",
            "status_label": "Seasonal application",
            "status_label_kn": "ಹಂಗಾಮುವಾರು ಅರ್ಜಿ",
            "description": "Umbrella price-support programme to help farmers obtain remunerative prices for pulses, oilseeds and copra through physical procurement (PSS) and price deficiency payment (PDPS).",
            "description_kn": "ದ್ವಿದಳ ಧಾನ್ಯ, ಎಣ್ಣೆಕಾಳು ಮತ್ತು ಕೊಬ್ಬರಿ ಬೆಳೆಗಾರರಿಗೆ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ (MSP) ಖಾತರಿಪಡಿಸುವ ಸಮಗ್ರ ಬೆಲೆ ಬೆಂಬಲ ಯೋಜನೆ.",
            "benefits": [
                "Guaranteed procurement at Minimum Support Price (MSP) during market distress.",
                "Direct payment into farmer's bank account for FAQ-grade produce within notified procurement period."
            ],
            "benefits_kn": [
                "ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ದರ ಕುಸಿದಾಗ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆಯಲ್ಲಿ (MSP) ಕಡ್ಡಾಯ ಖರೀದಿ.",
                "ಗುಣಮಟ್ಟದ ಉತ್ಪನ್ನಕ್ಕೆ ನೇರವಾಗಿ ರೈತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಬೆಂಬಲ ಬೆಲೆ ಜಮೆ."
            ],
            "eligibility_rules": [
                make_rule("pmaasha_crop", "Must produce notified pulses, oilseeds or copra registered in the seasonal procurement window.", "ಅಧಿಸೂಚಿತ ದ್ವಿದಳ ಧಾನ್ಯ, ಎಣ್ಣೆಕಾಳು ಅಥವಾ ಕೊಬ್ಬರಿ ಬೆಳೆಗಳನ್ನು ಬೆಳೆದಿರಬೇಕು.", "crops", "any_of", ["pulses", "oilseeds", "groundnut", "soybean", "copra", "coconut", "bengal gram", "tur", "urad", "tengu"], True, "PM-AASHA Guidelines", "verified", "Are you selling notified pulses, oilseeds, or copra?", "ನೀವು ಅಧಿಸೂಚಿತ ಬೇಳೆಕಾಳು, ಎಣ್ಣೆಕಾಳು ಅಥವಾ ಕೊಬ್ಬರಿ ಮಾರಾಟ ಮಾಡುತ್ತಿದ್ದೀರಾ?", "Registration at the designated procurement agency or mandi before notified date is mandatory.", "ನಿಗದಿತ ದಿನಾಂಕದೊಳಗೆ ಖರೀದಿ ಕೇಂದ್ರದಲ್ಲಿ ರೈತರ ನೋಂದಣಿ ಕಡ್ಡಾಯವಾಗಿದೆ.")
            ],
            "required_documents": [
                "Farmer ID / FRUITS registration",
                "RTC/Pahani showing verified crop survey entry",
                "Aadhaar-linked bank passbook",
                "Quality inspection weighment slip"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಸಂಖ್ಯೆ (FID / FRUITS)",
                "ಬೆಳೆ ಸಮೀಕ್ಷೆ ನಮೂದಾಗಿರುವ ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಜೋಡಿತ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್",
                "ಖರೀದಿ ಕೇಂದ್ರದ ತೂಕದ ರಸೀದಿ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Register on the state procurement portal / APMC yard during the announced window.",
                "Produce must meet Fair Average Quality (FAQ) parameters.",
                "Deliver to designated procurement center, obtain weighment receipt, and receive DBT payment."
            ],
            "application_steps_kn": [
                "ಖರೀದಿ ಅವಧಿಯಲ್ಲಿ ಎಪಿಎಂಸಿ ಅಥವಾ ಖರೀದಿ ಕೇಂದ್ರದಲ್ಲಿ ಹೆಸರು ನೋಂದಾಯಿಸಿ.",
                "ಉತ್ಪನ್ನವನ್ನು ನಿಗದಿತ ಗುಣಮಟ್ಟದ ಮಾನದಂಡಕ್ಕೆ (FAQ) ಅನುಗುಣವಾಗಿ ತನ್ನಿ.",
                "ತೂಕ ಮಾಡಿಸಿ ರಸೀದಿ ಪಡೆದು ನೇರ ಬ್ಯಾಂಕ್ ಜಮೆ ಮೂಲಕ ಹಣ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://agriwelfare.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare / NAFED / FCI",
            "verification_authority": "Karnataka State Agricultural Marketing Board / Designated Procurement Agencies",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Pulses", "Oilseeds", "Copra", "Bengal Gram", "Tur Dal", "Soybean"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Procurement operates during announced seasonal windows and is subject to state quantitative ceilings."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಖರೀದಿ ಪ್ರಕ್ರಿಯೆಯು ಸರ್ಕಾರ ಘೋಷಿಸಿದ ನಿರ್ದಿಷ್ಟ ಹಂಗಾಮಿನ ಅವಧಿಯಲ್ಲಿ ಮಾತ್ರ ಜಾರಿಯಲ್ಲಿರುತ್ತದೆ."
            ]
        },

        # 9. PMKSY-PDMC
        {
            "id": "pmksy-pdmc",
            "name": "PMKSY – Per Drop More Crop (PDMC)",
            "name_kn": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಕೃಷಿ ಸಿಂಚಾಯಿ ಯೋಜನೆ - ಪ್ರತಿ ಹನಿಗೆ ಹೆಚ್ಚು ಬೆಳೆ (ಪಿಡಿಎಂಸಿ)",
            "official_abbreviation": "PMKSY-PDMC",
            "government_level": "central",
            "scheme_type": "real",
            "category": "irrigation",
            "category_kn": "ಹನಿ ಮತ್ತು ತುಂತುರು ನೀರಾವರಿ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Promotes water-use efficiency through micro-irrigation systems (drip and sprinkler) with cost-sharing subsidies for agricultural and horticultural crops.",
            "description_kn": "ಹನಿ ಮತ್ತು ತುಂತುರು ನೀರಾವರಿ ಮೂಲಕ ನೀರಿನ ಸದ್ಬಳಕೆ ಹೆಚ್ಚಿಸಲು ಕೃಷಿ ಮತ್ತು ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳಿಗೆ ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Up to 55% financial assistance for small and marginal farmers, and 45% for other farmers on micro-irrigation systems.",
                "Enhanced state top-up subsidies in Karnataka extending up to 90% for small/marginal SC/ST farmers."
            ],
            "benefits_kn": [
                "ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಶೇ 55 ರವರೆಗೆ ಹಾಗೂ ಇತರೆ ರೈತರಿಗೆ ಶೇ 45 ರವರೆಗೆ ಕೇಂದ್ರ ಸಹಾಯಧನ.",
                "ಕರ್ನಾಟಕದಲ್ಲಿ ಹೆಚ್ಚುವರಿ ರಾಜ್ಯ ಪಾಲಿನೊಂದಿಗೆ ಸಣ್ಣ ರೈತರಿಗೆ ಶೇ 90 ರವರೆಗೆ ಸಹಾಯಧನ ಲಭ್ಯ."
            ],
            "eligibility_rules": [
                make_rule("pdmc_water_source", "Applicant must possess a viable water source (borewell, open well, farm pond, or canal access) and electricity/diesel connection.", "ಅರ್ಜಿದಾರರು ನಿರಂತರ ನೀರಿನ ಮೂಲ (ಬೋರ್‌ವೆಲ್, ಬಾವಿ, ಕೃಷಿ ಹೊಂಡ) ಹೊಂದಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, True, "PMKSY-PDMC Guidelines 2022", "verified", "Do you have an active irrigation water source on your farm?", "ನಿಮ್ಮ ಜಮೀನಿನಲ್ಲಿ ನೀರಾವರಿ ನೀರಿನ ಸೌಲಭ್ಯವಿದೆಯೇ?", "Water-use efficiency systems require an existing verified water delivery source.", "ಹನಿ ನೀರಾವರಿ ಅಳವಡಿಸಲು ನೀರಿನ ಲಭ್ಯತೆ ಕಡ್ಡಾಯವಾಗಿದೆ.")
            ],
            "required_documents": [
                "Farmer ID / FRUITS registration",
                "Land record (RTC / Pahani)",
                "Water and electricity source certificate / electricity bill",
                "Quotation from empanelled micro-irrigation manufacturer"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಸಂಖ್ಯೆ (FID / FRUITS)",
                "ಭೂದಾಖಲೆ ಪಹಣಿ (RTC)",
                "ನೀರಿನ ಮೂಲ ದೃಢೀಕರಣ / ವಿದ್ಯುತ್ ಬಿಲ್",
                "ಅಂಗೀಕೃತ ಕಂಪನಿಯಿಂದ ಪಡೆದ ಕೊಟೇಷನ್ (ಅಂದಾಜು ವೆಚ್ಚ)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Apply through state horticulture/agriculture department portal before purchasing or installing.",
                "Department inspects field, verifies water source, and issues work order.",
                "Empanelled vendor installs approved drip/sprinkler system.",
                "Geo-tagged verification and DBT subsidy credit."
            ],
            "application_steps_kn": [
                "ಅಳವಡಿಸುವ ಮುನ್ನ ತೋಟಗಾರಿಕೆ ಅಥವಾ ಕೃಷಿ ಇಲಾಖೆ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಅಧಿಕಾರಿಗಳು ಸ್ಥಳ ಪರಿಶೀಲನೆ ನಡೆಸಿ ವರ್ಕ್ ಆರ್ಡರ್ ನೀಡುತ್ತಾರೆ.",
                "ಮಾನ್ಯತೆ ಪಡೆದ ಕಂಪನಿ ಹನಿ ನೀರಾವರಿ ಘಟಕವನ್ನು ಅಳವಡಿಸುತ್ತದೆ.",
                "ಜಿಯೋ-ಟ್ಯಾಗ್ ತಪಾಸಣೆ ನಂತರ ಸಹಾಯಧನ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://pmksy.gov.in/",
            "issuing_authority": "Department of Agriculture & Farmers Welfare, Government of India",
            "verification_authority": "Department of Horticulture / Agriculture, Government of Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Sugarcane", "Arecanut", "Banana", "Vegetables", "Cotton", "Maize", "Pulses", "Orchards"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Prior administrative approval is compulsory before installation. Purchasing first can make the asset ineligible."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಅಳವಡಿಸುವ ಮುಂಚಿತವಾಗಿಯೇ ಅನುಮೋದನೆ ಪಡೆಯುವುದು ಕಡ್ಡಾಯವಾಗಿದೆ."
            ]
        },

        # 10. WDC-PMKSY
        {
            "id": "wdc-pmksy",
            "name": "Watershed Development Component of PMKSY (WDC-PMKSY)",
            "name_kn": "ಪಿಎಂಕೆಎಸ್‌ವೈ ಜಲಾನಯನ ಅಭಿವೃದ್ಧಿ ಘಟಕ (ಡಬ್ಲ್ಯೂಡಿಸಿ-ಪಿಎಂಕೆಎಸ್‌ವೈ)",
            "official_abbreviation": "WDC-PMKSY",
            "government_level": "central",
            "scheme_type": "real",
            "category": "irrigation",
            "category_kn": "ಜಲಾನಯನ ಅಭಿವೃದ್ಧಿ",
            "assistance_type": "irrigation_infrastructure",
            "status_label": "District-specific implementation",
            "status_label_kn": "ಜಿಲ್ಲಾವಾರು ಅನುಷ್ಠಾನ",
            "description": "Supports treatment of rainfed and degraded landscapes through contour bunds, drainage-line treatment, check dams, farm ponds, and groundwater recharge.",
            "description_kn": "ಮಳೆ ಆಶ್ರಿತ ಒಣಭೂಮಿ ಪ್ರದೇಶಗಳಲ್ಲಿ ಬದು ನಿರ್ಮಾಣ, ಚೆಕ್ ಡ್ಯಾಂ, ಕೃಷಿ ಹೊಂಡ ಮತ್ತು ಅಂತರ್ಜಲ ಮರುಪೂರಣ ಕಾಮಗಾರಿಗಳ ಮೂಲಕ ಜಲಾನಯನ ಅಭಿವೃದ್ಧಿ ಕೈಗೊಳ್ಳುವ ಯೋಜನೆ.",
            "benefits": [
                "Community and field-level soil and water conservation infrastructure.",
                "Enhanced groundwater recharge and protection against soil erosion."
            ],
            "benefits_kn": [
                "ಸಮುದಾಯ ಮತ್ತು ಜಮೀನು ಮಟ್ಟದಲ್ಲಿ ಮಣ್ಣು ಮತ್ತು ನೀರು ಸಂರಕ್ಷಣಾ ಕಾಮಗಾರಿಗಳು.",
                "ಅಂತರ್ಜಲ ಮರುಪೂರಣ ಮತ್ತು ಮಣ್ಣಿನ ಸವೆತ ತಡೆಗಟ್ಟುವಿಕೆ."
            ],
            "eligibility_rules": [
                make_rule("wdc_area", "Land must fall within an approved and notified watershed project area.", "ಜಮೀನು ಅನುಮೋದಿತ ಜಲಾನಯನ ಯೋಜನಾ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಇರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "WDC-PMKSY Guidelines", "verified", "Is your farm located in a notified watershed project area?", "ನಿಮ್ಮ ಜಮೀನು ಅಧಿಸೂಚಿತ ಜಲಾನಯನ ವ್ಯಾಪ್ತಿಯಲ್ಲಿದೆಯೇ?", "Works are sanctioned strictly according to watershed micro-plans.", "ಜಲಾನಯನ ಸೂಕ್ಷ್ಮ ಯೋಜನೆಯ ಅನ್ವಯ ಮಾತ್ರ ಕಾಮಗಾರಿಗಳನ್ನು ಕೈಗೊಳ್ಳಲಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "RTC / Pahani showing land location",
                "Consent letter for community/field contour structures"
            ],
            "required_documents_kn": [
                "ಜಮೀನಿನ ಪಹಣಿ (RTC)",
                "ಜಮೀನಿನಲ್ಲಿ ಬದು ನಿರ್ಮಾಣ ಕಾಮಗಾರಿಗೆ ಒಪ್ಪಿಗೆ ಪತ್ರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Contact the Village Watershed Committee, Gram Panchayat, or District Watershed Office.",
                "Check whether the village is covered under the approved Detailed Project Report (DPR).",
                "Participate in participatory rural appraisal (PRA) for work inclusion."
            ],
            "application_steps_kn": [
                "ಗ್ರಾಮ ಜಲಾನಯನ ಸಮಿತಿ, ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಅಥವಾ ಜಿಲ್ಲಾ ಜಲಾನಯನ ಕಚೇರಿಯನ್ನು ಸಂಪರ್ಕಿಸಿ.",
                "ನಿಮ್ಮ ಗ್ರಾಮವು ಜಲಾನಯನ ಯೋಜನಾ ವ್ಯಾಪ್ತಿಯಲ್ಲಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.",
                "ಕಾಮಗಾರಿಗಳ ಅನುಷ್ಠಾನಕ್ಕೆ ಸಭೆಯಲ್ಲಿ ಭಾಗವಹಿಸಿ."
            ],
            "official_source_url": "https://pmksy.gov.in/",
            "issuing_authority": "Department of Land Resources / Ministry of Rural Development",
            "verification_authority": "Watershed Development Department, Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["Notified Watershed Districts", "Karnataka"],
            "supported_crops": ["Rainfed crops, dryland horticulture"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Works are community/project based; there is no automatic individual cash entitlement."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ಸಮುದಾಯ ಆಧಾರಿತ ಕಾಮಗಾರಿಯಾಗಿದ್ದು ವೈಯಕ್ತಿಕ ನಗದು ಪಾವತಿಯಲ್ಲ."
            ]
        },

        # 11. PMKSY-MI
        {
            "id": "pmksy-mi",
            "name": "PMKSY – Major/Minor Irrigation and Command-Area Components",
            "name_kn": "ಪಿಎಂಕೆಎಸ್‌ವೈ ಪ್ರಮುಖ ಮತ್ತು ಸಣ್ಣ ನೀರಾವರಿ ಕಾಲುವೆ ಯೋಜನೆ",
            "official_abbreviation": "PMKSY-AIBP/CAD",
            "government_level": "central",
            "scheme_type": "real",
            "category": "irrigation",
            "category_kn": "ಬೃಹತ್ ಮತ್ತು ಸಣ್ಣ ನೀರಾವರಿ",
            "assistance_type": "irrigation_infrastructure",
            "status_label": "District-specific implementation",
            "status_label_kn": "ಜಿಲ್ಲಾವಾರು ಅನುಷ್ಠಾನ",
            "description": "Supports major and surface minor irrigation infrastructure, canal networks, and command-area water distribution to ensure field water access.",
            "description_kn": "ಬೃಹತ್, ಮಧ್ಯಮ ಹಾಗೂ ಸಣ್ಣ ನೀರಾವರಿ ಯೋಜನೆಗಳು ಮತ್ತು ಅಚ್ಚುಕಟ್ಟು ಪ್ರದೇಶದ ಕಾಲುವೆ ಅಭಿವೃದ್ಧಿ ಮೂಲಕ ಕೃಷಿ ಜಮೀನುಗಳಿಗೆ ನೀರು ಪೂರೈಸುವ ಯೋಜನೆ.",
            "benefits": [
                "Assured surface water delivery through canal networks and distributaries.",
                "Command area land leveling, field channels, and participatory water management."
            ],
            "benefits_kn": [
                "ಕಾಲುವೆಗಳ ಮೂಲಕ ಕೃಷಿ ಜಮೀನುಗಳಿಗೆ ಕಾಲೋಚಿತ ನೀರು ಸರಬರಾಜು.",
                "ಅಚ್ಚುಕಟ್ಟು ಪ್ರದೇಶ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ನೀರು ಬಳಕೆದಾರರ ಸಂಘಗಳ ಬಲವರ್ಧನೆ."
            ],
            "eligibility_rules": [
                make_rule("pmksy_cad_command", "Land must be situated within the notified command area of an approved irrigation project.", "ಜಮೀನು ಅನುಮೋದಿತ ನೀರಾವರಿ ಯೋಜನೆಯ ಅಚ್ಚುಕಟ್ಟು ಪ್ರದೇಶದ ವ್ಯಾಪ್ತಿಯಲ್ಲಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "CADWM Guidelines", "verified", "Is your land in an irrigation project command area?", "ನಿಮ್ಮ ಜಮೀನು ನೀರಾವರಿ ಅಚ್ಚುಕಟ್ಟು ಪ್ರದೇಶದಲ್ಲಿದೆಯೇ?", "Benefits arise through access to infrastructure rather than a direct cash subsidy.", "ಇದು ಮೂಲಸೌಕರ್ಯದ ಪ್ರಯೋಜನವಾಗಿದ್ದು ನೇರ ನಗದು ಸಬ್ಸಿಡಿಯಲ್ಲ.")
            ],
            "required_documents": ["Land record RTC showing ayacut/command area entry"],
            "required_documents_kn": ["ಅಚ್ಚುಕಟ್ಟು ವ್ಯಾಪ್ತಿ ತೋರಿಸುವ ಪಹಣಿ (RTC)"],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Enquire with the state water-resources / minor-irrigation department or local Water Users Association (WUA).",
                "Verify field channel alignment and water allocation schedule."
            ],
            "application_steps_kn": [
                "ಜಲಸಂಪನ್ಮೂಲ ಇಲಾಖೆ ಅಥವಾ ಸ್ಥಳೀಯ ನೀರು ಬಳಕೆದಾರರ ಸಂಘವನ್ನು (WUA) ಸಂಪರ್ಕಿಸಿ.",
                "ಕಾಲುವೆ ನೀರು ಬಿಡುವ ವೇಳಾಪಟ್ಟಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ."
            ],
            "official_source_url": "https://pmksy.gov.in/",
            "issuing_authority": "Ministry of Jal Shakti, Government of India",
            "verification_authority": "Water Resources Department / Minor Irrigation Dept, Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["Notified Command Areas", "Karnataka"],
            "supported_crops": ["Paddy", "Sugarcane", "Wheat", "Maize"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Benefits arise through access to irrigation infrastructure rather than a direct individual subsidy."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ಸಾರ್ವಜನಿಕ ನೀರಾವರಿ ಮೂಲಸೌಕರ್ಯ ಸೌಲಭ್ಯವಾಗಿದೆ."
            ]
        },

        # 12. SMAM
        {
            "id": "smam",
            "name": "Sub-Mission on Agricultural Mechanization (SMAM)",
            "name_kn": "ಕೃಷಿ ಯಾಂತ್ರೀಕರಣ ಉಪ ಅಭಿಯಾನ (ಎಸ್‌ಎಂಎಎಂ)",
            "official_abbreviation": "SMAM",
            "government_level": "central",
            "scheme_type": "real",
            "category": "mechanization",
            "category_kn": "ಕೃಷಿ ಯಾಂತ್ರೀಕರಣ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Promotes farm mechanisation through subsidies for individual farm equipment, custom hiring centres, hi-tech machinery hubs, and demonstrations.",
            "description_kn": "ಕೃಷಿ ವೆಚ್ಚ ಕಡಿಮೆ ಮಾಡಲು ಟ್ರ್ಯಾಕ್ಟರ್, ಪವರ್ ಟಿಲ್ಲರ್, ಬಿತ್ತನೆ ಉಪಕರಣಗಳು ಮತ್ತು ಕಟಾವು ಯಂತ್ರಗಳ ಖರೀದಿಗೆ ಸಹಾಯಧನ ನೀಡುವ ರಾಷ್ಟ್ರೀಯ ಯೋಜನೆ.",
            "benefits": [
                "40% to 50% subsidy for individual farmers (up to 50% for SC/ST/Small/Marginal/Women farmers) on approved implements.",
                "Assistance for establishment of Custom Hiring Centres (up to 40% project cost)."
            ],
            "benefits_kn": [
                "ಅಂಗೀಕೃತ ಯಂತ್ರೋಪಕರಣಗಳ ಖರೀದಿಗೆ ಶೇ 40 ರಿಂದ ಶೇ 50 ರವರೆಗೆ ಸಹಾಯಧನ (ಸಣ್ಣ/ಅತಿ ಸಣ್ಣ ಮತ್ತು ಮಹಿಳಾ ರೈತರಿಗೆ ಆದ್ಯತೆ).",
                "ಬಾಡಿಗೆ ಆಧಾರಿತ ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ಕೇಂದ್ರ ಸ್ಥಾಪನೆಗೆ ಶೇ 40 ರವರೆಗೆ ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("smam_farmer", "Must be a registered farmer possessing cultivable landholding in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರುವ ನೋಂದಾಯಿತ ರೈತರಾಗಿರಬೇಕು.", "ownership", "in", ["owned", "joint_owned"], True, "SMAM Operational Guidelines", "verified", "Do you own agricultural land for which machinery is required?", "ಯಂತ್ರೋಪಕರಣ ಬಳಸಲು ನೀವು ಸ್ವಂತ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿದ್ದೀರಾ?", "Land documents are verified to confirm need and previous subsidy restrictions.", "ಹಿಂದೆ ಇದೇ ಯಂತ್ರಕ್ಕೆ ಸಹಾಯಧನ ಪಡೆದಿಲ್ಲ ಎಂಬುದನ್ನು ದೃಢೀಕರಿಸಲು ಭೂದಾಖಲೆ ಅಗತ್ಯ.")
            ],
            "required_documents": [
                "Farmer ID / FRUITS registration",
                "Land Record (RTC / Pahani)",
                "Aadhaar card and bank passbook",
                "Quotation and pre-approval sanction"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಸಂಖ್ಯೆ (FRUITS / FID)",
                "ಭೂದಾಖಲೆ ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್",
                "ಅಧಿಕೃತ ಡೀಲರ್‌ನಿಂದ ಪಡೆದ ಕೊಟೇಷನ್ ಮತ್ತು ಇಲಾಖೆಯ ಪೂರ್ವ ಮಂಜೂರಾತಿ"
            ],
            "optional_documents": ["Caste certificate (for enhanced SC/ST subsidy)"],
            "optional_documents_kn": ["ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ (ಹೆಚ್ಚುವರಿ ಸಬ್ಸಿಡಿಗಾಗಿ)"],
            "application_steps": [
                "Apply online via agrimachinery.nic.in or state agriculture mechanization portal.",
                "Obtain prior administrative approval before purchasing machinery.",
                "Purchase from empanelled dealer, complete inspection, and receive DBT subsidy."
            ],
            "application_steps_kn": [
                "ಕೃಷಿ ಇಲಾಖೆ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಯಂತ್ರ ಖರೀದಿಸುವ ಮುನ್ನ ಇಲಾಖೆಯಿಂದ ಪೂರ್ವಾನುಮೋದನೆ ಪಡೆಯಿರಿ.",
                "ಅಂಗೀಕೃತ ಡೀಲರ್‌ನಿಂದ ಯಂತ್ರ ಖರೀದಿಸಿ ತಪಾಸಣೆ ನಂತರ ಖಾತೆಗೆ ಸಬ್ಸಿಡಿ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://agrimachinery.nic.in/",
            "issuing_authority": "Ministry of Agriculture & Farmers Welfare, Government of India",
            "verification_authority": "Department of Agriculture, Government of Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Prior administrative approval is compulsory; purchasing first can make the item ineligible."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಯಂತ್ರೋಪಕರಣ ಖರೀದಿಸುವ ಮುಂಚೆಯೇ ಇಲಾಖೆಯಿಂದ ಲಿಖಿತ ಅನುಮೋದನೆ ಪಡೆಯುವುದು ಕಡ್ಡಾಯ."
            ]
        },

        # 13. CHC-FMB
        {
            "id": "chc-fmb",
            "name": "Custom Hiring Centres (CHCs) and Farm Machinery Banks",
            "name_kn": "ಕಸ್ಟಮ್ ಹೈರಿಂಗ್ ಕೇಂದ್ರಗಳು ಮತ್ತು ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ಬ್ಯಾಂಕ್ (ಸಿಎಚ್‌ಸಿ)",
            "official_abbreviation": "CHC-FMB",
            "government_level": "central",
            "scheme_type": "real",
            "category": "mechanization",
            "category_kn": "ಬಾಡಿಗೆ ಆಧಾರಿತ ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ",
            "assistance_type": "equipment_rental",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Enables farmers to rent costly machinery (tractors, power tillers, harvesters, laser levelers) at regulated rental rates through service hubs.",
            "description_kn": "ಸಣ್ಣ ರೈತರು ದುಬಾರಿ ಯಂತ್ರಗಳನ್ನು ಖರೀದಿಸುವ ಬದಲು ಬಾಡಿಗೆ ಆಧಾರದಲ್ಲಿ ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಯಂತ್ರಗಳನ್ನು ಪಡೆಯಲು ಸ್ಥಾಪಿಸಲಾದ ಕೇಂದ್ರಗಳು.",
            "benefits": [
                "Affordable hourly or acre-based rental of farm tractors, transplanters, and harvesters.",
                "Eliminates heavy capital investment debt for small and marginal landholders."
            ],
            "benefits_kn": [
                "ಗಂಟೆ ಅಥವಾ ಎಕರೆ ಲೆಕ್ಕದಲ್ಲಿ ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಟ್ರ್ಯಾಕ್ಟರ್ ಮತ್ತು ಹಾರ್ವೆಸ್ಟರ್ ಬಾಡಿಗೆ ಸೌಲಭ್ಯ.",
                "ಸಣ್ಣ ರೈತರಿಗೆ ಯಂತ್ರಗಳ ಖರೀದಿಯ ಬಂಡವಾಳದ ಹೊರೆ ತಪ್ಪಿಸುತ್ತದೆ."
            ],
            "eligibility_rules": [
                make_rule("chc_access", "Open to all farmers in the operational service area of the Custom Hiring Centre.", "ಕೇಂದ್ರದ ವ್ಯಾಪ್ತಿಯಲ್ಲಿರುವ ಎಲ್ಲಾ ರೈತರಿಗೂ ಮುಕ್ತವಾಗಿದೆ.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "SMAM CHC Guidelines", "verified", "Do you require farm machinery on rental basis?", "ನಿಮಗೆ ಬಾಡಿಗೆ ಆಧಾರದಲ್ಲಿ ಕೃಷಿ ಯಂತ್ರೋಪಕರಣಗಳ ಅಗತ್ಯವಿದೆಯೇ?", "Farmers use functioning centres at applicable rental rates.", "ರೈತರು ನಿಗದಿತ ಬಾಡಿಗೆ ದರ ನೀಡಿ ಯಂತ್ರಗಳನ್ನು ಬಳಸಬಹುದು.")
            ],
            "required_documents": ["Farmer ID or Aadhaar card for booking"],
            "required_documents_kn": ["ಬುಕಿಂಗ್‌ಗಾಗಿ ರೈತರ ಗುರುತಿನ ಚೀಟಿ ಅಥವಾ ಆಧಾರ್"],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Contact local Custom Hiring Centre (CHC) / Krishi Yantra Dhare hub.",
                "Book required machinery with date and acreage particulars.",
                "Pay regulated hourly/acre rental upon completion."
            ],
            "application_steps_kn": [
                "ಸ್ಥಳೀಯ ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಕೇಂದ್ರ ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರವನ್ನು ಸಂಪರ್ಕಿಸಿ.",
                "ದಿನಾಂಕ ಮತ್ತು ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ ತಿಳಿಸಿ ಯಂತ್ರವನ್ನು ಬುಕ್ ಮಾಡಿ.",
                "ಕಾಮಗಾರಿ ಮುಗಿದ ನಂತರ ನಿಗದಿತ ರಿಯಾಯಿತಿ ಬಾಡಿಗೆ ಪಾವತಿಸಿ."
            ],
            "official_source_url": "https://agrimachinery.nic.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "Department of Agriculture Karnataka / Taluk ADA Office",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Current rental rates must be confirmed with the local Custom Hiring Centre.",
                "Establishment support is for approved operators/FPOs—not a universal cash grant to every farmer."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಬಾಡಿಗೆ ದರಗಳನ್ನು ಸ್ಥಳೀಯ ಕೇಂದ್ರದೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ಬಾಡಿಗೆ ಸೇವಾ ಸೌಲಭ್ಯವಾಗಿದ್ದು ವೈಯಕ್ತಿಕ ನಗದು ಸಹಾಯಧನವಲ್ಲ."
            ]
        },

        # 14. Namo Drone Didi
        {
            "id": "namo-drone-didi",
            "name": "Namo Drone Didi",
            "name_kn": "ನಮೋ ಡ್ರೋನ್ ದೀದಿ",
            "official_abbreviation": "Namo Drone Didi",
            "government_level": "central",
            "scheme_type": "real",
            "category": "mechanization",
            "category_kn": "ಕೃಷಿ ಡ್ರೋನ್ ಸೇವೆಗಳು",
            "assistance_type": "training_advisory",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "Supports selected women Self-Help Groups (SHGs) to become drone-based service providers for agriculture, spraying liquid fertilizers and pesticides efficiently.",
            "description_kn": "ಮಹಿಳಾ ಸ್ವಸಹಾಯ ಸಂಘಗಳಿಗೆ ಡ್ರೋನ್ ಮತ್ತು ಪೈಲಟ್ ತರಬೇತಿ ನೀಡಿ ರೈತರ ಜಮೀನಿನಲ್ಲಿ ನ್ಯಾನೋ ರಸಗೊಬ್ಬರ ಹಾಗೂ ಕೀಟನಾಶಕ ಸಿಂಪಡಣೆ ಸೇವೆ ಒದಗಿಸುವ ಯೋಜನೆ.",
            "benefits": [
                "Rapid, uniform precision spraying of liquid nano-urea and crop nutrients.",
                "Reduces water consumption by up to 90% and protects farmers from chemical exposure."
            ],
            "benefits_kn": [
                "ಕಡಿಮೆ ಸಮಯದಲ್ಲಿ ಸಮರ್ಪಕ ಕೀಟನಾಶಕ ಮತ್ತು ನ್ಯಾನೋ ಯೂರಿಯಾ ಸಿಂಪಡಣೆ.",
                "ಶೇ 90 ರಷ್ಟು ನೀರಿನ ಉಳಿತಾಯ ಹಾಗೂ ರಾಸಾಯನಿಕಗಳ ನೇರ ಸಂಪರ್ಕದಿಂದ ರೈತರಿಗೆ ರಕ್ಷಣೆ."
            ],
            "eligibility_rules": [
                make_rule("drone_shg", "Drone packages are allocated to eligible women SHGs under DAY-NRLM. Farmers access services on custom hire.", "ಡ್ರೋನ್ ಘಟಕಗಳನ್ನು ಮಹಿಳಾ ಸ್ವಸಹಾಯ ಸಂಘಗಳಿಗೆ ನೀಡಲಾಗುತ್ತದೆ. ರೈತರು ಬಾಡಿಗೆ ಆಧಾರದಲ್ಲಿ ಸೇವೆ ಪಡೆಯಬಹುದು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Namo Drone Didi Guidelines", "verified", "Do you wish to avail drone spraying services from local SHG Drone Didis?", "ನಿಮ್ಮ ಜಮೀನಿನಲ್ಲಿ ಡ್ರೋನ್ ಸಿಂಪಡಣೆ ಸೇವೆ ಪಡೆಯಲು ಬಯಸುತ್ತೀರಾ?", "Individual farmers benefit by hiring services from trained SHG operators.", "ರೈತರು ಸಂಘದಿಂದ ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಸಿಂಪಡಣೆ ಸೇವೆ ಪಡೆಯಬಹುದು.")
            ],
            "required_documents": ["Land record Pahani (RTC) showing crop acreage"],
            "required_documents_kn": ["ಬೆಳೆ ವಿವರ ತೋರಿಸುವ ಪಹಣಿ (RTC)"],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Enquire with the State Rural Livelihood Mission (Sanjeevini in Karnataka) or local RSK.",
                "Book drone spraying service through certified local Drone Didi SHG.",
                "Pay designated per-acre service charges."
            ],
            "application_steps_kn": [
                "ಸಂಜೀವಿನಿ ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಒಕ್ಕೂಟ ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರವನ್ನು ಸಂಪರ್ಕಿಸಿ.",
                "ತರಬೇತಿ ಪಡೆದ ಡ್ರೋನ್ ದೀದಿ ಬಳಿ ಸಿಂಪಡಣೆ ದಿನಾಂಕ ಬುಕ್ ಮಾಡಿ.",
                "ನಿಗದಿತ ಎಕರೆ ಶುಲ್ಕ ನೀಡಿ ಸೇವೆ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://agriwelfare.gov.in/",
            "issuing_authority": "Ministry of Agriculture & Farmers Welfare / Ministry of Rural Development",
            "verification_authority": "Karnataka State Rural Livelihood Mission (Sanjeevini) / DA&FW",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Paddy", "Sugarcane", "Cotton", "Maize", "Pulses", "Vegetables"],
            "notes": [
                "Current service rates must be confirmed with the implementing agency.",
                "This is not a direct drone-purchase cash subsidy for individual farmers. Farmers access services from participating SHGs."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸೇವಾ ದರಗಳನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ವೈಯಕ್ತಿಕ ರೈತರಿಗೆ ಡ್ರೋನ್ ಖರೀದಿಸುವ ಸಬ್ಸಿಡಿಯಲ್ಲ, ಸ್ವಸಹಾಯ ಸಂಘಗಳ ಮೂಲಕ ಒದಗಿಸಲಾಗುವ ಸೇವೆಯಾಗಿದೆ."
            ]
        },

        # 15. Soil Health Card
        {
            "id": "soil-health-card",
            "name": "Soil Health Card Scheme",
            "name_kn": "ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ ಯೋಜನೆ (ಎಸ್‌ಎಚ್‌ಸಿ)",
            "official_abbreviation": "SHC",
            "government_level": "central",
            "scheme_type": "real",
            "category": "soil_seeds_inputs",
            "category_kn": "ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಮತ್ತು ಪರೀಕ್ಷೆ",
            "assistance_type": "training_advisory",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Provides soil testing and a comprehensive report on 12 nutrient parameters with plot-specific fertilizer and amendment recommendations.",
            "description_kn": "ಕೃಷಿ ಭೂಮಿಯ ಮಣ್ಣಿನ ಮಾದರಿ ಪರೀಕ್ಷಿಸಿ 12 ಪೋಷಕಾಂಶಗಳ ಸ್ಥಿತಿಗತಿ ಹಾಗೂ ಬೆಳೆವಾರು ರಸಗೊಬ್ಬರ ಬಳಕೆಯ ಶಿಫಾರಸು ಪತ್ರ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Customized soil health card evaluating N, P, K, S, Zn, Fe, Cu, Mn, Bo, pH, EC, and OC.",
                "Reduces input costs by 15-25% by preventing excessive and unbalanced chemical fertilizer usage."
            ],
            "benefits_kn": [
                "12 ಪೋಷಕಾಂಶಗಳ ಮಟ್ಟವನ್ನು ವಿಶ್ಲೇಷಿಸುವ ಸಮಗ್ರ ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಕಾರ್ಡ್.",
                "ಅನಗತ್ಯ ರಸಗೊಬ್ಬರ ಬಳಕೆಯನ್ನು ತಡೆದು ಕೃಷಿ ವೆಚ್ಚದಲ್ಲಿ ಶೇ 15 ರಿಂದ 25 ರಷ್ಟು ಉಳಿತಾಯ."
            ],
            "eligibility_rules": [
                make_rule("shc_land", "Open to all farmers holding or cultivating agricultural land in India.", "ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರುವ ಅಥವಾ ಸಾಗುವಳಿ ಮಾಡುವ ಎಲ್ಲಾ ರೈತರಿಗೆ ಮುಕ್ತವಾಗಿದೆ.", "land_area.value_acres", "greater_than", 0, True, "Soil Health Card Scheme Guidelines", "verified", "Do you hold or cultivate agricultural land?", "ನೀವು ಕೃಷಿ ಜಮೀನು ಹೊಂದಿದ್ದೀರಾ?", "Testing is available through notified soil testing laboratories.", "ಅಧಿಸೂಚಿತ ಮಣ್ಣು ಪರೀಕ್ಷಾ ಪ್ರಯೋಗಾಲಯಗಳ ಮೂಲಕ ಈ ಸೇವೆ ದೊರೆಯುತ್ತದೆ.")
            ],
            "required_documents": [
                "Survey number and plot details",
                "Farmer ID / Aadhaar card"
            ],
            "required_documents_kn": [
                "ಸರ್ವೇ ನಂಬರ್ ಮತ್ತು ಜಮೀನಿನ ವಿವರ",
                "ರೈತರ ಗುರುತಿನ ಸಂಖ್ಯೆ / ಆಧಾರ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Collect soil sample as per standard zigzag sampling guidelines.",
                "Submit to nearest Raitha Samparka Kendra (RSK) or district soil testing laboratory.",
                "Receive printed / digital Soil Health Card with recommended nutrient doses."
            ],
            "application_steps_kn": [
                "ವೈಜ್ಞಾನಿಕ ವಿಧಾನದಲ್ಲಿ ಜಮೀನಿನ ಮಣ್ಣಿನ ಮಾದರಿ ಸಂಗ್ರಹಿಸಿ.",
                "ಹತ್ತಿರದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ ಅಥವಾ ಮಣ್ಣು ಪರೀಕ್ಷಾ ಕೇಂದ್ರಕ್ಕೆ ಸಲ್ಲಿಸಿ.",
                "ಶಿಫಾರಸು ಮಾಡಲಾದ ರಸಗೊಬ್ಬರ ವಿವರಗಳನ್ನೊಳಗೊಂಡ ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://soilhealth.dac.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "District Soil Testing Laboratories / Agriculture Dept Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Current testing charges (if any) must be confirmed with the local RSK.",
                "It is an advisory and testing service, not a direct cash grant."
            ],
            "notes_kn": [
                "ಇದು ಮಣ್ಣಿನ ಪರೀಕ್ಷೆ ಮತ್ತು ತಾಂತ್ರಿಕ ಸಲಹಾ ಸೇವೆಯಾಗಿದ್ದು, ನಗದು ಸಹಾಯಧನವಲ್ಲ."
            ]
        },

        # 16. SMSP
        {
            "id": "smsp",
            "name": "Sub-Mission on Seeds and Planting Material (SMSP)",
            "name_kn": "ಬೀಜ ಮತ್ತು ಸಸಿ ಅಭಿವೃದ್ಧಿ ಉಪ ಅಭಿಯಾನ (ಎಸ್‌ಎಂಎಸ್‌ಪಿ)",
            "official_abbreviation": "SMSP",
            "government_level": "central",
            "scheme_type": "real",
            "category": "soil_seeds_inputs",
            "category_kn": "ಗುಣಮಟ್ಟದ ಬಿತ್ತನೆ ಬೀಜ",
            "assistance_type": "input_assistance",
            "status_label": "Seasonal application",
            "status_label_kn": "ಹಂಗಾಮುವಾರು ಅರ್ಜಿ",
            "description": "Strengthens production, certified processing, seed testing, and subsidized distribution of quality certified seeds and planting material.",
            "description_kn": "ಪ್ರಮಾಣೀಕೃತ ಬಿತ್ತನೆ ಬೀಜಗಳ ಉತ್ಪಾದನೆ, ಸಂಸ್ಕರಣೆ ಮತ್ತು ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ವಿತರಣೆ ಮಾಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Subsidized distribution of certified/hybrid seeds through authorized outlets.",
                "Assistance for Seed Village Programme (seed production training and foundation seed distribution)."
            ],
            "benefits_kn": [
                "ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಗಳ ಮೂಲಕ ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಪ್ರಮಾಣೀಕೃತ ಬೀಜ ವಿತರಣೆ.",
                "ಬೀಜ ಗ್ರಾಮ ಯೋಜನೆಯಡಿ ತಳಿ ಬೀಜೋತ್ಪಾದನೆ ತರಬೇತಿ ಮತ್ತು ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("smsp_grower", "Registered farmers cultivating eligible crops during notified seasonal distribution.", "ಅಧಿಸೂಚಿತ ಹಂಗಾಮಿನಲ್ಲಿ ಅರ್ಹ ಬೆಳೆಗಳನ್ನು ಬೆಳೆಯುವ ನೋಂದಾಯಿತ ರೈತರು.", "crops", "any_of", ["paddy", "ragi", "maize", "pulses", "oilseeds", "groundnut", "wheat", "cotton", "bhatta", "jola"], True, "SMSP Guidelines", "verified", "Are you purchasing seasonal certified seed from authorized outlets?", "ನೀವು ಅಧಿಕೃತ ಕೇಂದ್ರಗಳಿಂದ ಪ್ರಮಾಣೀಕೃತ ಬೀಜ ಖರೀದಿಸುತ್ತಿದ್ದೀರಾ?", "Subsidy is directly discounted at authorized departmental outlets.", "ಇಲಾಖೆಯ ಅಧಿಕೃತ ಕೇಂದ್ರಗಳಲ್ಲಿ ಸಬ್ಸಿಡಿ ಮೊತ್ತ ಕಡಿತಗೊಳಿಸಿ ಬೀಜ ನೀಡಲಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "Farmer ID / FRUITS registration",
                "RTC / Pahani showing seasonal landholding",
                "Aadhaar card"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಸಂಖ್ಯೆ (FRUITS / FID)",
                "ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Check seasonal seed distribution notice at Raitha Samparka Kendra (RSK).",
                "Present Farmer ID (FID) and Pahani at the counter.",
                "Purchase certified seed at the subsidized rate with an authorized cash receipt."
            ],
            "application_steps_kn": [
                "ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ಹಂಗಾಮುವಾರು ಬೀಜ ವಿತರಣಾ ಪಟ್ಟಿ ಪರಿಶೀಲಿಸಿ.",
                "ಎಫ್‌ಐಡಿ ಮತ್ತು ಪಹಣಿ ನೀಡಿ ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಬೀಜ ಖರೀದಿಸಿ ರಸೀದಿ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://seednet.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "Karnataka State Seeds Corporation (KSSC) / Agriculture Dept",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Paddy", "Ragi", "Pulses", "Oilseeds", "Maize", "Groundnut"],
            "notes": [
                "Current subsidy percentage must be confirmed with the district agriculture office.",
                "Purchase certified seed, retain the bill and seed tag, and follow the recommended sowing window."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಬ್ಸಿಡಿ ದರವನ್ನು ಸ್ಥಳೀಯ ಆರ್ ಎಸ್ ಕೆ ಯಲ್ಲಿ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಪ್ರಮಾಣೀಕೃತ ಬೀಜ ಖರೀದಿಸಿ, ಬಿಲ್ ಮತ್ತು ಬೀಜದ ಟ್ಯಾಗ್ ಅನ್ನು ಜೋಪಾನವಾಗಿಡಿ."
            ]
        },

        # 17. PKVY
        {
            "id": "pkvy",
            "name": "Paramparagat Krishi Vikas Yojana (PKVY)",
            "name_kn": "ಪರಂಪರಾಗತ್ ಕೃಷಿ ವಿಕಾಸ ಯೋಜನೆ (ಪಿಕೆವಿವೈ)",
            "official_abbreviation": "PKVY",
            "government_level": "central",
            "scheme_type": "real",
            "category": "soil_seeds_inputs",
            "category_kn": "ಸಾವಯವ ಕೃಷಿ ಪ್ರೋತ್ಸಾಹ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Promotes cluster-based organic farming, farmer training, on-farm organic inputs, participatory guarantee (PGS) certification, and organic market linkages.",
            "description_kn": "ರೈತ ಗುಂಪುಗಳ (ಕ್ಲಸ್ಟರ್) ಮೂಲಕ ಸಾವಯವ ಕೃಷಿ, ಪಿಜಿಎಸ್ ಪ್ರಮಾಣೀಕರಣ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಸಂಪರ್ಕ ಕಲ್ಪಿಸುವ ಯೋಜನೆ.",
            "benefits": [
                "₹50,000 per hectare for 3 years, of which ₹31,000 is directly provided for organic inputs, vermicompost, and bio-fertilizers.",
                "Free PGS-India organic certification and branding assistance."
            ],
            "benefits_kn": [
                "3 ವರ್ಷಗಳ ಅವಧಿಗೆ ಹೆಕ್ಟೇರ್‌ಗೆ ₹50,000 ಆರ್ಥಿಕ ನೆರವು (ಇದರಲ್ಲಿ ₹31,000 ಸಾವಯವ ಪರಿಕರಗಳ ಖರೀದಿಗೆ ನೇರ ನೆರವು).",
                "ಉಚಿತ ಪಿಜಿಎಸ್-ಇಂಡಿಯಾ ಸಾವಯವ ಪ್ರಮಾಣೀಕರಣ."
            ],
            "eligibility_rules": [
                make_rule("pkvy_cluster", "Farmers willing to join an approved organic cluster (minimum 20 ha / 50 farmers) and follow organic production standards.", "ಕನಿಷ್ಠ 20 ಹೆಕ್ಟೇರ್ ಕ್ಲಸ್ಟರ್‌ನಲ್ಲಿ ಸೇರಲು ಮತ್ತು ಸಾವಯವ ಮಾನದಂಡ ಅನುಸರಿಸಲು ಸಿದ್ಧರಿರುವ ರೈತರು.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "PKVY Operational Guidelines", "verified", "Are you a member of a registered organic farming cluster or FPO?", "ನೀವು ನೋಂದಾಯಿತ ಸಾವಯವ ಕೃಷಿ ಕ್ಲಸ್ಟರ್‌ನ ಸದಸ್ಯರಾಗಿದ್ದೀರಾ?", "Support is routed through approved clusters and action plans.", "ಅನುಮೋದಿತ ಕ್ಲಸ್ಟರ್‌ಗಳ ಮೂಲಕ ಮಾತ್ರ ನೆರವು ನೀಡಲಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "Farmer ID / Aadhaar card",
                "Land Record (RTC) within cluster boundaries",
                "Cluster membership declaration and pledge to avoid synthetic inputs"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಚೀಟಿ / ಆಧಾರ್",
                "ಕ್ಲಸ್ಟರ್ ವ್ಯಾಪ್ತಿಯ ಪಹಣಿ (RTC)",
                "ರಾಸಾಯನಿಕ ಮುಕ್ತ ಕೃಷಿ ಮಾಡುವ ಸ್ವಯಂ ಘೋಷಣಾ ಪತ್ರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Join an authorized PKVY cluster formed by regional Lead Agency / Agriculture Department.",
                "Maintain farm diary recording biological inputs and soil amendments.",
                "Participate in peer group inspection and obtain PGS-India green/organic certificate."
            ],
            "application_steps_kn": [
                "ಕೃಷಿ ಇಲಾಖೆ ರಚಿಸಿರುವ ಸಾವಯವ ಕ್ಲಸ್ಟರ್ ಗುಂಪಿಗೆ ಸೇರಿ.",
                "ಕೃಷಿ ದಿನಚರಿ ನಿರ್ವಹಿಸಿ ಜೈವಿಕ ಪರಿಕರಗಳನ್ನು ಬಳಸಿ.",
                "ಗುಂಪು ತಪಾಸಣೆಯ ನಂತರ ಪಿಜಿಎಸ್-ಇಂಡಿಯಾ ಪ್ರಮಾಣಪತ್ರ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://pgsindia-ncof.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare / NCOF",
            "verification_authority": "Karnataka State Organic Farming Agency / District Agriculture Dept",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Millets", "Pulses", "Spices", "Horticulture", "Paddy"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Support is not normally an unrestricted individual cash payment; it is tied to cluster activities."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ವೈಯಕ್ತಿಕ ನಗದು ಪಾವತಿಯಲ್ಲ, ಕ್ಲಸ್ಟರ್ ಮೂಲಕ ಒದಗಿಸಲಾಗುವ ಸಾವಯವ ಪರಿಕರಗಳ ನೆರವು."
            ]
        },

        # 18. NMNF
        {
            "id": "nmnf",
            "name": "National Mission on Natural Farming (NMNF)",
            "name_kn": "ರಾಷ್ಟ್ರೀಯ ನೈಸರ್ಗಿಕ ಕೃಷಿ ಅಭಿಯಾನ (ಎನ್‌ಎಂಎನ್‌ಎಫ್)",
            "official_abbreviation": "NMNF",
            "government_level": "central",
            "scheme_type": "real",
            "category": "soil_seeds_inputs",
            "category_kn": "ನೈಸರ್ಗಿಕ ಕೃಷಿ ಪದ್ಧತಿ",
            "assistance_type": "training_advisory",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Promotes chemical-free indigenous natural farming through cluster demonstrations, farmer field schools, and bio-input resource centres.",
            "description_kn": "ರಾಸಾಯನಿಕ ಮುಕ್ತ ದೇಶಿ ನೈಸರ್ಗಿಕ ಕೃಷಿಯನ್ನು ಪ್ರೋತ್ಸಾಹಿಸಲು ಜೀವತಜ್ಞತೆ, ತರಬೇತಿ ಮತ್ತು ಜೈವಿಕ ಸಂಪನ್ಮೂಲ ಕೇಂದ್ರಗಳನ್ನು ಸ್ಥಾಪಿಸುವ ರಾಷ್ಟ್ರೀಯ ಯೋಜನೆ.",
            "benefits": [
                "Financial incentive of ₹15,000/ha for 3 years to adopt natural farming practices.",
                "Free access to Bio-input Resource Centres (BRCs) providing Jeevamrutha and Beejamrutha."
            ],
            "benefits_kn": [
                "ನೈಸರ್ಗಿಕ ಕೃಷಿ ಅಳವಡಿಕೆಗೆ 3 ವರ್ಷಗಳವರೆಗೆ ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ ₹15,000 ಆರ್ಥಿಕ ನೆರವು.",
                "ಜೀವಾಮೃತ ಮತ್ತು ಬೀಜಾಮೃತ ತಯಾರಿಕೆಯ ಜೈವಿಕ ಸಂಪನ್ಮೂಲ ಕೇಂದ್ರಗಳ ಉಚಿತ ಸೇವೆ."
            ],
            "eligibility_rules": [
                make_rule("nmnf_practice", "Farmers willing to adopt non-chemical natural farming practices in designated gram panchayat clusters.", "ರಾಸಾಯನಿಕ ಮುಕ್ತ ನೈಸರ್ಗಿಕ ಕೃಷಿ ಕೈಗೊಳ್ಳಲು ಸಿದ್ಧರಿರುವ ರೈತರು.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "NMNF Guidelines 2023", "verified", "Are you committed to chemical-free natural farming practices?", "ನೀವು ರಾಸಾಯನಿಕ ಮುಕ್ತ ನೈಸರ್ಗಿಕ ಕೃಷಿ ಮಾಡಲು ಸಿದ್ಧರಿದ್ದೀರಾ?", "Must participate in approved clusters and follow the programme's natural farming package.", "ಅಂಗೀಕೃತ ಕ್ಲಸ್ಟರ್‌ನಲ್ಲಿ ಪಾಲ್ಗೊಂಡು ನೈಸರ್ಗಿಕ ಕೃಷಿ ಪದ್ಧತಿ ಅನುಸರಿಸುವುದು ಕಡ್ಡಾಯ.")
            ],
            "required_documents": [
                "Farmer ID / Aadhaar card",
                "Land record RTC",
                "Natural farming cluster enrollment form"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಚೀಟಿ / ಆಧಾರ್",
                "ಪಹಣಿ (RTC)",
                "ಕ್ಲಸ್ಟರ್ ನೋಂದಣಿ ಅರ್ಜಿ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Contact local Krishi Vigyan Kendra (KVK) or Raitha Samparka Kendra.",
                "Register in the designated Gram Panchayat Natural Farming cluster.",
                "Attend Farmer Field School training and prepare bio-inputs on farm."
            ],
            "application_steps_kn": [
                "ಸ್ಥಳೀಯ ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರ (ಕೆವಿಕೆ) ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರವನ್ನು ಸಂಪರ್ಕಿಸಿ.",
                "ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ನೈಸರ್ಗಿಕ ಕೃಷಿ ಕ್ಲಸ್ಟರ್‌ನಲ್ಲಿ ಹೆಸರು ನೋಂದಾಯಿಸಿ.",
                "ತರಬೇತಿ ಪಡೆದು ಜೈವಿಕ ಪರಿಕರಗಳನ್ನು ಸ್ವತಃ ತಯಾರಿಸಿ ಬಳಸಿ."
            ],
            "official_source_url": "https://naturalfarming.dac.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "Department of Agriculture / ICAR-KVKs",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Specific support depends on the approved state action plan and active cluster locations."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ಅನುಮೋದಿತ ಕ್ಲಸ್ಟರ್ ಪ್ರದೇಶಗಳಿಗೆ ಮಾತ್ರ ಅನ್ವಯಿಸುತ್ತದೆ."
            ]
        },

        # 19. NBS
        {
            "id": "nbs",
            "name": "Nutrient Based Subsidy (NBS) and Fertiliser Subsidy",
            "name_kn": "ಪೋಷಕಾಂಶ ಆಧಾರಿತ ರಸಗೊಬ್ಬರ ಸಬ್ಸಿಡಿ (ಎನ್‌ಬಿಎಸ್)",
            "official_abbreviation": "NBS",
            "government_level": "central",
            "scheme_type": "real",
            "category": "soil_seeds_inputs",
            "category_kn": "ರಸಗೊಬ್ಬರ ಸಬ್ಸಿಡಿ",
            "assistance_type": "input_assistance",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Government subsidy on notified phosphatic and potassic (P&K) fertilisers and statutory price control on Urea, reflected directly in subsidized retail prices at point of sale.",
            "description_kn": "ರೈತರಿಗೆ ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಯೂರಿಯಾ, ಡಿಎಪಿ, ಎಂಒಪಿ ಮತ್ತು ಎನ್‌ಪಿಕೆ ಗೊಬ್ಬರಗಳು ಲಭ್ಯವಾಗುವಂತೆ ಕೇಂದ್ರ ಸರ್ಕಾರವು ರಸಗೊಬ್ಬರ ಕಂಪನಿಗಳಿಗೆ ನೀಡುವ ಸಬ್ಸಿಡಿ.",
            "benefits": [
                "Subsidized Maximum Retail Prices (MRP) on Urea, DAP, MOP, and complex fertilizers.",
                "Direct subsidy paid to manufacturers to keep retail prices affordable for all farmers."
            ],
            "benefits_kn": [
                "ಕಡಿಮೆ ನಿಯಂತ್ರಿತ ದರದಲ್ಲಿ ಯೂರಿಯಾ, ಡಿಎಪಿ ಮತ್ತು ಕಾಂಪ್ಲೆಕ್ಸ್ ರಸಗೊಬ್ಬರಗಳ ಲಭ್ಯತೆ.",
                "ರೈತರಿಗೆ ಕೈಗೆಟುಕುವ ದರದಲ್ಲಿ ರಸಗೊಬ್ಬರ ದೊರಕುವಂತೆ ಕೇಂದ್ರದಿಂದ ನೇರ ರಿಯಾಯಿತಿ."
            ],
            "eligibility_rules": [
                make_rule("nbs_pos", "Open to all farmers purchasing covered fertilizers from authorized retail dealers through biometric PoS.", "ಅಧಿಕೃತ ರಸಗೊಬ್ಬರ ಮಾರಾಟಗಾರರಿಂದ ಪಿಒಎಸ್ (PoS) ಯಂತ್ರದ ಮೂಲಕ ಖರೀದಿಸುವ ಎಲ್ಲಾ ರೈತರಿಗೆ ಲಭ್ಯ.", "land_area.value_acres", "greater_than", 0, True, "Department of Fertilizers Guidelines", "verified", "Do you purchase fertilizers from authorized licensed fertilizer dealers?", "ನೀವು ಅಧಿಕೃತ ಪರವಾನಗಿ ಪಡೆದ ಡೀಲರ್ ಬಳಿ ಗೊಬ್ಬರ ಖರೀದಿಸುತ್ತೀರಾ?", "Purchases must be authenticated via Point of Sale (PoS) machine.", "ಪಿಒಎಸ್ ಯಂತ್ರದಲ್ಲಿ ಆಧಾರ್ ದೃಢೀಕರಣದೊಂದಿಗೆ ಖರೀದಿಸುವುದು ಕಡ್ಡಾಯ.")
            ],
            "required_documents": ["Aadhaar card for PoS biometric authentication at retail point"],
            "required_documents_kn": ["ಖರೀದಿ ವೇಳೆ ಪಿಒಎಸ್ ಯಂತ್ರದಲ್ಲಿ ಆಧಾರ್ ಬಯೋಮೆಟ್ರಿಕ್ ಪರಿಶೀಲನೆ"],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Visit authorized fertilizer cooperative / retail outlet with Aadhaar card.",
                "Authenticate on Point of Sale (PoS) device.",
                "Purchase notified fertilizer bags at official subsidized MRP and obtain printed receipt."
            ],
            "application_steps_kn": [
                "ಆಧಾರ್ ಕಾರ್ಡ್‌ನೊಂದಿಗೆ ಅಧಿಕೃತ ರಸಗೊಬ್ಬರ ಅಂಗಡಿಗೆ ಭೇಟಿ ನೀಡಿ.",
                "ಪಿಒಎಸ್ ಯಂತ್ರದಲ್ಲಿ ಹೆಬ್ಬೆಟ್ಟಿನ ಗುರುತು ನೀಡಿ.",
                "ನಿಗದಿತ ಸಬ್ಸಿಡಿ ದರದಲ್ಲಿ ಗೊಬ್ಬರ ಖರೀದಿಸಿ ಬಿಲ್ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://fert.gov.in/",
            "issuing_authority": "Department of Fertilizers / Ministry of Chemicals and Fertilizers",
            "verification_authority": "Joint Director of Agriculture / District Fertilizer Inspectors",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Subsidy is directly reflected in controlled retail prices; it is not transferred as cash to the individual farmer.",
                "Urea is covered under statutory price control, and P&K under Nutrient Based Subsidy rates revised bi-annually."
            ],
            "notes_kn": [
                "ಸಹಾಯಧನವನ್ನು ಚಿಲ್ಲರೆ ಮಾರಾಟ ದರದಲ್ಲಿಯೇ ಕಡಿತಗೊಳಿಸಲಾಗಿರುತ್ತದೆ; ನಗದು ರೂಪದಲ್ಲಿ ಖಾತೆಗೆ ನೀಡಲಾಗುವುದಿಲ್ಲ.",
                "ಪೋಷಕಾಂಶಗಳ ಸಬ್ಸಿಡಿ ದರವನ್ನು ಕಾಲಕಾಲಕ್ಕೆ ಸರ್ಕಾರ ಪರಿಷ್ಕರಿಸುತ್ತದೆ."
            ]
        },

        # 20. MIDH
        {
            "id": "midh",
            "name": "Mission for Integrated Development of Horticulture (MIDH)",
            "name_kn": "ತೋಟಗಾರಿಕೆ ಸಮಗ್ರ ಅಭಿವೃದ್ಧಿ ಮಿಷನ್ (ಎಂಐಡಿಎಚ್)",
            "official_abbreviation": "MIDH",
            "government_level": "central",
            "scheme_type": "real",
            "category": "horticulture",
            "category_kn": "ತೋಟಗಾರಿಕೆ ಸಮಗ್ರ ಅಭಿವೃದ್ಧಿ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Centrally sponsored umbrella scheme covering high-density planting, protected cultivation, post-harvest pack houses, cold storage, and nurseries.",
            "description_kn": "ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳ ವಿಸ್ತರಣೆ, ಹಸಿರುಮನೆ, ಪಾಲಿಹೌಸ್, ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್ ಮತ್ತು ನರ್ಸರಿಗಳ ಸ್ಥಾಪನೆಗೆ ಸಮಗ್ರ ನೆರವು ನೀಡುವ ಕೇಂದ್ರ ಪುರಸ್ಕೃತ ಯೋಜನೆ.",
            "benefits": [
                "35% to 50% cost-sharing subsidy for fruit orchards, protected cultivation structures, and pack houses.",
                "High-tech nursery establishment support up to ₹25 lakh for certified planting material."
            ],
            "benefits_kn": [
                "ಹಣ್ಣಿನ ತೋಟ, ಹಸಿರುಮನೆ ಮತ್ತು ಕಟಾವಿನ ನಂತರದ ಶೀತಲ ಗೋದಾಮುಗಳಿಗೆ ಶೇ 35 ರಿಂದ 50 ರಷ್ಟು ಸಹಾಯಧನ.",
                "ಗುಣಮಟ್ಟದ ಸಸಿ ಉತ್ಪಾದಿಸುವ ಹೈಟೆಕ್ ನರ್ಸರಿಗಳಿಗೆ ₹25 ಲಕ್ಷದವರೆಗೆ ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("midh_horti_crop", "Must cultivate or establish notified horticultural crops (fruits, vegetables, spices, flowers, plantation crops).", "ಅಧಿಸೂಚಿತ ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳನ್ನು (ಹಣ್ಣು, ತರಕಾರಿ, ಹೂವು, ಸಂಬಾರ ಪದಾರ್ಥ) ಬೆಳೆಯುತ್ತಿರಬೇಕು.", "crops", "any_of", ["arecanut", "banana", "mango", "pomegranate", "vegetables", "flowers", "pepper", "coconut", "cardamom", "adike", "mavina", "bale", "tengu"], True, "MIDH Guidelines", "verified", "Do you cultivate horticultural or plantation crops?", "ನೀವು ತೋಟಗಾರಿಕಾ ಅಥವಾ ತೋಟದ ಬೆಳೆಗಳನ್ನು ಬೆಳೆಯುತ್ತಿದ್ದೀರಾ?", "Assistance follows component-specific cost norms and prior approval.", "ಘಟಕವಾರು ವೆಚ್ಚದ ಮಾನದಂಡ ಮತ್ತು ಪೂರ್ವಾನುಮೋದನೆ ಕಡ್ಡಾಯವಾಗಿದೆ.")
            ],
            "required_documents": [
                "Farmer ID / FRUITS registration",
                "Land record (RTC / Pahani)",
                "Detailed project plan / quotation from approved vendor",
                "Water source certificate"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಚೀಟಿ (FRUITS / FID)",
                "ಭೂದಾಖಲೆ ಪಹಣಿ (RTC)",
                "ಅಂಗೀಕೃತ ಯೋಜನಾ ವರದಿ / ಕೊಟೇಷನ್",
                "ನೀರಿನ ಲಭ್ಯತೆಯ ದೃಢೀಕರಣ ಪತ್ರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Apply online through state horticulture department portal before establishing the asset.",
                "Obtain prior written sanction from Senior Assistant Director of Horticulture (SADH).",
                "Execute works as per approved technical specifications.",
                "Geo-tagged field inspection and DBT subsidy release."
            ],
            "application_steps_kn": [
                "ಕಾಮಗಾರಿ ಕೈಗೊಳ್ಳುವ ಮುನ್ನ ತೋಟಗಾರಿಕೆ ಇಲಾಖೆ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ತೋಟಗಾರಿಕಾ ಸಹಾಯಕ ನಿರ್ದೇಶಕರಿಂದ (SADH) ಪೂರ್ವ ಮಂಜೂರಾತಿ ಪಡೆಯಿರಿ.",
                "ಅಂಗೀಕೃತ ಮಾನದಂಡದಂತೆ ಕಾಮಗಾರಿ ಪೂರ್ಣಗೊಳಿಸಿ ತಪಾಸಣೆಯ ನಂತರ ಸಬ್ಸಿಡಿ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://midh.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "Directorate of Horticulture, Government of Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Fruits", "Vegetables", "Spices", "Flowers", "Plantation Crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Obtain written administrative approval before starting construction or planting."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಕಾಮಗಾರಿ ಪ್ರಾರಂಭಿಸುವ ಮುನ್ನ ಇಲಾಖೆಯಿಂದ ಲಿಖಿತ ಅನುಮತಿ ಪಡೆಯುವುದು ಕಡ್ಡಾಯ."
            ]
        },

        # 21. NMEO-OP
        {
            "id": "nmeo-op",
            "name": "National Mission on Edible Oils – Oil Palm (NMEO-OP)",
            "name_kn": "ಖಾದ್ಯ ತೈಲ ತಾಳೆ ಬೆಳೆ ರಾಷ್ಟ್ರೀಯ ಅಭಿಯಾನ (ಎನ್‌ಎಂಇಒ-ಒಪಿ)",
            "official_abbreviation": "NMEO-OP",
            "government_level": "central",
            "scheme_type": "real",
            "category": "horticulture",
            "category_kn": "ತಾಳೆ ಎಣ್ಣೆ ಬೆಳೆ ಅಭಿವೃದ್ಧಿ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "District-specific implementation",
            "status_label_kn": "ಜಿಲ್ಲಾವಾರು ಅನುಷ್ಠಾನ",
            "description": "Supports oil-palm area expansion, planting material, 4-year gestation maintenance, intercropping, and price assurance mechanism (Viability Price).",
            "description_kn": "ತಾಳೆ ಬೆಳೆಯ ವಿಸ್ತರಣೆ, ಸಸಿ ನೆಡುವುದು, 4 ವರ್ಷಗಳ ನಿರ್ವಹಣಾ ವೆಚ್ಚ, ಅಂತರಬೆಳೆ ಹಾಗೂ ಖಾತರಿ ಬೆಲೆ ಒದಗಿಸುವ ರಾಷ್ಟ್ರೀಯ ಯೋಜನೆ.",
            "benefits": [
                "₹29,000 per hectare for planting material and intercropping support.",
                "Maintenance assistance for 4 years during pre-bearing gestation period.",
                "Price assurance formula guaranteeing Viability Price for Fresh Fruit Bunches (FFB)."
            ],
            "benefits_kn": [
                "ಸಸಿ ಮತ್ತು ಅಂತರಬೆಳೆ ಬೆಳೆಯಲು ಹೆಕ್ಟೇರ್‌ಗೆ ₹29,000 ಆರ್ಥಿಕ ನೆರವು.",
                "ಇಳುವರಿ ಬರುವವರೆಗಿನ 4 ವರ್ಷಗಳ ನಿರ್ವಹಣಾ ವೆಚ್ಚದ ಸಹಾಯಧನ.",
                "ತಾಳೆ ಹಣ್ಣಿನ ಗೊಂಚಲಿಗೆ (FFB) ಸರ್ಕಾರದ ಖಾತರಿ ಬೆಲೆ ಬೆಂಬಲ."
            ],
            "eligibility_rules": [
                make_rule("nmeo_district", "Land must be located in agro-climatically suitable districts with assured perennial irrigation.", "ನಿರಂತರ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿರುವ ಅಧಿಸೂಚಿತ ತಾಳೆ ಬೆಳೆ ವ್ಯಾಪ್ತಿಯ ಜಿಲ್ಲೆಯಾಗಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, True, "NMEO-OP Guidelines", "verified", "Do you have dependable perennial irrigation for oil palm cultivation?", "ತಾಳೆ ಬೆಳೆಯಲು ನಿಮ್ಮಲ್ಲಿ ವರ್ಷಪೂರ್ತಿ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿದೆಯೇ?", "Oil palm requires continuous water supply throughout the year.", "ತಾಳೆ ಕೃಷಿಗೆ ವರ್ಷಪೂರ್ತಿ ನಿರಂತರ ನೀರಾವರಿ ಅಗತ್ಯವಿರುತ್ತದೆ.")
            ],
            "required_documents": [
                "RTC / Pahani showing suitable land",
                "Water source certificate (borewell / canal)",
                "Tripartite agreement with designated oil palm processing company"
            ],
            "required_documents_kn": [
                "ಜಮೀನಿನ ಪಹಣಿ (RTC)",
                "ನೀರಿನ ಮೂಲದ ದೃಢೀಕರಣ",
                "ಅಂಗೀಕೃತ ತಾಳೆ ಎಣ್ಣೆ ಸಂಸ್ಕರಣಾ ಕಂಪನಿಯೊಂದಿಗೆ ಒಪ್ಪಂದ ಪತ್ರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Enquire with the District Horticulture Office regarding oil-palm suitability mapping.",
                "Enter into planting and buyback agreement with the designated district processor.",
                "Receive subsidized certified seedlings, plant with prescribed spacing, and claim annual maintenance."
            ],
            "application_steps_kn": [
                "ಜಿಲ್ಲಾ ತೋಟಗಾರಿಕಾ ಇಲಾಖೆಯನ್ನು ಸಂಪರ್ಕಿಸಿ ತಾಳೆ ಕೃಷಿ ಅರ್ಹತೆ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.",
                "ಅಧಿಸೂಚಿತ ಪ್ರೊಸೆಸಿಂಗ್ ಕಂಪನಿಯೊಂದಿಗೆ ಖರೀದಿ ಒಪ್ಪಂದ ಮಾಡಿಕೊಳ್ಳಿ.",
                "ರಿಯಾಯಿತಿ ದರದ ಸಸಿ ಪಡೆದು ನೆಟ್ಟು ನಿರ್ವಹಣಾ ಸಹಾಯಧನ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://nmeo.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "Department of Horticulture, Karnataka / State Oil Palm Wing",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["Notified Oil Palm Districts", "Karnataka"],
            "supported_crops": ["Oil Palm"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Implemented in identified suitable districts with processor/industry linkage."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಕಂಪನಿಗಳ ಸಂಸ್ಕರಣಾ ಘಟಕದ ವ್ಯಾಪ್ತಿಯಲ್ಲಿರುವ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಮಾತ್ರ ಇದು ಅನ್ವಯಿಸುತ್ತದೆ."
            ]
        },

        # 22. NMEO-Oilseeds
        {
            "id": "nmeo-oilseeds",
            "name": "National Mission on Edible Oils – Oilseeds",
            "name_kn": "ಖಾದ್ಯ ತೈಲ ಬೀಜಗಳ ರಾಷ್ಟ್ರೀಯ ಅಭಿಯಾನ (ಎನ್‌ಎಂಇಒ-ಆಯಿಲ್‌ಸೀಡ್ಸ್)",
            "official_abbreviation": "NMEO-Oilseeds",
            "government_level": "central",
            "scheme_type": "real",
            "category": "horticulture",
            "category_kn": "ಎಣ್ಣೆಕಾಳು ಉತ್ಪಾದನೆ",
            "assistance_type": "input_assistance",
            "status_label": "Seasonal application",
            "status_label_kn": "ಹಂಗಾಮುವಾರು ಅರ್ಜಿ",
            "description": "Aims to increase domestic edible oilseed production (groundnut, soybean, mustard, sunflower, sesame) through certified seed hubs, agronomy demonstrations, and processing support.",
            "description_kn": "ಕಡಲೆಕಾಯಿ, ಸೋಯಾಬೀನ್, ಸೂರ್ಯಕಾಂತಿ ಮತ್ತು ಸಾಸಿವೆ ಉತ್ಪಾದನೆ ಹೆಚ್ಚಿಸಲು ಗುಣಮಟ್ಟದ ಬೀಜ ಹಾಗೂ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ನೆರವು ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Certified seed minikits and demonstrations for high-yielding oilseed varieties.",
                "Post-harvest oil extraction and primary processing cluster assistance."
            ],
            "benefits_kn": [
                "ಹೆಚ್ಚು ಇಳುವರಿ ನೀಡುವ ಎಣ್ಣೆಕಾಳುಗಳ ಬಿತ್ತನೆ ಬೀಜ ಕಿಟ್ ಮತ್ತು ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ನೆರವು.",
                "ಎಣ್ಣೆ ಗಾಣ ಮತ್ತು ಪ್ರಾಥಮಿಕ ಸಂಸ್ಕರಣೆಗೆ ಕ್ಲಸ್ಟರ್ ಆಧಾರಿತ ಪ್ರೋತ್ಸಾಹ."
            ],
            "eligibility_rules": [
                make_rule("oilseeds_grower", "Farmers cultivating notified oilseed crops in designated production clusters.", "ಅಧಿಸೂಚಿತ ಕ್ಲಸ್ಟರ್‌ಗಳಲ್ಲಿ ಎಣ್ಣೆಕಾಳು ಬೆಳೆಯುವ ರೈತರು.", "crops", "any_of", ["groundnut", "soybean", "sunflower", "sesame", "mustard", "oilseeds"], True, "NMEO-Oilseeds Guidelines", "verified", "Do you cultivate groundnut, soybean, sunflower, or other oilseeds?", "ನೀವು ಕಡಲೆಕಾಯಿ, ಸೋಯಾಬೀನ್ ಅಥವಾ ಸೂರ್ಯಕಾಂತಿ ಬೆಳೆಯುತ್ತಿದ್ದೀರಾ?", "Input support is available in notified state action plan areas.", "ರಾಜ್ಯ ಕ್ರಿಯಾ ಯೋಜನೆಯಲ್ಲಿ ಅಧಿಸೂಚಿತ ಪ್ರದೇಶಗಳಿಗೆ ಮಾತ್ರ ಲಭ್ಯವಿರುತ್ತದೆ.")
            ],
            "required_documents": [
                "Farmer ID / FRUITS registration",
                "Land record Pahani showing oilseed sowing intention"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಚೀಟಿ (FRUITS / FID)",
                "ಎಣ್ಣೆಕಾಳು ಬೆಳೆ ನಮೂದಾಗಿರುವ ಪಹಣಿ (RTC)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Register for seasonal oilseed demonstrations at local Raitha Samparka Kendra.",
                "Receive high-yielding seed minikits and bio-fertilizer packages.",
                "Implement recommended agronomic package with extension guidance."
            ],
            "application_steps_kn": [
                "ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ಹಂಗಾಮುವಾರು ಎಣ್ಣೆಕಾಳು ಪ್ರಾತ್ಯಕ್ಷಿಕೆಗೆ ಹೆಸರು ನೋಂದಾಯಿಸಿ.",
                "ಉಚಿತ/ರಿಯಾಯಿತಿ ಬೀಜದ ಕಿಟ್ ಪಡೆದು ಶಿಫಾರಸು ಮಾಡಿದಂತೆ ಬಿತ್ತನೆ ಮಾಡಿ."
            ],
            "official_source_url": "https://agriwelfare.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "Department of Agriculture, Karnataka / ICAR Institutions",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Groundnut", "Soybean", "Sunflower", "Sesame", "Mustard"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Check seasonal crop/seed demonstrations and input support with the district agriculture office."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಹಂಗಾಮಿನ ಬಿತ್ತನೆಗೆ ಮುಂಚಿತವಾಗಿ ಆರ್ ಎಸ್ ಕೆ ಯಲ್ಲಿ ವಿಚಾರಿಸಿ."
            ]
        },

        # 23. NBM
        {
            "id": "national-bamboo-mission",
            "name": "National Bamboo Mission (NBM)",
            "name_kn": "ರಾಷ್ಟ್ರೀಯ ಬಿದಿರು ಮಿಷನ್ (ಎನ್‌ಬಿಎಂ)",
            "official_abbreviation": "NBM",
            "government_level": "central",
            "scheme_type": "real",
            "category": "horticulture",
            "category_kn": "ಬಿದಿರು ಕೃಷಿ ಮತ್ತು ಕೈಗಾರಿಕೆ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Requires official confirmation",
            "status_label_kn": "ಅಧಿಕೃತ ದೃಢೀಕರಣ ಅಗತ್ಯವಿದೆ",
            "description": "Supports commercial bamboo plantation on non-forest private agricultural lands, establishment of nurseries, primary processing units, and product development.",
            "description_kn": "ಅರಣ್ಯೇತರ ಕೃಷಿ ಭೂಮಿಯಲ್ಲಿ ವಾಣಿಜ್ಯ ಬಿದಿರು ಕೃಷಿ, ನರ್ಸರಿ ಸ್ಥಾಪನೆ ಮತ್ತು ಬಿದಿರು ಉತ್ಪನ್ನಗಳ ಸಂಸ್ಕರಣೆಗೆ ನೆರವು ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Subsidy for bamboo plantation (up to ₹50,000 per ha spread over 3 years).",
                "Financial assistance for high-tech tissue culture nurseries and bamboo post-harvest processing."
            ],
            "benefits_kn": [
                "ಬಿದಿರು ಕೃಷಿ ಮಾಡಲು 3 ವರ್ಷಗಳಿಗೆ ಹೆಕ್ಟೇರ್‌ಗೆ ₹50,000 ವರೆಗೆ ಸಹಾಯಧನ.",
                "ಬಿದಿರು ಸಂಸ್ಕರಣಾ ಘಟಕ ಮತ್ತು ನರ್ಸರಿ ಸ್ಥಾಪನೆಗೆ ಆರ್ಥಿಕ ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("nbm_land", "Must possess clear land title on non-forest agricultural/private land suitable for commercial bamboo varieties.", "ಅರಣ್ಯೇತರ ಖಾಸಗಿ ಕೃಷಿ ಭೂಮಿಯ ಸ್ಪಷ್ಟ ಮಾಲೀಕತ್ವ ಹೊಂದಿರಬೇಕು.", "ownership", "in", ["owned", "joint_owned", "leased"], True, "NBM Guidelines", "verified", "Do you hold private agricultural land suitable for bamboo plantation?", "ಬಿದಿರು ಬೆಳೆಯಲು ಸೂಕ್ತವಾದ ಖಾಸಗಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿದ್ದೀರಾ?", "Plantations on forest lands are not covered under agricultural NBM.", "ಅರಣ್ಯ ಭೂಮಿಯ ಕೃಷಿಗೆ ಇದು ಅನ್ವಯಿಸುವುದಿಲ್ಲ.")
            ],
            "required_documents": [
                "Land ownership record (RTC) showing non-forest status",
                "Detailed project plan for plantation or processing unit",
                "Aadhaar and bank details"
            ],
            "required_documents_kn": [
                "ಅರಣ್ಯೇತರ ಕೃಷಿ ಭೂಮಿಯನ್ನು ದೃಢೀಕರಿಸುವ ಪಹಣಿ (RTC)",
                "ಬಿದಿರು ಕೃಷಿ ಯೋಜನಾ ವರದಿ",
                "ಆಧಾರ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Submit project proposal to State Bamboo Mission / Directorate of Horticulture.",
                "Technical committee inspects proposed land and sanctions planting material quota.",
                "Plant certified bamboo saplings and claim staged subsidy installments."
            ],
            "application_steps_kn": [
                "ರಾಜ್ಯ ಬಿದಿರು ಮಿಷನ್ ಅಥವಾ ತೋಟಗಾರಿಕಾ ಇಲಾಖೆಗೆ ಯೋಜನಾ ಪ್ರಸ್ತಾವನೆ ಸಲ್ಲಿಸಿ.",
                "ತಾಂತ್ರಿಕ ಪರಿಶೀಲನೆ ನಂತರ ಸಸಿ ನೆಡಲು ಮಂಜೂರಾತಿ ಪಡೆಯಿರಿ.",
                "ಕಾಮಗಾರಿ ಪೂರ್ಣಗೊಳಿಸಿ ಹಂತ-ಹಂತವಾಗಿ ಸಬ್ಸಿಡಿ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://nbm.nic.in/",
            "issuing_authority": "Ministry of Agriculture & Farmers Welfare, Government of India",
            "verification_authority": "Karnataka State Bamboo Mission / Forest & Horticulture Departments",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Bamboo"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Contact the state nodal agency or relevant horticulture/forest department for current calls and cost norms."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಚಾಲ್ತಿಯಲ್ಲಿರುವ ನಿಯಮಾವಳಿಗಳನ್ನು ರಾಜ್ಯ ಬಿದಿರು ಮಿಷನ್ ಕಚೇರಿಯಿಂದ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ."
            ]
        },

        # 24. NBHM
        {
            "id": "nbhm",
            "name": "National Beekeeping and Honey Mission (NBHM)",
            "name_kn": "ರಾಷ್ಟ್ರೀಯ ಜೇನುಸಾಕಣೆ ಮತ್ತು ಜೇನುತುಪ್ಪ ಅಭಿಯಾನ (ಎನ್‌ಬಿಎಚ್‌ಎಂ)",
            "official_abbreviation": "NBHM",
            "government_level": "central",
            "scheme_type": "real",
            "category": "horticulture",
            "category_kn": "ಜೇನುಸಾಕಣೆ ಅಭಿಯಾನ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Promotes scientific beekeeping for crop pollination and honey production with assistance for bee colonies, scientific hives, extraction equipment, and custom hiring centres.",
            "description_kn": "ಪರಾಗಸ್ಪರ್ಶ ಹೆಚ್ಚಿಸಲು ಮತ್ತು ಗುಣಮಟ್ಟದ ಜೇನುತುಪ್ಪ ಉತ್ಪಾದಿಸಲು ಜೇನು ಪೆಟ್ಟಿಗೆ, ಜೇನು ಕುಟುಂಬಗಳು ಮತ್ತು ಸಂಸ್ಕರಣಾ ಉಪಕರಣಗಳಿಗೆ ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Up to 40% to 50% subsidy on beehives, bee colonies, and honey extraction equipment sets.",
                "Custom Hiring Centres and honey processing/testing lab establishment grants."
            ],
            "benefits_kn": [
                "ಜೇನು ಪೆಟ್ಟಿಗೆ, ಜೇನು ನೊಣಗಳ ಕುಟುಂಬ ಮತ್ತು ಉಪಕರಣಗಳ ಖರೀದಿಗೆ ಶೇ 40 ರಿಂದ 50 ರಷ್ಟು ಸಹಾಯಧನ.",
                "ಜೇನುತುಪ್ಪ ಸಂಸ್ಕರಣಾ ಘಟಕ ಮತ್ತು ಜೇನು ಪರೀಕ್ಷಾ ಪ್ರಯೋಗಾಲಯ ಸ್ಥಾಪನೆಗೆ ಆರ್ಥಿಕ ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("nbhm_beekeeping", "Beekeepers, farmers, SHGs, and FPOs who have undergone certified training in scientific apiculture.", "ವೈಜ್ಞಾನಿಕ ಜೇನುಸಾಕಣೆ ತರಬೇತಿ ಪಡೆದಿರುವ ರೈತರು ಅಥವಾ ಜೇನು ಕೃಷಿಕರು.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "NBHM Guidelines", "verified", "Have you completed scientific beekeeping training or currently manage beehives?", "ನೀವು ವೈಜ್ಞಾನಿಕ ಜೇನುಸಾಕಣೆ ತರಬೇತಿ ಪಡೆದಿದ್ದೀರಾ?", "Training certification is required for scientific colony management.", "ಜೇನು ಕುಟುಂಬಗಳ ಸರಿಯಾದ ನಿರ್ವಹಣೆಗೆ ತರಬೇತಿ ಪ್ರಮಾಣಪತ್ರ ಅಗತ್ಯ.")
            ],
            "required_documents": [
                "Beekeeping training completion certificate",
                "Aadhaar card and bank passbook",
                "Quotation for hives and extraction equipment from National Bee Board empanelled breeders"
            ],
            "required_documents_kn": [
                "ಜೇನುಸಾಕಣೆ ತರಬೇತಿ ಪ್ರಮಾಣಪತ್ರ",
                "ಆಧಾರ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್",
                "ಅಂಗೀಕೃತ ಸಂಸ್ಥೆಯಿಂದ ಪಡೆದ ಜೇನು ಪೆಟ್ಟಿಗೆಗಳ ಕೊಟೇಷನ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Register on the Madhukranti portal (madhukranti.in) and National Bee Board.",
                "Submit application to District Horticulture Officer.",
                "Receive sanctioned bee colonies and modern wooden hives with inspection confirmation."
            ],
            "application_steps_kn": [
                "ಮಧುಕ್ರಾಂತಿ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ (madhukranti.in) ಹೆಸರು ನೋಂದಾಯಿಸಿ.",
                "ಜಿಲ್ಲಾ ತೋಟಗಾರಿಕಾ ಕಚೇರಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ತಪಾಸಣೆಯ ನಂತರ ಸಬ್ಸಿಡಿ ದರದಲ್ಲಿ ಜೇನು ಪೆಟ್ಟಿಗೆಗಳನ್ನು ಪಡೆದುಕೊಳ್ಳಿ."
            ],
            "official_source_url": "https://nbhm.gov.in/",
            "issuing_authority": "National Bee Board / Ministry of Agriculture & Farmers Welfare",
            "verification_authority": "Department of Horticulture, Karnataka / National Bee Board",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Horticultural crops, coffee, plantation crops, mustard, sunflower"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Requires prior certified beekeeping training from recognized KVK, horticulture department, or National Bee Board."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಮಾನ್ಯತೆ ಪಡೆದ ಸಂಸ್ಥೆಯಿಂದ ಜೇನುಸಾಕಣೆ ತರಬೇತಿ ಪೂರ್ಣಗೊಳಿಸಿರುವುದು ಕಡ್ಡಾಯ."
            ]
        },

        # 25. 10,000 FPOs
        {
            "id": "10000-fpos",
            "name": "Formation and Promotion of 10,000 FPOs",
            "name_kn": "10,000 ರೈತ ಉತ್ಪಾದಕ ಸಂಸ್ಥೆಗಳ ರಚನೆ ಮತ್ತು ಪ್ರೋತ್ಸಾಹ (ಎಫ್‌ಪಿಒ)",
            "official_abbreviation": "10,000 FPOs",
            "government_level": "central",
            "scheme_type": "real",
            "category": "market_fpo",
            "category_kn": "ರೈತ ಉತ್ಪಾದಕ ಸಂಸ್ಥೆಗಳು (FPO)",
            "assistance_type": "market_access",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Supports formation and nurturing of 10,000 Farmer Producer Organisations with equity grants up to ₹15 lakh per FPO, credit guarantee covers, and management handholding.",
            "description_kn": "ರೈತರು ಒಗ್ಗೂಡಿ ಕೃಷಿ ಪರಿಕರಗಳನ್ನು ಕಡಿಮೆ ದರದಲ್ಲಿ ಖರೀದಿಸಲು ಹಾಗೂ ಬೆಳೆಗೆ ಉತ್ತಮ ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಪಡೆಯಲು 10,000 ಎಫ್‌ಪಿಒಗಳನ್ನು ರಚಿಸುವ ಕೇಂದ್ರ ಯೋಜನೆ.",
            "benefits": [
                "Matching equity grant up to ₹2,000 per farmer member (maximum ₹15 lakh per FPO).",
                "Credit guarantee cover up to ₹2 crore on institutional loans without collateral.",
                "Management cost support of ₹18 lakh per FPO over 3 years."
            ],
            "benefits_kn": [
                "ಪ್ರತಿ ರೈತ ಸದಸ್ಯರಿಗೆ ₹2,000 ರಂತೆ ಗರಿಷ್ಠ ₹15 ಲಕ್ಷದವರೆಗೆ ಈಕ್ವಿಟಿ ಅನುದಾನ.",
                "ಕೊಲ್ಯಾಟರಲ್ ರಹಿತ ಬ್ಯಾಂಕ್ ಸಾಲಕ್ಕೆ ₹2 ಕೋಟಿವರೆಗಿನ ಕ್ರೆಡಿಟ್ ಗ್ಯಾರಂಟಿ ರಕ್ಷಣೆ.",
                "ಎಫ್‌ಪಿಒ ನಿರ್ವಹಣಾ ವೆಚ್ಚಕ್ಕೆ 3 ವರ್ಷಗಳಲ್ಲಿ ₹18 ಲಕ್ಷ ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("fpo_membership", "Open to small and marginal farmers who subscribe to shares and become voting members of a registered FPO.", "ನೋಂದಾಯಿತ ಎಫ್‌ಪಿಒದ ಷೇರುಗಳನ್ನು ಖರೀದಿಸಿ ಸದಸ್ಯರಾಗಲು ಬಯಸುವ ರೈತರು.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "10,000 FPO Guidelines", "verified", "Are you a shareholder member of a registered Farmer Producer Organisation (FPO)?", "ನೀವು ನೋಂದಾಯಿತ ರೈತ ಉತ್ಪಾದಕ ಸಂಸ್ಥೆಯ (FPO) ಷೇರುದಾರ ಸದಸ್ಯರಾಗಿದ್ದೀರಾ?", "Individual farmers benefit by joining an FPO; institutional grants are not personal cash payments.", "ರೈತರು ಎಫ್‌ಪಿಒ ಮೂಲಕ ಒಟ್ಟಾಗಿ ಪ್ರಯೋಜನ ಪಡೆಯುತ್ತಾರೆ; ಇದು ವೈಯಕ್ತಿಕ ನಗದು ಪಾವತಿಯಲ್ಲ.")
            ],
            "required_documents": [
                "Farmer ID / Aadhaar card",
                "Land record (RTC) or crop cultivation proof",
                "FPO share subscription application"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಚೀಟಿ / ಆಧಾರ್",
                "ಪಹಣಿ (RTC) ಅಥವಾ ಸಾಗುವಳಿ ದೃಢೀಕರಣ",
                "ಎಫ್‌ಪಿಒ ಷೇರು ಖರೀದಿ ಅರ್ಜಿ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Contact local Cluster-Based Business Organisation (CBBO), NABARD, or SFAC empanelled FPO.",
                "Purchase minimum prescribed member shares (usually ₹500 to ₹1,000).",
                "Avail bulk input discounts, machinery hiring, and aggregated market selling through FPO."
            ],
            "application_steps_kn": [
                "ಸ್ಥಳೀಯ ಎಫ್‌ಪಿಒ ಅಥವಾ ನಬಾರ್ಡ್ ನಿಯೋಜಿತ ಸಿಬಿಬಿಒ ಸಂಸ್ಥೆಯನ್ನು ಸಂಪರ್ಕಿಸಿ.",
                "ನಿಗದಿತ ಷೇರು ಶುಲ್ಕ ಪಾವತಿಸಿ ಸದಸ್ಯತ್ವ ಪಡೆಯಿರಿ.",
                "ಎಫ್‌ಪಿಒ ಮೂಲಕ ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ರಸಗೊಬ್ಬರ, ಬೀಜ ಪಡೆದು ಒಟ್ಟಾಗಿ ಮಾರಾಟ ಮಾಡಿ ಲಾಭ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://sfacindia.com/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare / SFAC / NABARD / NCDC",
            "verification_authority": "SFAC / NABARD Karnataka Regional Office",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["All agricultural and horticultural produce"],
            "notes": [
                "Current scheme allocations must be confirmed with the implementing CBBO/FPO.",
                "Individual farmers benefit by joining an FPO; institutional grants are for the registered collective."
            ],
            "notes_kn": [
                "ಇದು ರೈತರ ಒಕ್ಕೂಟಗಳಿಗೆ ನೀಡಲಾಗುವ ಸಾಂಸ್ಥಿಕ ನೆರವಾಗಿದ್ದು, ವೈಯಕ್ತಿಕ ನಗದು ಪಾವತಿಯಲ್ಲ."
            ]
        },

        # 26. e-NAM
        {
            "id": "enam",
            "name": "e-NAM – National Agriculture Market",
            "name_kn": "ಇ-ನಾಮ್ - ರಾಷ್ಟ್ರೀಯ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ",
            "official_abbreviation": "e-NAM",
            "government_level": "central",
            "scheme_type": "real",
            "category": "market_fpo",
            "category_kn": "ರಾಷ್ಟ್ರೀಯ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ (ಇ-ನಾಮ್)",
            "assistance_type": "market_access",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Pan-India electronic trading portal networking regulated APMC mandis to create a unified national market with transparent online price discovery and direct online payments.",
            "description_kn": "ರೈತರು ತಮ್ಮ ಉತ್ಪನ್ನಗಳಿಗೆ ದೇಶದ ಯಾವುದೇ ಭಾಗದ ಖರೀದಿದಾರರಿಂದ ಸ್ಪರ್ಧಾತ್ಮಕ ಆನ್‌ಲೈನ್ ಬಿಡ್ಡಿಂಗ್ ಮೂಲಕ ಉತ್ತಮ ಬೆಲೆ ಪಡೆಯಲು ನೆರವಾಗುವ ವಿದ್ಯುನ್ಮಾನ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ.",
            "benefits": [
                "Transparent online bidding ensuring fair commodity prices and eliminating local cartelization.",
                "Direct electronic bank settlement (online payment) upon weighing and quality assaying.",
                "Free quality testing and assaying at integrated mandi laboratories."
            ],
            "benefits_kn": [
                "ಪಾರದರ್ಶಕ ಆನ್‌ಲೈನ್ ಬಿಡ್ಡಿಂಗ್ ಮೂಲಕ ಬೆಳೆಗೆ ಸೂಕ್ತ ಹಾಗೂ ಸ್ಪರ್ಧಾತ್ಮಕ ಮಾರುಕಟ್ಟೆ ದರ.",
                "ತೂಕ ಮತ್ತು ಗುಣಮಟ್ಟ ಪರಿಶೀಲನೆಯ ನಂತರ ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಆನ್‌ಲೈನ್ ಪಾವತಿ.",
                "ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಉಚಿತ ಗುಣಮಟ್ಟ ಪರೀಕ್ಷೆ."
            ],
            "eligibility_rules": [
                make_rule("enam_trader", "Open to any farmer bringing agricultural commodities to an e-NAM integrated APMC market yard.", "ಇ-ನಾಮ್ ಅಳವಡಿಸಿಕೊಂಡಿರುವ ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆಗೆ ಉತ್ಪನ್ನ ತರುವ ಎಲ್ಲಾ ರೈತರಿಗೆ ಲಭ್ಯ.", "ownership", "in", ["owned", "joint_owned", "tenant", "leased"], True, "e-NAM Guidelines", "verified", "Do you market your agricultural produce through APMC mandis?", "ನೀವು ಕೃಷಿ ಉತ್ಪನ್ನಗಳನ್ನು ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಮಾರಾಟ ಮಾಡುತ್ತೀರಾ?", "Commodity assaying and trading rules apply at the integrated mandi.", "ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಗುಣಮಟ್ಟ ಪರೀಕ್ಷೆ ಮತ್ತು ಬಿಡ್ಡಿಂಗ್ ನಿಯಮಗಳು ಅನ್ವಯಿಸುತ್ತವೆ.")
            ],
            "required_documents": [
                "Farmer ID / Aadhaar card",
                "Bank passbook details with IFSC",
                "Mandi lot entry gate pass"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಸಂಖ್ಯೆ / ಆಧಾರ್",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ವಿವರ",
                "ಎಪಿಎಂಸಿ ಗೇಟ್ ಪಾಸ್ ಮತ್ತು ಲಾಟ್ ವಿವರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Register at enam.gov.in or at the gate counter of an integrated APMC yard.",
                "Bring cleaned produce to the yard; assaying lab tests quality and generates digital lot.",
                "Traders bid online nationwide; farmer accepts best bid and receives direct bank transfer."
            ],
            "application_steps_kn": [
                "enam.gov.in ನಲ್ಲಿ ಅಥವಾ ಎಪಿಎಂಸಿ ಗೇಟ್‌ನಲ್ಲಿ ಆಧಾರ್ ನೀಡಿ ನೋಂದಾಯಿಸಿ.",
                "ಉತ್ಪನ್ನವನ್ನು ಮಾರುಕಟ್ಟೆಗೆ ತಂದು ಗುಣಮಟ್ಟ ಪರೀಕ್ಷಿಸಿ ಲಾಟ್ ರಚಿಸಿ.",
                "ಆನ್‌ಲೈನ್ ಬಿಡ್ಡಿಂಗ್‌ನಲ್ಲಿ ಉತ್ತಮ ಬೆಲೆ ಬಂದಾಗ ಒಪ್ಪಿಗೆ ನೀಡಿ ನೇರ ಬ್ಯಾಂಕ್ ಪಾವತಿ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://enam.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare / SFAC",
            "verification_authority": "Karnataka State Agricultural Marketing Board (KSAMB) / Local APMCs",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["Food grains", "Pulses", "Oilseeds", "Spices", "Fruits", "Vegetables"],
            "notes": [
                "It is a transparent market-access and trading service, not a direct cash subsidy.",
                "Payment is settled through e-payment gateway directly into the farmer's bank account."
            ],
            "notes_kn": [
                "ಇದು ಮುಕ್ತ ಮಾರುಕಟ್ಟೆ ಮತ್ತು ಪಾರದರ್ಶಕ ವ್ಯಾಪಾರ ವೇದಿಕೆಯಾಗಿದ್ದು, ನಗದು ಸಹಾಯಧನವಲ್ಲ."
            ]
        },

        # 27. RKVY
        {
            "id": "rkvy",
            "name": "Rashtriya Krishi Vikas Yojana (RKVY)",
            "name_kn": "ರಾಷ್ಟ್ರೀಯ ಕೃಷಿ ವಿಕಾಸ ಯೋಜನೆ (ಆರ್‌ಕೆವಿವೈ)",
            "official_abbreviation": "RKVY",
            "government_level": "central",
            "scheme_type": "real",
            "category": "infrastructure_convergence",
            "category_kn": "ರಾಷ್ಟ್ರೀಯ ಕೃಷಿ ವಿಕಾಸ ಯೋಜನೆ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "District-specific implementation",
            "status_label_kn": "ಜಿಲ್ಲಾವಾರು ಅನುಷ್ಠಾನ",
            "description": "State-led agricultural investment initiative offering flexible funding for farm infrastructure, value addition, seed multiplication, innovation, and agri-startups.",
            "description_kn": "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ, ಸಂಸ್ಕರಣೆ, ಬೀಜೋತ್ಪಾದನೆ ಮತ್ತು ಕೃಷಿ ನವೋದ್ಯಮಗಳಿಗೆ ಪ್ರೋತ್ಸಾಹ ನೀಡಲು ರಾಜ್ಯ ಸರ್ಕಾರಗಳಿಗೆ ಸ್ವಾಯತ್ತತೆ ನೀಡುವ ಸಮಗ್ರ ಕೇಂದ್ರ ಯೋಜನೆ.",
            "benefits": [
                "State-specific custom projects addressing regional productivity gaps and post-harvest bottlenecks.",
                "Innovation grant support up to ₹25 lakh for seed-stage agri-startups and FPO infrastructure."
            ],
            "benefits_kn": [
                "ಸ್ಥಳೀಯ ಕೃಷಿ ಸಮಸ್ಯೆಗಳನ್ನು ಪರಿಹರಿಸುವ ಯೋಜನೆಗಳಿಗೆ ವಿಶೇಷ ಸಹಾಯಧನ.",
                "ಕೃಷಿ ನವೋದ್ಯಮಗಳಿಗೆ ₹25 ಲಕ್ಷದವರೆಗೆ ಅನುದಾನ ಹಾಗೂ ಎಫ್‌ಪಿಒ ಮೂಲಸೌಕರ್ಯ ಬೆಂಬಲ."
            ],
            "eligibility_rules": [
                make_rule("rkvy_project", "Beneficiaries must be selected under state-approved Annual Action Plan projects.", "ರಾಜ್ಯ ಅನುಮೋದಿತ ವಾರ್ಷಿಕ ಕ್ರಿಯಾ ಯೋಜನೆಯಡಿ ಆಯ್ಕೆಯಾದ ಫಲಾನುಭವಿಯಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "RKVY Guidelines", "verified", "Are you applying under an approved state RKVY district project?", "ನೀವು ರಾಜ್ಯದ ಅನುಮೋದಿತ ಆರ್ ಕೆವಿವೈ ಯೋಜನೆಯಡಿ ಅರ್ಜಿ ಸಲ್ಲಿಸುತ್ತಿದ್ದೀರಾ?", "Farmers benefit through approved departmental projects rather than universal entitlement.", "ಇಲಾಖೆಯು ಅನುಮೋದಿಸಿದ ನಿರ್ದಿಷ್ಟ ಯೋಜನೆಗಳ ಮೂಲಕ ಮಾತ್ರ ಇದು ಅನ್ವಯಿಸುತ್ತದೆ.")
            ],
            "required_documents": [
                "Farmer ID / Registration",
                "Land Record RTC",
                "Specific project / component application form"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಚೀಟಿ (FRUITS)",
                "ಪಹಣಿ (RTC)",
                "ಯೋಜನಾ ಘಟಕದ ಅರ್ಜಿ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Track notifications from the State Department of Agriculture / Horticulture.",
                "Submit application for sanctioned RKVY components at district office.",
                "Approved beneficiaries receive direct component subsidy upon verification."
            ],
            "application_steps_kn": [
                "ಕೃಷಿ ಅಥವಾ ತೋಟಗಾರಿಕಾ ಇಲಾಖೆಯ ವಾರ್ಷಿಕ ಅಧಿಸೂಚನೆಗಳನ್ನು ಗಮನಿಸಿ.",
                "ಜಿಲ್ಲಾ ಕಚೇರಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಪರಿಶೀಲನೆಯ ನಂತರ ಮಂಜೂರಾತಿ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://rkvy.nic.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "State Level Sanctioning Committee (SLSC) / Agriculture Dept Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["All agricultural, horticultural and allied sectors"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Project-specific components change annually based on state sanctioning committee approvals."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ವಾರ್ಷಿಕ ಕ್ರಿಯಾ ಯೋಜನೆಗೆ ಅನುಗುಣವಾಗಿ ಯೋಜನೆಗಳು ಬದಲಾಗುತ್ತವೆ."
            ]
        },

        # 28. PM Dhan-Dhaanya
        {
            "id": "pm-dhan-dhaanya",
            "name": "PM Dhan-Dhaanya Krishi Yojana",
            "name_kn": "ಪಿಎಂ ಧನ-ಧಾನ್ಯ ಕೃಷಿ ಯೋಜನೆ",
            "official_abbreviation": "PM Dhan-Dhaanya",
            "government_level": "central",
            "scheme_type": "real",
            "category": "infrastructure_convergence",
            "category_kn": "ಕೃಷಿ ಒಮ್ಮುಖ ಅಭಿವೃದ್ಧಿ",
            "assistance_type": "infrastructure_convergence",
            "status_label": "District-specific implementation",
            "status_label_kn": "ಜಿಲ್ಲಾವಾರು ಅನುಷ್ಠಾನ",
            "description": "District-focused convergence programme intended to improve agricultural productivity and economic opportunity through better irrigation, storage, credit, and scheme integration.",
            "description_kn": "ಆಯ್ದ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ನೀರಾವರಿ, ಸಂಗ್ರಹಣೆ, ಸಾಲ ಮತ್ತು ವಿವಿಧ ಯೋಜನೆಗಳ ಒಮ್ಮುಖ ಅನುಷ್ಠಾನದ ಮೂಲಕ ಕೃಷಿ ಉತ್ಪಾದಕತೆ ಹೆಚ್ಚಿಸುವ ಯೋಜನೆ.",
            "benefits": [
                "Integrated saturation of irrigation, storage, soil health, and credit schemes in priority districts.",
                "Promotes crop diversification towards high-value and climate-resilient commodities."
            ],
            "benefits_kn": [
                "ಆದ್ಯತಾ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ನೀರಾವರಿ, ಗೋದಾಮು ಮತ್ತು ಸಾಲ ಸೌಲಭ್ಯಗಳ ಸಮಗ್ರ ಸಂಯೋಜನೆ.",
                "ಲಾಭದಾಯಕ ಮತ್ತು ಹವಾಮಾನ ಸ್ಥಿತಿಸ್ಥಾಪಕ ಬೆಳೆಗಳ ಕೃಷಿಗೆ ಉತ್ತೇಜನ."
            ],
            "eligibility_rules": [
                make_rule("dhandhaanya_district", "Farmers located in designated priority convergence districts selected by government.", "ಸರ್ಕಾರ ಆಯ್ಕೆ ಮಾಡಿದ ಆದ್ಯತಾ ಜಿಲ್ಲೆಗಳಲ್ಲಿರುವ ರೈತರು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "PM Dhan-Dhaanya Framework", "verified", "Is your farm located in a focus convergence district?", "ನಿಮ್ಮ ಜಮೀನು ಆದ್ಯತಾ ಅಭಿವೃದ್ಧಿ ಜಿಲ್ಲೆಯ ವ್ಯಾಪ್ತಿಯಲ್ಲಿದೆಯೇ?", "Benefits depend on district action plans and rules of converged schemes.", "ಜಿಲ್ಲಾ ಕ್ರಿಯಾ ಯೋಜನೆ ಮತ್ತು ಒಮ್ಮುಖ ಯೋಜನೆಗಳ ನಿಯಮಾವಳಿಗಳ ಮೇಲೆ ಪ್ರಯೋಜನಗಳು ನಿರ್ಧಾರವಾಗುತ್ತವೆ.")
            ],
            "required_documents": [
                "Farmer ID / FRUITS registration",
                "Land record (RTC / Pahani)"
            ],
            "required_documents_kn": [
                "ರೈತರ ಗುರುತಿನ ಚೀಟಿ (FRUITS)",
                "ಪಹಣಿ (RTC)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Enquire with District Administration / Joint Director of Agriculture (JDA).",
                "Participate in district convergence plan activities.",
                "Avail aligned benefits across micro-irrigation, storage, and diversification."
            ],
            "application_steps_kn": [
                "ಜಿಲ್ಲಾ ಕೃಷಿ ಇಲಾಖೆ ಕಚೇರಿಯಲ್ಲಿ ಆದ್ಯತಾ ಜಿಲ್ಲಾ ಯೋಜನೆಗಳ ವಿವರ ಪಡೆಯಿರಿ.",
                "ಒಮ್ಮುಖ ಅಭಿವೃದ್ಧಿ ಕಾಮಗಾರಿಗಳಲ್ಲಿ ನೋಂದಾಯಿಸಿ ಪ್ರಯೋಜನ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://agriwelfare.gov.in/",
            "issuing_authority": "Ministry of Agriculture and Farmers Welfare, Government of India",
            "verification_authority": "District Administration / Agriculture Department Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["Selected Priority Districts", "Karnataka"],
            "supported_crops": ["Food grains, pulses, oilseeds, horticulture"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Convergence framework; not a standalone flat cash payment to every farmer."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ವಿವಿಧ ಯೋಜನೆಗಳ ಒಮ್ಮುಖ ಅನುಷ್ಠಾನ ಕಾರ್ಯಕ್ರಮವಾಗಿದೆ."
            ]
        }
    ]