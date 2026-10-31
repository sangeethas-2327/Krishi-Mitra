def make_rule(rule_id, desc, desc_kn, field, operator, expected_value, mandatory=True, ref=None, status="verified", q=None, q_kn=None, why=None, why_kn=None):
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
                make_rule("rs_crops", "Must cultivate notified millet crops (Ragi, Jowar, Minor millets).", "ಅಧಿಸೂಚಿತ ಸಿರಿಧಾನ್ಯಗಳನ್ನು (ರಾಗಿ, ಜೋಳ, ನವಣೆ, ಸಾಮೆ ಇತ್ಯಾದಿ) ಬೆಳೆದಿರಬೇಕು.", "crops", "any_of", ["ragi", "jowar", "millet", "millets", "foxtail_millet", "little_millet", "kodo_millet", "barnyard_millet", "proso_millet", "siridhanya"], True, "Department of Agriculture Millet Notification", "verified", "What millets are you currently cultivating or planning to sow?", "ನೀವು ಪ್ರಸ್ತುತ ಯಾವ ಸಿರಿಧಾನ್ಯಗಳನ್ನು ಬೆಳೆಯುತ್ತಿದ್ದೀರಿ?", "Millet crop verification via Karnataka Digital Crop Survey is strictly mandatory.", "ಕರ್ನಾಟಕ ಬೆಳೆ ಸಮೀಕ್ಷೆಯಲ್ಲಿ ಸಿರಿಧಾನ್ಯ ನಮೂದಾಗಿರಬೇಕು.")
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
                make_rule("kmi_water", "Must possess an assured water source (Borewell, Open well, River/Canal lifting).", "ಸುಸ್ಥಿರ ನೀರಿನ ಮೂಲ (ಬೋರ್‌ವೆಲ್, ತೆರೆದ ಬಾವಿ ಅಥವಾ ನದಿ ಮೂಲ) ಹೊಂದಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, True, "Micro Irrigation Technical Guidelines", "verified", "Do you have an active borewell, open well, or irrigation water source?", "ನಿಮ್ಮ ಜಮೀನಿನಲ್ಲಿ ಬೋರ್‌ವೆಲ್ ಅಥವಾ ನೀರಿನ ಮೂಲವಿದೆಯೇ?", "Drip or sprinkler installation is technically unfeasible without a functional water source.", "ನೀರಿನ ಮೂಲವಿಲ್ಲದೆ ಹನಿ ನೀರಾವರಿ ಅಳವಡಿಸಲು ಸಾಧ್ಯವಿಲ್ಲ."),
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
        },
