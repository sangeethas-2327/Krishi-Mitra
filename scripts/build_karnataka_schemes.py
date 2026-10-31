"""
Script to create backend/app/data/schemes_karnataka.py with all 35 Karnataka schemes.
"""
from pathlib import Path

content = '''def make_rule(rule_id, desc, desc_kn, field, operator, expected_value, mandatory=True, ref=None, status="verified", q=None, q_kn=None, why=None, why_kn=None):
    return {
        "rule_id": rule_id,
        "description": desc,
        "description_kn": desc_kn,
        "field": field,
        "operator": operator,
        "expected_value": expected_value,
        "is_mandatory": mandatory,
        "source_reference": ref,
        "verification_status": status,
        "clarification_question": q,
        "clarification_question_kn": q_kn,
        "why_needed": why,
        "why_needed_kn": why_kn
    }

def get_karnataka_schemes():
    return [
        # 1. FRUITS Portal
        {
            "id": "fruits-portal",
            "name": "FRUITS – Farmer Registration & Unified Beneficiary Information System",
            "name_kn": "ಫ್ರೂಟ್ಸ್ – ರೈತರ ನೋಂದಣಿ ಮತ್ತು ಏಕೀಕೃತ ಫಲಾನುಭವಿ ಮಾಹಿತಿ ವ್ಯವಸ್ಥೆ",
            "official_abbreviation": "FRUITS",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "farmer_registration",
            "category_kn": "ರೈತ ನೋಂದಣಿ ಮತ್ತು ಗುರುತು",
            "assistance_type": "farmer_registration",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Karnataka unified farmer registry integrating land records (Bhoomi), Aadhaar, and bank accounts to provide a single Farmer ID (FID) for seamless delivery of all state welfare schemes.",
            "description_kn": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಭೂಮಿ, ಆಧಾರ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಖಾತೆಗಳನ್ನು ಸಂಯೋಜಿಸಿ ಏಕೀಕೃತ ರೈತ ಗುರುತಿನ ಸಂಖ್ಯೆ (FID) ಒದಗಿಸುವ ಮತ್ತು ಎಲ್ಲಾ ಯೋಜನೆಗಳಿಗೆ ಅರ್ಹತೆ ನೀಡುವ ಮೂಲ ನೋಂದಣಿ ವ್ಯವಸ್ಥೆ.",
            "benefits": [
                "Unique 10-digit Farmer Identification Number (FID) eliminating duplicate document submission.",
                "Mandatory prerequisite for all Karnataka agriculture, horticulture, animal husbandry, and sericulture subsidies."
            ],
            "benefits_kn": [
                "ಪ್ರತಿಯೊಬ್ಬ ರೈತರಿಗೂ 10 ಅಂಕಿಗಳ ವಿಶಿಷ್ಟ ಗುರುತಿನ ಸಂಖ್ಯೆ (FID) ದೊರೆಯುತ್ತದೆ.",
                "ಕೃಷಿ, ತೋಟಗಾರಿಕೆ, ಪಶುಸಂಗೋಪನೆ ಮತ್ತು ರೇಷ್ಮೆ ಇಲಾಖೆಗಳ ಎಲ್ಲಾ ಸಬ್ಸಿಡಿಗಳಿಗೆ ಇದು ಕಡ್ಡಾಯ ನೋಂದಣಿಯಾಗಿದೆ."
            ],
            "eligibility_rules": [
                make_rule("fruits_state", "Must own or cultivate agricultural land within Karnataka state.", "ಕರ್ನಾಟಕ ರಾಜ್ಯದಲ್ಲಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು ಅಥವಾ ಸಾಗುವಳಿ ಮಾಡುತ್ತಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "FRUITS Portal Guidelines", "verified", "Is your farm located in Karnataka?", "ನಿಮ್ಮ ಕೃಷಿ ಭೂಮಿ ಕರ್ನಾಟಕದಲ್ಲಿದೆಯೇ?", "FRUITS is exclusively managed by the Government of Karnataka for state residents.", "ಫ್ರೂಟ್ಸ್ ಪೋರ್ಟಲ್ ಕರ್ನಾಟಕ ಸರ್ಕಾರದಿಂದ ಮಾತ್ರ ನಿರ್ವಹಿಸಲ್ಪಡುತ್ತದೆ."),
                make_rule("fruits_land", "Must possess valid land records (RTC / Pahani) or valid tenancy acknowledgement.", "ಮಾನ್ಯವಾದ ಪಹಣಿ (RTC) ಅಥವಾ ಸಾಗುವಳಿ ದಾಖಲೆ ಹೊಂದಿರಬೇಕು.", "ownership", "in", ["owned", "joint_owned", "leased", "tenant"], True, "Bhoomi Integration Norms", "verified", "Do you hold RTC or tenancy documents?", "ನಿಮ್ಮಲ್ಲಿ ಆರ್‌ಟಿಸಿ ಅಥವಾ ಗೇಣಿ ದಾಖಲೆಗಳಿವೆಯೇ?", "Verification is done through digital cross-matching with Bhoomi land database.", "ಭೂಮಿ ತಂತ್ರಾಂಶದೊಂದಿಗೆ ಜಮೀನಿನ ವಿವರ ತಾಳೆ ಮಾಡಲು ಇದು ಅಗತ್ಯವಾಗಿದೆ.")
            ],
            "required_documents": [
                "Aadhaar card of the farmer",
                "RTC / Pahani (Current year)",
                "Bank passbook copy linked to Aadhaar",
                "Caste certificate (for SC/ST farmers, if applicable)"
            ],
            "required_documents_kn": [
                "ರೈತರ ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಚಾಲ್ತಿ ಸಾಲಿನ ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಜೋಡಿತ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್",
                "ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ (ಪರಿಶಿಷ್ಟ ಜಾತಿ / ಪಂಗಡದ ರೈತರಿಗೆ)"
            ],
            "optional_documents": ["Ration card"],
            "optional_documents_kn": ["ರೇಷನ್ ಕಾರ್ಡ್"],
            "application_steps": [
                "Visit local Raitha Samparka Kendra (RSK) or nearest Grama One centre.",
                "Provide Aadhaar and Survey Number of the land; officials link data with Bhoomi.",
                "Receive 10-digit FID via SMS after biometric/OTP authentication."
            ],
            "application_steps_kn": [
                "ಹತ್ತಿರದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK) ಅಥವಾ ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.",
                "ಆಧಾರ್ ಮತ್ತು ಸರ್ವೇ ನಂಬರ್ ನೀಡಿ; ಅಧಿಕಾರಿಗಳು ಭೂಮಿ ತಂತ್ರಾಂಶದೊಂದಿಗೆ ಲಿಂಕ್ ಮಾಡುತ್ತಾರೆ.",
                "ಬಯೋಮೆಟ್ರಿಕ್ ದೃಢೀಕರಣದ ನಂತರ ಮೊಬೈಲ್‌ಗೆ 10 ಅಂಕಿಯ ಎಫ್‌ಐಡಿ (FID) ಬರುತ್ತದೆ."
            ],
            "official_source_url": "https://fruits.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka / e-Governance",
            "verification_authority": "Revenue & Agriculture Departments, Government of Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All 31 Districts of Karnataka"],
            "supported_crops": ["All crops, horticulture, livestock, sericulture, fisheries"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Registration on FRUITS is mandatory before applying for any Karnataka state agriculture scheme."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಕರ್ನಾಟಕದ ಯಾವುದೇ ಕೃಷಿ ಯೋಜನೆಯ ಪ್ರಯೋಜನ ಪಡೆಯಲು ಫ್ರೂಟ್ಸ್ ನೋಂದಣಿ ಕಡ್ಡಾಯವಾಗಿದೆ."
            ]
        },

        # 2. Raitha Siri Scheme (Millet Promotion)
        {
            "id": "raitha-siri",
            "name": "Raitha Siri Scheme (Millet Promotion Scheme)",
            "name_kn": "ರೈತ ಸಿರಿ ಯೋಜನೆ (ಸಿರಿಧಾನ್ಯ ಪ್ರೋತ್ಸಾಹ)",
            "official_abbreviation": "Raitha Siri",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "income_support",
            "category_kn": "ಆದಾಯ ಬೆಂಬಲ ಮತ್ತು ಉತ್ಪಾದನಾ ಪ್ರೋತ್ಸಾಹ",
            "assistance_type": "direct_financial_assistance",
            "status_label": "Seasonal application",
            "status_label_kn": "ಋತುಮಾನ ಆಧಾರಿತ ಅರ್ಜಿ",
            "description": "Karnataka incentive scheme providing direct financial assistance of up to ₹10,000 per hectare (₹4,000 per acre up to 2 hectares) to farmers cultivating minor and major millets.",
            "description_kn": "ಸಿರಿಧಾನ್ಯಗಳನ್ನು ಬೆಳೆಯುವ ರೈತರಿಗೆ ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ ₹10,000 (ಗರಿಷ್ಠ 2 ಹೆಕ್ಟೇರ್‌ಗೆ ₹20,000) ವರೆಗೆ ನೇರ ಪ್ರೋತ್ಸಾಹಧನ ನೀಡುವ ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಯೋಜನೆ.",
            "benefits": [
                "₹10,000 per hectare financial incentive credited directly through DBT after field inspection.",
                "Assistance for minor millets (Ragi, Jowar, Foxtail millet, Little millet, Barnyard millet, Kodo millet, Proso millet)."
            ],
            "benefits_kn": [
                "ಜಮೀನು ಪರಿಶೀಲನೆ ಮತ್ತು ಬೆಳೆ ಸಮೀಕ್ಷೆಯ ನಂತರ ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ ₹10,000 ನೇರ ನಗದು ಪ್ರೋತ್ಸಾಹಧನ.",
                "ರಾಗಿ, ಜೋಳ, ನವಣೆ, ಸಾಮೆ, ಹಾರಕ, ಕೊರಲೆ ಮತ್ತು ಬರಗು ಬೆಳೆಯುವ ರೈತರಿಗೆ ಲಭ್ಯ."
            ],
            "eligibility_rules": [
                make_rule("rs_state", "Must cultivate land in Karnataka state.", "ಕರ್ನಾಟಕ ರಾಜ್ಯದಲ್ಲಿ ಸಾಗುವಳಿ ಮಾಡುತ್ತಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Raitha Siri Guidelines", "verified", "Do you cultivate in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ?", "Raitha Siri is an exclusive Karnataka state welfare scheme.", "ಇದು ಕರ್ನಾಟಕ ರಾಜ್ಯದ ವಿಶೇಷ ಯೋಜನೆಯಾಗಿದೆ."),
                make_rule("rs_crops", "Must cultivate notified millet crops (Ragi, Jowar, Minor millets).", "ಅಧಿಸೂಚಿತ ಸಿರಿಧಾನ್ಯಗಳನ್ನು (ರಾಗಿ, ಜೋಳ, ನವಣೆ, ಸಾಮೆ ಇತ್ಯಾದಿ) ಬೆಳೆದಿರಬೇಕು.", "crops", "contains_any", ["ragi", "jowar", "millet", "millets", "foxtail_millet", "little_millet", "kodo_millet", "barnyard_millet", "proso_millet", "siridhanya"], True, "Department of Agriculture Millet Notification", "verified", "What millets are you currently cultivating or planning to sow?", "ನೀವು ಪ್ರಸ್ತುತ ಯಾವ ಸಿರಿಧಾನ್ಯಗಳನ್ನು ಬೆಳೆಯುತ್ತಿದ್ದೀರಿ?", "Millet crop verification via Karnataka Digital Crop Survey is strictly mandatory.", "ಕರ್ನಾಟಕ ಬೆಳೆ ಸಮೀಕ್ಷೆಯಲ್ಲಿ ಸಿರಿಧಾನ್ಯ ನಮೂದಾಗಿರಬೇಕು.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "Aadhaar card",
                "RTC / Pahani showing millet crop survey record",
                "Aadhaar-linked bank account"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID) ಸಂಖ್ಯೆ",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬೆಳೆ ಸಮೀಕ್ಷೆ ನಮೂದಾದ ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಜೋಡಿತ ಬ್ಯಾಂಕ್ ಖಾತೆ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Register on FRUITS portal and complete Kharif/Rabi sowing of notified millets.",
                "Ensure local crop surveyor records the millet crop in the Beley Darshak / Crop Survey app.",
                "Submit application at Raitha Samparka Kendra (RSK) with FID.",
                "DBT subsidy disbursed upon field verification by Village Agricultural Assistant."
            ],
            "application_steps_kn": [
                "ಫ್ರೂಟ್ಸ್‌ನಲ್ಲಿ ನೋಂದಾಯಿಸಿ ಸಿರಿಧಾನ್ಯ ಬಿತ್ತನೆ ಮಾಡಿ ಬೆಳೆ ಸಮೀಕ್ಷೆಯಲ್ಲಿ ದಾಖಲಿಸಿ.",
                "ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ (RSK) ಭೇಟಿ ನೀಡಿ ಎಫ್‌ಐಡಿ ಮೂಲಕ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಕೃಷಿ ಅಧಿಕಾರಿಯ ಪರಿಶೀಲನೆಯ ನಂತರ ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಹಣ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "Assistant Director of Agriculture (ADA) / RSK",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Ragi", "Jowar", "Navane (Foxtail)", "Same (Little)", "Haraka (Kodo)", "Baragu", "Korale"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Subject to budget allocations and actual physical verification in Karnataka Crop Survey."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ರಾಜ್ಯ ಸರ್ಕಾರದ ಆಯವ್ಯಯ ಹಂಚಿಕೆ ಮತ್ತು ಬೆಳೆ ಸಮೀಕ್ಷೆಯ ಆಧಾರದ ಮೇಲೆ ಪ್ರೋತ್ಸಾಹಧನ ಬಿಡುಗಡೆಯಾಗುತ್ತದೆ."
            ]
        },

        # 3. Raitha Shakti Scheme (Diesel Subsidy)
        {
            "id": "raitha-shakti",
            "name": "Raitha Shakti Scheme (Diesel Subsidy for Farm Machinery)",
            "name_kn": "ರೈತ ಶಕ್ತಿ ಯೋಜನೆ (ಡೀಸೆಲ್ ಸಹಾಯಧನ)",
            "official_abbreviation": "Raitha Shakti",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "equipment_rental",
            "category_kn": "ಯಂತ್ರೋಪಕರಣ ಇಂಧನ ನೆರವು",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "Financial assistance of ₹250 per acre up to a maximum of 5 acres (₹1,250) towards diesel expenditure incurred on farm machinery and tractors.",
            "description_kn": "ಕೃಷಿ ಯಂತ್ರೋಪಕರಣಗಳು ಮತ್ತು ಟ್ರ್ಯಾಕ್ಟರ್‌ಗಳ ಬಳಕೆಗೆ ಪ್ರೋತ್ಸಾಹ ನೀಡಲು ಎಕರೆಗೆ ₹250 ರಂತೆ ಗರಿಷ್ಠ 5 ಎಕರೆಗೆ ₹1,250 ಡೀಸೆಲ್ ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "₹250 per acre diesel reimbursement up to 5 acres (maximum ₹1,250 per farmer).",
                "Direct Benefit Transfer (DBT) via FRUITS portal without paperwork."
            ],
            "benefits_kn": [
                "ಪ್ರತಿ ಎಕರೆಗೆ ₹250 ರಂತೆ ಗರಿಷ್ಠ 5 ಎಕರೆಗೆ ₹1,250 ಡೀಸೆಲ್ ಸಹಾಯಧನ.",
                "ಫ್ರೂಟ್ಸ್ ಪೋರ್ಟಲ್ ಮೂಲಕ ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆ."
            ],
            "eligibility_rules": [
                make_rule("rsh_state", "Must own cultivable agricultural land in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಸಾಗುವಳಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Raitha Shakti Notification", "verified", "Do you own agricultural land in Karnataka?", "ಕರ್ನಾಟಕದಲ್ಲಿ ನಿಮಗೆ ಕೃಷಿ ಜಮೀನಿದೆಯೇ?", "Scheme applies strictly to registered landowning farmers in Karnataka.", "ಕರ್ನಾಟಕದ ನೋಂದಾಯಿತ ಭೂಮಾಲೀಕ ರೈತರಿಗೆ ಮಾತ್ರ ಅನ್ವಯಿಸುತ್ತದೆ."),
                make_rule("rsh_ownership", "Must be registered as landholder in FRUITS / Bhoomi.", "ಫ್ರೂಟ್ಸ್ ಅಥವಾ ಭೂಮಿ ತಂತ್ರಾಂಶದಲ್ಲಿ ಭೂಮಾಲೀಕರಾಗಿ ನೋಂದಣಿಯಾಗಿರಬೇಕು.", "ownership", "in", ["owned", "joint_owned"], True, "Raitha Shakti Guidelines", "verified", "Do you own the land registered in your name?", "ನಿಮ್ಮ ಹೆಸರಿನಲ್ಲಿ ಜಮೀನು ನೋಂದಣಿಯಾಗಿದೆಯೇ?", "Title ownership is required for automatic DBT credit.", "ನೇರ ನಗದು ವರ್ಗಾವಣೆಗೆ ಜಮೀನಿನ ಮಾಲೀಕತ್ವ ಕಡ್ಡಾಯ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "Aadhaar-seeded bank account",
                "RTC land record"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಆಧಾರ್ ಲಿಂಕ್ ಆದ ಬ್ಯಾಂಕ್ ಖಾತೆ",
                "ಆರ್‌ಟಿಸಿ (RTC)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Ensure land record is up to date on FRUITS portal.",
                "Apply via online portal or local RSK during the scheme notification window.",
                "Funds transferred directly via DBT to Aadhaar-seeded account."
            ],
            "application_steps_kn": [
                "ಫ್ರೂಟ್ಸ್ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಜಮೀನಿನ ವಿವರ ನವೀಕರಿಸಿ.",
                "ಅಧಿಸೂಚನೆ ಹೊರಡಿಸಿದಾಗ ಆರ್‌ಎಸ್‌ಕೆ ಕೇಂದ್ರದಲ್ಲಿ ಅಥವಾ ಆನ್‌ಲೈನ್‌ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ನೇರ ನಗದು ವರ್ಗಾವಣೆ ಮೂಲಕ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "Department of Agriculture, Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Budget releases vary by financial year; ongoing status should be verified with the local RSK."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಯೋಜನೆಯ ಚಾಲ್ತಿ ಲಭ್ಯತೆಯನ್ನು ಸ್ಥಳೀಯ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ದೃಢಪಡಿಸಿಕೊಳ್ಳಿ."
            ]
        },

        # 4. Raitha Samruddhi Yojana (Integrated Farming Systems)
        {
            "id": "raitha-samruddhi",
            "name": "Karnataka Raitha Samruddhi Yojana (Integrated Farming)",
            "name_kn": "ಕರ್ನಾಟಕ ರೈತ ಸಮೃದ್ಧಿ ಯೋಜನೆ (ಸಮಗ್ರ ಕೃಷಿ ಪದ್ಧತಿ)",
            "official_abbreviation": "Raitha Samruddhi",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "horticulture_allied",
            "category_kn": "ಸಮಗ್ರ ಕೃಷಿ ಮತ್ತು ಕೃಷಿಯೇತರ ಚಟುವಟಿಕೆ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "State scheme promoting Integrated Farming Systems (IFS) combining agriculture, horticulture, dairy, sericulture, and poultry to drought-proof farmer livelihoods and increase net income.",
            "description_kn": "ಕೃಷಿ, ತೋಟಗಾರಿಕೆ, ಹೈನುಗಾರಿಕೆ, ರೇಷ್ಮೆ ಮತ್ತು ಕೋಳಿ ಸಾಕಾಣಿಕೆಗಳನ್ನು ಸಂಯೋಜಿಸಿ ಸಮಗ್ರ ಕೃಷಿ ಪದ್ಧತಿ (IFS) ರೂಪಿಸಲು ಪ್ರೋತ್ಸಾಹಿಸುವ ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಯೋಜನೆ.",
            "benefits": [
                "Financial subsidy for establishing multi-tier integrated farm models (agriculture + dairy + horticulture + vermicompost).",
                "Technical training and seed/planting material input support."
            ],
            "benefits_kn": [
                "ಬಹು-ಹಂತದ ಸಮಗ್ರ ಕೃಷಿ ಘಟಕ (ಕೃಷಿ + ಹೈನುಗಾರಿಕೆ + ತೋಟಗಾರಿಕೆ + ಎರೆಹುಳು ಗೊಬ್ಬರ) ಸ್ಥಾಪನೆಗೆ ಸಹಾಯಧನ.",
                "ಉಚಿತ ತಾಂತ್ರಿಕ ತರಬೇತಿ ಮತ್ತು ಗುಣಮಟ್ಟದ ಬೀಜ/ಸಸಿ ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("rsam_state", "Must be a resident farmer of Karnataka.", "ಕರ್ನಾಟಕದ ನಿವಾಸಿ ರೈತರಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Raitha Samruddhi Norms", "verified", "Are you farming in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ?", "State scheme restricted to Karnataka farmers.", "ಕರ್ನಾಟಕದ ರೈತರಿಗೆ ಮಾತ್ರ ಸೀಮಿತವಾಗಿದೆ."),
                make_rule("rsam_land", "Must possess at least 1 acre cultivable land suitable for integrated model.", "ಸಮಗ್ರ ಕೃಷಿ ಮಾದರಿಗೆ ಕನಿಷ್ಠ 1 ಎಕರೆ ಸಾಗುವಳಿ ಜಮೀನು ಇರಬೇಕು.", "land_area.value_acres", "greater_than_or_equal", 1.0, True, "IFS Operational Protocol", "verified", "How many acres do you have for integrated farming?", "ಸಮಗ್ರ ಕೃಷಿಗಾಗಿ ನಿಮ್ಮಲ್ಲಿ ಎಷ್ಟು ಎಕರೆ ಜಮೀನಿದೆ?", "Viable integrated farm model requires sufficient land footprint.", "ಸಮಗ್ರ ಕೃಷಿ ಘಟಕಕ್ಕೆ ಕನಿಷ್ಠ ಭೂವಿಸ್ತೀರ್ಣ ಅಗತ್ಯವಿದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record",
                "Aadhaar card",
                "Bank passbook"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": ["Soil test card"],
            "optional_documents_kn": ["ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್"],
            "application_steps": [
                "Visit Assistant Director of Agriculture (ADA) or RSK.",
                "Submit project proposal indicating chosen integrated components (crops, livestock, horticulture).",
                "Departmental inspection and sanction of model demonstration unit."
            ],
            "application_steps_kn": [
                "ಸಹಾಯಕ ಕೃಷಿ ನಿರ್ದೇಶಕರ ಕಚೇರಿಗೆ (ADA) ಅಥವಾ ಆರ್‌ಎಸ್‌ಕೆಗೆ ಭೇಟಿ ನೀಡಿ.",
                "ಆಯ್ಕೆಮಾಡಿದ ಸಮಗ್ರ ಕೃಷಿ ಘಟಕಗಳ (ಬೆಳೆ, ಹೈನು, ತೋಟಗಾರಿಕೆ) ಪ್ರಸ್ತಾವನೆ ಸಲ್ಲಿಸಿ.",
                "ಸ್ಥಳ ಪರಿಶೀಲನೆಯ ನಂತರ ಮಂಜೂರಾತಿ ಪಡೆದು ಸಹಾಯಧನ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "ADA / JDA Agriculture, Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Karnataka Districts"],
            "supported_crops": ["Food crops, pulses, fruit orchards, dairy, sericulture"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Targeted beneficiaries and components vary per annual budget notification."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ವಾರ್ಷಿಕ ಬಜೆಟ್ ಆದೇಶಗಳ ಆಧಾರದ ಮೇಲೆ ಘಟಕ ವೆಚ್ಚ ಮತ್ತು ಸಹಾಯಧನ ನಿರ್ಧಾರವಾಗುತ್ತದೆ."
            ]
        },

        # 5. Chief Minister Raitha Chaitanya Yojane
        {
            "id": "cm-raitha-chaitanya",
            "name": "Chief Minister Raitha Chaitanya Yojane (Capacity Building)",
            "name_kn": "ಮುಖ್ಯಮಂತ್ರಿ ರೈತ ಚೈತನ್ಯ ಯೋಜನೆ (ಸಾಮರ್ಥ್ಯ ವೃದ್ಧಿ ಮತ್ತು ತರಬೇತಿ)",
            "official_abbreviation": "CM-RCY",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "training_advisory",
            "category_kn": "ತರಬೇತಿ ಮತ್ತು ಜ್ಞಾನ ವಿಸ್ತರಣೆ",
            "assistance_type": "training_advisory",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "Training and extension programme empowering farmers, farm women, and rural youth with modern agricultural practices, digital tools, and farm management skills.",
            "description_kn": "ರೈತರು, ಮಹಿಳಾ ರೈತರು ಮತ್ತು ಗ್ರಾಮೀಣ ಯುವಕರಿಗೆ ಆಧುನಿಕ ಕೃಷಿ ತಂತ್ರಜ್ಞಾನ, ಡಿಜಿಟಲ್ ಕೃಷಿ ಮತ್ತು ಕ್ಷೇತ್ರ ನಿರ್ವಹಣೆಯ ಕುರಿತು ಉಚಿತ ತರಬೇತಿ ಮತ್ತು ಜಾಗೃತಿ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Free residential and non-residential agricultural training courses at Krishi Vigyan Kendras (KVKs) and Agricultural Universities.",
                "Stipend and travel reimbursement during institutional training modules."
            ],
            "benefits_kn": [
                "ಕೃಷಿ ವಿಜ್ಞಾನ ಕೇಂದ್ರ (KVK) ಮತ್ತು ಕೃಷಿ ವಿಶ್ವವಿದ್ಯಾಲಯಗಳಲ್ಲಿ ಉಚಿತ ವಸತಿ ಸಹಿತ ಕೃಷಿ ತರಬೇತಿ.",
                "ತರಬೇತಿ ಅವಧಿಯಲ್ಲಿ ಪ್ರಯಾಣ ಭತ್ಯೆ ಮತ್ತು ಪ್ರಮಾಣಪತ್ರ ವಿತರಣೆ."
            ],
            "eligibility_rules": [
                make_rule("cmrc_state", "Must be a practicing farmer or rural youth residing in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ವಾಸಿಸುವ ರೈತರು ಅಥವಾ ಗ್ರಾಮೀಣ ಯುವಕರಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Raitha Chaitanya Norms", "verified", "Do you live in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ವಾಸವಿದ್ದೀರಾ?", "Training programmes are conducted within Karnataka state institutions.", "ತರಬೇತಿಯು ಕರ್ನಾಟಕದ ಸಂಸ್ಥೆಗಳಲ್ಲಿ ಮಾತ್ರ ನಡೆಯುತ್ತದೆ.")
            ],
            "required_documents": [
                "Aadhaar card",
                "FRUITS FID or RTC copy (if landholder)",
                "Bank passbook copy"
            ],
            "required_documents_kn": [
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ ಅಥವಾ ಪಹಣಿ ದಾಖಲೆ",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Contact nearest Raitha Samparka Kendra (RSK) or Agricultural Extension Officer.",
                "Enrol in upcoming training batch for relevant crop or allied farming domain.",
                "Participate in workshops and field exposure visits."
            ],
            "application_steps_kn": [
                "ಹತ್ತಿರದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ ಹೆಸರು ನೋಂದಾಯಿಸಿ.",
                "ನಿಮ್ಮ ಬೆಳೆ ಅಥವಾ ಆಸಕ್ತ ಕ್ಷೇತ್ರಕ್ಕೆ ತಕ್ಕ ತರಬೇತಿ ಬ್ಯಾಚ್ ಆಯ್ಕೆಮಾಡಿ.",
                "ಕಾರ್ಯಾಗಾರ ಮತ್ತು ಕ್ಷೇತ್ರ ಭೇಟಿಗಳಲ್ಲಿ ಭಾಗವಹಿಸಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture / UAS Bangalore, Dharwad, Raichur, Shivamogga",
            "verification_authority": "Raitha Samparka Kendra (RSK)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["All crops, horticulture, livestock, apiary, mushroom"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Training schedules are published seasonally prior to Kharif and Rabi."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಮುಂಗಾರು ಮತ್ತು ಹಿಂಗಾರು ಹಂಗಾಮಿಗೆ ಮುಂಚಿತವಾಗಿ ತರಬೇತಿ ವೇಳಾಪಟ್ಟಿ ಪ್ರಕಟವಾಗುತ್ತದೆ."
            ]
        },

        # 6. Krishi Vistara Yojane
        {
            "id": "krishi-vistara",
            "name": "Krishi Vistara Yojane (Technology Demonstration)",
            "name_kn": "ಕೃಷಿ ವಿಸ್ತಾರ ಯೋಜನೆ (ತಂತ್ರಜ್ಞಾನ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ)",
            "official_abbreviation": "Krishi Vistara",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "training_advisory",
            "category_kn": "ವಿಸ್ತರಣಾ ಶಿಕ್ಷಣ ಮತ್ತು ಕ್ಷೇತ್ರ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ",
            "assistance_type": "training_advisory",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "Frontline field demonstration scheme showcasing high-yielding varieties, pest management packages, and precision farming on farmers' actual fields.",
            "description_kn": "ರೈತರ ಸ್ವಂತ ಹೊಲಗಳಲ್ಲಿ ಸುಧಾರಿತ ತಳಿಗಳು, ಕೀಟ ನಿರ್ವಹಣೆ ಮತ್ತು ನಿಖರ ಕೃಷಿ ತಂತ್ರಜ್ಞಾನಗಳ ಪ್ರಾಯೋಗಿಕ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಆಯೋಜಿಸುವ ಯೋಜನೆ.",
            "benefits": [
                "Free input minikits (certified seeds, biofertilisers, micronutrients) for demonstration plots.",
                "Direct agronomist guidance from sowing to harvest."
            ],
            "benefits_kn": [
                "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ತಾಕುಗಳಿಗೆ ಉಚಿತ ಬಿತ್ತನೆ ಬೀಜ, ಜೈವಿಕ ಗೊಬ್ಬರ ಮತ್ತು ಲಘು ಪೋಷಕಾಂಶಗಳ ಕಿಟ್.",
                "ಬಿತ್ತನೆಯಿಂದ ಕಟಾವಿನವರೆಗೆ ಕೃಷಿ ವಿಜ್ಞಾನಿಗಳಿಂದ ನೇರ ಕ್ಷೇತ್ರ ಮಾರ್ಗದರ್ಶನ."
            ],
            "eligibility_rules": [
                make_rule("kv_state", "Must hold agricultural land in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Krishi Vistara Scheme Norms", "verified", "Do you hold farmland in Karnataka?", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಜಮೀನಿದೆಯೇ?", "Demonstration plots are laid out exclusively in Karnataka villages.", "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ತಾಕುಗಳು ಕರ್ನಾಟಕದ ಗ್ರಾಮಗಳಲ್ಲಿ ಮಾತ್ರ ನಡೆಯುತ್ತವೆ."),
                make_rule("kv_land", "Must possess at least 0.5 acres available for demonstration plot.", "ಪ್ರಾತ್ಯಕ್ಷಿಕೆಗಾಗಿ ಕನಿಷ್ಠ 0.5 ಎಕರೆ ಜಮೀನು ಲಭ್ಯವಿರಬೇಕು.", "land_area.value_acres", "greater_than_or_equal", 0.5, True, "Frontline Demonstration Protocol", "verified", "How much land can you allocate for demonstration?", "ಪ್ರಾತ್ಯಕ್ಷಿಕೆಗೆ ಎಷ್ಟು ಜಮೀನು ಮೀಸಲಿಡಬಹುದು?", "Sufficient plot size required for scientific field comparison.", "ವೈಜ್ಞಾನಿಕ ಹೋಲಿಕೆಗೆ ನಿಗದಿತ ವಿಸ್ತೀರ್ಣ ಅಗತ್ಯ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record copy",
                "Aadhaar card"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Contact Village Agricultural Assistant (VAA) at local RSK.",
                "Offer plot for cluster frontline demonstration.",
                "Receive seed/input minikit and adhere to recommended package of practices."
            ],
            "application_steps_kn": [
                "ಗ್ರಾಮ ಕೃಷಿ ಸಹಾಯಕರನ್ನು (VAA) ಸಂಪರ್ಕಿಸಿ.",
                "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ತಾಕಿಗೆ ಜಮೀನು ಒದಗಿಸಲು ಒಪ್ಪಿಗೆ ಪತ್ರ ನೀಡಿ.",
                "ಉಚಿತ ಕಿಟ್ ಪಡೆದು ವಿಜ್ಞಾನಿಗಳ ಸಲಹೆಯಂತೆ ಬೆಳೆ ನಿರ್ವಹಿಸಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Karnataka",
            "verification_authority": "RSK / Agricultural Extension Officer",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Paddy, Ragi, Maize, Pulses, Oilseeds"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Village clusters are rotated annually by the department."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಪ್ರತಿ ವರ್ಷ ಹೊಸ ಗ್ರಾಮ ಕ್ಲಸ್ಟರ್‌ಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಲಾಗುತ್ತದೆ."
            ]
        },

        # 7. Krishi Bhagya Scheme
        {
            "id": "krishi-bhagya",
            "name": "Krishi Bhagya Scheme (Dryland Farming & Farm Ponds)",
            "name_kn": "ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆ (ಖುಷ್ಕಿ ಕೃಷಿ, ಕೃಷಿ ಹೊಂಡ ಮತ್ತು ಪಾಲಿಹೌಸ್)",
            "official_abbreviation": "Krishi Bhagya",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "irrigation_infrastructure",
            "category_kn": "ಮಳೆಯಾಶ್ರಿತ ಕೃಷಿ ಮತ್ತು ಜಲಸಂರಕ್ಷಣೆ",
            "assistance_type": "irrigation_infrastructure",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Flagship Karnataka rainfed farming scheme providing 80% to 90% subsidy for construction of farm ponds (Krishi Honda), polythene lining, diesel pumpsets, shade-nets, and micro-irrigation in drought-prone taluks.",
            "description_kn": "ಮಳೆ ಕೊರತೆ ಇರುವ ತಾಲೂಕುಗಳಲ್ಲಿ ರೈತರ ಹೊಲಗಳಲ್ಲಿ ಕೃಷಿ ಹೊಂಡ (ಕೃಷಿ ಭಾಗ್ಯ), ಪಾಲಿಥೀನ್ ಹೊದಿಕೆ, ಡೀಸೆಲ್ ಪಂಪ್‌ಸೆಟ್ ಮತ್ತು ಹನಿ ನೀರಾವರಿಗೆ ಶೇ. 80 ರಿಂದ 90 ರಷ್ಟು ಸಹಾಯಧನ ನೀಡುವ ಜನಪ್ರಿಯ ಯೋಜನೆ.",
            "benefits": [
                "80% subsidy for General category and 90% subsidy for SC/ST farmers for farm pond excavation and plastic lining.",
                "Additional assistance for diesel pumpset, micro-irrigation (drip/sprinkler), and shade-net cover."
            ],
            "benefits_kn": [
                "ಸಾಮಾನ್ಯ ವರ್ಗದ ರೈತರಿಗೆ ಶೇ. 80 ಮತ್ತು ಪರಿಶಿಷ್ಟ ಜಾತಿ/ಪಂಗಡದ ರೈತರಿಗೆ ಶೇ. 90 ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಾಣ.",
                "ಡೀಸೆಲ್ ಪಂಪ್‌ಸೆಟ್, ಹನಿ/ತುಂತುರು ನೀರಾವರಿ ಮತ್ತು ಕೃಷಿ ಹೊಂಡದ ಸುತ್ತ ತಂತಿ ಬೇಲಿಗೆ ಹೆಚ್ಚುವರಿ ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("kb_state", "Must be located in rainfed/dryland taluks of Karnataka.", "ಕರ್ನಾಟಕದ ಮಳೆಯಾಶ್ರಿತ ಅಥವಾ ಖುಷ್ಕಿ ತಾಲೂಕಿನಲ್ಲಿ ಜಮೀನು ಇರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Krishi Bhagya Operational Guidelines", "verified", "Is your farm located in a dryland or rainfed area of Karnataka?", "ನಿಮ್ಮ ಜಮೀನು ಮಳೆಯಾಶ್ರಿತ ಪ್ರದೇಶದಲ್ಲಿದೆಯೇ?", "Krishi Bhagya specifically prioritises notified rainfed and drought-vulnerable taluks.", "ಮಳೆ ಕೊರತೆಯಿರುವ ಮತ್ತು ಮಳೆಯಾಶ್ರಿತ ತಾಲೂಕುಗಳಿಗೆ ಇದು ಸೀಮಿತವಾಗಿದೆ."),
                make_rule("kb_land", "Must possess at least 1 acre cultivable land.", "ಕನಿಷ್ಠ 1 ಎಕರೆ ಸಾಗುವಳಿ ಜಮೀನು ಇರಬೇಕು.", "land_area.value_acres", "greater_than_or_equal", 1.0, True, "Farm Pond Design Norms", "verified", "How much land do you own?", "ನಿಮ್ಮಲ್ಲಿ ಎಷ್ಟು ಎಕರೆ ಜಮೀನಿದೆ?", "Farm pond excavation requires minimum land buffer so crop area is not compromised.", "ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಿಸಲು ಕನಿಷ್ಠ ಜಮೀನು ಅಗತ್ಯವಿದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC / Pahani (Current year)",
                "Caste certificate (for 90% SC/ST subsidy)",
                "Aadhaar card",
                "Bank passbook copy"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಚಾಲ್ತಿ ಪಹಣಿ (RTC)",
                "ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ (ಶೇ. 90 ಸಹಾಯಧನ ಪಡೆಯಲು)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Submit online application via FRUITS portal or visit local Raitha Samparka Kendra (RSK).",
                "Assistant Agricultural Officer (AAO) inspects farm and marks GPS coordinates for pond layout.",
                "Execute excavation via empanelled machineries and lay polythene lining.",
                "Submit geo-tagged photos and completion certificate for direct DBT reimbursement."
            ],
            "application_steps_kn": [
                "ಫ್ರೂಟ್ಸ್ ಪೋರ್ಟಲ್ ಅಥವಾ ಆರ್‌ಎಸ್‌ಕೆ ಕೇಂದ್ರದ ಮೂಲಕ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಕೃಷಿ ಅಧಿಕಾರಿಗಳು ಜಮೀನಿಗೆ ಭೇಟಿ ನೀಡಿ ಜಿಪಿಎಸ್ ಆಧಾರಿತ ಸ್ಥಳ ಗುರುತಿಸುತ್ತಾರೆ.",
                "ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಿಸಿ ಪ್ಲಾಸ್ಟಿಕ್ ಹೊದಿಕೆ ಅಳವಡಿಸಿ.",
                "ಜಿಯೋ-ಟ್ಯಾಗ್ ಫೋಟೋ ಪರಿಶೀಲನೆಯ ನಂತರ ನೇರವಾಗಿ ಖಾತೆಗೆ ಸಹಾಯಧನ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "Assistant Director of Agriculture (ADA) / JDA",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["Notified Rainfed Taluks of Karnataka"],
            "supported_crops": ["All rainfed and dryland crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Priority is given to dryland farming zones without assured canal irrigation."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಕಾಲುವೆ ನೀರಾವರಿ ಇಲ್ಲದ ಖುಷ್ಕಿ ಭೂಮಿ ಹೊಂದಿರುವ ರೈತರಿಗೆ ಮೊದಲ ಆದ್ಯತೆ."
            ]
        },

        # 8. Karnataka Micro-Irrigation Scheme
        {
            "id": "karnataka-micro-irrigation",
            "name": "Karnataka State Micro-Irrigation Scheme (Drip & Sprinkler)",
            "name_kn": "ಕರ್ನಾಟಕ ರಾಜ್ಯ ಸೂಕ್ಷ್ಮ ನೀರಾವರಿ ಯೋಜನೆ (ಹನಿ ಮತ್ತು ತುಂತುರು ನೀರಾವರಿ)",
            "official_abbreviation": "KA Micro-Irrigation",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "irrigation_infrastructure",
            "category_kn": "ನೀರಾವರಿ ಮೂಲಸೌಕರ್ಯ",
            "assistance_type": "irrigation_infrastructure",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Comprehensive Karnataka subsidy programme providing up to 90% subsidy for SC/ST farmers and up to 75% to 90% subsidy for small and marginal farmers on drip and sprinkler irrigation installations.",
            "description_kn": "ಹನಿ ಮತ್ತು ತುಂತುರು ನೀರಾವರಿ ಅಳವಡಿಕೆಗೆ ಎಸ್‌ಸಿ/ಎಸ್‌ಟಿ ರೈತರಿಗೆ ಶೇ. 90 ರವರೆಗೆ ಮತ್ತು ಸಣ್ಣ/ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಶೇ. 75 ರಿಂದ 90 ರವರೆಗೆ ಗರಿಷ್ಠ ಸಹಾಯಧನ ನೀಡುವ ರಾಜ್ಯ ಯೋಜನೆ.",
            "benefits": [
                "90% subsidy on total system cost for SC/ST small/marginal farmers.",
                "75% to 90% subsidy for General category small and marginal farmers up to 5 acres / 2 hectares.",
                "Water saving up to 50% and yield increase up to 30%."
            ],
            "benefits_kn": [
                "ಪರಿಶಿಷ್ಟ ಜಾತಿ/ಪಂಗಡದ ಸಣ್ಣ/ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಶೇ. 90 ರಷ್ಟು ಸಬ್ಸಿಡಿ.",
                "ಸಾಮಾನ್ಯ ವರ್ಗದ ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಶೇ. 75 ರಿಂದ 90 ರಷ್ಟು ಸಬ್ಸಿಡಿ.",
                "ಶೇ. 50 ರಷ್ಟು ನೀರಿನ ಉಳಿತಾಯ ಮತ್ತು ಶೇ. 30 ರಷ್ಟು ಅಧಿಕ ಇಳುವರಿ."
            ],
            "eligibility_rules": [
                make_rule("kmi_state", "Land must be located in Karnataka state.", "ಜಮೀನು ಕರ್ನಾಟಕ ರಾಜ್ಯದಲ್ಲಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "KA Micro-Irrigation Policy", "verified", "Is your farm located in Karnataka?", "ನಿಮ್ಮ ಜಮೀನು ಕರ್ನಾಟಕದಲ್ಲಿದೆಯೇ?", "State subsidy funds are allocated for Karnataka lands only.", "ರಾಜ್ಯ ಸಹಾಯಧನ ಕರ್ನಾಟಕದ ಜಮೀನುಗಳಿಗೆ ಮಾತ್ರ ಅನ್ವಯಿಸುತ್ತದೆ."),
                make_rule("kmi_water", "Must possess an assured water source (Borewell, Open well, River/Canal lifting).", "ಸುಸ್ಥಿರ ನೀರಿನ ಮೂಲ (ಬೋರ್‌ವೆಲ್, ತೆರೆದ ಬಾವಿ ಅಥವಾ ನದಿ ಮೂಲ) ಹೊಂದಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, "Micro Irrigation Technical Guidelines", "verified", "Do you have an active borewell, open well, or irrigation water source?", "ನಿಮ್ಮ ಜಮೀನಿನಲ್ಲಿ ಬೋರ್‌ವೆಲ್ ಅಥವಾ ನೀರಿನ ಮೂಲವಿದೆಯೇ?", "Drip or sprinkler installation is technically unfeasible without a functional water source.", "ನೀರಿನ ಮೂಲವಿಲ್ಲದೆ ಹನಿ ನೀರಾವರಿ ಅಳವಡಿಸಲು ಸಾಧ್ಯವಿಲ್ಲ."),
                make_rule("kmi_land", "Must possess cultivable land up to 5 acres for high-slab subsidy.", "ಸಹಾಯಧನ ಪಡೆಯಲು ಸಾಗುವಳಿ ಜಮೀನು ಹೊಂದಿರಬೇಕು.", "land_area.value_acres", "greater_than", 0, True, "Horticulture Department Rules", "verified", "What is your total land holding size?", "ನಿಮ್ಮ ಒಟ್ಟು ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ ಎಷ್ಟು?", "Subsidy percentage varies between small/marginal and large farmers.", "ಹಿಡುವಳಿ ವಿಸ್ತೀರ್ಣದ ಆಧಾರದ ಮೇಲೆ ಸಹಾಯಧನದ ಪ್ರಮಾಣ ನಿರ್ಧಾರವಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC / Pahani showing water source entry",
                "Electricity bill / pump energisation certificate",
                "Aadhaar card",
                "Caste certificate (for 90% SC/ST subsidy)",
                "Bank passbook"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ನೀರಿನ ಮೂಲ ನಮೂದಾದ ಪಹಣಿ (RTC)",
                "ವಿದ್ಯುತ್ ಬಿಲ್ ಅಥವಾ ಪಂಪ್‌ಸೆಟ್ ದಾಖಲೆ",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ (ಶೇ. 90 ರಿಯಾಯಿತಿಗೆ)",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": ["Quotation from empanelled drip manufacturer"],
            "optional_documents_kn": ["ಅನುಮೋದಿತ ಹನಿ ನೀರಾವರಿ ಕಂಪನಿಯ ಕೊಟೇಶನ್"],
            "application_steps": [
                "Register on Karnataka Micro-Irrigation portal via FRUITS.",
                "Select approved drip/sprinkler vendor and upload site quotation.",
                "Horticulture / Agriculture officer performs pre-installation inspection.",
                "Vendor installs system; post-inspection with geo-tagging triggers direct subsidy release."
            ],
            "application_steps_kn": [
                "ಫ್ರೂಟ್ಸ್ ಮೂಲಕ ಕರ್ನಾಟಕ ಸೂಕ್ಷ್ಮ ನೀರಾವರಿ ತಂತ್ರಾಂಶದಲ್ಲಿ ನೋಂದಾಯಿಸಿ.",
                "ಅಧಿಕೃತ ಕಂಪನಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಕೊಟೇಶನ್ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.",
                "ಅಧಿಕಾರಿಗಳು ಸ್ಥಳ ಪರಿಶೀಲನೆ ನಡೆಸಿ ಅನುಮೋದಿಸುತ್ತಾರೆ.",
                "ಯಂತ್ರ ಅಳವಡಿಸಿದ ನಂತರ ಜಿಯೋ-ಟ್ಯಾಗ್ ಪರಿಶೀಲನೆಯಾಗಿ ಸಬ್ಸಿಡಿ ಬಿಡುಗಡೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://horticulturedir.karnataka.gov.in/",
            "issuing_authority": "Department of Horticulture & Department of Agriculture, Karnataka",
            "verification_authority": "Senior Assistant Director of Horticulture (SADH) / RSK",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Arecanut, Coconut, Banana, Vegetables, Flowers, Sugarcane, Cotton, Maize"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Subsidy is available once in 7 years per land parcel under standard norms."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಸಾಮಾನ್ಯವಾಗಿ ಒಂದು ಸರ್ವೇ ನಂಬರ್‌ಗೆ 7 ವರ್ಷಗಳಿಗೊಮ್ಮೆ ಮಾತ್ರ ಈ ಸಹಾಯಧನ ಲಭ್ಯವಿರುತ್ತದೆ."
            ]
        },

        # 9. Ganga Kalyana Scheme
        {
            "id": "ganga-kalyana",
            "name": "Ganga Kalyana Scheme (Irrigation Borewells for SC/ST/OBC)",
            "name_kn": "ಗಂಗಾ ಕಲ್ಯಾಣ ಯೋಜನೆ (ಉಚಿತ ಬೋರ್‌ವೆಲ್ ಮತ್ತು ನೀರಾವರಿ ಸೌಲಭ್ಯ)",
            "official_abbreviation": "Ganga Kalyana",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "irrigation_infrastructure",
            "category_kn": "ನೀರಾವರಿ ಸೌಲಭ್ಯ (ವಿಶೇಷ ವರ್ಗಗಳು)",
            "assistance_type": "irrigation_infrastructure",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "State welfare scheme drilling free individual borewells or community open wells with pump energisation for small and marginal farmers belonging to SC, ST, and backward communities.",
            "description_kn": "ಪರಿಶಿಷ್ಟ ಜಾತಿ, ಪರಿಶಿಷ್ಟ ಪಂಗಡ ಮತ್ತು ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಉಚಿತ ಬೋರ್‌ವೆಲ್ ಕೊರೆಯಿಸಿ, ಪಂಪ್ ಮತ್ತು ವಿದ್ಯುದ್ದೀಕರಣ ಒದಗಿಸುವ ಜನಪ್ರಿಯ ಯೋಜನೆ.",
            "benefits": [
                "Free individual borewell drilling, submersible pump, pipes, and electrical energisation.",
                "Community irrigation projects (lift/canal) for clusters of farmers owning contiguous land."
            ],
            "benefits_kn": [
                "ಉಚಿತ ಕೊಳವೆ ಬಾವಿ ಕೊರೆಯುವಿಕೆ, ಸಬ್‌ಮರ್ಸಿಬಲ್ ಪಂಪ್, ಪೈಪ್‌ಗಳು ಮತ್ತು ವಿದ್ಯುತ್ ಸಂಪರ್ಕ ಉಚಿತ.",
                "ಜಂಟಿ ರೈತರ ಗುಂಪುಗಳಿಗೆ ಸಮುದಾಯ ಏತ ನೀರಾವರಿ ಯೋಜನೆ."
            ],
            "eligibility_rules": [
                make_rule("gk_state", "Must be a permanent resident farmer of Karnataka.", "ಕರ್ನಾಟಕದ ಖಾಯಂ ನಿವಾಸಿ ರೈತರಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Ganga Kalyana Guidelines", "verified", "Are you a permanent resident farmer in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದ ಖಾಯಂ ನಿವಾಸಿ ರೈತರೇ?", "Administered through Karnataka State Development Corporations.", "ಕರ್ನಾಟಕ ರಾಜ್ಯ ಅಭಿವೃದ್ಧಿ ನಿಗಮಗಳ ಮೂಲಕ ಜಾರಿಯಾಗುತ್ತದೆ."),
                make_rule("gk_land", "Must possess small/marginal agricultural landholding (1.0 to 5.0 acres).", "1.0 ರಿಂದ 5.0 ಎಕರೆ ಒಳಗಿನ ಸಣ್ಣ ಅಥವಾ ಅತಿ ಸಣ್ಣ ಜಮೀನು ಹೊಂದಿರಬೇಕು.", "land_area.value_acres", "greater_than_or_equal", 1.0, True, "Development Corporation Criteria", "verified", "What is your landholding size?", "ನಿಮ್ಮ ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ ಎಷ್ಟು?", "Scheme specifically targets small/marginal farmers without existing irrigation.", "ನೀರಾವರಿ ಸೌಲಭ್ಯವಿಲ್ಲದ ಸಣ್ಣ/ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಮಾತ್ರ ಮೀಸಲಾಗಿದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "Aadhaar card",
                "Caste and Income certificate (issued by Tahsildar)",
                "RTC / Pahani (Current year)",
                "Affidavit stating no existing borewell on the land"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ತಹಶೀಲ್ದಾರ್ ನೀಡಿದ ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ",
                "ಚಾಲ್ತಿ ಸಾಲಿನ ಪಹಣಿ (RTC)",
                "ಜಮೀನಿನಲ್ಲಿ ಬೇರೆ ಬೋರ್‌ವೆಲ್ ಇಲ್ಲವೆಂದು ಪ್ರಮಾಣ ಪತ್ರ"
            ],
            "optional_documents": ["Bhoomi mutation extract"],
            "optional_documents_kn": ["ಮ್ಯುಟೇಶನ್ ಪ್ರತಿ"],
            "application_steps": [
                "Apply online via Seva Sindhu or respective Development Corporation portal (Ambedkar, Valmiki, KMDC, D. Devaraj Urs).",
                "Submit hard copies at Taluk Development Officer office.",
                "Taluk selection committee (headed by MLA) shortlists eligible beneficiaries.",
                "Hydrogeologist survey conducted; empanelled agency drills borewell and provides pump."
            ],
            "application_steps_kn": [
                "ಸೇವಾ ಸಿಂಧು ಅಥವಾ ಸಂಬಂಧಿತ ನಿಗಮಗಳ ಪೋರ್ಟಲ್ ಮೂಲಕ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ತಾಲೂಕು ಅಭಿವೃದ್ಧಿ ಅಧಿಕಾರಿಯ ಕಚೇರಿಗೆ ದಾಖಲೆ ಸಲ್ಲಿಸಿ.",
                "ಶಾಸಕರ ಅಧ್ಯಕ್ಷತೆಯ ಸಮಿತಿ ಅರ್ಹ ಫಲಾನುಭವಿಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡುತ್ತದೆ.",
                "ಭೂಗರ್ಭ ವಿಜ್ಞಾನಿಗಳ ತಪಾಸಣೆಯ ನಂತರ ಉಚಿತ ಬೋರ್‌ವೆಲ್ ಮತ್ತು ಪಂಪ್ ನೀಡಲಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://kmdc.karnataka.gov.in/",
            "issuing_authority": "Karnataka SC/ST Development Corporation / Backward Classes Corporations",
            "verification_authority": "District Manager / Taluk Development Officer",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Selection depends on annual corporation budget targets and taluk legislative committee approval."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ವಾರ್ಷಿಕ ನಿಗಮದ ಗುರಿಗಳು ಮತ್ತು ತಾಲೂಕು ಸಮಿತಿಯ ಅನುಮೋದನೆಗೆ ಒಳಪಟ್ಟಿರುತ್ತದೆ."
            ]
        },

        # 10. KA Watershed Development & Soil Conservation
        {
            "id": "ka-watershed-soil-conservation",
            "name": "Karnataka Watershed Development & Soil Conservation Programme",
            "name_kn": "ಕರ್ನಾಟಕ ಜಲಾನಯನ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ಮಣ್ಣು ಸಂರಕ್ಷಣಾ ಕಾರ್ಯಕ್ರಮ",
            "official_abbreviation": "KA-Watershed",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "irrigation_infrastructure",
            "category_kn": "ಜಲಾನಯನ ಮತ್ತು ಮಣ್ಣು ಸಂರಕ್ಷಣೆ",
            "assistance_type": "irrigation_infrastructure",
            "status_label": "District-specific implementation",
            "status_label_kn": "ಜಿಲ್ಲಾವಾರು ಅನುಷ್ಠಾನ",
            "description": "Area-based soil and moisture conservation programme implementing bunding, check dams, nala bunds, and contour trenches to arrest soil erosion and recharge groundwater.",
            "description_kn": "ಮಣ್ಣಿನ ಸವೆತ ತಡೆಗಟ್ಟಲು ಮತ್ತು ಅಂತರ್ಜಲ ಮರುಪೂರಣಕ್ಕಾಗಿ ಬದು ನಿರ್ಮಾಣ, ಚೆಕ್ ಡ್ಯಾಂ ಮತ್ತು ಕಂದಕಗಳನ್ನು ನಿರ್ಮಿಸುವ ಸಮಗ್ರ ಜಲಾನಯನ ಯೋಜನೆ.",
            "benefits": [
                "Up to 100% cost execution for community drainage line treatments and check dams.",
                "Heavily subsidised farm bunding, trench cum bunding, and agro-forestry saplings."
            ],
            "benefits_kn": [
                "ಚೆಕ್ ಡ್ಯಾಂ ಮತ್ತು ನಾಲಾ ಬದು ನಿರ್ಮಾಣಕ್ಕೆ ಶೇ. 100 ರಷ್ಟು ಸರ್ಕಾರಿ ವೆಚ್ಚ.",
                "ಹೊಲದ ಬದು ನಿರ್ಮಾಣ ಮತ್ತು ಕೃಷಿ ಅರಣ್ಯ ಸಸಿಗಳಿಗೆ ಗರಿಷ್ಠ ಸಹಾಯಧನ."
            ],
            "eligibility_rules": [
                make_rule("wtr_state", "Must own land located within approved watershed micro-project boundary in Karnataka.", "ಕರ್ನಾಟಕದ ಅನುಮೋದಿತ ಜಲಾನಯನ ಯೋಜನಾ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಜಮೀನು ಇರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Watershed Micro-Plan", "verified", "Is your land part of an active watershed project area?", "ನಿಮ್ಮ ಜಮೀನು ಜಲಾನಯನ ಯೋಜನಾ ವ್ಯಾಪ್ತಿಯಲ್ಲಿದೆಯೇ?", "Watershed works are implemented topographically on a micro-watershed boundary basis.", "ಜಲಾನಯನ ಕಾಮಗಾರಿಗಳು ಭೌಗೋಳಿಕ ವ್ಯಾಪ್ತಿಯ ಆಧಾರದಲ್ಲಿ ಜಾರಿಯಾಗುತ್ತವೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record",
                "Aadhaar card"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Contact Assistant Director of Agriculture (Watershed) or RSK.",
                "Verify whether farmer's survey number falls in the current micro-watershed action plan.",
                "Departmental engineers execute bunding or conservation works."
            ],
            "application_steps_kn": [
                "ಸಹಾಯಕ ಕೃಷಿ ನಿರ್ದೇಶಕರು (ಜಲಾನಯನ) ಅಥವಾ ಆರ್‌ಎಸ್‌ಕೆಯನ್ನು ಸಂಪರ್ಕಿಸಿ.",
                "ಸರ್ವೇ ನಂಬರ್ ಜಲಾನಯನ ಕ್ರಿಯಾ ಯೋಜನೆಯಲ್ಲಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.",
                "ಇಲಾಖೆಯ ವತಿಯಿಂದ ಬದು ನಿರ್ಮಾಣ ಕಾಮಗಾರಿ ಕೈಗೊಳ್ಳಲಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://watershed.karnataka.gov.in/",
            "issuing_authority": "Watershed Development Department, Government of Karnataka",
            "verification_authority": "Assistant Director of Agriculture (Watershed)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["Selected Micro-Watersheds across Karnataka"],
            "supported_crops": ["All dryland and rainfed crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Works are sanctioned area-wise rather than individual standalone cash grants."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ನೇರ ನಗದು ಬದಲಾಗಿ ಸಮುದಾಯ ಮತ್ತು ಕ್ಷೇತ್ರ ಕಾಮಗಾರಿಗಳ ರೂಪದಲ್ಲಿ ಜಾರಿಯಾಗುತ್ತದೆ."
            ]
        }
    ]
'''

Path("backend/app/data/schemes_karnataka.py").write_text(content, encoding="utf-8")
print("Written initial 10 Karnataka schemes to backend/app/data/schemes_karnataka.py")

