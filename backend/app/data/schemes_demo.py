def get_demo_schemes():
    return [
        {
            "id": "demo-micro-irrigation",
            "name": "Demo Micro-Irrigation Support",
            "name_kn": "ಮಾದರಿ ಸೂಕ್ಷ್ಮ ನೀರಾವರಿ ಸಹಾಯಧನ",
            "official_abbreviation": "DEMO-IRRIG",
            "government_level": "karnataka",
            "scheme_type": "demonstration",
            "category": "irrigation_infrastructure",
            "category_kn": "ನೀರಾವರಿ ಮೂಲಸೌಕರ್ಯ",
            "assistance_type": "irrigation_infrastructure",
            "status_label": "Requires official confirmation",
            "status_label_kn": "ಅಧಿಕೃತ ದೃಢೀಕರಣದ ಅಗತ್ಯವಿದೆ",
            "description": "DEMONSTRATION ONLY - FOR TESTING PURPOSES. Demonstration programme for micro-irrigation and water conservation subsidy matching.",
            "description_kn": "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಉದ್ದೇಶಕ್ಕೆ ಮಾತ್ರ. ಹನಿ ನೀರಾವರಿ ಮತ್ತು ತುಂತುರು ನೀರಾವರಿ ಸೌಲಭ್ಯಗಳ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಯೋಜನೆ.",
            "benefits": [
                "Demonstration subsidy for drip irrigation layout up to 5 acres.",
                "Technical advisory on fertigation and water budgeting."
            ],
            "benefits_kn": [
                "5 ಎಕರೆವರೆಗಿನ ಹನಿ ನೀರಾವರಿ ಅಳವಡಿಕೆಗೆ ಮಾದರಿ ಸಹಾಯಧನ.",
                "ನೀರಿನ ಮಿತವ್ಯಯ ಮತ್ತು ರಸಾವರಿ ಕುರಿತು ತಾಂತ್ರಿಕ ಸಲಹೆ."
            ],
            "eligibility_rules": [
                {
                    "rule_id": "demo_irrig_state",
                    "description": "Must be located in Karnataka state for demonstration test.",
                    "description_kn": "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಪರೀಕ್ಷೆಗೆ ಕರ್ನಾಟಕ ರಾಜ್ಯದಲ್ಲಿರಬೇಕು.",
                    "field": "location.state",
                    "operator": "in",
                    "expected_value": ["Karnataka", "karnataka", "KA"],
                    "is_mandatory": True,
                    "source_reference": "Demo Architecture Spec 2026",
                    "verification_status": "synthetic"
                },
                {
                    "rule_id": "demo_irrig_land",
                    "description": "Cultivable land holding must be at least 0.5 acres.",
                    "description_kn": "ಕನಿಷ್ಠ 0.5 ಎಕರೆ ಸಾಗುವಳಿ ಜಮೀನು ಇರಬೇಕು.",
                    "field": "land_area.value_acres",
                    "operator": "greater_than_or_equal",
                    "expected_value": 0.5,
                    "is_mandatory": True,
                    "source_reference": "Demo Architecture Spec 2026",
                    "verification_status": "synthetic"
                },
                {
                    "rule_id": "demo_irrig_max_land",
                    "description": "Cultivable land holding must not exceed 12.5 acres.",
                    "description_kn": "ಸಾಗುವಳಿ ಜಮೀನು 12.5 ಎಕರೆ ಮೀರಬಾರದು.",
                    "field": "land_area.value_acres",
                    "operator": "less_than_or_equal",
                    "expected_value": 12.5,
                    "is_mandatory": True,
                    "source_reference": "Demo Architecture Spec 2026",
                    "verification_status": "synthetic"
                }
            ],
            "required_documents": [
                "Land record (RTC)",
                "Water source proof (Borewell / Open well / Canal entry)"
            ],
            "required_documents_kn": [
                "ಪಹಣಿ (RTC)",
                "ನೀರಿನ ಮೂಲದ ದಾಖಲೆ (ಬೋರ್‌ವೆಲ್ / ಬಾವಿ / ಕಾಲುವೆ)"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Demonstration workflow step 1: Verify landholding and water availability.",
                "Demonstration workflow step 2: Select drip system vendor."
            ],
            "application_steps_kn": [
                "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಹಂತ 1: ಜಮೀನು ಮತ್ತು ನೀರಿನ ಲಭ್ಯತೆ ಪರಿಶೀಲನೆ.",
                "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಹಂತ 2: ಹನಿ ನೀರಾವರಿ ವಿತರಕರ ಆಯ್ಕೆ."
            ],
            "official_source_url": None,
            "issuing_authority": "Demonstration Agricultural Testing Engine",
            "verification_authority": "Local Raitha Samparka Kendra (RSK)",
            "last_verified_at": "2026-10-30",
            "verification_status": "synthetic",
            "applicable_locations": ["Karnataka"],
            "supported_crops": ["Horticulture crops", "Commercial crops", "Sugarcane"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "This is a demonstration scheme record for offline testing and automated verification."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಇದು ಆಫ್‌ಲೈನ್ ಪರೀಕ್ಷೆ ಮತ್ತು ಸ್ವಯಂಚಾಲಿತ ಪರಿಶೀಲನೆಗಾಗಿ ರಚಿಸಲಾದ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಯೋಜನೆಯಾಗಿದೆ."
            ]
        },
        {
            "id": "demo-equipment-assistance",
            "name": "Demo Agricultural Equipment Assistance",
            "name_kn": "ಮಾದರಿ ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ಸಹಾಯಧನ",
            "official_abbreviation": "DEMO-EQUIP",
            "government_level": "karnataka",
            "scheme_type": "demonstration",
            "category": "equipment_rental",
            "category_kn": "ಯಂತ್ರೋಪಕರಣ ನೆರವು",
            "assistance_type": "equipment_rental",
            "status_label": "Requires official confirmation",
            "status_label_kn": "ಅಧಿಕೃತ ದೃಢೀಕರಣದ ಅಗತ್ಯವಿದೆ",
            "description": "DEMONSTRATION ONLY - FOR TESTING PURPOSES. Demonstration programme for power tiller, sprayer, and farm mechanisation subsidies.",
            "description_kn": "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಉದ್ದೇಶಕ್ಕೆ ಮಾತ್ರ. ಪವರ್ ಟಿಲ್ಲರ್, ಸ್ಪ್ರೇಯರ್ ಮತ್ತು ಕೃಷಿ ಯಂತ್ರೋಪಕರಣಗಳ ಮಾದರಿ ಸಹಾಯಧನ ಯೋಜನೆ.",
            "benefits": [
                "Demonstration subsidy for small farm implements and sprayers.",
                "Priority booking through custom hiring centres."
            ],
            "benefits_kn": [
                "ಸಣ್ಣ ಕೃಷಿ ಉಪಕರಣಗಳು ಮತ್ತು ಸ್ಪ್ರೇಯರ್‌ಗಳಿಗೆ ಮಾದರಿ ಸಹಾಯಧನ.",
                "ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಕೇಂದ್ರಗಳ ಮೂಲಕ ಆದ್ಯತೆಯ ಬುಕಿಂಗ್."
            ],
            "eligibility_rules": [
                {
                    "rule_id": "demo_equip_state",
                    "description": "Must be located in Karnataka.",
                    "description_kn": "ಕರ್ನಾಟಕ ರಾಜ್ಯದಲ್ಲಿರಬೇಕು.",
                    "field": "location.state",
                    "operator": "in",
                    "expected_value": ["Karnataka", "karnataka", "KA"],
                    "is_mandatory": True,
                    "source_reference": "Demo Architecture Spec 2026",
                    "verification_status": "synthetic"
                },
                {
                    "rule_id": "demo_equip_land",
                    "description": "Cultivable land holding must be at least 1.0 acre.",
                    "description_kn": "ಕನಿಷ್ಠ 1.0 ಎಕರೆ ಸಾಗುವಳಿ ಜಮೀನು ಇರಬೇಕು.",
                    "field": "land_area.value_acres",
                    "operator": "greater_than_or_equal",
                    "expected_value": 1.0,
                    "is_mandatory": True,
                    "source_reference": "Demo Architecture Spec 2026",
                    "verification_status": "synthetic"
                }
            ],
            "required_documents": [
                "Aadhaar card",
                "Land record (RTC / Pahani)",
                "Bank passbook"
            ],
            "required_documents_kn": [
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಪಹಣಿ (RTC)",
                "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Demonstration application step: Check available machinery at RSK.",
                "Demonstration application step: Submit invoice after purchase."
            ],
            "application_steps_kn": [
                "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಅರ್ಜಿ ಹಂತ: ಆರ್‌ಎಸ್‌ಕೆ ಕೇಂದ್ರದಲ್ಲಿ ಲಭ್ಯವಿರುವ ಯಂತ್ರೋಪಕರಣ ಪರಿಶೀಲನೆ.",
                "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಅರ್ಜಿ ಹಂತ: ಖರೀದಿಯ ನಂತರ ಇನ್‌ವಾಯ್ಸ್ ಸಲ್ಲಿಕೆ."
            ],
            "official_source_url": None,
            "issuing_authority": "Demonstration Agricultural Testing Engine",
            "verification_authority": "Department of Agriculture, Karnataka",
            "last_verified_at": "2026-10-30",
            "verification_status": "synthetic",
            "applicable_locations": ["Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Demonstration scheme for software validation."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಸಾಫ್ಟ್‌ವೇರ್ ಮೌಲ್ಯಮಾಪನಕ್ಕಾಗಿ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಯೋಜನೆ."
            ]
        },
        {
            "id": "demo-soil-improvement",
            "name": "Demo Soil Improvement Support",
            "name_kn": "ಮಾದರಿ ಮಣ್ಣು ಸುಧಾರಣಾ ಸಹಾಯಧನ",
            "official_abbreviation": "DEMO-SOIL",
            "government_level": "central",
            "scheme_type": "demonstration",
            "category": "input_assistance",
            "category_kn": "ಇನ್‌ಪುಟ್ ನೆರವು",
            "assistance_type": "input_assistance",
            "status_label": "Requires official confirmation",
            "status_label_kn": "ಅಧಿಕೃತ ದೃಢೀಕರಣದ ಅಗತ್ಯವಿದೆ",
            "description": "DEMONSTRATION ONLY - FOR TESTING PURPOSES. Demonstration programme for soil organic carbon enrichment and micronutrient distribution.",
            "description_kn": "ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಉದ್ದೇಶಕ್ಕೆ ಮಾತ್ರ. ಮಣ್ಣಿನ ಸಾವಯವ ಇಂಗಾಲ ವೃದ್ಧಿ ಮತ್ತು ಲಘು ಪೋಷಕಾಂಶಗಳ ವಿತರಣೆಯ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಯೋಜನೆ.",
            "benefits": [
                "Free soil testing sample collection and diagnostic card.",
                "Subsidised biofertilisers and soil conditioners."
            ],
            "benefits_kn": [
                "ಉಚಿತ ಮಣ್ಣು ಪರೀಕ್ಷೆ ಮಾದರಿ ಸಂಗ್ರಹ ಮತ್ತು ತಪಾಸಣಾ ಕಾರ್ಡ್.",
                "ರಿಯಾಯಿತಿ ದರದ ಜೈವಿಕ ಗೊಬ್ಬರಗಳು ಮತ್ತು ಮಣ್ಣು ಸುಧಾರಕಗಳು."
            ],
            "eligibility_rules": [
                {
                    "rule_id": "demo_soil_state",
                    "description": "Applicable across Karnataka and India.",
                    "description_kn": "ಕರ್ನಾಟಕ ಮತ್ತು ಭಾರತಾದ್ಯಂತ ಅನ್ವಯಿಸುತ್ತದೆ.",
                    "field": "location.state",
                    "operator": "in",
                    "expected_value": ["Karnataka", "karnataka", "KA", "All India"],
                    "is_mandatory": True,
                    "source_reference": "Demo Architecture Spec 2026",
                    "verification_status": "synthetic"
                }
            ],
            "required_documents": [
                "Aadhaar card",
                "Land survey number"
            ],
            "required_documents_kn": [
                "ಆಧಾರ್ ಕಾರ್ಡ್",
                "ಸರ್ವೇ ನಂಬರ್ ವಿವರ"
            ],
            "optional_documents": [],
            "optional_documents_kn": [],
            "application_steps": [
                "Demonstration soil sample submission at local laboratory."
            ],
            "application_steps_kn": [
                "ಸ್ಥಳೀಯ ಮಣ್ಣು ಪರೀಕ್ಷಾ ಕೇಂದ್ರಕ್ಕೆ ಮಾದರಿ ಸಲ್ಲಿಕೆ."
            ],
            "official_source_url": None,
            "issuing_authority": "Demonstration Agricultural Testing Engine",
            "verification_authority": "Soil Health Laboratory Network",
            "last_verified_at": "2026-10-30",
            "verification_status": "synthetic",
            "applicable_locations": ["All India", "Karnataka"],
            "supported_crops": ["All crops"],
            "notes": [
                "Current subsidy amount must be confirmed with the implementing department.",
                "Demonstration scheme for testing deterministic rule execution."
            ],
            "notes_kn": [
                "ಪ್ರಸ್ತುತ ಸಹಾಯಧನದ ಮೊತ್ತವನ್ನು ಅನುಷ್ಠಾನ ಇಲಾಖೆಯೊಂದಿಗೆ ದೃಢಪಡಿಸಿಕೊಳ್ಳಬೇಕು.",
                "ಡಿಟರ್ಮಿನಿಸ್ಟಿಕ್ ನಿಯಮ ಮೌಲ್ಯಮಾಪನ ಪರೀಕ್ಷೆಗಾಗಿ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಯೋಜನೆ."
            ]
        }
    ]