# 11. Agricultural Pump-Set Electricity Subsidy Scheme
        {
            "id": "agri-pumpset-electricity",
            "name": "Agricultural Pump-Set Free/Subsidised Electricity Scheme",
            "name_kn": "ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್‌ಗಳಿಗೆ ಉಚಿತ/ರಿಯಾಯಿತಿ ವಿದ್ಯುತ್ ಯೋಜನೆ",
            "official_abbreviation": "Agri-Power Subsidy",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "irrigation_infrastructure",
            "category_kn": "ವಿದ್ಯುತ್ ನೆರವು ಮತ್ತು ನೀರಾವರಿ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Karnataka government policy providing free electricity to individual farmers for agricultural irrigation pumpsets up to 10 Horse Power (HP).",
            "description_kn": "10 ಹೆಚ್.ಪಿ (HP) ವರೆಗಿನ ಕೃಷಿ ನೀರಾವರಿ ಪಂಪ್‌ಸೆಟ್‌ಗಳಿಗೆ ಸಂಪೂರ್ಣ ಉಚಿತ ವಿದ್ಯುತ್ ಒದಗಿಸುವ ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಮಹತ್ವದ ಯೋಜನೆ.",
            "benefits": [
                "100% electricity tariff subsidy for agricultural IP sets up to 10 HP capacity.",
                "Direct subsidy payment from state exchequer to ESCOMs (BESCOM, MESCOM, HESCOM, GESCOM, CHESCOM)."
            ],
            "benefits_kn": [
                "10 ಹೆಚ್.ಪಿ ವರೆಗಿನ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್‌ಗಳಿಗೆ ಸಂಪೂರ್ಣ ಉಚಿತ ವಿದ್ಯುತ್ ಸರಬರಾಜು.",
                "ವಿದ್ಯುತ್ ಸರಬರಾಜು ಕಂಪನಿಗಳಿಗೆ (ಎಸ್ಕಾಮ್‌ಗಳು) ಸರ್ಕಾರದಿಂದಲೇ ಪೂರ್ಣ ಸಬ್ಸಿಡಿ ಪಾವತಿ."
            ],
            "eligibility_rules": [
                make_rule("ep_state", "Farmland and registered IP set must be in Karnataka state.", "ಕೃಷಿ ಭೂಮಿ ಮತ್ತು ಪಂಪ್‌ಸೆಟ್ ಕರ್ನಾಟಕ ರಾಜ್ಯದಲ್ಲಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "KERC Tariff Order & Govt Orders", "verified", "Is your farm pump energised in Karnataka?", "ನಿಮ್ಮ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್ ಕರ್ನಾಟಕದಲ್ಲಿದೆಯೇ?", "Applicable strictly to agricultural consumers of Karnataka ESCOMs.", "ಕರ್ನಾಟಕದ ಎಸ್ಕಾಮ್ ಗ್ರಾಹಕರಿಗೆ ಮಾತ್ರ ಅನ್ವಯಿಸುತ್ತದೆ."),
                make_rule("ep_irrigation", "Must have functional irrigation pumpset up to 10 HP.", "10 ಹೆಚ್‌ಪಿ ವರೆಗಿನ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್ ಹೊಂದಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, True, "ESCOM Agricultural Consumer Norms", "verified", "Do you have an irrigation pumpset installed?", "ನೀವು ನೀರಾವರಿ ಪಂಪ್‌ಸೆಟ್ ಹೊಂದಿದ್ದೀರಾ?", "Electricity subsidy applies exclusively to active agricultural irrigation connections.", "ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್ ಸಂಪರ್ಕಗಳಿಗೆ ಮಾತ್ರ ಇದು ಅನ್ವಯಿಸುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC showing land and borewell/well details",
                "Aadhaar card",
                "Electricity Account ID / RR Number from respective ESCOM"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಆರ್‌ಟಿಸಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಎಸ್ಕಾಮ್ ಆರ್‌ಆರ್ ಸಂಖ್ಯೆ (RR Number) / ಖಾತೆ ಸಂಖ್ಯೆ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Register agricultural borewell / open well connection with local ESCOM section office.",
                "Ensure Aadhaar and FRUITS FID are linked with the RR Number.",
                "Benefit is automatically credited as zero energy bill under agricultural tariff."
            ],
            "application_steps_kn": [
                "ಸ್ಥಳೀಯ ಎಸ್ಕಾಮ್ ಕಚೇರಿಯಲ್ಲಿ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್ ಆರ್‌ಆರ್ ನಂಬರ್ ನೋಂದಾಯಿಸಿ.",
                "ಆರ್‌ಆರ್ ನಂಬರ್‌ಗೆ ಆಧಾರ್ ಮತ್ತು ಫ್ರೂಟ್ಸ್ ಲಿಂಕ್ ಮಾಡಿ.",
                "ಪ್ರತಿ ತಿಂಗಳ ಬಿಲ್‌ನಲ್ಲಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಉಚಿತ ವಿದ್ಯುತ್ ರಿಯಾಯಿತಿ ದೊರೆಯುತ್ತದೆ."
            ],
            "official_source_url": "https://energy.karnataka.gov.in/",
            "issuing_authority": "Department of Energy, Government of Karnataka / ESCOMs",
            "verification_authority": "Local ESCOM Sub-Division & Department of Agriculture",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Karnataka Districts"],
            "supported_crops": ["All crops requiring irrigation"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Commercial or non-agricultural use on the same line attracts cancellation and penalty."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಕೃಷಿಯೇತರ ಬಳಕೆಗೆ ಈ ವಿದ್ಯುತ್ ಬಳಸುವುದನ್ನು ಕಟ್ಟುನಿಟ್ಟಾಗಿ ನಿಷೇಧಿಸಲಾಗಿದೆ."
            ]
        },

        # 12. Farm Mechanisation Subsidy Scheme
        {
            "id": "farm-mechanisation-subsidy",
            "name": "Karnataka Farm Mechanisation Subsidy Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ಕೃಷಿ ಯಾಂತ್ರೀಕರಣ ಸಹಾಯಧನ ಯೋಜನೆ",
            "official_abbreviation": "Farm Mechanisation",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "equipment_rental",
            "category_kn": "ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ನೆರವು",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "State subsidy programme providing 50% subsidy for General category and up to 90% subsidy for SC/ST farmers for purchasing tractors, power tillers, rotavators, weeders, and sprayers.",
            "description_kn": "ಟ್ರ್ಯಾಕ್ಟರ್, ಪವರ್ ಟಿಲ್ಲರ್, ರೋಟಾವೇಟರ್, ಕಳೆ ಕೀಳುವ ಯಂತ್ರ ಮತ್ತು ಸ್ಪ್ರೇಯರ್‌ಗಳ ಖರೀದಿಗೆ ಸಾಮಾನ್ಯ ರೈತರಿಗೆ ಶೇ. 50 ಮತ್ತು ಎಸ್‌ಸಿ/ಎಸ್‌ಟಿ ರೈತರಿಗೆ ಶೇ. 90 ವರೆಗೆ ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "50% subsidy for General category and 90% subsidy for SC/ST farmers on approved farm machineries.",
                "Covers power tillers, rotavators, seed drills, multi-crop threshers, and power sprayers."
            ],
            "benefits_kn": [
                "ಸಾಮಾನ್ಯ ರೈತರಿಗೆ ಶೇ. 50 ಮತ್ತು ಪರಿಶಿಷ್ಟ ಜಾತಿ/ಪಂಗಡದ ರೈತರಿಗೆ ಶೇ. 90 ರಷ್ಟು ಸಹಾಯಧನ.",
                "ಪವರ್ ಟಿಲ್ಲರ್, ರೋಟಾವೇಟರ್, ಬಿತ್ತನೆ ಯಂತ್ರ, ಕಟಾವು ಯಂತ್ರ ಮತ್ತು ಸ್ಪ್ರೇಯರ್‌ಗಳು ಲಭ್ಯ."
            ],
            "eligibility_rules": [
                make_rule("fm_state", "Must own cultivable agricultural land in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಸಾಗುವಳಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "KA Farm Mechanisation Norms", "verified", "Do you own agricultural land in Karnataka?", "ಕರ್ನಾಟಕದಲ್ಲಿ ನಿಮಗೆ ಕೃಷಿ ಜಮೀನಿದೆಯೇ?", "Subsidy is funded through Karnataka state agricultural budget.", "ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕೃಷಿ ಇಲಾಖೆಯಿಂದ ಈ ನೆರವು ನೀಡಲಾಗುತ್ತದೆ."),
                make_rule("fm_land", "Must possess at least 1 acre cultivable land (more for heavy tractors).", "ಕನಿಷ್ಠ 1 ಎಕರೆ ಕೃಷಿ ಜಮೀನು ಇರಬೇಕು.", "land_area.value_acres", "greater_than_or_equal", 1.0, True, "Machinery Eligibility Criteria", "verified", "How much land do you hold?", "ನಿಮ್ಮ ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ ಎಷ್ಟು?", "Heavy tractor subsidy requires larger holding, small implements require 1 acre.", "ಟ್ರ್ಯಾಕ್ಟರ್‌ಗೆ ಕನಿಷ್ಠ ಹಿಡುವಳಿ ಅಗತ್ಯವಿದೆ; ಸಣ್ಣ ಉಪಕರಣಗಳಿಗೆ 1 ಎಕರೆ ಸಾಕು.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record (Current year)",
                "Aadhaar card",
                "Caste certificate (for SC/ST 90% subsidy)",
                "Bank passbook",
                "Driving licence (for tractor applicants)"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಚಾಲ್ತಿ ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ (ಶೇ. 90 ಸಹಾಯಧನಕ್ಕೆ)",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್",
                "ಚಾಲನಾ ಪರವಾನಗಿ (ಟ್ರ್ಯಾಕ್ಟರ್ ಅರ್ಜಿದಾರರಿಗೆ)"
            ],
            "optional_documents": ["Quotation from empanelled machinery dealer"],
            "optional_documents_kn": ["ಅನುಮೋದಿತ ಡೀಲರ್ ಕೊಟೇಶನ್"],
            "application_steps": [
                "Apply online through Karnataka DBT / FRUITS portal or visit local RSK.",
                "Submit preferred machinery specification and dealer quotation.",
                "Department issues Purchase Order (PO) based on seniority/lottery.",
                "Physical inspection and GPS engraving of serial number prior to subsidy release."
            ],
            "application_steps_kn": [
                "ಡಿಬಿಟಿ / ಫ್ರೂಟ್ಸ್ ಪೋರ್ಟಲ್ ಮೂಲಕ ಅಥವಾ ಆರ್‌ಎಸ್‌ಕೆ ಕೇಂದ್ರದಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಮೆಷಿನ್ ಕೊಟೇಶನ್ ಮತ್ತು ದಾಖಲೆಗಳನ್ನು ಸಲ್ಲಿಸಿ.",
                "ಅನುಮೋದನೆ ಪತ್ರ (PO) ಬಂದ ನಂತರ ಯಂತ್ರ ಖರೀದಿ ಮಾಡಿ.",
                "ಅಧಿಕಾರಿಗಳ ತಪಾಸಣೆ ಮತ್ತು ಜಿಪಿಎಸ್ ಸೀರಿಯಲ್ ನಂಬರ್ ದಾಖಲಿಸಿದ ನಂತರ ಸಬ್ಸಿಡಿ ಬಿಡುಗಡೆ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "Assistant Director of Agriculture (ADA)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["All agricultural crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Machinery cannot be sold or transferred for a minimum lock-in period of 5 years."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಖರೀದಿಸಿದ ಯಂತ್ರೋಪಕರಣಗಳನ್ನು ಕನಿಷ್ಠ 5 ವರ್ಷಗಳವರೆಗೆ ಮಾರಾಟ ಮಾಡುವಂತಿಲ್ಲ."
            ]
        },

        # 13. Krishi Yantra Dhare
        {
            "id": "krishi-yantra-dhare",
            "name": "Krishi Yantra Dhare (Custom Hiring Service Centres)",
            "name_kn": "ಕೃಷಿ ಯಂತ್ರಧಾರೆ (ಬಾಡಿಗೆ ಆಧಾರಿತ ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ಕೇಂದ್ರಗಳು)",
            "official_abbreviation": "Krishi Yantra Dhare",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "equipment_rental",
            "category_kn": "ಕೃಷಿ ಯಂತ್ರ ಬಾಡಿಗೆ ಸೇವೆ",
            "assistance_type": "equipment_rental",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Network of hobli-level custom hiring service centres established through PPP (SKDRDP and others) offering tractors, harvesters, and implements to small farmers at government-regulated affordable rental rates.",
            "description_kn": "ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ರಿಯಾಯಿತಿ ಬಾಡಿಗೆ ದರದಲ್ಲಿ ಟ್ರ್ಯಾಕ್ಟರ್, ಕಟಾವು ಯಂತ್ರ ಮತ್ತು ಕೃಷಿ ಸಲಕರಣೆಗಳನ್ನು ಒದಗಿಸುವ ಹೋಬಳಿ ಮಟ್ಟದ ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಕೇಂದ್ರಗಳು.",
            "benefits": [
                "Rental access to high-cost machinery (paddy transplanters, combine harvesters, rotavators) at subsidised hourly rates.",
                "Overcomes capital barrier for small and marginal farmers who cannot afford purchasing heavy machinery."
            ],
            "benefits_kn": [
                "ದುಬಾರಿ ಕೃಷಿ ಯಂತ್ರಗಳನ್ನು (ನಾಟಿ ಯಂತ್ರ, ಕಂಬೈನ್ ಹಾರ್ವೆಸ್ಟರ್) ಕೈಗೆಟುಕುವ ಗಂಟೆಯ ಬಾಡಿಗೆ ದರದಲ್ಲಿ ಪಡೆಯುವ ಸೌಲಭ್ಯ.",
                "ಸ್ವಂತ ಯಂತ್ರ ಖರೀದಿಸಲು ಸಾಧ್ಯವಾಗದ ಸಣ್ಣ ರೈತರಿಗೆ ಭಾರಿ ಉಳಿತಾಯ."
            ],
            "eligibility_rules": [
                make_rule("kyd_state", "Must cultivate land in Karnataka near a functional Krishi Yantra Dhare centre.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Krishi Yantra Dhare Operational Norms", "verified", "Do you cultivate in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ?", "Centres operate across Karnataka hoblis.", "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಹೋಬಳಿಗಳಲ್ಲಿ ಈ ಕೇಂದ್ರಗಳು ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿವೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number or Aadhaar card",
                "RTC / Pahani copy for booking confirmation"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID) ಅಥವಾ ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬುಕಿಂಗ್ ಮಾಡಲು ಪಹಣಿ (RTC)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Visit nearest Hobli Krishi Yantra Dhare Centre or book via the official Karnataka Agri Mobile App.",
                "Specify required machine (tractor, rotavator, harvester) and date.",
                "Pay regulated rental fee upon completion of field operation."
            ],
            "application_steps_kn": [
                "ಹತ್ತಿರದ ಹೋಬಳಿ ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ ಅಥವಾ ಮೊಬೈಲ್ ಆಪ್ ಮೂಲಕ ಬುಕ್ ಮಾಡಿ.",
                "ಅಗತ್ಯವಿರುವ ಯಂತ್ರ ಮತ್ತು ದಿನಾಂಕವನ್ನು ಮುಂಗಡವಾಗಿ ಕಾಯ್ದಿರಿಸಿ.",
                "ಕೆಲಸ ಮುಗಿದ ನಂತರ ನಿಗದಿತ ರಿಯಾಯಿತಿ ಬಾಡಿಗೆ ಪಾವತಿಸಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Karnataka (in partnership with SKDRDP / agencies)",
            "verification_authority": "Local Krishi Yantra Dhare Centre Manager / RSK",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Hoblis across Karnataka"],
            "supported_crops": ["Paddy, Ragi, Maize, Sugarcane, Pulses, Commercial crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Advance booking is strongly advised during peak sowing and harvesting seasons."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಬಿತ್ತನೆ ಮತ್ತು ಕಟಾವು ಸಮಯದಲ್ಲಿ ಮುಂಗಡ ಬುಕಿಂಗ್ ಮಾಡಿಕೊಳ್ಳುವುದು ಉತ್ತಮ."
            ]
        },

        # 14. Agro-Processing & Tarpaulins Distribution Scheme
        {
            "id": "agro-processing-tarpaulins",
            "name": "Agro-Processing & Tarpaulins Distribution Scheme",
            "name_kn": "ಕೃಷಿ ಉತ್ಪನ್ನ ಸಂಸ್ಕರಣೆ ಮತ್ತು ತಾಡಪಾಲು ವಿತರಣಾ ಯೋಜನೆ",
            "official_abbreviation": "Tarpaulins Scheme",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "equipment_rental",
            "category_kn": "ಕೊಯ್ಲೋತ್ತರ ಸಂಸ್ಕರಣೆ ಮತ್ತು ತಾಡಪಾಲು",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Distribution of heavy-duty HDPE tarpaulins, mini dal mills, flour mills, and solar dryers at 50% to 90% subsidy to prevent post-harvest grain losses.",
            "description_kn": "ಧಾನ್ಯ ಒಣಗಿಸಲು ಮತ್ತು ಮಳೆಯಿಂದ ರಕ್ಷಿಸಲು ಗುಣಮಟ್ಟದ ತಾಡಪಾಲು (Tarpaulins), ಮಿನಿ ದಾಲ್ ಮಿಲ್ ಮತ್ತು ಹಿಟ್ಟಿನ ಗಿರಣಿಗಳನ್ನು ಶೇ. 50 ರಿಂದ 90 ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ವಿತರಿಸುವ ಯೋಜನೆ.",
            "benefits": [
                "Subsidised HDPE tarpaulin sheets (24x18 ft, 250+ GSM) at ₹500 to ₹1,000 farmer share (up to 75%-90% subsidy).",
                "Subsidised small post-harvest processing equipment for farm-level value addition."
            ],
            "benefits_kn": [
                "ಉತ್ತಮ ಗುಣಮಟ್ಟದ ತಾಡಪಾಲುಗಳನ್ನು ಶೇ. 75 ರಿಂದ 90 ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ (ಅಲ್ಪ ರೈತ ವಂತಿಗೆಯಲ್ಲಿ) ವಿತರಣೆ.",
                "ಕೊಯ್ಲೋತ್ತರ ನಷ್ಟ ತಡೆಗಟ್ಟಲು ಮಿನಿ ಸಂಸ್ಕರಣಾ ಘಟಕಗಳಿಗೆ ಸಹಾಯಧನ."
            ],
            "eligibility_rules": [
                make_rule("tp_state", "Must be a practicing farmer with land in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರುವ ರೈತರಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Agro Processing Scheme Norms", "verified", "Do you cultivate in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ?", "Tarpaulins are supplied through Karnataka RSK network.", "ಕರ್ನಾಟಕದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಗಳ ಮೂಲಕ ವಿತರಿಸಲಾಗುತ್ತದೆ."),
                make_rule("tp_land", "Must possess cultivable land record (RTC).", "ಕೃಷಿ ಜಮೀನಿನ ಪಹಣಿ (RTC) ಹೊಂದಿರಬೇಕು.", "land_area.value_acres", "greater_than", 0, True, "RSK Distribution Norms", "verified", "Do you hold valid RTC?", "ನಿಮ್ಮ ಬಳಿ ಚಾಲ್ತಿ ಪಹಣಿ ಇದೆಯೇ?", "One tarpaulin per farmer family / FID based on landholding.", "ಭೂಹಿಡುವಳಿಯ ಆಧಾರದಲ್ಲಿ ಪ್ರತಿ ರೈತ ಕುಟುಂಬಕ್ಕೆ ತಾಡಪಾಲು ವಿತರಣೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "Aadhaar card",
                "RTC land record",
                "Caste certificate (for SC/ST higher subsidy)"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಪಹಣಿ (RTC)",
                "ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ (ಹೆಚ್ಚುವರಿ ಸಬ್ಸಿಡಿಗೆ)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Visit local Raitha Samparka Kendra (RSK) during pre-harvest notification window.",
                "Submit FID and register demand for tarpaulins or mini processing units.",
                "Pay designated beneficiary contribution and collect tarpaulin directly at RSK."
            ],
            "application_steps_kn": [
                "ಕೊಯ್ಲು ಸಮಯಕ್ಕೆ ಮುಂಚಿತವಾಗಿ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ (RSK) ಭೇಟಿ ನೀಡಿ.",
                "ಎಫ್‌ಐಡಿ ನೀಡಿ ತಾಡಪಾಲಿಗಾಗಿ ನೋಂದಾಯಿಸಿ.",
                "ನಿಗದಿತ ರೈತ ವಂತಿಗೆ ಪಾವತಿಸಿ ಸ್ಥಳದಲ್ಲೇ ತಾಡಪಾಲು ಪಡೆದುಕೊಳ್ಳಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "Raitha Samparka Kendra (RSK) Agricultural Officer",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Paddy, Ragi, Maize, Jowar, Pulses, Oilseeds, Coffee, Arecanut"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Distribution is on a first-come, first-served basis subject to RSK physical stock."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಆರ್‌ಎಸ್‌ಕೆ ಸ್ಟಾಕ್ ಲಭ್ಯತೆಯ ಆಧಾರದ ಮೇಲೆ ಮೊದಲು ಬಂದವರಿಗೆ ಮೊದಲ ಆದ್ಯತೆ."
            ]
        },

        # 15. Hi-Tech Harvester Hubs
        {
            "id": "hitech-harvester-hubs",
            "name": "Karnataka Hi-Tech Harvester Hubs Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ಹೈಟೆಕ್ ಹಾರ್ವೆಸ್ಟರ್ ಹಬ್ ಯೋಜನೆ",
            "official_abbreviation": "Harvester Hubs",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "equipment_rental",
            "category_kn": "ಹೈಟೆಕ್ ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ಹಬ್",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "Establishment of specialized combine harvester and sugarcane harvester hubs through Farmer Producer Organisations (FPOs) and entrepreneurs with up to 50% capital subsidy.",
            "description_kn": "ರೈತ ಉತ್ಪಾದಕ ಸಂಸ್ಥೆಗಳು (FPO) ಮತ್ತು ಗ್ರಾಮೀಣ ಉದ್ಯಮಿಗಳ ಮೂಲಕ ಕಂಬೈನ್ ಹಾರ್ವೆಸ್ಟರ್ ಮತ್ತು ಕಬ್ಬು ಕಟಾವು ಯಂತ್ರಗಳ ಹಬ್ ಸ್ಥಾಪನೆಗೆ ಶೇ. 50 ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Capital subsidy up to 50% (capped as per project guidelines) for high-value harvesting machinery packages.",
                "Mitigates severe agricultural labour shortages during peak harvesting windows."
            ],
            "benefits_kn": [
                "ಭಾರಿ ವೆಚ್ಚದ ಕಟಾವು ಯಂತ್ರಗಳ ಪ್ಯಾಕೇಜ್ ಖರೀದಿಗೆ ಶೇ. 50 ರವರೆಗೆ ಬಂಡವಾಳ ಸಹಾಯಧನ.",
                "ಕಟಾವು ಸಂದರ್ಭದಲ್ಲಿ ತೀವ್ರ ಕೃಷಿ ಕೂಲಿ ಕಾರ್ಮಿಕರ ಕೊರತೆ ನೀಗಿಸಲು ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("hh_state", "Must be registered FPO, PACCS, or agricultural entrepreneur in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ನೋಂದಾಯಿತ FPO, ಸಹಕಾರ ಸಂಘ ಅಥವಾ ಕೃಷಿ ಉದ್ಯಮಿಯಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Harvester Hub Policy", "verified", "Is your enterprise based in Karnataka?", "ನಿಮ್ಮ ಸಂಸ್ಥೆ ಕರ್ನಾಟಕದಲ್ಲಿದೆಯೇ?", "Hubs are established in intensive paddy, sugarcane, and maize belts in Karnataka.", "ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಕೃಷಿ ವಲಯಗಳಲ್ಲಿ ಈ ಹಬ್‌ಗಳು ಸ್ಥಾಪನೆಯಾಗುತ್ತವೆ.")
            ],
            "required_documents": [
                "FPO registration certificate / Entrepreneur Aadhaar & PAN",
                "Detailed Project Report (DPR)",
                "Bank loan sanction letter for machinery package"
            ],
            "required_documents_kn": [
                "ಎಫ್‌ಪಿಒ ನೋಂದಣಿ ಪತ್ರ / ಉದ್ಯಮಿ ಆಧಾರ್ ಮತ್ತು ಪ್ಯಾನ್",
                "ಯೋಜನಾ ವರದಿ (DPR)",
                "ಬ್ಯಾಂಕ್ ಸಾಲ ಮಂಜೂರಾತಿ ಪತ್ರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Submit project proposal to District Joint Director of Agriculture (JDA).",
                "State Level Executive Committee approves viable proposals.",
                "Subsidy released back-ended upon machinery procurement and physical audit."
            ],
            "application_steps_kn": [
                "ಜಿಲ್ಲಾ ಜಂಟಿ ಕೃಷಿ ನಿರ್ದೇಶಕರಿಗೆ (JDA) ಯೋಜನಾ ಪ್ರಸ್ತಾವನೆ ಸಲ್ಲಿಸಿ.",
                "ರಾಜ್ಯ ಸಮಿತಿ ಪರಿಶೀಲಿಸಿ ಅನುಮೋದಿಸುತ್ತದೆ.",
                "ಯಂತ್ರ ಖರೀದಿಯ ನಂತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಸಹಾಯಧನ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "Joint Director of Agriculture (JDA)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["Notified Paddy & Sugarcane Districts"],
            "supported_crops": ["Paddy, Sugarcane, Maize, Wheat"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Requires bank tie-up and technical project evaluation."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಬ್ಯಾಂಕ್ ಸಾಲ ಸಂಯೋಜನೆ ಮತ್ತು ತಾಂತ್ರಿಕ ಮೌಲ್ಯಮಾಪನ ಅಗತ್ಯ."
            ]
        },

        # 16. Subsidised Certified Seed Distribution Scheme
        {
            "id": "subsidised-seed-distribution",
            "name": "Karnataka Subsidised Certified Seed Distribution Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ರಿಯಾಯಿತಿ ದರದ ಪ್ರಮಾಣಿತ ಬಿತ್ತನೆ ಬೀಜ ವಿತರಣಾ ಯೋಜನೆ",
            "official_abbreviation": "Seed Subsidy",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "input_assistance",
            "category_kn": "ಬಿತ್ತನೆ ಬೀಜ ಮತ್ತು ರಿಯಾಯಿತಿ ಪರಿಕರ",
            "assistance_type": "input_assistance",
            "status_label": "Seasonal application",
            "status_label_kn": "ಋತುಮಾನ ಆಧಾರಿತ ಅರ್ಜಿ",
            "description": "Pre-monsoon and post-monsoon distribution of high-yielding certified seeds (paddy, ragi, pulses, groundnut, sunflower) through RSKs at 50% to 75% subsidy.",
            "description_kn": "ಮುಂಗಾರು ಮತ್ತು ಹಿಂಗಾರು ಹಂಗಾಮಿನಲ್ಲಿ ಭತ್ತ, ರಾಗಿ, ತೊಗರಿ, ಕಡಲೆ, ಶೇಂಗಾ ಮುಂತಾದ ಪ್ರಮಾಣಿತ ಬಿತ್ತನೆ ಬೀಜಗಳನ್ನು ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಗಳ ಮೂಲಕ ಶೇ. 50 ರಿಂದ 75 ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ವಿತರಿಸುವ ಯೋಜನೆ.",
            "benefits": [
                "Subsidised certified seed bags (50% to 75% subsidy depending on crop and farmer category).",
                "High germination assurance and certified seed replacement rate (SRR) improvement."
            ],
            "benefits_kn": [
                "ಪ್ರಮಾಣಿತ ಬಿತ್ತನೆ ಬೀಜಗಳಿಗೆ ಶೇ. 50 ರಿಂದ 75 ರಷ್ಟು ಸರ್ಕಾರಿ ರಿಯಾಯಿತಿ.",
                "ಉತ್ತಮ ಮೊಳಕೆ ಸಾಮರ್ಥ್ಯ ಮತ್ತು ರೋಗ ನಿರೋಧಕ ಉತ್ತಮ ಇಳುವರಿ ಖಾತರಿ."
            ],
            "eligibility_rules": [
                make_rule("sd_state", "Must be a cultivating farmer in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಸಾಗುವಳಿ ಮಾಡುವ ರೈತರಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Seed Distribution Guidelines", "verified", "Do you cultivate in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ?", "Distributed exclusively through Karnataka RSK network.", "ಕರ್ನಾಟಕದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಗಳ ಮೂಲಕ ಮಾತ್ರ ವಿತರಣೆ."),
                make_rule("sd_land", "Must possess valid land record (RTC) matching crop season.", "ಹಂಗಾಮಿಗೆ ಹೊಂದಿಕೆಯಾಗುವ ಪಹಣಿ (RTC) ಹೊಂದಿರಬೇಕು.", "land_area.value_acres", "greater_than", 0, True, "Seed Quota Norms", "verified", "Do you have valid RTC records?", "ನಿಮ್ಮ ಬಳಿ ಚಾಲ್ತಿ ಪಹಣಿ ಇದೆಯೇ?", "Seed quantity quota is allotted strictly proportional to RTC land area (max 2-5 acres quota).", "ಪಹಣಿಯಲ್ಲಿರುವ ವಿಸ್ತೀರ್ಣಕ್ಕೆ ಅನುಗುಣವಾಗಿ ಬೀಜದ ಪ್ರಮಾಣ ನಿಗದಿಯಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "Aadhaar card",
                "Current year RTC / Pahani"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಚಾಲ್ತಿ ಸಾಲಿನ ಪಹಣಿ (RTC)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Visit local Raitha Samparka Kendra (RSK) at beginning of sowing season.",
                "Provide FID number; system automatically checks land eligibility quota in FRUITS.",
                "Pay subsidised farmer share and collect certified seed bags on spot."
            ],
            "application_steps_kn": [
                "ಬಿತ್ತನೆ ಹಂಗಾಮು ಪ್ರಾರಂಭವಾದಾಗ ಹತ್ತಿರದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ (RSK) ಭೇಟಿ ನೀಡಿ.",
                "ಎಫ್‌ಐಡಿ ನೀಡಿದಾಗ ಸಿಸ್ಟಂ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅರ್ಹ ಬೀಜದ ಕೋಟಾ ತೋರಿಸುತ್ತದೆ.",
                "ರಿಯಾಯಿತಿ ದರ ಪಾವತಿಸಿ ತಕ್ಷಣವೇ ಬೀಜದ ಚೀಲಗಳನ್ನು ಪಡೆದುಕೊಳ್ಳಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Karnataka State Seeds Corporation (KSSC) / Department of Agriculture",
            "verification_authority": "Raitha Samparka Kendra (RSK)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Paddy, Ragi, Jowar, Maize, Red gram, Bengal gram, Groundnut, Soybean"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Subject to RSK seasonal quota and variety availability."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಹಂಗಾಮಿನಲ್ಲಿ ಆರ್‌ಎಸ್‌ಕೆ ದಾಸ್ತಾನು ಮತ್ತು ತಳಿ ಲಭ್ಯತೆಗೆ ಒಳಪಟ್ಟಿರುತ್ತದೆ."
            ]
        },

        # 17. Soil Testing & Soil Health Management (Karnataka)
        {
            "id": "ka-soil-testing",
            "name": "Karnataka Soil Testing & Soil Health Management Programme",
            "name_kn": "ಕರ್ನಾಟಕ ಮಣ್ಣು ಪರೀಕ್ಷೆ ಮತ್ತು ಮಣ್ಣು ಆರೋಗ್ಯ ನಿರ್ವಹಣಾ ಕಾರ್ಯಕ್ರಮ",
            "official_abbreviation": "KA Soil Testing",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "training_advisory",
            "category_kn": "ಮಣ್ಣು ಪರೀಕ್ಷೆ ಮತ್ತು ಸಲಹೆ",
            "assistance_type": "training_advisory",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Comprehensive state soil diagnostic testing service through district and taluk laboratories providing crop-specific nutrient recommendations and soil amelioration advice.",
            "description_kn": "ಜಿಲ್ಲಾ ಮತ್ತು ತಾಲೂಕು ಮಣ್ಣು ಪರೀಕ್ಷಾ ಪ್ರಯೋಗಾಲಯಗಳ ಮೂಲಕ ಉಚಿತ/ಅಲ್ಪಶುಲ್ಕದಲ್ಲಿ ಮಣ್ಣು ಪರೀಕ್ಷೆ ನಡೆಸಿ, ಬೆಳೆವಾರು ರಸಗೊಬ್ಬರ ಶಿಫಾರಸು ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Detailed 12-parameter soil test report (pH, EC, Organic Carbon, N, P, K, S, Zn, Fe, Cu, Mn, B).",
                "Scientific fertilizer dosage card preventing over-application and reducing cost of cultivation."
            ],
            "benefits_kn": [
                "12 ಪ್ರಮುಖ ನಿಯತಾಂಕಗಳ (pH, ಲವಣಾಂಶ, ಸಾವಯವ ಇಂಗಾಲ, ಸಾರಜನಕ, ರಂಜಕ, ಪೊಟ್ಯಾಷ್ ಮತ್ತು ಲಘು ಪೋಷಕಾಂಶಗಳು) ವಿವರವಾದ ಪರೀಕ್ಷಾ ವರದಿ.",
                "ಅನಗತ್ಯ ರಸಗೊಬ್ಬರ ಬಳಕೆ ತಡೆದು ವೆಚ್ಚ ಕಡಿಮೆ ಮಾಡಲು ವೈಜ್ಞಾನಿಕ ಗೊಬ್ಬರ ಶಿಫಾರಸು ಪತ್ರ."
            ],
            "eligibility_rules": [
                make_rule("st_state", "Farmland must be located in Karnataka.", "ಕೃಷಿ ಜಮೀನು ಕರ್ನಾಟಕದಲ್ಲಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Soil Testing Norms", "verified", "Is your farm located in Karnataka?", "ನಿಮ್ಮ ಜಮೀನು ಕರ್ನಾಟಕದಲ್ಲಿದೆಯೇ?", "Testing services are routed through Karnataka Department of Agriculture labs.", "ಕರ್ನಾಟಕ ಕೃಷಿ ಇಲಾಖೆಯ ಲ್ಯಾಬ್‌ಗಳಲ್ಲಿ ಈ ಪರೀಕ್ಷೆ ನಡೆಯುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land survey number copy",
                "Properly dried 500g composite soil sample"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಸರ್ವೇ ನಂಬರ್ ವಿವರವಿರುವ ಪಹಣಿ (RTC)",
                "ವೈಜ್ಞಾನಿಕವಾಗಿ ಸಂಗ್ರಹಿಸಿದ 500 ಗ್ರಾಂ ಮಣ್ಣಿನ ಮಾದರಿ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Collect 'V-shape' composite soil sample from 8-10 points across the plot.",
                "Submit sample at nearest Raitha Samparka Kendra (RSK) or District Soil Testing Lab.",
                "Receive printed Soil Health Card with fertilizer recommendation within 2 to 3 weeks."
            ],
            "application_steps_kn": [
                "ಹೊಲದಲ್ಲಿ 'V' ಆಕಾರದಲ್ಲಿ 8-10 ಕಡೆಗಳಿಂದ ಮಣ್ಣಿನ ಮಾದರಿ ಸಂಗ್ರಹಿಸಿ ಒಣಗಿಸಿ.",
                "ಹತ್ತಿರದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ ಅಥವಾ ಜಿಲ್ಲಾ ಮಣ್ಣು ಪರೀಕ್ಷಾ ಕೇಂದ್ರಕ್ಕೆ ನೀಡಿ.",
                "2-3 ವಾರಗಳಲ್ಲಿ ರಸಗೊಬ್ಬರ ಶಿಫಾರಸು ಸಹಿತ ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ ಪಡೆಯಿರಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "Assistant Director of Agriculture (Soil Testing Lab)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Soil testing is recommended once every 3 years."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಪ್ರತಿ 3 ವರ್ಷಕ್ಕೊಮ್ಮೆ ಮಣ್ಣು ಪರೀಕ್ಷೆ ಮಾಡಿಸಿಕೊಳ್ಳುವುದು ಉತ್ತಮ."
            ]
        },

        # 18. Bhoo Chetana Scheme
        {
            "id": "bhoo-chetana",
            "name": "Bhoo Chetana Scheme (Soil Fertility & Micro-Nutrient Management)",
            "name_kn": "ಭೂ ಚೇತನ ಯೋಜನೆ (ಮಣ್ಣಿನ ಫಲವತ್ತತೆ ಮತ್ತು ಲಘು ಪೋಷಕಾಂಶ ನಿರ್ವಹಣೆ)",
            "official_abbreviation": "Bhoo Chetana",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "input_assistance",
            "category_kn": "ಮಣ್ಣು ಫಲವತ್ತತೆ ಮತ್ತು ಸೂಕ್ಷ್ಮ ಪೋಷಕಾಂಶ",
            "assistance_type": "input_assistance",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "State initiative in collaboration with ICRISAT delivering subsidised gypsum, zinc sulphate, and borax to correct widespread secondary and micronutrient deficiencies in dryland soils.",
            "description_kn": "ಖುಷ್ಕಿ ಜಮೀನುಗಳಲ್ಲಿ ಲಘು ಪೋಷಕಾಂಶಗಳ ಕೊರತೆ ನೀಗಿಸಲು ಜಿಪ್ಸಂ, ಜಿಂಕ್ ಸಲ್ಫೇಟ್ ಮತ್ತು ಬೋರಾಕ್ಸ್ ಅನ್ನು ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ವಿತರಿಸುವ ಕರ್ನಾಟಕ-ಇಕ್ರಿಸ್ಯಾಟ್ ಸಹಭಾಗಿತ್ವದ ಯೋಜನೆ.",
            "benefits": [
                "50% subsidy on micronutrient packs (Gypsum, Zinc, Borax) distributed via RSKs.",
                "Proven yield enhancement of 20% to 35% in rainfed crops."
            ],
            "benefits_kn": [
                "ಜಿಪ್ಸಂ, ಸತು ಮತ್ತು ಬೋರಾನ್ ಲಘು ಪೋಷಕಾಂಶಗಳಿಗೆ ಶೇ. 50 ರಷ್ಟು ರಿಯಾಯಿತಿ.",
                "ಮಳೆಯಾಶ್ರಿತ ಬೆಳೆಗಳಲ್ಲಿ ಶೇ. 20 ರಿಂದ 35 ರಷ್ಟು ಹೆಚ್ಚುವರಿ ಇಳುವರಿ."
            ],
            "eligibility_rules": [
                make_rule("bc_state", "Must hold dryland/rainfed agricultural land in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಖುಷ್ಕಿ/ಮಳೆಯಾಶ್ರಿತ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Bhoo Chetana Mission Norms", "verified", "Is your farm rainfed or dryland in Karnataka?", "ನಿಮ್ಮ ಜಮೀನು ಕರ್ನಾಟಕದ ಮಳೆಯಾಶ್ರಿತ ಪ್ರದೇಶದಲ್ಲಿದೆಯೇ?", "Focuses on rainfed and semi-arid tracts of Karnataka.", "ಮಳೆಯಾಶ್ರಿತ ಒಣಭೂಮಿ ಪ್ರದೇಶಗಳಿಗೆ ಇದು ಅನ್ವಯಿಸುತ್ತದೆ.")
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
                "Visit RSK before sowing season.",
                "Collect subsidised gypsum / zinc sulphate packet as per plot requirement.",
                "Incorporate into soil during basal land preparation."
            ],
            "application_steps_kn": [
                "ಬಿತ್ತನೆಗೆ ಮುನ್ನ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.",
                "ರಿಯಾಯಿತಿ ದರದ ಜಿಪ್ಸಂ ಮತ್ತು ಜಿಂಕ್ ಪ್ಯಾಕೆಟ್ ಪಡೆದುಕೊಳ್ಳಿ.",
                "ಕೊನೆಯ ಉಳುಮೆ ಸಮಯದಲ್ಲಿ ಮಣ್ಣಿಗೆ ಸೇರಿಸಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "Raitha Samparka Kendra (RSK)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["Rainfed Districts across Karnataka"],
            "supported_crops": ["Ragi, Jowar, Maize, Pulses, Groundnut"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Distributed subject to seasonal laboratory deficiency mapping."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಸ್ಥಳೀಯ ಮಣ್ಣಿನ ಕೊರತೆಯ ಆಧಾರದ ಮೇಲೆ ಪೋಷಕಾಂಶಗಳ ವಿತರಣೆ ನಿರ್ಧಾರವಾಗುತ್ತದೆ."
            ]
        },

        # 19. Organic & Natural Farming Support Scheme
        {
            "id": "ka-organic-natural-farming",
            "name": "Karnataka Organic & Natural Farming Support Scheme (Jaivik Krishi)",
            "name_kn": "ಕರ್ನಾಟಕ ಸಾವಯವ ಮತ್ತು ನೈಸರ್ಗಿಕ ಕೃಷಿ ಪ್ರೋತ್ಸಾಹ ಯೋಜನೆ (ಜೈವಿಕ ಕೃಷಿ)",
            "official_abbreviation": "Jaivik Krishi",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "input_assistance",
            "category_kn": "ಸಾವಯವ ಮತ್ತು ನೈಸರ್ಗಿಕ ಕೃಷಿ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "State scheme promoting chemical-free agriculture through vermicompost pit subsidies, Jeevamrutha preparation units, organic certification, and Jaivik farmer federation brand marketing.",
            "description_kn": "ರಾಸಾಯನಿಕ ಮುಕ್ತ ಕೃಷಿಗೆ ಪ್ರೋತ್ಸಾಹಿಸಲು ಎರೆಹುಳು ಗೊಬ್ಬರ ಘಟಕ, ಜೀವಾಮೃತ ತಯಾರಿ ಘಟಕ, ಸಾವಯವ ಪ್ರಮಾಣೀಕರಣ ಮತ್ತು 'ಜೈವಿಕ ಕೃಷಿ' ಮಾರಾಟ ಒಕ್ಕೂಟಗಳಿಗೆ ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Subsidy up to ₹10,000 for permanent vermicompost units and plastic silpaulin compost beds.",
                "Assistance for native cow maintenance, Jeevamrutha drums, and organic third-party certification."
            ],
            "benefits_kn": [
                "ಶಾಶ್ವತ ಎರೆಹುಳು ತೊಟ್ಟಿ ನಿರ್ಮಾಣಕ್ಕೆ ₹10,000 ವರೆಗೆ ಸಹಾಯಧನ.",
                "ಜೀವಾಮೃತ ತಯಾರಿ ಡ್ರಮ್‌ಗಳು, ದೇಸಿ ಹಸು ನಿರ್ವಹಣೆ ಮತ್ತು ಸಾವಯವ ಪ್ರಮಾಣೀಕರಣಕ್ಕೆ ನೆರವು."
            ],
            "eligibility_rules": [
                make_rule("onf_state", "Must cultivate farmland in Karnataka adopting chemical-free methods.", "ಕರ್ನಾಟಕದಲ್ಲಿ ರಾಸಾಯನಿಕ ಮುಕ್ತ ಕೃಷಿ ಮಾಡುವ ರೈತರಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Organic Farming Policy Karnataka", "verified", "Are you practicing or transitioning to organic farming in Karnataka?", "ನೀವು ಸಾವಯವ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ ಅಥವಾ ಬದಲಾಗಲು ಇಚ್ಛಿಸುತ್ತೀರಾ?", "Promoted through Karnataka State Organic Farming Mission.", "ಕರ್ನಾಟಕ ರಾಜ್ಯ ಸಾವಯವ ಕೃಷಿ ಮಿಷನ್ ಮೂಲಕ ಜಾರಿಯಾಗುತ್ತದೆ.")
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
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Register with local RSK or District Organic Farming Federation.",
                "Join an organic farmer cluster or apply for individual vermicompost unit subsidy.",
                "Officer inspects constructed compost unit and certifies for DBT release."
            ],
            "application_steps_kn": [
                "ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ ಅಥವಾ ಸಾವಯವ ಒಕ್ಕೂಟದಲ್ಲಿ ನೋಂದಾಯಿಸಿ.",
                "ಎರೆಹುಳು ಘಟಕ ನಿರ್ಮಾಣಕ್ಕೆ ಪ್ರಸ್ತಾವನೆ ಸಲ್ಲಿಸಿ.",
                "ಅಧಿಕಾರಿಗಳು ಘಟಕ ಪರಿಶೀಲಿಸಿದ ನಂತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಸಹಾಯಧನ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture / Karnataka Organic Farming Mission",
            "verification_authority": "Assistant Director of Agriculture (Organic Farming)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["All organic agricultural and horticultural crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Preference given to cluster-based adoption."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ರೈತ ಸಂಘಗಳು ಮತ್ತು ಕ್ಲಸ್ಟರ್‌ಗಳಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸುವವರಿಗೆ ಹೆಚ್ಚಿನ ಆದ್ಯತೆ."
            ]
        },

        # 20. Plant Protection & Integrated Pest Management (IPM)
        {
            "id": "ka-plant-protection-ipm",
            "name": "Plant Protection & Integrated Pest Management (IPM) Scheme",
            "name_kn": "ಸಸ್ಯ ಸಂರಕ್ಷಣೆ ಮತ್ತು ಸಮಗ್ರ ಕೀಟ ನಿರ್ವಹಣೆ (IPM) ಯೋಜನೆ",
            "official_abbreviation": "KA Plant Protection",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "input_assistance",
            "category_kn": "ಸಸ್ಯ ಸಂರಕ್ಷಣೆ ಮತ್ತು ಕೀಟ ನಿಯಂತ್ರಣ",
            "assistance_type": "input_assistance",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Subsidised supply of bio-agents, pheromone traps, yellow sticky traps, light traps, and botanical pesticides through RSKs to control pests with minimal chemical load.",
            "description_kn": "ಬೆಳೆಗಳಲ್ಲಿ ರೋಗ ಮತ್ತು ಕೀಟಗಳ ನಿಯಂತ್ರಣಕ್ಕಾಗಿ ಜೈವಿಕ ನಿಯಂತ್ರಕಗಳು, ಮೋಹಕ ಬಲೆಗಳು (Pheromone traps), ಹಳದಿ ಅಂಟು ಬಲೆಗಳು ಮತ್ತು ಜೈವಿಕ ಕೀಟನಾಶಕಗಳನ್ನು ಶೇ. 50 ರಿಯಾಯಿತಿಯಲ್ಲಿ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "50% subsidy on pheromone traps, light traps, and trichogramma bio-cards.",
                "Emergency pest outbreak plant protection chemicals at subsidised rates during pest attacks (e.g., fall armyworm, shoot borer)."
            ],
            "benefits_kn": [
                "ಮೋಹಕ ಬಲೆಗಳು ಮತ್ತು ಜೈವಿಕ ಕೀಟನಾಶಕಗಳಿಗೆ ಶೇ. 50 ರಷ್ಟು ಸಬ್ಸಿಡಿ.",
                "ಹಠಾತ್ ಕೀಟಬಾಧೆ (ಉದಾ: ಲದ್ದಿ ಹುಳು, ಕಾಯಿಕೊರಕ) ಕಾಣಿಸಿಕೊಂಡಾಗ ತುರ್ತು ಔಷಧ ವಿತರಣೆ."
            ],
            "eligibility_rules": [
                make_rule("pp_state", "Must cultivate agricultural land in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Plant Protection Protocol", "verified", "Do you cultivate in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ?", "Supplied through local Karnataka RSKs.", "ಸ್ಥಳೀಯ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಗಳ ಮೂಲಕ ವಿತರಿಸಲಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "Aadhaar card",
                "RTC land record"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಪಹಣಿ (RTC)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Visit RSK upon early pest detection or crop season advisory.",
                "Obtain pheromone/sticky traps or recommended bio-pesticides at subsidised price.",
                "Deploy in field as per technical demonstration."
            ],
            "application_steps_kn": [
                "ಕೀಟಬಾಧೆಯ ಆರಂಭಿಕ ಹಂತದಲ್ಲಿ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.",
                "ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಮೋಹಕ ಬಲೆಗಳು ಅಥವಾ ಜೈವಿಕ ಕೀಟನಾಶಕ ಪಡೆದುಕೊಳ್ಳಿ.",
                "ಕೃಷಿ ಅಧಿಕಾರಿಗಳ ಮಾರ್ಗದರ್ಶನದಂತೆ ಹೊಲದಲ್ಲಿ ಅಳವಡಿಸಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka",
            "verification_authority": "Raitha Samparka Kendra (RSK)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Maize, Cotton, Paddy, Pulses, Vegetables, Coconut"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Stock releases correlate with seasonal pest forecasts."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಕಾಲೋಚಿತ ಕೀಟ ಎಚ್ಚರಿಕೆಗಳಿಗೆ ಅನುಗುಣವಾಗಿ ದಾಸ್ತಾನು ವಿತರಿಸಲಾಗುತ್ತದೆ."
            ]
        },

        # 21. Karnataka Comprehensive Horticulture Development Scheme
        {
            "id": "ka-horticulture-development",
            "name": "Karnataka Comprehensive Horticulture Development Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ಸಮಗ್ರ ತೋಟಗಾರಿಕೆ ಅಭಿವೃದ್ಧಿ ಯೋಜನೆ",
            "official_abbreviation": "KA Horticulture Scheme",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "horticulture_allied",
            "category_kn": "ತೋಟಗಾರಿಕೆ ಅಭಿವೃದ್ಧಿ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Umbrella state horticulture programme providing subsidies for new orchard plantation (mango, pomegranate, guava, citrus), hybrid vegetable seedlings, flower cultivation, and packhouses.",
            "description_kn": "ಮಾವು, ದಾಳಿಂಬೆ, ಪೇರಲ, ಕಿತ್ತಳೆ, ಹೈಬ್ರಿಡ್ ತರಕಾರಿ, ಹೂವುಗಳ ಹೊಸ ತೋಟ ನಿರ್ಮಾಣ ಮತ್ತು ಪ್ಯಾಕ್‌ಹೌಸ್ ಸ್ಥಾಪನೆಗೆ ಶೇ. 40 ರಿಂದ 50 ರಷ್ಟು ಸಹಾಯಧನ ನೀಡುವ ಸಮಗ್ರ ತೋಟಗಾರಿಕೆ ಯೋಜನೆ.",
            "benefits": [
                "40% to 50% subsidy for new fruit orchard establishment spread over 3 years (cost sharing 60:20:20).",
                "Assistance for hybrid vegetable seedlings from departmental nurseries and high-density planting."
            ],
            "benefits_kn": [
                "ಹೊಸ ಹಣ್ಣಿನ ತೋಟಗಳ ಸ್ಥಾಪನೆಗೆ 3 ವರ್ಷಗಳ ಅವಧಿಯಲ್ಲಿ ಶೇ. 40 ರಿಂದ 50 ರಷ್ಟು ಸಹಾಯಧನ.",
                "ಇಲಾಖಾ ನರ್ಸರಿಗಳಿಂದ ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಹೈಬ್ರಿಡ್ ತರಕಾರಿ ಸಸಿಗಳು ಮತ್ತು ಹೂವಿನ ಗಿಡಗಳ ವಿತರಣೆ."
            ],
            "eligibility_rules": [
                make_rule("kh_state", "Farmland must be located in Karnataka.", "ಕೃಷಿ ಜಮೀನು ಕರ್ನಾಟಕದಲ್ಲಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Horticulture Department Manual", "verified", "Is your farm located in Karnataka?", "ನಿಮ್ಮ ಜಮೀನು ಕರ್ನಾಟಕದಲ್ಲಿದೆಯೇ?", "Administered through Karnataka Department of Horticulture.", "ಕರ್ನಾಟಕ ತೋಟಗಾರಿಕೆ ಇಲಾಖೆಯ ಮೂಲಕ ಜಾರಿಯಾಗುತ್ತದೆ."),
                make_rule("kh_water", "Must have assured irrigation facility for perennial orchards.", "ತೋಟಗಾರಿಕೆ ಬೆಳೆಗಳಿಗೆ ನೀರಾವರಿ ಸೌಲಭ್ಯ ಹೊಂದಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, True, "Orchard Plantation Norms", "verified", "Do you have irrigation for horticulture crops?", "ನಿಮ್ಮಲ್ಲಿ ತೋಟಗಾರಿಕೆ ಬೆಳೆಗೆ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿದೆಯೇ?", "Perennial fruit trees require guaranteed water supply for survival.", "ಹಣ್ಣಿನ ತೋಟಗಳ ಉಳಿವಿಗೆ ನೀರಾವರಿ ಸೌಲಭ್ಯ ಅತ್ಯಗತ್ಯ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record",
                "Aadhaar card",
                "Bank passbook",
                "Caste certificate (for SC/ST higher subsidy rate)"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್",
                "ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ (ಹೆಚ್ಚುವರಿ ಸಬ್ಸಿಡಿಗೆ)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Apply online via FRUITS / Karnataka Horticulture portal or visit Senior Assistant Director of Horticulture (SADH).",
                "Officer inspects land and issues planting permission.",
                "Procure genuine planting material from approved nurseries; post-planting audit triggers DBT subsidy in installments."
            ],
            "application_steps_kn": [
                "ಫ್ರೂಟ್ಸ್ ಅಥವಾ ತೋಟಗಾರಿಕಾ ಇಲಾಖೆ ಕಚೇರಿಯಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಅಧಿಕಾರಿಗಳು ಸ್ಥಳ ಪರಿಶೀಲಿಸಿ ನಾಟಿಗೆ ಅನುಮತಿ ನೀಡುತ್ತಾರೆ.",
                "ಅನುಮೋದಿತ ನರ್ಸರಿಯಿಂದ ಗಿಡ ಖರೀದಿಸಿ ನಾಟಿ ಮಾಡಿದ ನಂತರ 3 ಕಂತುಗಳಲ್ಲಿ ಸಬ್ಸಿಡಿ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://horticulturedir.karnataka.gov.in/",
            "issuing_authority": "Department of Horticulture, Government of Karnataka",
            "verification_authority": "Senior Assistant Director of Horticulture (SADH)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Mango, Pomegranate, Banana, Guava, Sapota, Citrus, Vegetables, Flowers"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Subsidy is linked to plant survival rate in subsequent years."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಮುಂದಿನ ವರ್ಷಗಳಲ್ಲಿ ಗಿಡಗಳ ಬದುಕುಳಿಯುವಿಕೆಯ ಆಧಾರದ ಮೇಲೆ ಮುಂದಿನ ಕಂತುಗಳು ಬಿಡುಗಡೆಯಾಗುತ್ತವೆ."
            ]
        },

        # 22. Polyhouse / Greenhouse Subsidy Scheme
        {
            "id": "polyhouse-greenhouse-subsidy",
            "name": "Karnataka Polyhouse & Protected Cultivation Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ಪಾಲಿಹೌಸ್ ಮತ್ತು ಸಂರಕ್ಷಿತ ಬೇಸಾಯ ಯೋಜನೆ",
            "official_abbreviation": "KA Polyhouse Scheme",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "horticulture_allied",
            "category_kn": "ಸಂರಕ್ಷಿತ ಬೇಸಾಯ ಮತ್ತು ಪಾಲಿಹೌಸ್",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Subsidy of 50% for General farmers and up to 75% for SC/ST farmers for construction of Naturally Ventilated Polyhouses (NVPH) up to 4,000 sq. metres for commercial flowers and exotic vegetables.",
            "description_kn": "ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಹೂವುಗಳು ಮತ್ತು ತರಕಾರಿಗಳ ವಾಣಿಜ್ಯ ಬೇಸಾಯಕ್ಕಾಗಿ ಸ್ವಾಭಾವಿಕ ಗಾಳಿಯಾಡುವ ಪಾಲಿಹೌಸ್ (NVPH) ನಿರ್ಮಾಣಕ್ಕೆ ಶೇ. 50 ರಿಂದ 75 ರಷ್ಟು ಬೃಹತ್ ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "50% subsidy on standard cost (approx ₹4.5 lakh to ₹5.5 lakh per 1,000 sq.m) for General category; up to 75% for SC/ST.",
                "Covers GI tubular structure, 200-micron UV-stabilized polythene sheet, insect net, and micro-irrigation."
            ],
            "benefits_kn": [
                "ಪಾಲಿಹೌಸ್ ನಿರ್ಮಾಣಕ್ಕೆ ಸಾಮಾನ್ಯ ರೈತರಿಗೆ ಶೇ. 50 ಮತ್ತು ಎಸ್‌ಸಿ/ಎಸ್‌ಟಿ ರೈತರಿಗೆ ಶೇ. 75 ರಷ್ಟು ಸಬ್ಸಿಡಿ.",
                "ಜಿಐ ಪೈಪ್ ರಚನೆ, 200 ಮೈಕ್ರಾನ್ ಯುವಿ ಶೀಟ್, ಕೀಟ ನಿರೋಧಕ ನೆಟ್ ಮತ್ತು ಹನಿ ನೀರಾವರಿ ಒಳಗೊಂಡಿದೆ."
            ],
            "eligibility_rules": [
                make_rule("ph_state", "Land must be located in Karnataka.", "ಜಮೀನು ಕರ್ನಾಟಕ ರಾಜ್ಯದಲ್ಲಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Protected Cultivation Manual", "verified", "Is your land located in Karnataka?", "ನಿಮ್ಮ ಜಮೀನು ಕರ್ನಾಟಕದಲ್ಲಿದೆಯೇ?", "Scheme funded under MIDH and Karnataka state mission.", "ತೋಟಗಾರಿಕಾ ಇಲಾಖೆಯ ಮೂಲಕ ಈ ನೆರವು ನೀಡಲಾಗುತ್ತದೆ."),
                make_rule("ph_water", "Must possess round-the-year assured good-quality water source (EC < 1.0).", "ಉತ್ತಮ ಗುಣಮಟ್ಟದ ವರ್ಷಪೂರ್ತಿ ನೀರಿನ ಸೌಲಭ್ಯ ಹೊಂದಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, True, "Polyhouse Technical Feasibility", "verified", "Do you have an assured borewell or water source?", "ನಿಮ್ಮಲ್ಲಿ ವರ್ಷಪೂರ್ತಿ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿದೆಯೇ?", "Protected cultivation requires continuous drip fertigation and humidity management.", "ಪಾಲಿಹೌಸ್ ಬೇಸಾಯಕ್ಕೆ ನಿರಂತರ ನೀರು ಮತ್ತು ರಸಾವರಿ ಸೌಲಭ್ಯ ಅನಿವಾರ್ಯ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record",
                "Water and soil test report",
                "Aadhaar card",
                "Bank loan sanction letter (if bank-financed)",
                "Approved vendor technical design drawing"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಪಹಣಿ (RTC)",
                "ನೀರು ಮತ್ತು ಮಣ್ಣು ಪರೀಕ್ಷಾ ವರದಿ",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬ್ಯಾಂಕ್ ಸಾಲ ಮಂಜೂರಾತಿ ಪತ್ರ",
                "ಅನುಮೋದಿತ ಕಂಪನಿಯ ವಿನ್ಯಾಸ ನಕ್ಷೆ ಮತ್ತು ಕೊಟೇಶನ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Submit application to Senior Assistant Director of Horticulture (SADH).",
                "Technical committee verifies water quality and soil suitability.",
                "Administrative sanction issued; construction by empanelled polyhouse agency.",
                "Departmental inspection and GPS video recording before subsidy release to loan/bank account."
            ],
            "application_steps_kn": [
                "ಹಿರಿಯ ಸಹಾಯಕ ತೋಟಗಾರಿಕೆ ನಿರ್ದೇಶಕರ (SADH) ಕಚೇರಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ತಾಂತ್ರಿಕ ಸಮಿತಿ ನೀರು ಮತ್ತು ಮಣ್ಣು ಪರಿಶೀಲಿಸಿ ಮಂಜೂರಾತಿ ನೀಡುತ್ತದೆ.",
                "ಅಧಿಕೃತ ಕಂಪನಿಯ ಮೂಲಕ ಪಾಲಿಹೌಸ್ ನಿರ್ಮಾಣ ಪೂರ್ಣಗೊಳಿಸಿ.",
                "ಅಧಿಕಾರಿಗಳ ಜಂಟಿ ಪರಿಶೀಲನೆಯ ನಂತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಸಹಾಯಧನ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://horticulturedir.karnataka.gov.in/",
            "issuing_authority": "Department of Horticulture, Government of Karnataka",
            "verification_authority": "Senior Assistant Director of Horticulture (SADH) / JDH",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Roses, Gerbera, Carnation, Capsicum (Color bell pepper), European Cucumber, Tomatoes"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Requires prior administrative approval before commencing fabrication."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಕಾಮಗಾರಿ ಪ್ರಾರಂಭಿಸುವ ಮುನ್ನ ಇಲಾಖೆಯಿಂದ ಪೂರ್ವಾನುಮತಿ ಪಡೆಯುವುದು ಕಡ್ಡಾಯ."
            ]
        },

        # 23. Shade-Net House Construction Subsidy Scheme
        {
            "id": "shadenet-house-subsidy",
            "name": "Karnataka Shade-Net House Construction Subsidy Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ಶೇಡ್‌ನೆಟ್ ಹೌಸ್ ನಿರ್ಮಾಣ ಸಹಾಯಧನ ಯೋಜನೆ",
            "official_abbreviation": "Shade-Net Scheme",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "horticulture_allied",
            "category_kn": "ಶೇಡ್‌ನೆಟ್ ಮತ್ತು ನರ್ಸರಿ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Financial assistance of 50% for construction of shade-net houses up to 4,000 sq. metres for commercial vegetable seedling production, nurseries, and leafy greens.",
            "description_kn": "ತರಕಾರಿ ಸಸಿಗಳ ಉತ್ಪಾದನೆ, ಹೈಟೆಕ್ ನರ್ಸರಿ ಮತ್ತು ತರಕಾರಿ ಕೃಷಿಗಾಗಿ ಶೇಡ್‌ನೆಟ್ ಹೌಸ್ ನಿರ್ಮಾಣಕ್ಕೆ ಶೇ. 50 ರಷ್ಟು ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "50% capital subsidy on prescribed cost norms for tubular shade-net structures.",
                "Protection against excessive solar radiation, scorching heat, and hail damage."
            ],
            "benefits_kn": [
                "ಶೇಡ್‌ನೆಟ್ ಹೌಸ್ ನಿರ್ಮಾಣಕ್ಕೆ ಶೇ. 50 ರಷ್ಟು ಬಂಡವಾಳ ಸಹಾಯಧನ.",
                "ಬಿಸಿಲಿನ ತಾಪ ಮತ್ತು ಆಲಿಕಲ್ಲು ಮಳೆಯಿಂದ ತರಕಾರಿ ಸಸಿಗಳ ಸಂರಕ್ಷಣೆ."
            ],
            "eligibility_rules": [
                make_rule("snh_state", "Must possess farmland in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Shade Net Norms", "verified", "Do you own farmland in Karnataka?", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಜಮೀನಿದೆಯೇ?", "Implemented via Karnataka Horticulture Department.", "ಕರ್ನಾಟಕ ತೋಟಗಾರಿಕೆ ಇಲಾಖೆಯ ಮೂಲಕ ಅನುಷ್ಠಾನ."),
                make_rule("snh_water", "Must have functional irrigation source.", "ಕಾರ್ಯನಿರ್ವಹಿಸುವ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, True, "Nursery Feasibility", "verified", "Do you have an irrigation water source?", "ನಿಮ್ಮಲ್ಲಿ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿದೆಯೇ?", "Shade-net cultivation relies on micro-sprinklers and foggers.", "ಶೇಡ್‌ನೆಟ್ ಬೇಸಾಯಕ್ಕೆ ಮೈಕ್ರೋ ಸ್ಪ್ರಿಂಕ್ಲರ್ ಅಥವಾ ನೀರಾವರಿ ಅಗತ್ಯ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record",
                "Aadhaar card",
                "Bank passbook",
                "Vendor design and estimate"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್",
                "ಕೊಟೇಶನ್ ಮತ್ತು ವಿನ್ಯಾಸ ನಕ್ಷೆ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Submit application to local Taluk Horticulture Office.",
                "Site verification by Horticulture Officer.",
                "Erection of shade-net by approved agency; inspection and subsidy release."
            ],
            "application_steps_kn": [
                "ತಾಲೂಕು ತೋಟಗಾರಿಕೆ ಕಚೇರಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಅಧಿಕಾರಿಗಳಿಂದ ಸ್ಥಳ ಪರಿಶೀಲನೆ.",
                "ಶೇಡ್‌ನೆಟ್ ನಿರ್ಮಾಣದ ನಂತರ ಜಂಟಿ ಪರಿಶೀಲನೆ ನಡೆಸಿ ಸಬ್ಸಿಡಿ ಬಿಡುಗಡೆ."
            ],
            "official_source_url": "https://horticulturedir.karnataka.gov.in/",
            "issuing_authority": "Department of Horticulture, Government of Karnataka",
            "verification_authority": "Senior Assistant Director of Horticulture (SADH)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Vegetable seedlings, Betelvine, Flowers, Medicinal plants, Leafy greens"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Subject to annual district physical targets."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಜಿಲ್ಲಾವಾರು ವಾರ್ಷಿಕ ಗುರಿಗಳಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತದೆ."
            ]
        },

        # 24. Fruit Orchard Rejuvenation and Canopy Management Scheme
        {
            "id": "fruit-orchard-rejuvenation",
            "name": "Fruit Orchard Rejuvenation and Canopy Management Scheme",
            "name_kn": "ಹಣ್ಣಿನ ತೋಟಗಳ ಪುನಶ್ಚೇತನ ಮತ್ತು ಮೇಲ್ಚಾವಣಿ ನಿರ್ವಹಣಾ ಯೋಜನೆ",
            "official_abbreviation": "Orchard Rejuvenation",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "horticulture_allied",
            "category_kn": "ತೋಟಗಾರಿಕೆ ಮರುಜೀವ ಮತ್ತು ನಿರ್ವಹಣೆ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "Financial assistance up to ₹20,000 per hectare for scientific pruning, top working, and rejuvenation of old, senile, and unproductive mango, guava, and citrus orchards.",
            "description_kn": "ಇಳುವರಿ ಕಡಿಮೆಯಾಗಿರುವ ಹಳೆಯ ಮಾವು, ಪೇರಲ ಮತ್ತು ಸಿಟ್ರಸ್ ತೋಟಗಳನ್ನು ಕತ್ತರಿಸಿ ಸವರಿ, ಪುನಶ್ಚೇತನಗೊಳಿಸಲು ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ ₹20,000 ವರೆಗೆ ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Financial subsidy of 50% up to ₹20,000/ha for pruning, canopy management, and plant health inputs.",
                "Restores fruit size, sunlight penetration, and yield in 20+ year old orchards without uprooting."
            ],
            "benefits_kn": [
                "ಕವಲು ಸವರುವಿಕೆ ಮತ್ತು ಪೋಷಕಾಂಶ ನಿರ್ವಹಣೆಗೆ ಹೆಕ್ಟೇರ್‌ಗೆ ₹20,000 ವರೆಗೆ ಸಹಾಯಧನ.",
                "ಹಳೆಯ ತೋಟಗಳನ್ನು ಕಡಿಯದೆ ಮರುಜೀವ ನೀಡಿ ಇಳುವರಿ ಮತ್ತು ಹಣ್ಣಿನ ಗುಣಮಟ್ಟ ಹೆಚ್ಚಳ."
            ],
            "eligibility_rules": [
                make_rule("or_state", "Must own existing fruit orchard in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಹಳೆಯ ಹಣ್ಣಿನ ತೋಟ ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Rejuvenation Guidelines", "verified", "Do you own an established fruit orchard in Karnataka?", "ನಿಮ್ಮಲ್ಲಿ ಹಳೆಯ ಹಣ್ಣಿನ ತೋಟವಿದೆಯೇ?", "Applicable strictly to existing established orchards in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿರುವ ಹಳೆಯ ಹಣ್ಣಿನ ತೋಟಗಳಿಗೆ ಮಾತ್ರ ಅನ್ವಯಿಸುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record showing established orchard trees",
                "Aadhaar card",
                "Bank passbook"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಹಣ್ಣಿನ ಗಿಡಗಳು ನಮೂದಾದ ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Contact local SADH office before monsoon pruning season.",
                "Field inspection by Horticulture Officer to assess tree condition and canopy density.",
                "Execute pruning under technical guidance; post-pruning audit unlocks DBT reimbursement."
            ],
            "application_steps_kn": [
                "ಸ್ಥಳೀಯ ತೋಟಗಾರಿಕೆ ಕಚೇರಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಅಧಿಕಾರಿಗಳು ಬಂದು ಮರಗಳ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸುತ್ತಾರೆ.",
                "ತಾಂತ್ರಿಕ ಸಲಹೆಯಂತೆ ಸವರಿಕೆ ಕಾರ್ಯ ಮುಗಿಸಿದ ನಂತರ ಸಬ್ಸಿಡಿ ಬಿಡುಗಡೆ."
            ],
            "official_source_url": "https://horticulturedir.karnataka.gov.in/",
            "issuing_authority": "Department of Horticulture, Government of Karnataka",
            "verification_authority": "Senior Assistant Director of Horticulture (SADH)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Fruit Growing Districts of Karnataka"],
            "supported_crops": ["Mango, Guava, Pomegranate, Citrus, Sapota"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Trees must be at least 15 to 20 years old to qualify."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಸಾಮಾನ್ಯವಾಗಿ 15-20 ವರ್ಷ ಮೇಲ್ಪಟ್ಟ ಹಳೆಯ ತೋಟಗಳಿಗೆ ಮಾತ್ರ ಲಭ್ಯ."
            ]
        },

        # 25. Milk Producer Incentive Scheme (Ksheera Dhaare)
        {
            "id": "ksheera-dhaare",
            "name": "Karnataka Special Incentive Scheme for Milk Producers (Ksheera Dhaare)",
            "name_kn": "ಕ್ಷೀರಧಾರೆ – ಹಾಲು ಉತ್ಪಾದಕರಿಗೆ ವಿಶೇಷ ಪ್ರೋತ್ಸಾಹಧನ ಯೋಜನೆ (₹5/ಲೀಟರ್)",
            "official_abbreviation": "Ksheera Dhaare",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "income_support",
            "category_kn": "ಹೈನುಗಾರಿಕೆ ಮತ್ತು ಆದಾಯ ಪ್ರೋತ್ಸಾಹ",
            "assistance_type": "direct_financial_assistance",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Direct cash incentive of ₹5 per litre poured by dairy farmers to registered Village Milk Producers Cooperative Societies (MPCS) affiliated with KMF (Nandini).",
            "description_kn": "ಕೆಎಂಎಫ್ (ನಂದಿನಿ) ಒಕ್ಕೂಟದ ಹಾಲು ಉತ್ಪಾದಕರ ಸಹಕಾರ ಸಂಘಗಳಿಗೆ (MPCS) ಹಾಲು ಪೂರೈಸುವ ರೈತರಿಗೆ ಪ್ರತಿ ಲೀಟರ್ ಹಾಲಿಗೆ ₹5 ನೇರ ಪ್ರೋತ್ಸಾಹಧನ ನೀಡುವ ರಾಜ್ಯ ಸರ್ಕಾರದ ಪ್ರಮುಖ ಯೋಜನೆ.",
            "benefits": [
                "Direct Benefit Transfer (DBT) of ₹5 per litre of milk directly into the farmer's bank account.",
                "Reliable supplementary income supporting rural dairy livelihoods."
            ],
            "benefits_kn": [
                "ಪೂರೈಸಿದ ಪ್ರತಿ ಲೀಟರ್ ಹಾಲಿಗೆ ₹5 ರಂತೆ ನೇರವಾಗಿ ರೈತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆ.",
                "ಹೈನುಗಾರಿಕೆಯನ್ನು ಲಾಭದಾಯಕವಾಗಿಸಲು ನಿರಂತರ ಮಾಸಿಕ ಆರ್ಥಿಕ ಬೆಂಬಲ."
            ],
            "eligibility_rules": [
                make_rule("kd_state", "Must be a dairy farmer resident in Karnataka pouring milk to a recognized MPCS.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಹೈನುಗಾರಿಕೆ ಮಾಡಿ ಹಾಲು ಸಂಘಕ್ಕೆ ಹಾಲು ಪೂರೈಸುತ್ತಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "KMF Ksheera Dhaare Rules", "verified", "Do you pour milk to a Karnataka dairy cooperative (KMF / Nandini)?", "ನೀವು ಹಾಲು ಉತ್ಪಾದಕರ ಸಹಕಾರ ಸಂಘಕ್ಕೆ ಹಾಲು ಹಾಕುತ್ತಿದ್ದೀರಾ?", "Administered through KMF District Milk Unions and Animal Husbandry Dept.", "ಕೆಎಂಎಫ್ ಮತ್ತು ಪಶುಸಂಗೋಪನಾ ಇಲಾಖೆಯ ಮೂಲಕ ಈ ಹಣ ಪಾವತಿಯಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "Village Milk Producers Cooperative Society (MPCS) Passbook / Member Number",
                "Aadhaar card",
                "Aadhaar-seeded bank account details"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಹಾಲು ಉತ್ಪಾದಕರ ಸಹಕಾರ ಸಂಘದ (MPCS) ಸದಸ್ಯತ್ವ / ಖಾತೆ ಸಂಖ್ಯೆ",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಆಧಾರ್ ಲಿಂಕ್ ಆದ ಬ್ಯಾಂಕ್ ಖಾತೆ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Enrol as a member of local Village Milk Producers Cooperative Society (MPCS).",
                "Link Aadhaar and bank details with the dairy society testing system.",
                "Incentive is calculated automatically based on monthly computerized milk passbook records and credited via DBT."
            ],
            "application_steps_kn": [
                "ಗ್ರಾಮದ ಹಾಲು ಉತ್ಪಾದಕರ ಸಹಕಾರ ಸಂಘದಲ್ಲಿ ಸದಸ್ಯತ್ವ ಪಡೆಯಿರಿ.",
                "ಹಾಲು ಸಂಘದಲ್ಲಿ ಆಧಾರ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಖಾತೆಯನ್ನು ನೋಂದಾಯಿಸಿ.",
                "ಪ್ರತಿ ತಿಂಗಳು ಪೂರೈಸಿದ ಹಾಲಿನ ಲೆಕ್ಕದಂತೆ ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಹಣ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://ahvs.karnataka.gov.in/",
            "issuing_authority": "Department of Animal Husbandry and Veterinary Services / KMF",
            "verification_authority": "District Milk Producers Cooperative Union / Local MPCS Secretary",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Cow milk, Buffalo milk, Dairy farming"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Milk quality must meet minimum FAT and SNF standards established by KMF."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಹಾಲು ಕೆಎಂಎಫ್ ನಿಗದಿಪಡಿಸಿದ ಕನಿಷ್ಠ ಕೊಬ್ಬು (FAT) ಮತ್ತು ಎಸ್‌ಎನ್‌ಎಫ್ (SNF) ಗುಣಮಟ್ಟ ಹೊಂದಿರಬೇಕು."
            ]
        },

        # 26. Pashu Bhagya Scheme
        {
            "id": "pashu-bhagya",
            "name": "Karnataka Pashu Bhagya Scheme (Livestock Assistance)",
            "name_kn": "ಕರ್ನಾಟಕ ಪಶು ಭಾಗ್ಯ ಯೋಜನೆ (ಜಾನುವಾರು ನೆರವು)",
            "official_abbreviation": "Pashu Bhagya",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "horticulture_allied",
            "category_kn": "ಪಶುಸಂಗೋಪನೆ ಮತ್ತು ಜಾನುವಾರು",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "Comprehensive livestock scheme providing subsidies and soft loans for establishing cattle units (cows/buffaloes), sheep/goat units, piggery, and poultry farms.",
            "description_kn": "ಹಸು, ಎಮ್ಮೆ, ಕುರಿ, ಮೇಕೆ, ಹಂದಿ ಮತ್ತು ಕೋಳಿ ಸಾಕಾಣಿಕೆ ಘಟಕಗಳನ್ನು ಸ್ಥಾಪಿಸಲು ಶೇ. 25 ರಿಂದ 33 ರಷ್ಟು (ಎಸ್‌ಸಿ/ಎಸ್‌ಟಿ ಗಳಿಗೆ ಶೇ. 50 ರವರೆಗೆ) ಸಹಾಯಧನ ನೀಡುವ ಜನಪ್ರಿಯ ಯೋಜನೆ.",
            "benefits": [
                "Subsidy up to 50% for SC/ST and up to 25%-33% for General category on bank-linked dairy and livestock rearing units.",
                "Includes fodder plot establishment and animal insurance subsidy."
            ],
            "benefits_kn": [
                "ಹೈನುಗಾರಿಕೆ ಮತ್ತು ಕುರಿ/ಮೇಕೆ ಘಟಕಗಳಿಗೆ ಎಸ್‌ಸಿ/ಎಸ್‌ಟಿ ಗಳಿಗೆ ಶೇ. 50 ಮತ್ತು ಸಾಮಾನ್ಯರಿಗೆ ಶೇ. 25-33 ರಷ್ಟು ಸಬ್ಸಿಡಿ.",
                "ಮೇವು ಬೆಳೆಸಲು ಮತ್ತು ಜಾನುವಾರು ವಿಮೆಗೆ ಹೆಚ್ಚುವರಿ ಸಹಾಯಧನ."
            ],
            "eligibility_rules": [
                make_rule("pb_state", "Must be a resident small/marginal farmer or agricultural labourer in Karnataka.", "ಕರ್ನಾಟಕದ ಸಣ್ಣ/ಅತಿ ಸಣ್ಣ ರೈತರು ಅಥವಾ ಕೃಷಿ ಕಾರ್ಮಿಕರಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Pashu Bhagya Guidelines", "verified", "Are you a resident small farmer or farm worker in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ವಾಸಿಸುವ ಸಣ್ಣ ರೈತರು ಅಥವಾ ಕೃಷಿ ಕೂಲಿಕಾರರೇ?", "Aimed at livelihood enhancement for rural households in Karnataka.", "ಗ್ರಾಮೀಣ ಕೃಷಿಕರ ಹೆಚ್ಚುವರಿ ಆದಾಯಕ್ಕಾಗಿ ರೂಪಿಸಲಾದ ಯೋಜನೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "Aadhaar card",
                "Caste and Income certificate",
                "Bank passbook",
                "Land record (RTC) or proof of shed space"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್",
                "ಪಹಣಿ (RTC) ಅಥವಾ ಕೊಟ್ಟಿಗೆ ಜಾಗದ ದಾಖಲೆ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Apply online via Seva Sindhu or visit local Veterinary Hospital / Taluk Assistant Director (AHVS).",
                "Select preferred livestock unit (Dairy, Sheep/Goat, Poultry).",
                "District committee sanctions bank loan tie-up and releases back-ended subsidy."
            ],
            "application_steps_kn": [
                "ಸೇವಾ ಸಿಂಧು ಅಥವಾ ಸ್ಥಳೀಯ ಪಶು ಆಸ್ಪತ್ರೆಗೆ ಭೇಟಿ ನೀಡಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ನಿಮಗೆ ಬೇಕಾದ ಜಾನುವಾರು ಘಟಕವನ್ನು (ಹಸು, ಕುರಿ/ಮೇಕೆ, ಕೋಳಿ) ಆಯ್ಕೆಮಾಡಿ.",
                "ಸಮಿತಿ ಅನುಮೋದನೆಯ ನಂತರ ಬ್ಯಾಂಕ್ ಸಾಲ ಮತ್ತು ಸಬ್ಸಿಡಿ ಮಂಜೂರಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://ahvs.karnataka.gov.in/",
            "issuing_authority": "Department of Animal Husbandry and Veterinary Services, Karnataka",
            "verification_authority": "Assistant Director (AH&VS) / Veterinary Officer",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Dairy cows, Buffaloes, Sheep, Goat, Piggery, Poultry"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Animal purchase is executed through official cattle purchase melas in presence of veterinary doctor."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಪಶುವೈದ್ಯರ ಸಮ್ಮುಖದಲ್ಲಿ ಜಾನುವಾರು ಸಂತೆಗಳಲ್ಲಿ ಖರೀದಿ ಮಾಡಬೇಕು."
            ]
        },

        # 27. Mobile Veterinary Clinics & Tele-Medicine Services (1962 Call Centre)
        {
            "id": "mobile-veterinary-1962",
            "name": "Karnataka Mobile Veterinary Clinics & 1962 Toll-Free Ambulance",
            "name_kn": "ಕರ್ನಾಟಕ ಸಂಚಾರಿ ಪಶು ಚಿಕಿತ್ಸಾಲಯ ಮತ್ತು 1962 ಟೋಲ್-ಫ್ರೀ ಆಂಬ್ಯುಲೆನ್ಸ್ ಸೇವೆ",
            "official_abbreviation": "1962 Agri-Vet",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "training_advisory",
            "category_kn": "ಪಶು ಆರೋಗ್ಯ ಮತ್ತು ತುರ್ತು ಚಿಕಿತ್ಸೆ",
            "assistance_type": "training_advisory",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "24x7 doorstep emergency animal treatment, artificial insemination, and tele-consultation service accessed via toll-free number 1962.",
            "description_kn": "ರೈತರ ಮನೆಬಾಗಿಲಿಗೆ ಬಂದು ಜಾನುವಾರುಗಳಿಗೆ ಉಚಿತ ತುರ್ತು ಚಿಕಿತ್ಸೆ, ಕೃತಕ ಗರ್ಭಧಾರಣೆ ಮತ್ತು ಸಲಹೆ ನೀಡುವ 24x7 ಸಂಚಾರಿ ಪಶು ಆಂಬ್ಯುಲೆನ್ಸ್ (ಟೋಲ್-ಫ್ರೀ: 1962) ಸೇವೆ.",
            "benefits": [
                "Free doorstep veterinary treatment, emergency animal surgery, vaccination, and deworming.",
                "Custom-equipped ambulance with veterinary doctor, para-vet, diagnostic kit, and medicines."
            ],
            "benefits_kn": [
                "ಮನೆಬಾಗಿಲಿಗೆ ಬಂದು ಉಚಿತ ಜಾನುವಾರು ಚಿಕಿತ್ಸೆ, ಶಸ್ತ್ರಚಿಕಿತ್ಸೆ, ಲಸಿಕೆ ಮತ್ತು ಜಂತುನಾಶಕ ವಿತರಣೆ.",
                "ವೈದ್ಯರು ಮತ್ತು ಅಗತ್ಯ ಔಷಧಿಗಳನ್ನೊಳಗೊಂಡ ಸುಸಜ್ಜಿತ ಸಂಚಾರಿ ಪಶು ಆಂಬ್ಯುಲೆನ್ಸ್."
            ],
            "eligibility_rules": [
                make_rule("mv_state", "Must own domestic cattle or livestock in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಜಾನುವಾರು ಸಾಕಾಣಿಕೆ ಮಾಡುತ್ತಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "1962 Operational Protocol", "verified", "Do you own livestock in Karnataka?", "ನಿಮ್ಮಲ್ಲಿ ಜಾನುವಾರುಗಳಿವೆಯೇ?", "Service is operational across all 31 districts of Karnataka.", "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಈ ಆಂಬ್ಯುಲೆನ್ಸ್ ಸೇವೆ ಲಭ್ಯವಿದೆ.")
            ],
            "required_documents": [
                "Livestock ear tag number (Bharat Pashudhan)",
                "Aadhaar card of owner"
            ],
            "required_documents_kn": [
                "ಜಾನುವಾರಿನ ಕಿವಿಯ ಟ್ಯಾಗ್ ಸಂಖ್ಯೆ (ಭಾರತ್ ಪಶುಧನ್)",
                "ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Dial toll-free helpline 1962 from any mobile phone.",
                "Provide village location, owner name, and livestock symptoms.",
                "Nearest mobile veterinary ambulance is dispatched to farmer's shed."
            ],
            "application_steps_kn": [
                "ಯಾವುದೇ ಮೊಬೈಲ್‌ನಿಂದ ಉಚಿತ ಸಹಾಯವಾಣಿ 1962 ಕ್ಕೆ ಕರೆ ಮಾಡಿ.",
                "ನಿಮ್ಮ ಊರು ಮತ್ತು ಜಾನುವಾರಿನ ಸಮಸ್ಯೆಯನ್ನು ತಿಳಿಸಿ.",
                "ಹತ್ತಿರದ ಸಂಚಾರಿ ಪಶು ಆಂಬ್ಯುಲೆನ್ಸ್ ನಿಮ್ಮ ಕೊಟ್ಟಿಗೆಯ ಬಳಿಗೆ ಬರುತ್ತದೆ."
            ],
            "official_source_url": "https://ahvs.karnataka.gov.in/",
            "issuing_authority": "Department of Animal Husbandry and Veterinary Services, Karnataka",
            "verification_authority": "1962 Central Command & Control Centre",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All 31 Districts of Karnataka"],
            "supported_crops": ["Cows, Buffaloes, Sheep, Goats, Horses, Livestock"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Emergency doorstep visits are free of consultation fee."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಮನೆಬಾಗಿಲಿಗೆ ಬರುವ ಈ ತುರ್ತು ಪಶುವೈದ್ಯಕೀಯ ಸೇವೆ ಉಚಿತವಾಗಿರುತ್ತದೆ."
            ]
        },

        # 28. Fodder Development Scheme
        {
            "id": "ka-fodder-development",
            "name": "Karnataka Fodder Development Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ಮೇವು ಅಭಿವೃದ್ಧಿ ಯೋಜನೆ",
            "official_abbreviation": "Fodder Scheme",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "input_assistance",
            "category_kn": "ಹಸಿರು ಮೇವು ಮತ್ತು ಸಿಲೇಜ್",
            "assistance_type": "input_assistance",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Distribution of certified high-yielding perennial fodder root slips (CoFS-29, Super Napier) and minikits at 75% subsidy, plus assistance for silage pit units and chaff cutters.",
            "description_kn": "ಬೇಸಿಗೆಯಲ್ಲಿ ಮೇವಿನ ಕೊರತೆ ನೀಗಿಸಲು ಸುಪರ್ ನೇಪಿಯರ್, ಸಿಒಎಫ್‌ಎಸ್ ಮುಂತಾದ ಮೇವಿನ ಕಡ್ಡಿಗಳು/ಬೀಜಗಳನ್ನು ಶೇ. 75 ರಿಯಾಯಿತಿಯಲ್ಲಿ ನೀಡುವ ಮತ್ತು ಮೇವು ಕತ್ತರಿಸುವ ಯಂತ್ರಗಳಿಗೆ (ಚಾಫ್ ಕಟ್ಟರ್) ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "75% subsidy on perennial fodder slips and seeds minikits.",
                "Up to 50% subsidy on mechanized chaff cutters to prevent fodder wastage."
            ],
            "benefits_kn": [
                "ಉತ್ತಮ ತಳಿಯ ಮೇವಿನ ಕಡ್ಡಿಗಳು ಮತ್ತು ಬೀಜಗಳಿಗೆ ಶೇ. 75 ರಷ್ಟು ಸಬ್ಸಿಡಿ.",
                "ಮೇವು ವ್ಯರ್ಥವಾಗುವುದನ್ನು ತಡೆಯಲು ಮೇವು ಕತ್ತರಿಸುವ ಯಂತ್ರಗಳಿಗೆ (ಚಾಫ್ ಕಟ್ಟರ್) ಶೇ. 50 ಸಹಾಯಧನ."
            ],
            "eligibility_rules": [
                make_rule("fd_state", "Must own cattle and cultivable land in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಜಾನುವಾರು ಮತ್ತು ಜಮೀನು ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Fodder Development Norms", "verified", "Do you own cattle and land in Karnataka?", "ನಿಮ್ಮಲ್ಲಿ ಜಾನುವಾರು ಮತ್ತು ಕೃಷಿ ಜಮೀನಿದೆಯೇ?", "Distributed through veterinary dispensaries and RSKs.", "ಸ್ಥಳೀಯ ಪಶು ಆಸ್ಪತ್ರೆಗಳ ಮೂಲಕ ವಿತರಿಸಲಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record",
                "Aadhaar card",
                "Cattle ownership proof / Milk pouring receipt"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಜಾನುವಾರು ದಾಖಲೆ / ಹಾಲು ಹಾಕಿದ ರಸೀದಿ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Visit local Veterinary Hospital or RSK before monsoon.",
                "Request fodder minikit or chaff cutter subsidy.",
                "Receive slips/seeds on payment of subsidized farmer share."
            ],
            "application_steps_kn": [
                "ಮುಂಗಾರಿಗೆ ಮುನ್ನ ಸ್ಥಳೀಯ ಪಶು ಆಸ್ಪತ್ರೆಗೆ ಭೇಟಿ ನೀಡಿ.",
                "ಮೇವಿನ ಕಿಟ್ ಅಥವಾ ಚಾಫ್ ಕಟ್ಟರ್‌ಗಾಗಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ರಿಯಾಯಿತಿ ದರ ಪಾವತಿಸಿ ಮೇವಿನ ಕಡ್ಡಿಗಳನ್ನು ಪಡೆದುಕೊಳ್ಳಿ."
            ],
            "official_source_url": "https://ahvs.karnataka.gov.in/",
            "issuing_authority": "Department of Animal Husbandry and Veterinary Services, Karnataka",
            "verification_authority": "Veterinary Officer / Assistant Director (AHVS)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Super Napier, CoFS-29, Lucerne, Fodder Maize, Sorghum"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Priority in drought-declared taluks."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಬರಪೀಡಿತ ತಾಲೂಕುಗಳಿಗೆ ವಿಶೇಷ ಆದ್ಯತೆ ನೀಡಲಾಗುತ್ತದೆ."
            ]
        },

        # 29. Inland & Marine Fisheries Development Scheme
        {
            "id": "ka-fisheries-development",
            "name": "Karnataka Inland & Marine Fisheries Development Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ಒಳನಾಡು ಮತ್ತು ಕರಾವಳಿ ಮೀನುಗಾರಿಕೆ ಅಭಿವೃದ್ಧಿ ಯೋಜನೆ",
            "official_abbreviation": "KA Fisheries",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "horticulture_allied",
            "category_kn": "ಮೀನುಗಾರಿಕೆ ಮತ್ತು ಜಲಚರ ಸಾಕಾಣಿಕೆ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Application availability to be verified",
            "status_label_kn": "ಅರ್ಜಿ ಲಭ್ಯತೆ ಪರಿಶೀಲಿಸಬೇಕು",
            "description": "Subsidies for farm pond fish culture, fish fingerlings stocking, aerators, insulated ice boxes, and mechanized boat engines for inland and coastal fishermen.",
            "description_kn": "ಕೃಷಿ ಹೊಂಡಗಳಲ್ಲಿ ಮೀನು ಸಾಕಾಣಿಕೆ, ಮೀನು ಮರಿಗಳ ವಿತರಣೆ, ಏರೇಟರ್, ಐಸ್ ಬಾಕ್ಸ್ ಮತ್ತು ಬೋಟ್ ಇಂಜಿನ್‌ಗಳಿಗೆ ಶೇ. 40 ರಿಂದ 60 ರಷ್ಟು ಸಹಾಯಧನ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "40% to 60% subsidy for construction of new freshwater aquaculture ponds and fingerling inputs.",
                "Subsidised motorized two-wheelers with ice boxes for fresh fish vendors."
            ],
            "benefits_kn": [
                "ಕೃಷಿ ಹೊಂಡ ಅಥವಾ ಮೀನು ಕೊಳ ನಿರ್ಮಾಣ ಮತ್ತು ಮೀನು ಮರಿ ಖರೀದಿಗೆ ಶೇ. 40 ರಿಂದ 60 ಸಬ್ಸಿಡಿ.",
                "ಮೀನು ಮಾರಾಟಗಾರರಿಗೆ ಐಸ್ ಬಾಕ್ಸ್ ಸಹಿತ ದ್ವಿಚಕ್ರ ವಾಹನ ಖರೀದಿಗೆ ಸಹಾಯಧನ."
            ],
            "eligibility_rules": [
                make_rule("fsh_state", "Must possess farm pond / water body in Karnataka or be a traditional fisherman.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಜಲಮೂಲ/ಕೃಷಿ ಹೊಂಡ ಹೊಂದಿರಬೇಕು ಅಥವಾ ಮೀನುಗಾರರಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "KA Fisheries Policy", "verified", "Do you have an aquaculture pond or practice fishing in Karnataka?", "ನಿಮ್ಮಲ್ಲಿ ಮೀನು ಸಾಕಾಣಿಕೆ ಹೊಂಡವಿದೆಯೇ ಅಥವಾ ನೀವು ಮೀನುಗಾರರೇ?", "Managed by Karnataka Fisheries Department.", "ಕರ್ನಾಟಕ ಮೀನುಗಾರಿಕಾ ಇಲಾಖೆಯ ಮೂಲಕ ಜಾರಿಯಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID or Fishermen Registration Card",
                "RTC showing farm pond / water body",
                "Aadhaar card",
                "Bank passbook"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID) ಅಥವಾ ಮೀನುಗಾರರ ಗುರುತಿನ ಚೀಟಿ",
                "ಕೃಷಿ ಹೊಂಡವಿರುವ ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Apply at Taluk Assistant Director of Fisheries office.",
                "Department inspects water body and supplies certified fingerlings (Catla, Rohu, Grass carp).",
                "Subsidy credited upon stocking verification."
            ],
            "application_steps_kn": [
                "ತಾಲೂಕು ಸಹಾಯಕ ಮೀನುಗಾರಿಕೆ ನಿರ್ದೇಶಕರ ಕಚೇರಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಅಧಿಕಾರಿಗಳು ಸ್ಥಳ ಪರಿಶೀಲಿಸಿ ಪ್ರಮಾಣಿತ ಮೀನು ಮರಿಗಳನ್ನು ವಿತರಿಸುತ್ತಾರೆ.",
                "ಪರಿಶೀಲನೆಯ ನಂತರ ಖಾತೆಗೆ ಸಹಾಯಧನ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://fisheries.karnataka.gov.in/",
            "issuing_authority": "Department of Fisheries, Government of Karnataka",
            "verification_authority": "Assistant Director of Fisheries (ADF)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Inland & Coastal Districts of Karnataka"],
            "supported_crops": ["Catla, Rohu, Mrigal, Tilapia, Prawns, Marine fish"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Fingerlings released during monsoon reservoir filling."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಮುಂಗಾರು ಹಂಗಾಮಿನಲ್ಲಿ ಜಲಾಶಯ ಮತ್ತು ಹೊಂಡಗಳಿಗೆ ಮೀನು ಮರಿ ಬಿಡಲಾಗುತ್ತದೆ."
            ]
        },

        # 30. Sericulture Development Scheme
        {
            "id": "ka-sericulture-development",
            "name": "Karnataka Sericulture Development Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ರೇಷ್ಮೆ ಕೃಷಿ ಅಭಿವೃದ್ಧಿ ಯೋಜನೆ",
            "official_abbreviation": "KA Sericulture",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "horticulture_allied",
            "category_kn": "ರೇಷ್ಮೆ ಕೃಷಿ ಮತ್ತು ಹಿಪ್ಪುನೇರಳೆ",
            "assistance_type": "subsidy_cost_sharing",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Financial assistance for new mulberry plantation (V-1 variety), drip irrigation for mulberry gardens, silkworm rearing house construction, and cocoon production incentives.",
            "description_kn": "ಹಿಪ್ಪುನೇರಳೆ (ವಿ-1 ತಳಿ) ತೋಟ ನಿರ್ಮಾಣ, ಹಿಪ್ಪುನೇರಳೆ ತೋಟಕ್ಕೆ ಹನಿ ನೀರಾವರಿ, ರೇಷ್ಮೆ ಹುಳು ಸಾಕಾಣಿಕೆ ಮನೆ (Rearing Shed) ನಿರ್ಮಾಣ ಮತ್ತು ಗೂಡು ಉತ್ಪಾದನೆಗೆ ಭಾರಿ ಸಬ್ಸಿಡಿ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Subsidy up to ₹1.5 lakh to ₹2.75 lakh for silkworm rearing shed construction depending on category.",
                "Subsidy for high-yielding V-1 mulberry saplings, rearing equipment (chawki trays, shoot rearing racks), and ₹10 to ₹30/kg cocoon incentive."
            ],
            "benefits_kn": [
                "ರೇಷ್ಮೆ ಸಾಕಾಣಿಕೆ ಮನೆ ನಿರ್ಮಾಣಕ್ಕೆ ₹1.5 ಲಕ್ಷದಿಂದ ₹2.75 ಲಕ್ಷದವರೆಗೆ ಬೃಹತ್ ಸಹಾಯಧನ.",
                "ಹಿಪ್ಪುನೇರಳೆ ಸಸಿಗಳು, ಸಾಕಾಣಿಕೆ ಉಪಕರಣಗಳು ಮತ್ತು ರೇಷ್ಮೆ ಗೂಡಿಗೆ ಪ್ರತಿ ಕೆಜಿಗೆ ಹೆಚ್ಚುವರಿ ಪ್ರೋತ್ಸಾಹಧನ."
            ],
            "eligibility_rules": [
                make_rule("ser_state", "Must possess cultivable land in Karnataka suitable for mulberry cultivation.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಹಿಪ್ಪುನೇರಳೆ ಕೃಷಿಗೆ ಯೋಗ್ಯವಾದ ಜಮೀನು ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Sericulture Policy Guidelines", "verified", "Do you cultivate or plan to plant mulberry in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಹಿಪ್ಪುನೇರಳೆ ಬೆಳೆಯುತ್ತಿದ್ದೀರಾ?", "Karnataka is India's leading silk producing state; schemes operate via Sericulture Dept.", "ಕರ್ನಾಟಕ ರೇಷ್ಮೆ ಇಲಾಖೆಯ ಮೂಲಕ ಈ ನೆರವು ನೀಡಲಾಗುತ್ತದೆ."),
                make_rule("ser_water", "Must possess irrigation for perennial mulberry plot (minimum 0.5 to 1 acre).", "ಹಿಪ್ಪುನೇರಳೆ ತೋಟಕ್ಕೆ ನೀರಾವರಿ ಸೌಲಭ್ಯ ಹೊಂದಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, True, "Mulberry Agronomy Norms", "verified", "Do you have an active irrigation facility?", "ನಿಮ್ಮಲ್ಲಿ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿದೆಯೇ?", "Mulberry leaf production requires regular irrigation for high silk cocoon quality.", "ಗುಣಮಟ್ಟದ ರೇಷ್ಮೆ ಗೂಡು ಉತ್ಪಾದನೆಗೆ ಹಿಪ್ಪುನೇರಳೆ ತೋಟಕ್ಕೆ ನೀರಾವರಿ ಅಗತ್ಯ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record",
                "Aadhaar card",
                "Caste certificate (for higher SC/ST subsidy)",
                "Bank passbook",
                "Approved rearing shed structural estimate"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಜಾತಿ ಪ್ರಮಾಣ ಪತ್ರ (ಹೆಚ್ಚಿನ ಸಬ್ಸಿಡಿಗೆ)",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್",
                "ರೇಷ್ಮೆ ಮನೆ ನಿರ್ಮಾಣದ ಅಂದಾಜು ಪಟ್ಟಿ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Apply at nearest Taluk Sericulture Extension Officer (SEO) or Assistant Director of Sericulture (ADS).",
                "Officer verifies land and water; issues planting approval for V-1 mulberry.",
                "Submit building plan for rearing shed; subsidy released in 2-3 stages based on physical foundation/roof verification."
            ],
            "application_steps_kn": [
                "ತಾಲೂಕು ರೇಷ್ಮೆ ವಿಸ್ತರಣಾಧಿಕಾರಿ (SEO) ಅಥವಾ ಸಹಾಯಕ ನಿರ್ದೇಶಕರ ಕಚೇರಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಅಧಿಕಾರಿಗಳು ಸ್ಥಳ ಪರಿಶೀಲಿಸಿ ಹಿಪ್ಪುನೇರಳೆ ನಾಟಿಗೆ ಅನುಮೋದನೆ ನೀಡುತ್ತಾರೆ.",
                "ರೇಷ್ಮೆ ಮನೆ ನಿರ್ಮಾಣದ ಹಂತಗಳ (ಫೌಂಡೇಶನ್, ರೂಫ್) ಪರಿಶೀಲನೆಯ ನಂತರ ಹಂತ-ಹಂತವಾಗಿ ಸಬ್ಸಿಡಿ ಬಿಡುಗಡೆ."
            ],
            "official_source_url": "https://sericulture.karnataka.gov.in/",
            "issuing_authority": "Department of Sericulture, Government of Karnataka",
            "verification_authority": "Assistant Director of Sericulture (ADS)",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Traditional & Non-Traditional Sericulture Districts of Karnataka"],
            "supported_crops": ["Mulberry, Bivoltine silkworm cocoons, CB silkworm cocoons"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Rearing shed dimensions must strictly adhere to departmental blueprint."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ರೇಷ್ಮೆ ಮನೆಯು ಇಲಾಖೆಯ ಅಧಿಕೃತ ನಕ್ಷೆಗೆ ಅನುಗುಣವಾಗಿರಬೇಕು."
            ]
        },

        # 31. Zero-Interest Short-Term Crop Loan Scheme
        {
            "id": "zero-interest-crop-loans",
            "name": "Karnataka Zero-Interest Short-Term Crop Loan Scheme (Cooperative Banks)",
            "name_kn": "ಕರ್ನಾಟಕ ಶೂನ್ಯ ಬಡ್ಡಿ ದರದ ಅಲ್ಪಾವಧಿ ಬೆಳೆ ಸಾಲ ಯೋಜನೆ (ಸಹಕಾರ ಬ್ಯಾಂಕ್‌ಗಳು)",
            "official_abbreviation": "Zero-Interest Crop Loan",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "agricultural_credit",
            "category_kn": "ಕೃಷಿ ಸಾಲ ಮತ್ತು ಬಡ್ಡಿ ಸಹಾಯಧನ",
            "assistance_type": "agricultural_credit",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Short-term seasonal agricultural production credit up to ₹5 lakh provided at 0% interest rate to farmers through Primary Agricultural Credit Cooperative Societies (PACS / DCC Banks).",
            "description_kn": "ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರ ಸಂಘಗಳು (PACS) ಮತ್ತು ಡಿಸಿಸಿ ಬ್ಯಾಂಕ್‌ಗಳ ಮೂಲಕ ರೈತರಿಗೆ ₹5 ಲಕ್ಷದವರೆಗೆ ಸಂಪೂರ್ಣ ಶೂನ್ಯ ಬಡ್ಡಿ (0% Interest) ದರದಲ್ಲಿ ಅಲ್ಪಾವಧಿ ಬೆಳೆ ಸಾಲ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "100% interest subvention up to ₹5,00,000 for short-term seasonal crop loans.",
                "Zero interest cost if repaid promptly within statutory 12-month due date."
            ],
            "benefits_kn": [
                "₹5,00,000 ವರೆಗಿನ ಅಲ್ಪಾವಧಿ ಬೆಳೆ ಸಾಲಕ್ಕೆ ಸಂಪೂರ್ಣ 0% ಬಡ್ಡಿ ದರ.",
                "12 ತಿಂಗಳ ನಿಗದಿತ ಅವಧಿಯೊಳಗೆ ಮರುಪಾವತಿಸಿದರೆ ಯಾವುದೇ ಬಡ್ಡಿ ಇರುವುದಿಲ್ಲ (ಸರ್ಕಾರವೇ ಬಡ್ಡಿ ಭರಿಸುತ್ತದೆ)."
            ],
            "eligibility_rules": [
                make_rule("zl_state", "Must be a cultivating farmer with land in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರುವ ರೈತರಾಗಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Cooperation Department Govt Orders", "verified", "Do you cultivate farmland in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಮಾಡುತ್ತಿದ್ದೀರಾ?", "Administered through Karnataka Cooperative Credit structure.", "ಕರ್ನಾಟಕ ಸಹಕಾರ ಸಂಘಗಳು ಮತ್ತು ಡಿಸಿಸಿ ಬ್ಯಾಂಕ್‌ಗಳ ಮೂಲಕ ಜಾರಿಯಾಗುತ್ತದೆ."),
                make_rule("zl_land", "Must possess valid land record (RTC) for crop loan limit fixation.", "ಬೆಳೆ ಸಾಲದ ಮಿತಿ ನಿಗದಿಗೆ ಪಹಣಿ (RTC) ಹೊಂದಿರಬೇಕು.", "land_area.value_acres", "greater_than", 0, True, "Scale of Finance Norms", "verified", "Do you hold RTC records?", "ನಿಮ್ಮ ಬಳಿ ಚಾಲ್ತಿ ಪಹಣಿ ಇದೆಯೇ?", "Loan limit is determined by the district Scale of Finance multiplied by crop acreage.", "ಜಿಲ್ಲಾ ಸಾಲದ ಪ್ರಮಾಣ (Scale of Finance) ಮತ್ತು ಬೆಳೆ ವಿಸ್ತೀರ್ಣದ ಆಧಾರದಲ್ಲಿ ಸಾಲ ನಿಗದಿಯಾಗುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land records (Current year Pahani)",
                "Aadhaar card",
                "Membership passbook of Primary Agricultural Credit Society (PACS)",
                "No-dues certificate from commercial bank in same jurisdiction"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಚಾಲ್ತಿ ಸಾಲಿನ ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರ ಸಂಘದ (PACS) ಸದಸ್ಯತ್ವ ಪುಸ್ತಕ",
                "ಬ್ಯಾಂಕ್ ಬಾಕಿ ಇಲ್ಲದಿರುವ ಪ್ರಮಾಣ ಪತ್ರ (No-dues)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Enrol as a member of local Village Primary Agricultural Credit Cooperative Society (PACS).",
                "Submit RTC, FID, and crop cultivation declaration before sowing season.",
                "Managing committee sanctions loan limit as per district Scale of Finance; amount disbursed directly to savings account."
            ],
            "application_steps_kn": [
                "ಸ್ಥಳೀಯ ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರ ಸಂಘದಲ್ಲಿ (PACS / ಸೊಸೈಟಿ) ಸದಸ್ಯರಾಗಿ.",
                "ಪಹಣಿ, ಎಫ್‌ಐಡಿ ಮತ್ತು ಬಿತ್ತನೆ ಬೆಳೆಯ ವಿವರ ಸಲ್ಲಿಸಿ.",
                "ಸೊಸೈಟಿಯ ಸಮಿತಿ ಸಾಲ ಮಂಜೂರು ಮಾಡಿ ನಿಮ್ಮ ಖಾತೆಗೆ ಹಣ ವರ್ಗಾವಣೆ ಮಾಡುತ್ತದೆ."
            ],
            "official_source_url": "https://cooperation.karnataka.gov.in/",
            "issuing_authority": "Department of Cooperation, Government of Karnataka / DCC Banks",
            "verification_authority": "Primary Agricultural Credit Society (PACS) Secretary & DCC Bank Inspector",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All 31 Districts of Karnataka"],
            "supported_crops": ["All seasonal agricultural and horticultural crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Zero interest benefit is contingent upon prompt repayment within 1 year; default attracts regular commercial interest rates."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "1 ವರ್ಷದೊಳಗೆ ಮರುಪಾವತಿಸಿದರೆ ಮಾತ್ರ 0% ಬಡ್ಡಿ ಅನ್ವಯಿಸುತ್ತದೆ; ತಪ್ಪಿದರೆ ಸಾಮಾನ್ಯ ಬಡ್ಡಿ ವಿಧಿಸಲಾಗುತ್ತದೆ."
            ]
        },

        # 32. Concessional Medium-Term & Long-Term Agricultural Loans
        {
            "id": "concessional-mt-lt-loans",
            "name": "Karnataka Concessional Medium & Long-Term Agricultural Loans (3% Interest)",
            "name_kn": "ಕರ್ನಾಟಕ ರಿಯಾಯಿತಿ ದರದ ಮಧ್ಯಮಾವಧಿ ಮತ್ತು ದೀರ್ಘಾವಧಿ ಕೃಷಿ ಸಾಲ (3% ಬಡ್ಡಿ)",
            "official_abbreviation": "3% Term Loan",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "agricultural_credit",
            "category_kn": "ದೀರ್ಘಾವಧಿ ಕೃಷಿ ಬಂಡವಾಳ ಸಾಲ",
            "assistance_type": "agricultural_credit",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Medium-term and long-term agricultural development loans up to ₹15 lakh at a highly subsidized interest rate of 3% per annum for tractors, dairy units, and polyhouses through DCC and PCARD banks.",
            "description_kn": "ಟ್ರ್ಯಾಕ್ಟರ್, ಹೈನುಗಾರಿಕೆ, ತೋಟ ನಿರ್ಮಾಣ ಮತ್ತು ಪಾಲಿಹೌಸ್ ಸ್ಥಾಪನೆಗೆ ಡಿಸಿಸಿ ಮತ್ತು ಪಿಕಾರ್ಡ್ (PCARD) ಬ್ಯಾಂಕ್‌ಗಳ ಮೂಲಕ ₹15 ಲಕ್ಷದವರೆಗೆ ಕೇವಲ 3% ರಿಯಾಯಿತಿ ಬಡ್ಡಿದರದಲ್ಲಿ ದೀರ್ಘಾವಧಿ ಕೃಷಿ ಸಾಲ ನೀಡುವ ಯೋಜನೆ.",
            "benefits": [
                "Concessional 3% interest rate on term loans up to ₹15,00,000 (government subsidises balance interest).",
                "Repayment tenure of 3 to 7 years with moratorium period for perennial orchard gestation."
            ],
            "benefits_kn": [
                "₹15 ಲಕ್ಷದವರೆಗಿನ ದೀರ್ಘಾವಧಿ ಸಾಲಕ್ಕೆ ಕೇವಲ 3% ಬಡ್ಡಿದರ (ಉಳಿದ ಬಡ್ಡಿಯನ್ನು ಸರ್ಕಾರವೇ ಭರಿಸುತ್ತದೆ).",
                "3 ರಿಂದ 7 ವರ್ಷಗಳ ಸುಲಭ ಮರುಪಾವತಿ ಅವಧಿ."
            ],
            "eligibility_rules": [
                make_rule("ctl_state", "Must own agricultural land in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Term Loan Guidelines", "verified", "Do you own agricultural land in Karnataka?", "ಕರ್ನಾಟಕದಲ್ಲಿ ಕೃಷಿ ಜಮೀನಿದೆಯೇ?", "Channelled through Karnataka State Cooperative Agriculture and Rural Development Bank (KSCARD) and DCC banks.", "ಪಿಕಾರ್ಡ್ ಮತ್ತು ಡಿಸಿಸಿ ಬ್ಯಾಂಕ್‌ಗಳ ಮೂಲಕ ಜಾರಿಯಾಗುತ್ತದೆ."),
                make_rule("ctl_land", "Must possess sufficient unencumbered land for mortgage security.", "ಅಡಮಾನ ಭದ್ರತೆಗೆ ಸಾಲಕ್ಕೆ ತಕ್ಕಂತೆ ಜಮೀನು ಹೊಂದಿರಬೇಕು.", "ownership", "in", ["owned", "joint_owned"], True, "Cooperative Lending Rules", "verified", "Is the land clear of encumbrances for mortgage?", "ಜಮೀನಿನ ಮೇಲೆ ಯಾವುದೇ ಇತರೆ ಸಾಲದ ಹೊರೆ ಇಲ್ಲವೇ?", "Medium and long-term loans require registered mortgage charge (Gehan) on land.", "ದೀರ್ಘಾವಧಿ ಸಾಲಕ್ಕೆ ಜಮೀನಿನ ಮೇಲೆ 'ಗೇಹಾನ್' (ಗೆಹಾನ್ ನೋಂದಣಿ) ಮಾಡುವುದು ಕಡ್ಡಾಯ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "Complete RTC extract (30 years search report / Nil Encumbrance Certificate)",
                "Mutation extract and title deeds",
                "Aadhaar card",
                "Quotation/estimate of asset to be created (Tractor, shed, dairy animals)"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "30 ವರ್ಷಗಳ ಇಸಿ (Encumbrance Certificate) ಮತ್ತು ಪಹಣಿ",
                "ಮ್ಯುಟೇಶನ್ ಪ್ರತಿ ಮತ್ತು ಕ್ರಯಪತ್ರ",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಖರೀದಿಸುವ ಯಂತ್ರ ಅಥವಾ ನಿರ್ಮಿಸುವ ಘಟಕದ ಕೊಟೇಶನ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Apply at local Taluk PCARD Bank or District Central Cooperative (DCC) Bank branch.",
                "Bank legal advisor inspects title records and registers simple mortgage (Gehan).",
                "Loan sanctioned at 3% interest; disbursement made directly to machine dealer or civil contractor."
            ],
            "application_steps_kn": [
                "ತಾಲೂಕು ಪಿಕಾರ್ಡ್ ಬ್ಯಾಂಕ್ (PCARD) ಅಥವಾ ಡಿಸಿಸಿ ಬ್ಯಾಂಕ್ ಶಾಖೆಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
                "ಕಾನೂನು ಸಲಹೆಗಾರರು ದಾಖಲೆ ಪರಿಶೀಲಿಸಿ ಸರಳ ಅಡಮಾನ (ಗೇಹಾನ್) ಮಾಡಿಸುತ್ತಾರೆ.",
                "3% ಬಡ್ಡಿದರದಲ್ಲಿ ಸಾಲ ಮಂಜೂರಾಗಿ ಯಂತ್ರೋಪಕರಣ ಡೀಲರ್‌ಗೆ ಹಣ ಪಾವತಿಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://cooperation.karnataka.gov.in/",
            "issuing_authority": "Department of Cooperation, Government of Karnataka / KSCARD Bank",
            "verification_authority": "PCARD Bank Manager & Legal Scrutiny Committee",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka"],
            "supported_crops": ["Tractors, Farm Equipment, Dairy Units, Horticulture Orchards, Polyhouses"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Interest subvention applies only when annual repayment installments are remitted within the scheduled due date."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ವಾರ್ಷಿಕ ಕಂತುಗಳನ್ನು ಸರಿಯಾದ ಸಮಯಕ್ಕೆ ಪಾವತಿಸಿದಾಗ ಮಾತ್ರ 3% ಬಡ್ಡಿದರದ ರಿಯಾಯಿತಿ ಅನ್ವಯಿಸುತ್ತದೆ."
            ]
        },

        # 33. Karnataka Raitha Suraksha Pradhan Mantri Fasal Bima Yojana
        {
            "id": "ka-raitha-suraksha-pmfby",
            "name": "Karnataka Raitha Suraksha Pradhan Mantri Fasal Bima Yojana (State PMFBY)",
            "name_kn": "ಕರ್ನಾಟಕ ರೈತ ಸುರಕ್ಷಾ ಪ್ರಧಾನ ಮಂತ್ರಿ ಫಸಲ್ ಬಿಮಾ ಯೋಜನೆ (ರಾಜ್ಯ ಸಂಯೋಜಿತ ಬೆಳೆ ವಿಮೆ)",
            "official_abbreviation": "KA-PMFBY",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "crop_insurance",
            "category_kn": "ಬೆಳೆ ವಿಮೆ ಮತ್ತು ನಷ್ಟ ಪರಿಹಾರ",
            "assistance_type": "crop_insurance",
            "status_label": "Current status verified",
            "status_label_kn": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
            "description": "Karnataka comprehensive crop insurance scheme combining central PMFBY with state-specific coverage (Kalyana Karnataka / Samrakshane portal) providing risk cover against drought, flood, pests, and localized calamities at nominal farmer premium (1.5% to 2%).",
            "description_kn": "ಕರ್ನಾಟಕದ 'ಸಂರಕ್ಷಣೆ' (Samrakshane) ಪೋರ್ಟಲ್ ಮೂಲಕ ಜಾರಿಯಾಗುವ ಸಮಗ್ರ ಬೆಳೆ ವಿಮೆ ಯೋಜನೆ. ಕೇವಲ 1.5% ರಿಂದ 2% ಅಲ್ಪ ಪ್ರೀಮಿಯಂ ದರದಲ್ಲಿ ಬರ, ಪ್ರವಾಹ ಮತ್ತು ಬೆಳೆ ನಷ್ಟಕ್ಕೆ ಪೂರ್ಣ ವಿಮಾ ರಕ್ಷಣೆ ಒದಗಿಸುತ್ತದೆ.",
            "benefits": [
                "Comprehensive risk insurance from prevented sowing, mid-season adversity, to post-harvest losses.",
                "Farmer premium only 2% for Kharif crops, 1.5% for Rabi/Summer crops, and 5% for annual commercial/horticulture crops; remainder subsidized equally by State and Central Governments.",
                "Direct electronic settlement of claims into farmer accounts via Samrakshane portal without delays."
            ],
            "benefits_kn": [
                "ಬಿತ್ತನೆ ವಿಫಲತೆ, ಹಂಗಾಮಿನ ಬರ, ರೋಗ-ಕೀಟಬಾಧೆ ಮತ್ತು ಕೊಯ್ಲೋತ್ತರ ಬೆಳೆ ನಷ್ಟಕ್ಕೆ ಸಮಗ್ರ ಪರಿಹಾರ.",
                "ರೈತರು ಪಾವತಿಸಬೇಕಾದ ಪ್ರೀಮಿಯಂ: ಮುಂಗಾರು ಬೆಳೆಗೆ ಕೇವಲ 2%, ಹಿಂಗಾರು ಬೆಳೆಗೆ 1.5% ಮತ್ತು ವಾಣಿಜ್ಯ/ತೋಟಗಾರಿಕೆ ಬೆಳೆಗೆ 5% ಮಾತ್ರ.",
                "'ಸಂರಕ್ಷಣೆ' ಪೋರ್ಟಲ್ ಮೂಲಕ ನೇರವಾಗಿ ರೈತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಪರಿಹಾರ ಜಮೆ."
            ],
            "eligibility_rules": [
                make_rule("kpm_state", "Must cultivate notified crops in notified insurance hoblis/gram panchayats in Karnataka.", "ಕರ್ನಾಟಕದ ಅಧಿಸೂಚಿತ ವಿಮಾ ಘಟಕದಲ್ಲಿ ಅಧಿಸೂಚಿತ ಬೆಳೆ ಬೆಳೆದಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Samrakshane Insurance Notification", "verified", "Are you cultivating a notified crop in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಸೂಚಿತ ವಿಮಾ ಬೆಳೆ ಬೆಳೆಯುತ್ತಿದ್ದೀರಾ?", "Insurance coverage is notified crop-wise and hobli/gram panchayat-wise each season.", "ಪ್ರತಿ ಹಂಗಾಮಿನಲ್ಲಿ ಹೋಬಳಿ ಮತ್ತು ಗ್ರಾಮ ಪಂಚಾಯ್ತಿವಾರು ಬೆಳೆಗಳನ್ನು ಅಧಿಸೂಚಿಸಲಾಗುತ್ತದೆ."),
                make_rule("kpm_crops", "Must cultivate notified crops (Paddy, Ragi, Maize, Red gram, Cotton, Groundnut, Sugarcane, Onion, etc.).", "ಅಧಿಸೂಚಿತ ಬೆಳೆಗಳನ್ನು ಬೆಳೆದಿರಬೇಕು.", "crops", "any_of", ["paddy", "ragi", "maize", "jowar", "red_gram", "bengal_gram", "cotton", "groundnut", "soybean", "sugarcane", "onion", "chilli", "potato", "sunflower"], True, "Karnataka Seasonal Crop Insurance Gazette", "verified", "Which specific crops are you cultivating this season?", "ಈ ಹಂಗಾಮಿನಲ್ಲಿ ನೀವು ಯಾವ ಬೆಳೆಗಳನ್ನು ಬೆಳೆದಿದ್ದೀರಿ?", "Coverage is legally valid only for notified crops in that specific defined insurance unit.", "ಅಧಿಸೂಚಿತ ಪ್ರದೇಶದಲ್ಲಿ ಅಧಿಸೂಚಿತ ಬೆಳೆಗಳಿಗೆ ಮಾತ್ರ ವಿಮೆ ಅನ್ವಯಿಸುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC / Pahani (Current year)",
                "Crop Sowing Certificate / Crop Survey acknowledgement (Beley Darshak)",
                "Aadhaar card",
                "Bank passbook copy with IFSC"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಚಾಲ್ತಿ ಸಾಲಿನ ಪಹಣಿ (RTC)",
                "ಬೆಳೆ ದೃಢೀಕರಣ ಪತ್ರ / ಬೆಳೆ ಸಮೀಕ್ಷೆ ದಾಖಲೆ",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": ["Tenancy certificate (for tenant farmers)"],
            "optional_documents_kn": ["ಗೇಣಿ ದೃಢೀಕರಣ ಪತ್ರ (ಗೇಣಿ ರೈತರಿಗೆ)"],
            "application_steps": [
                "Check cut-off dates on Samrakshane portal (samrakshane.karnataka.gov.in) before sowing deadline.",
                "Visit nearest Grama One centre, Common Service Centre (CSC), or bank branch.",
                "Provide FID and survey number; pay nominal farmer premium and collect system-generated acknowledgement receipt.",
                "Crop-cutting experiments (CCEs) by Department of Agriculture evaluate threshold yield and trigger automatic compensation."
            ],
            "application_steps_kn": [
                "ಸಂರಕ್ಷಣೆ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ (samrakshane.karnataka.gov.in) ಅರ್ಜಿ ಸಲ್ಲಿಕೆಯ ಕೊನೆಯ ದಿನಾಂಕ ಗಮನಿಸಿ.",
                "ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರ, ಸಿಎಸ್‌ಸಿ ಕೇಂದ್ರ ಅಥವಾ ಬ್ಯಾಂಕ್ ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ.",
                "ಎಫ್‌ಐಡಿ ನೀಡಿ ಅಲ್ಪ ಪ್ರೀಮಿಯಂ ಮೊತ್ತ ಪಾವತಿಸಿ ಕಂಪ್ಯೂಟರ್ ರಸೀದಿ ಪಡೆದುಕೊಳ್ಳಿ.",
                "ಬೆಳೆ ಕಟಾವು ಪ್ರಯೋಗಗಳ (CCE) ನಂತರ ನಷ್ಟ ಸಂಭವಿಸಿದಲ್ಲಿ ನೇರವಾಗಿ ಪರಿಹಾರ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://samrakshane.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Government of Karnataka / Empanelled Insurance Companies",
            "verification_authority": "Director of Agriculture & Directorate of Economics and Statistics",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Districts of Karnataka (Notified Insurance Units)"],
            "supported_crops": ["Paddy, Ragi, Maize, Jowar, Red gram, Green gram, Black gram, Bengal gram, Groundnut, Soybean, Sunflower, Cotton, Sugarcane, Onion, Potato, Chilli"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Cut-off dates for premium payment are strictly non-extendable by local officers."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ವಿಮೆ ಕಂತು ಪಾವತಿಸಲು ನಿಗದಿಪಡಿಸಿದ ಕೊನೆಯ ದಿನಾಂಕವನ್ನು ಯಾವುದೇ ಕಾರಣಕ್ಕೂ ವಿಸ್ತರಿಸಲಾಗುವುದಿಲ್ಲ."
            ]
        },

        # 34. Minimum Support Price (MSP) & Market Intervention Scheme
        {
            "id": "ka-msp-procurement",
            "name": "Karnataka Minimum Support Price (MSP) & Market Intervention Procurement Scheme",
            "name_kn": "ಕರ್ನಾಟಕ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ (MSP) ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಮಧ್ಯಪ್ರವೇಶ ಖರೀದಿ ಯೋಜನೆ",
            "official_abbreviation": "MSP Procurement",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "procurement_price_support",
            "category_kn": "ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ ಮತ್ತು ಬೆಲೆ ರಕ್ಷಣೆ",
            "assistance_type": "procurement_price_support",
            "status_label": "Seasonal application",
            "status_label_kn": "ಋತುಮಾನ ಆಧಾರಿತ ಅರ್ಜಿ",
            "description": "Government procurement of notified food grains and commercial commodities (Ragi, Jowar, Paddy, Copra, Bengal gram) at official Minimum Support Price (MSP) plus state bonus to protect farmers during distress market crashes.",
            "description_kn": "ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ದರ ಕುಸಿದಾಗ ರೈತರನ್ನು ರಕ್ಷಿಸಲು ಸರ್ಕಾರವೇ ಬೆಂಬಲ ಬೆಲೆಯಲ್ಲಿ (MSP) ಮತ್ತು ಹೆಚ್ಚುವರಿ ರಾಜ್ಯ ಪ್ರೋತ್ಸಾಹಧನದಲ್ಲಿ ರಾಗಿ, ಜೋಳ, ಭತ್ತ, ಕೊಬ್ಬರಿ, ತೊಗರಿ ಮತ್ತು ಕಡಲೆ ಖರೀದಿಸುವ ಯೋಜನೆ.",
            "benefits": [
                "Guaranteed statutory purchase price directly credited to bank account via DBT within 7 to 15 days.",
                "State bonus top-up on selected staples (e.g., Ragi and White Jowar procurement under Public Distribution System).",
                "Shields farmers from predatory trader cartels and distress selling."
            ],
            "benefits_kn": [
                "ಮಾರುಕಟ್ಟೆ ಕುಸಿತದ ಸಂದರ್ಭದಲ್ಲಿ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ ಖಾತರಿ ಮತ್ತು 15 ದಿನಗಳಲ್ಲಿ ನೇರ ಬ್ಯಾಂಕ್ ಜಮೆ.",
                "ಸಾರ್ವಜನಿಕ ವಿತರಣಾ ವ್ಯವಸ್ಥೆಗಾಗಿ (ಅನ್ನಭಾಗ್ಯ) ರಾಗಿ ಮತ್ತು ಬಿಳಿಜೋಳಕ್ಕೆ ವಿಶೇಷ ರಾಜ್ಯ ಬೋನಸ್.",
                "ಮಧ್ಯವರ್ತಿಗಳ ಹಾವಳಿಯಿಂದ ರೈತರಿಗೆ ಸಂಪೂರ್ಣ ರಕ್ಷಣೆ."
            ],
            "eligibility_rules": [
                make_rule("msp_state", "Must cultivate and harvest notified crops in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಸೂಚಿತ ಬೆಳೆ ಬೆಳೆದು ಕಟಾವು ಮಾಡಿರಬೇಕು.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Procurement Guidelines Karnataka", "verified", "Did you harvest a notified procurement crop in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಸೂಚಿತ ಬೆಳೆ ಕಟಾವು ಮಾಡಿದ್ದೀರಾ?", "Procurement centers are set up in APMC yards and primary cooperative societies across Karnataka.", "ಕರ್ನಾಟಕದ ಎಪಿಎಂಸಿ ಮತ್ತು ಸಹಕಾರ ಸಂಘಗಳ ಖರೀದಿ ಕೇಂದ್ರಗಳಲ್ಲಿ ಮಾತ್ರ ಖರೀದಿ ನಡೆಯುತ್ತದೆ."),
                make_rule("msp_crops", "Must produce notified crops (Ragi, Jowar, Paddy, Copra, Pulses).", "ಅಧಿಸೂಚಿತ ಬೆಳೆಗಳನ್ನು (ರಾಗಿ, ಜೋಳ, ಭತ್ತ, ಕೊಬ್ಬರಿ, ತೊಗರಿ ಇತ್ಯಾದಿ) ಉತ್ಪಾದಿಸಿರಬೇಕು.", "crops", "any_of", ["ragi", "jowar", "paddy", "copra", "coconut", "red_gram", "bengal_gram", "green_gram", "black_gram"], True, "Government Order for Seasonal Procurement", "verified", "What crop are you bringing to the procurement centre?", "ನೀವು ಯಾವ ಬೆಳೆಯನ್ನು ಖರೀದಿ ಕೇಂದ್ರಕ್ಕೆ ತರುತ್ತಿದ್ದೀರಿ?", "Procurement applies only to commodities officially notified by the government during market intervention.", "ಸರ್ಕಾರ ಅಧಿಕೃತವಾಗಿ ಆದೇಶ ಹೊರಡಿಸಿದ ಬೆಳೆಗಳಿಗೆ ಮಾತ್ರ ಬೆಂಬಲ ಬೆಲೆ ಅನ್ವಯಿಸುತ್ತದೆ.")
            ],
            "required_documents": [
                "FRUITS FID Number",
                "RTC land record reflecting crop survey entry",
                "Aadhaar card",
                "Aadhaar-seeded bank passbook copy"
            ],
            "required_documents_kn": [
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ (FID)",
                "ಬೆಳೆ ಸಮೀಕ್ಷೆ ನಮೂದಾದ ಪಹಣಿ (RTC)",
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಆಧಾರ್ ಲಿಂಕ್ ಆದ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Register at nearest designated APMC / PACS procurement centre upon government notification.",
                "Slot allotment SMS received with specified date for grain delivery.",
                "Deliver cleaned, FAQ-standard produce to procurement centre.",
                "Weighment slip generated; payment credited directly to bank account via DBT."
            ],
            "application_steps_kn": [
                "ಸರ್ಕಾರ ಅಧಿಸೂಚನೆ ಹೊರಡಿಸಿದಾಗ ಹತ್ತಿರದ ಖರೀದಿ ಕೇಂದ್ರದಲ್ಲಿ ಎಫ್‌ಐಡಿ ನೀಡಿ ನೋಂದಾಯಿಸಿ.",
                "ಧಾನ್ಯ ತರಲು ದಿನಾಂಕ ನಿಗದಿಪಡಿಸಿದ ಎಸ್‌ಎಂಎಸ್ (SMS) ಸಂದೇಶ ಬರುತ್ತದೆ.",
                "ಗುಣಮಟ್ಟದ (FAQ) ಧಾನ್ಯವನ್ನು ಖರೀದಿ ಕೇಂದ್ರಕ್ಕೆ ತಂದು ತೂಕ ಮಾಡಿಸಿ.",
                "ರಸೀದಿ ಪಡೆದ 7 ರಿಂದ 15 ದಿನಗಳಲ್ಲಿ ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಹಣ ಜಮೆಯಾಗುತ್ತದೆ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Karnataka State Agricultural Marketing Board (KSAMB) / Food & Civil Supplies Department",
            "verification_authority": "APMC Procurement Officer & Food Sheristedar",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All APMC & PACS Centres in Karnataka"],
            "supported_crops": ["Ragi, Jowar, Paddy, Red gram, Bengal gram, Ball Copra, Milling Copra"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Produce must conform strictly to Fair Average Quality (FAQ) moisture and purity specifications."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಧಾನ್ಯಗಳು ಸರ್ಕಾರ ನಿಗದಿಪಡಿಸಿದ ತೇವಾಂಶ (FAQ) ಮಾನದಂಡಗಳನ್ನು ಹೊಂದಿರಬೇಕು."
            ]
        },

        # 35. Krishi Abhiyana
        {
            "id": "krishi-abhiyana",
            "name": "Karnataka Krishi Abhiyana (Integrated Agricultural Outreach Campaign)",
            "name_kn": "ಕರ್ನಾಟಕ ಕೃಷಿ ಅಭಿಯಾನ (ಸಮಗ್ರ ಕೃಷಿ ಮಾಹಿತಿ ಮತ್ತು ತಂತ್ರಜ್ಞಾನ ಆಂದೋಲನ)",
            "official_abbreviation": "Krishi Abhiyana",
            "government_level": "karnataka",
            "scheme_type": "real",
            "category": "training_advisory",
            "category_kn": "ಕೃಷಿ ಆಂದೋಲನ ಮತ್ತು ಮನೆಬಾಗಿಲ ಸಲಹೆ",
            "assistance_type": "training_advisory",
            "status_label": "Seasonal application",
            "status_label_kn": "ಋತುಮಾನ ಆಧಾರಿತ ಅರ್ಜಿ",
            "description": "Pre-Kharif mobile extension campaign bringing scientists, agricultural officers, input agencies, and soil diagnostic vans directly to gram panchayats to advise farmers on climate-resilient packages and government schemes.",
            "description_kn": "ಮುಂಗಾರು ಹಂಗಾಮಿಗೆ ಮುನ್ನ ಕೃಷಿ ವಿಜ್ಞಾನಿಗಳು, ಅಧಿಕಾರಿಗಳು ಮತ್ತು ಸಂಚಾರಿ ಮಣ್ಣು ಪರೀಕ್ಷಾ ವಾಹನಗಳು ನೇರವಾಗಿ ಗ್ರಾಮ ಪಂಚಾಯ್ತಿಗಳಿಗೆ ಭೇಟಿ ನೀಡಿ ರೈತರಿಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡುವ ವಾರ್ಷಿಕ ಕೃಷಿ ಅಭಿಯಾನ.",
            "benefits": [
                "Free doorstep diagnostic advisory for pest management, soil testing, and certified seed selection.",
                "On-the-spot registration for FRUITS, crop insurance, and departmental machinery subsidies."
            ],
            "benefits_kn": [
                "ಗ್ರಾಮ ಪಂಚಾಯ್ತಿ ಮಟ್ಟದಲ್ಲಿ ಕೃಷಿ ವಿಜ್ಞಾನಿಗಳಿಂದ ನೇರ ಸಲಹೆ, ಮಣ್ಣು ಪರೀಕ್ಷೆ ಮತ್ತು ಬೀಜ ತಳಿ ಆಯ್ಕೆ ಮಾರ್ಗದರ್ಶನ.",
                "ಸ್ಥಳದಲ್ಲೇ ಫ್ರೂಟ್ಸ್ ನೋಂದಣಿ, ಬೆಳೆ ವಿಮೆ ಮತ್ತು ಸಬ್ಸಿಡಿ ಅರ್ಜಿಗಳ ಸ್ವೀಕಾರ."
            ],
            "eligibility_rules": [
                make_rule("ka_state", "Open to all farmers and rural households residing in Karnataka.", "ಕರ್ನಾಟಕದಲ್ಲಿ ವಾಸಿಸುವ ಎಲ್ಲಾ ರೈತರು ಮತ್ತು ಸಾರ್ವಜನಿಕರಿಗೆ ಮುಕ್ತವಾಗಿದೆ.", "location.state", "in", ["Karnataka", "karnataka", "KA"], True, "Krishi Abhiyana Campaign Protocol", "verified", "Do you reside in Karnataka?", "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿ ವಾಸವಿದ್ದೀರಾ?", "Statewide outreach held at every Hobli and Gram Panchayat in Karnataka.", "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಹೋಬಳಿ ಮತ್ತು ಗ್ರಾಮ ಪಂಚಾಯ್ತಿಗಳಲ್ಲಿ ಈ ಜಾಥಾ ನಡೆಯುತ್ತದೆ.")
            ],
            "required_documents": [
                "Aadhaar card",
                "FRUITS FID or RTC copy (for scheme registration on the spot)"
            ],
            "required_documents_kn": [
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಫ್ರೂಟ್ಸ್ ಎಫ್‌ಐಡಿ ಅಥವಾ ಪಹಣಿ (ಸ್ಥಳದಲ್ಲೇ ಅರ್ಜಿ ಸಲ್ಲಿಸಲು)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Attend scheduled Krishi Abhiyana vehicle visit at local Gram Panchayat.",
                "Interact with agricultural scientists and extension officers.",
                "Avail free soil diagnostic checks, minikits, and scheme registrations."
            ],
            "application_steps_kn": [
                "ಗ್ರಾಮ ಪಂಚಾಯ್ತಿಗೆ ಕೃಷಿ ಅಭಿಯಾನ ವಾಹನ ಬರುವ ದಿನಾಂಕದಂದು ಹಾಜರಾಗಿ.",
                "ಕೃಷಿ ವಿಜ್ಞಾನಿಗಳೊಂದಿಗೆ ಚರ್ಚಿಸಿ ನಿಮ್ಮ ಜಮೀನಿನ ಸಮಸ್ಯೆಗಳಿಗೆ ಪರಿಹಾರ ಕಂಡುಕೊಳ್ಳಿ.",
                "ಸ್ಥಳದಲ್ಲೇ ಮಣ್ಣು ಪರೀಕ್ಷೆ ಮಾಡಿಸಿ ಸರ್ಕಾರದ ಸವಲತ್ತುಗಳಿಗೆ ನೋಂದಾಯಿಸಿ."
            ],
            "official_source_url": "https://raitamitra.karnataka.gov.in/",
            "issuing_authority": "Department of Agriculture, Horticulture, Animal Husbandry, Karnataka",
            "verification_authority": "Assistant Director of Agriculture (ADA) & Local RSK",
            "last_verified_at": "2026-10-30",
            "verification_status": "verified",
            "applicable_locations": ["All Gram Panchayats in Karnataka"],
            "supported_crops": ["All crops, horticulture, livestock, fisheries, sericulture"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Held annually in May-June preceding the South-West Monsoon."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಪ್ರತಿ ವರ್ಷ ಮುಂಗಾರು ಮಳೆಗೆ ಮುನ್ನ ಮೇ-ಜೂನ್ ತಿಂಗಳಲ್ಲಿ ಈ ಅಭಿಯಾನ ನಡೆಯುತ್ತದೆ."
            ]
        }
    ]
