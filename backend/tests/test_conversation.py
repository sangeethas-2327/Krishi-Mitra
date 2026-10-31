import pytest
from app.services.profile_extractor import ProfileExtractor
from app.services.conversation_manager import ConversationManager
from app.models.farmer import FarmerProfile

def test_acceptance_scenario_utterance_extraction():
    # Prompt Section 17 scenario:
    utterance = "ನನಗೆ ಕೃಷಿಗೆ ಸಹಾಯಧನ ಬೇಕು. ನಾನು ಮೂರು ಎಕರೆ ಅಡಿಕೆ ಬೆಳೆಯುತ್ತೇನೆ."
    profile, extracted = ProfileExtractor.extract_from_text(utterance)

    # 1. Verify extracted crops
    assert "arecanut" in profile.crops

    # 2. Verify land area & unit normalization (ಮೂರು ಎಕರೆ -> 3.0 acres)
    assert profile.land_area.value == 3.0
    assert profile.land_area.value_acres == 3.0

    # 3. Verify assistance need
    assert "subsidy" in profile.assistance_needs

    # 4. Unknown fields MUST remain unknown, not invented!
    assert profile.location.district is None
    assert profile.ownership is None
    assert "location.district" in profile.unknown_fields

def test_land_unit_conversions():
    # 40 guntha = 1.0 acre
    profile1, _ = ProfileExtractor.extract_from_text("ನನ್ನ ಬಳಿ 40 ಗುಂಟೆ ಜಮೀನಿದೆ")
    assert profile1.land_area.value == 40.0
    assert profile1.land_area.unit == "guntha"
    assert profile1.land_area.value_acres == 1.0

    # 2 hectare = ~4.942 acres
    profile2, _ = ProfileExtractor.extract_from_text("ನನ್ನ ಬಳಿ 2 ಹೆಕ್ಟೇರ್ ಜಮೀನಿದೆ")
    assert profile2.land_area.value == 2.0
    assert profile2.land_area.unit == "hectare"
    assert profile2.land_area.value_acres is not None
    assert profile2.land_area.value_acres > 4.9

def test_explicit_correction():
    initial_profile = FarmerProfile(crops=["arecanut"])
    updated_profile, _ = ProfileExtractor.extract_from_text("ಅಡಿಕೆ ಅಲ್ಲ, ಬದಲಿಗೆ ರಾಗಿ ಬೆಳೆಯುತ್ತೇನೆ", initial_profile)
    assert "ragi" in updated_profile.crops

@pytest.mark.asyncio
async def test_adaptive_followup_and_multi_turn():
    # Turn 1
    session_id = "test-session-turn"
    resp1 = await ConversationManager.process_message(
        session_id=session_id,
        message="ನನಗೆ ಕೃಷಿಗೆ ಸಹಾಯಧನ ಬೇಕು. ನಾನು ಮೂರು ಎಕರೆ ಅಡಿಕೆ ಬೆಳೆಯುತ್ತೇನೆ."
    )
    assert resp1.updated_profile.land_area.value_acres == 3.0
    assert "arecanut" in resp1.updated_profile.crops
    # Follow-up question should be present because district or ownership is unknown
    assert resp1.next_question_kn is not None

    # Turn 2: Farmer provides district and ownership
    resp2 = await ConversationManager.process_message(
        session_id=session_id,
        message="ನನ್ನ ಜಮೀನು ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯಲ್ಲಿದೆ ಮತ್ತು ಇದು ನನ್ನ ಸ್ವಂತ ಜಮೀನು."
    )
    assert resp2.updated_profile.location.district == "Shivamogga"
    assert resp2.updated_profile.ownership == "owned"

    # Now PM-KISAN should be POTENTIALLY_SUITABLE
    suitable_names = [r.scheme.id for r in resp2.recommendations if r.evaluation_status.value == "POTENTIALLY_SUITABLE"]
    assert "pm-kisan" in suitable_names
