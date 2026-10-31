import re
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from ..models.farmer import FarmerProfile, LandArea, Location, IrrigationInfo

logger = logging.getLogger(__name__)

VOCAB_PATH = Path(__file__).resolve().parent.parent / "data" / "vocabulary_kn.json"

class ProfileExtractor:
    _vocab: Optional[Dict[str, Any]] = None

    @classmethod
    def load_vocab(cls) -> Dict[str, Any]:
        if cls._vocab is None:
            try:
                with open(VOCAB_PATH, "r", encoding="utf-8") as f:
                    cls._vocab = json.load(f)
            except Exception as e:
                logger.error(f"Could not load vocabulary from {VOCAB_PATH}: {e}")
                cls._vocab = {}
        return cls._vocab

    @classmethod
    def convert_to_acres(cls, value: float, unit: str) -> Optional[float]:
        vocab = cls.load_vocab()
        conversions = vocab.get("unit_conversions_to_acres", {
            "acre": 1.0,
            "guntha": 0.025,
            "hectare": 2.47105,
            "cent": 0.01,
            "bigha": 0.625
        })
        std_unit = unit.lower().strip()
        factor = conversions.get(std_unit, 1.0 if "acre" in std_unit else None)
        if factor is not None:
            return round(value * factor, 3)
        return None

    @classmethod
    def extract_from_text(
        cls,
        text: str,
        existing_profile: Optional[FarmerProfile] = None
    ) -> Tuple[FarmerProfile, Dict[str, Any]]:
        """
        Extracts agricultural facts from natural Kannada / English text.
        Preserves existing facts, detects explicit updates/corrections, tracks ambiguities,
        and records provenance/confidence for each field without guessing.
        """
        vocab = cls.load_vocab()
        profile = existing_profile.model_copy(deep=True) if existing_profile else FarmerProfile()
        text_lower = text.lower()
        extracted_summary: Dict[str, Any] = {}
        ambiguities: List[Dict[str, Any]] = []

        # 0. Detect Negation / Correction patterns
        is_correction = any(neg in text for neg in ["ಅಲ್ಲ", "ಬದಲಿಗೆ", "ತಪ್ಪು", "not", "instead", "mistake", "actually"])

        # 1. Ambiguity Detection (e.g. standalone "ಜೋಳ" without "ಮೆಕ್ಕೆ" or "ಬಿಳಿ")
        ambiguous_crop_terms = vocab.get("ambiguous_crop_terms", {})
        for term, ambig_info in ambiguous_crop_terms.items():
            if term == "ಜೋಳ" and "ಮೆಕ್ಕೆಜೋಳ" not in text and "ಬಿಳಿ ಜೋಳ" not in text and "ಮುಸುಕಿನ ಜೋಳ" not in text:
                if re.search(r"(^|[^\u0C80-\u0CFF])ಜೋಳ([^\u0C80-\u0CFF]|$)", text):
                    ambiguities.append({
                        "term": "ಜೋಳ",
                        "field": "crops",
                        "options": ambig_info.get("possible_crops", []),
                        "question_kn": ambig_info.get("clarification_question_kn"),
                        "question_en": ambig_info.get("clarification_question")
                    })

        # 2. Extract Crops (Supporting Multiple Crops)
        crops_vocab = vocab.get("crops", {})
        extracted_crops = []
        for word, std_crop in crops_vocab.items():
            # Match whole word or substring bounded by spaces/punctuation
            if word in text or word in text_lower:
                # If ambiguous term detected and no qualifier, wait for clarification
                if word == "ಜೋಳ" and any(a["term"] == "ಜೋಳ" for a in ambiguities):
                    continue
                if std_crop not in extracted_crops:
                    extracted_crops.append(std_crop)

        if extracted_crops:
            if is_correction and any(c in text for c in ["ಅಲ್ಲ", "not"]):
                # User is replacing crops
                profile.crops = extracted_crops
            else:
                for c in extracted_crops:
                    if c not in profile.crops:
                        profile.crops.append(c)

            profile.set_field_value(
                field_name="crops",
                value=profile.crops,
                confidence=0.95,
                source="user_explicit",
                status="confirmed"
            )
            extracted_summary["crops"] = profile.crops

        # 3. Extract Land Area and Unit
        land_units_vocab = vocab.get("land_units", {})
        kn_numbers = vocab.get("kannada_numbers", {})

        # Pattern 0: Correction pair: e.g. "3 ಎಕರೆ ಅಲ್ಲ 2 ಎಕರೆ" or "not 5 acres, 2 acres"
        corr_pair_match = re.search(
            r"(\d+(?:\.\d+)?)\s*(ಎಕರೆ|ಎಕ್ರೆ|ಎಕರ|acres?|ಗುಂಟೆ|ಗುಂಟಾ|gunthas?|guntas?|gunte|ಹೆಕ್ಟೇರ್|ಹೆಕ್ಟೇರು|hectares?)\s*(?:ಅಲ್ಲ|not|ಬದಲಿಗೆ|instead)\s*,?\s*(?:but\s+)?(\d+(?:\.\d+)?)\s*(ಎಕರೆ|ಎಕ್ರೆ|ಎಕರ|acres?|ಗುಂಟೆ|ಗುಂಟಾ|gunthas?|guntas?|gunte|ಹೆಕ್ಟೇರ್|ಹೆಕ್ಟೇರು|hectares?)?",
            text,
            re.IGNORECASE
        )

        # Pattern A: Digits followed by unit (e.g., 3 ಎಕರೆ, 2.5 acre, 40 ಗುಂಟೆ, 1 hectare)
        digit_match = re.search(
            r"(\d+(?:\.\d+)?)\s*(ಎಕರೆ|ಎಕ್ರೆ|ಎಕರ|acres?|ಗುಂಟೆ|ಗುಂಟಾ|gunthas?|guntas?|gunte|ಹೆಕ್ಟೇರ್|ಹೆಕ್ಟೇರು|hectares?|ಸೆಂಟು|ಸೆಂಟ್|cents?|ಬಿಘಾ|bigha)",
            text,
            re.IGNORECASE
        )
        # Pattern B: Kannada number word followed by unit (e.g., ಮೂರು ಎಕರೆ, ಎರಡು ಗುಂಟೆ, ಅರ್ಧ ಎಕರೆ)
        kn_match = re.search(
            r"(ಅರ್ಧ|ಕಾಲು|ಮುಕ್ಕಾಲು|ಒಂದು|ಒಂದೂವರೆ|ಎರಡು|ಎರಡೂವರೆ|ಮೂರು|ಮೂರಾವರೆ|ನಾಲ್ಕು|ನಾಲ್ಕೂವರೆ|ಐದು|ಆರು|ಏಳು|ಎಂಟು|ಒಂಬತ್ತು|ಹತ್ತು|ಹನ್ನೆರಡು|ಹದಿನೈದು|ಇಪ್ಪತ್ತು|ಇಪ್ಪತ್ತೈದು)\s*(ಎಕರೆ|ಎಕ್ರೆ|ಎಕರ|acres?|ಗುಂಟೆ|ಗುಂಟಾ|gunthas?|guntas?|gunte|ಹೆಕ್ಟೇರ್|ಹೆಕ್ಟೇರು|hectares?|ಸೆಂಟು|ಸೆಂಟ್|cents?|ಬಿಘಾ|bigha)",
            text,
            re.IGNORECASE
        )

        area_val: Optional[float] = None
        unit_str: Optional[str] = None

        if corr_pair_match:
            try:
                area_val = float(corr_pair_match.group(3))
                unit_raw = (corr_pair_match.group(4) or corr_pair_match.group(2)).lower()
                unit_str = land_units_vocab.get(unit_raw, "acre")
            except (ValueError, IndexError):
                pass
        elif digit_match:
            try:
                area_val = float(digit_match.group(1))
                unit_raw = digit_match.group(2).lower()
                unit_str = land_units_vocab.get(unit_raw, "acre")
            except ValueError:
                pass
        elif kn_match:
            kn_num_word = kn_match.group(1)
            unit_raw = kn_match.group(2).lower()
            area_val = kn_numbers.get(kn_num_word)
            unit_str = land_units_vocab.get(unit_raw, "acre")

        if area_val is not None and unit_str is not None:
            acres = cls.convert_to_acres(area_val, unit_str)
            profile.land_area = LandArea(
                value=area_val,
                unit=unit_str,
                value_acres=acres
            )
            profile.set_field_value(
                field_name="land_area.value_acres",
                value=acres,
                confidence=0.95,
                source="user_explicit",
                status="confirmed"
            )
            extracted_summary["land_area"] = f"{area_val} {unit_str} ({acres} acres)"

        # 4. Extract Taluk and Village
        districts_vocab = vocab.get("districts", {})
        taluks_vocab = vocab.get("taluks", {})
        for t_word, t_data in taluks_vocab.items():
            if t_word in text or t_word.lower() in text_lower:
                profile.location.taluk = t_data["taluk"]
                if not profile.location.district:
                    profile.location.district = t_data["district"]
                    profile.set_field_value("location.district", t_data["district"], confidence=0.90, source="inferred_from_taluk")
                profile.set_field_value("location.taluk", t_data["taluk"], confidence=0.95, source="user_explicit")
                extracted_summary["taluk"] = t_data["taluk"]
                break

        # Check for village patterns e.g. "ಆಗುಂಬೆ ಗ್ರಾಮ", "village XYZ"
        village_match = re.search(r"(?:^|\s)([A-Za-z\u0C80-\u0CFF]+)\s+(?:ಗ್ರಾಮ|ಗ್ರಾಮದ|ಗ್ರಾಮದಲ್ಲಿ|ಗ್ರಾಮದಲ್ಲಿದೆ|village)", text, re.IGNORECASE)
        if not village_match:
            village_match = re.search(r"village\s+([A-Za-z\u0C80-\u0CFF]+)", text, re.IGNORECASE)

        if village_match:
            v_name = village_match.group(1).strip()
            # Ensure it's not a reserved keyword or taluk/district
            reserved = ["ನನ್ನ", "ನಮ್ಮ", "ಈ", "my", "our", "ತಾಲೂಕಿನ", "ಜಿಲ್ಲೆಯ", "ತಾಲೂಕು", "ಜಿಲ್ಲೆ"]
            if v_name not in reserved and v_name.lower() not in taluks_vocab and v_name.lower() not in districts_vocab:
                profile.location.village = v_name
                profile.set_field_value("location.village", v_name, confidence=0.85, source="user_explicit")
                extracted_summary["village"] = v_name

        # 5. Extract District and State
        for dist_term, std_dist in districts_vocab.items():
            if dist_term in text or dist_term.lower() in text_lower:
                profile.location.district = std_dist
                profile.set_field_value("location.district", std_dist, confidence=0.95, source="user_explicit")
                extracted_summary["district"] = std_dist
                break

        if any(st in text or st in text_lower for st in ["ಕರ್ನಾಟಕ", "karnataka"]):
            profile.location.state = "Karnataka"
            profile.set_field_value("location.state", "Karnataka", confidence=0.99, source="user_explicit")

        # 6. Extract Ownership
        ownership_vocab = vocab.get("ownership", {})
        for own_term, std_own in ownership_vocab.items():
            if own_term in text or own_term.lower() in text_lower:
                profile.ownership = std_own
                profile.set_field_value("ownership", std_own, confidence=0.95, source="user_explicit")
                extracted_summary["ownership"] = std_own
                break

        # 7. Extract Irrigation Facilities
        irr_vocab = vocab.get("irrigation_sources", {})
        for irr_term, std_irr in irr_vocab.items():
            if irr_term in text or irr_term.lower() in text_lower:
                if std_irr == "rainfed":
                    profile.irrigation.has_irrigation = False
                    profile.irrigation.source = "rainfed"
                    profile.additional_details["water_source_available"] = False
                else:
                    profile.irrigation.has_irrigation = True
                    profile.irrigation.source = std_irr
                    if std_irr in ["drip", "sprinkler"]:
                        profile.irrigation.type = std_irr
                    profile.additional_details["water_source_available"] = True

                profile.set_field_value("irrigation.source", std_irr, confidence=0.95, source="user_explicit")
                extracted_summary["irrigation"] = std_irr
                break

        # 8. Extract Assistance Needs
        assistance_vocab = vocab.get("assistance_needs", {})
        for need_term, std_need in assistance_vocab.items():
            if need_term in text or need_term.lower() in text_lower:
                if std_need not in profile.assistance_needs:
                    profile.assistance_needs.append(std_need)
                profile.set_field_value("assistance_needs", profile.assistance_needs, confidence=0.90, source="user_explicit")
                extracted_summary["assistance_needs"] = profile.assistance_needs

        # 9. Extract Season
        season_vocab = vocab.get("seasons", {})
        for s_term, std_s in season_vocab.items():
            if s_term in text or s_term.lower() in text_lower:
                profile.season = std_s
                profile.set_field_value("season", std_s, confidence=0.95, source="user_explicit")
                extracted_summary["season"] = std_s
                break

        # 10. Additional Specific Criteria (income tax payer, etc.)
        if any(w in text or w in text_lower for w in ["ತೆರಿಗೆ", "ಇನ್‌ಕಂ ಟ್ಯಾಕ್ಸ್", "income tax", "tax payer"]):
            if any(neg in text for neg in ["ಇಲ್ಲ", "ಕಟ್ಟುತ್ತಿಲ್ಲ", "not", "no"]):
                profile.additional_details["is_income_tax_payer"] = False
                profile.set_field_value("additional_details.is_income_tax_payer", False, confidence=0.95, source="user_explicit")
            else:
                profile.additional_details["is_income_tax_payer"] = True
                profile.set_field_value("additional_details.is_income_tax_payer", True, confidence=0.95, source="user_explicit")

        if ambiguities:
            profile.additional_details["pending_ambiguities"] = ambiguities
            extracted_summary["ambiguities"] = ambiguities

        return profile, extracted_summary
