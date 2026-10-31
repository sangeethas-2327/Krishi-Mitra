import pytest
from app.services.profile_extractor import ProfileExtractor
from app.models.farmer import FarmerProfile, Location, LandArea, IrrigationInfo

def test_multiple_crops_extraction():
    text = "ನಾನು 4 ಎಕರೆ ಜಮೀನಿನಲ್ಲಿ ಅಡಿಕೆ, ಭತ್ತ ಮತ್ತು ರಾಗಿ ಬೆಳೆಯುತ್ತೇನೆ."
    profile, summary = ProfileExtractor.extract_from_text(text)

    # Must extract all 3 crops
    assert "arecanut" in profile.crops
    assert "paddy" in profile.crops
    assert "ragi" in profile.crops
    assert len(profile.crops) == 3

    # Field metadata must be recorded
    assert "crops" in profile.fields_metadata
    assert profile.fields_metadata["crops"].confidence >= 0.9
    assert profile.fields_metadata["crops"].confirmation_status == "confirmed"

def test_kannada_vocabulary_spellings_and_transliterations():
    # Test transliterated crops & spelling variations
    t1, _ = ProfileExtractor.extract_from_text("I grow adike and kabbu")
    assert "arecanut" in t1.crops
    assert "sugarcane" in t1.crops

    t2, _ = ProfileExtractor.extract_from_text("We cultivate bhatta and mekke jola in our field")
    assert "paddy" in t2.crops
    assert "maize" in t2.crops

    t3, _ = ProfileExtractor.extract_from_text("ನನ್ನ ಬಳಿ ಕಾಫಿ ಮತ್ತು ಕಾಳುಮೆಣಸು ತೋಟವಿದೆ")
    assert "coffee" in t3.crops
    assert "pepper" in t3.crops

def test_land_unit_normalization_and_acre_conversions():
    # 80 gunthas = 2.0 acres
    p1, _ = ProfileExtractor.extract_from_text("ನನ್ನ ಬಳಿ 80 ಗುಂಟೆ ಜಮೀನಿದೆ")
    assert p1.land_area.value == 80.0
    assert p1.land_area.unit == "guntha"
    assert p1.land_area.value_acres == 2.0

    # 1 hectare = ~2.471 acres
    p2, _ = ProfileExtractor.extract_from_text("I hold 1 hectare of land")
    assert p2.land_area.value == 1.0
    assert p2.land_area.unit == "hectare"
    assert p2.land_area.value_acres == 2.471

    # 100 cents = 1.0 acre
    p3, _ = ProfileExtractor.extract_from_text("ನನ್ನ ಬಳಿ 100 ಸೆಂಟ್ ಭೂಮಿ ಇದೆ")
    assert p3.land_area.value == 100.0
    assert p3.land_area.unit == "cent"
    assert p3.land_area.value_acres == 1.0

def test_ambiguous_crop_detection():
    # Standalone 'ಜೋಳ' without qualifier triggers ambiguity clarification
    text = "ನಾನು 2 ಎಕರೆ ಜಮೀನಿನಲ್ಲಿ ಜೋಳ ಬೆಳೆಯುತ್ತೇನೆ"
    profile, summary = ProfileExtractor.extract_from_text(text)

    # Should detect ambiguity
    assert "ambiguities" in summary
    assert any(a["term"] == "ಜೋಳ" for a in summary["ambiguities"])
    # Does not incorrectly force jowar when maize might be meant
    assert "pending_ambiguities" in profile.additional_details

def test_taluk_and_village_extraction():
    text = "ನನ್ನ ಜಮೀನು ತೀರ್ಥಹಳ್ಳಿ ತಾಲೂಕಿನ ಆಗುಂಬೆ ಗ್ರಾಮದಲ್ಲಿದೆ"
    profile, summary = ProfileExtractor.extract_from_text(text)

    assert profile.location.taluk == "Thirthahalli"
    assert profile.location.district == "Shivamogga"  # Inferred from taluk
    assert profile.location.village == "ಆಗುಂಬೆ"

def test_irrigation_facilities_extraction():
    # Borewell with drip irrigation
    text = "ನನ್ನ ತೋಟದಲ್ಲಿ ಬೋರ್‌ವೆಲ್ ಮತ್ತು ಹನಿ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿದೆ"
    profile, summary = ProfileExtractor.extract_from_text(text)

    assert profile.irrigation.has_irrigation is True
    assert profile.irrigation.source in ["borewell", "drip"]
    assert profile.additional_details.get("water_source_available") is True

    # Rainfed cultivation
    text_rain = "ನಮ್ಮದು ಮಳೆಯಾಶ್ರಿತ ಖುಷ್ಕಿ ಭೂಮಿ"
    profile_rain, _ = ProfileExtractor.extract_from_text(text_rain)
    assert profile_rain.irrigation.has_irrigation is False
    assert profile_rain.irrigation.source == "rainfed"

def test_conflict_tracking_and_user_corrections():
    profile = FarmerProfile()
    profile.set_field_value("ownership", "tenant", confidence=0.9, source="user_explicit")
    assert profile.ownership is None or profile.fields_metadata["ownership"].value == "tenant"

    # User corrects value: now owned
    profile.set_field_value("ownership", "owned", confidence=0.95, source="user_edit")
    assert profile.fields_metadata["ownership"].value == "owned"
    assert "ownership" in profile.conflict_fields
    assert len(profile.conflict_fields["ownership"]) == 1
    assert profile.conflict_fields["ownership"][0]["old_value"] == "tenant"
    assert profile.conflict_fields["ownership"][0]["new_value"] == "owned"
    assert "tenant" in profile.fields_metadata["ownership"].previous_values

