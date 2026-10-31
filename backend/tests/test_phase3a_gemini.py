import pytest
import json
from unittest.mock import AsyncMock, patch, MagicMock
from fastapi.testclient import TestClient

from app.main import app
from app.config import settings
from app.models.farmer import FarmerProfile, ExtractedFarmerInfo, Location, LandArea
from app.models.scheme import SchemeStatus
from app.services.llm_service import LLMService, GroundedResponseSchema
from app.services.conversation_manager import ConversationManager
from app.services.scheme_recommender import SchemeRecommender

client = TestClient(app)

class MockGeminiResponse:
    def __init__(self, text: str):
        self.text = text

# 1. Connection & Key Validation Tests
def test_gemini_client_initialization_with_missing_key():
    """When API key is empty, get_client returns None and avoids throwing exceptions."""
    client_obj = LLMService.get_client("")
    assert client_obj is None

    client_obj2 = LLMService.get_client("   ")
    assert client_obj2 is None

@pytest.mark.asyncio
async def test_gemini_graceful_handling_on_invalid_key():
    """When an invalid API key is provided, LLMService handles ClientError gracefully and falls back."""
    # Force live mode with invalid key
    with patch.object(settings, "DEMO_MODE", False):
        with patch.object(settings, "GEMINI_API_KEY", "invalid_api_key_xyz_123"):
            profile = FarmerProfile()
            extracted = await LLMService.extract_farmer_profile_with_gemini(
                message="ನನ್ನ ಬಳಿ 3 ಎಕರೆ ಅಡಿಕೆ ತೋಟವಿದೆ",
                current_profile=profile
            )
            # Should fail gracefully and return None instead of raising an unhandled exception
            assert extracted is None

            recs = SchemeRecommender.get_recommendations(profile)
            response = await LLMService.generate_response(
                user_message="ಹಲೋ",
                profile=profile,
                recommendations=recs,
                next_question_en="What is your district?",
                next_question_kn="ನಿಮ್ಮ ಜಿಲ್ಲೆ ಯಾವುದು?",
                language="kn"
            )
            # Should have fallen back to deterministic generator
            assert response is not None
            assert "kannada" in response
            assert "english" in response
            assert response.get("is_fallback") is True

# 2. Structured Extraction Schema Validation
def test_extracted_farmer_info_schema_validation():
    """Validates that ExtractedFarmerInfo properly parses JSON and validates types."""
    sample_json = json.dumps({
        "district": "Shivamogga",
        "taluk": "Thirthahalli",
        "village": "Agumbe",
        "land_area": 3.5,
        "land_unit": "acre",
        "land_area_acres": 3.5,
        "crops": ["arecanut", "paddy"],
        "ownership": "owned",
        "season": "kharif",
        "irrigation_source": "borewell",
        "has_irrigation": True,
        "assistance_needs": ["micro_irrigation", "crop_insurance"],
        "is_correction": False,
        "corrected_fields": []
    })
    extracted = ExtractedFarmerInfo.model_validate_json(sample_json)
    assert extracted.district == "Shivamogga"
    assert extracted.taluk == "Thirthahalli"
    assert extracted.land_area_acres == 3.5
    assert len(extracted.crops) == 2
    assert "arecanut" in extracted.crops
    assert "paddy" in extracted.crops
    assert extracted.ownership == "owned"
    assert extracted.has_irrigation is True

# 3. Malformed LLM Response Fallback
@pytest.mark.asyncio
async def test_malformed_llm_response_fallback():
    """When Gemini returns truncated or invalid JSON, extraction returns None without crashing."""
    mock_bad_resp = MockGeminiResponse('{"district": "Mysuru", "land_area": 4, broken_json...')
    
    mock_genai_client = MagicMock()
    mock_genai_client.aio.models.generate_content = AsyncMock(return_value=mock_bad_resp)

    with patch.object(settings, "DEMO_MODE", False):
        with patch.object(settings, "GEMINI_API_KEY", "mock_key"):
            with patch.object(LLMService, "get_client", return_value=mock_genai_client):
                res = await LLMService.extract_farmer_profile_with_gemini(
                    message="ನನ್ನ ಜಿಲ್ಲೆ ಮೈಸೂರು",
                    current_profile=FarmerProfile()
                )
                assert res is None

# 4. Protection of Confirmed Fields without Explicit Correction
@pytest.mark.asyncio
async def test_confirmed_field_protection():
    """LLM should NEVER overwrite a confirmed fact without an explicit correction flag/signal."""
    session_id = "test_sess_protect_confirmed"
    ConversationManager.reset_session(session_id)
    session = ConversationManager.get_or_create_session(session_id)

    # Farmer has already confirmed Shivamogga district
    session.profile.location.district = "Shivamogga"
    session.profile.set_field_value("location.district", "Shivamogga", status="confirmed")
    assert "location.district" in session.profile.confirmed_fields

    # Now mock an extraction that returns Mandya, but is_correction is False
    mock_extracted = ExtractedFarmerInfo(
        district="Mandya",
        is_correction=False,
        corrected_fields=[]
    )

    with patch.object(LLMService, "extract_farmer_profile_with_gemini", AsyncMock(return_value=mock_extracted)):
        res = await ConversationManager.process_message(
            session_id=session_id,
            message="ನಾನು ಭತ್ತ ಬೆಳೆಯುತ್ತೇನೆ",  # user didn't say Mandya or correction
            language="kn"
        )
        # Shivamogga must be preserved!
        assert res.updated_profile.location.district == "Shivamogga"

# 5. Explicit Conversational Correction Handling
@pytest.mark.asyncio
async def test_explicit_conversational_correction():
    """When farmer explicitly corrects previous information, the field is updated and conflict logged."""
    session_id = "test_sess_correction_handling"
    ConversationManager.reset_session(session_id)
    session = ConversationManager.get_or_create_session(session_id)

    # Stated 5 acres initially
    session.profile.land_area.value_acres = 5.0
    session.profile.set_field_value("land_area.value_acres", 5.0, status="confirmed")

    # Farmer corrects: "ನನ್ನದು 5 ಎಕರೆ ಅಲ್ಲ, 2 ಎಕರೆ"
    mock_extracted = ExtractedFarmerInfo(
        land_area=2.0,
        land_unit="acre",
        land_area_acres=2.0,
        is_correction=True,
        corrected_fields=["land_area"]
    )

    with patch.object(LLMService, "extract_farmer_profile_with_gemini", AsyncMock(return_value=mock_extracted)):
        res = await ConversationManager.process_message(
            session_id=session_id,
            message="ನನ್ನದು 5 ಎಕರೆ ಅಲ್ಲ 2 ಎಕರೆ",
            language="kn"
        )
        # Land area must be corrected to 2.0
        assert res.updated_profile.land_area.value_acres == 2.0
        assert "land_area.value_acres" in res.updated_profile.conflict_fields
        conflicts = res.updated_profile.conflict_fields["land_area.value_acres"]
        assert len(conflicts) > 0
        assert conflicts[0]["old_value"] == 5.0
        assert conflicts[0]["new_value"] == 2.0

# 6. Multiple Crops Extraction
@pytest.mark.asyncio
async def test_multiple_crops_extraction():
    """Verify that multiple crops mentioned are parsed and accumulated properly."""
    session_id = "test_sess_multiple_crops"
    ConversationManager.reset_session(session_id)

    mock_extracted = ExtractedFarmerInfo(
        crops=["arecanut", "coconut", "paddy"],
        is_correction=False
    )

    with patch.object(LLMService, "extract_farmer_profile_with_gemini", AsyncMock(return_value=mock_extracted)):
        res = await ConversationManager.process_message(
            session_id=session_id,
            message="ನಾನು ಅಡಿಕೆ, ತೆಂಗು ಮತ್ತು ಭತ್ತ ಬೆಳೆಯುತ್ತೇನೆ",
            language="kn"
        )
        assert len(res.updated_profile.crops) >= 3
        assert "arecanut" in res.updated_profile.crops
        assert "coconut" in res.updated_profile.crops
        assert "paddy" in res.updated_profile.crops

# 7. Strict Eligibility Separation
@pytest.mark.asyncio
async def test_strict_eligibility_engine_independence():
    """
    CRITICAL: Gemini must NEVER override rule engine results.
    Even if Gemini generates a response claiming eligibility, the structured
    recommendations in ChatResponse MUST strictly follow the deterministic rule engine.
    """
    session_id = "test_sess_eligibility_independence"
    ConversationManager.reset_session(session_id)
    session = ConversationManager.get_or_create_session(session_id)

    # Set farmer as tenant farmer (PM-KISAN requires owned landholder)
    session.profile.ownership = "tenant"
    session.profile.crops = ["paddy"]
    session.profile.land_area.value_acres = 2.0
    session.profile.location.district = "Mandya"

    # Mock Gemini hallucinating that tenant farmer is eligible
    mock_hallucinated_response = {
        "kannada": "ನೀವು ಪಿಎಂ-ಕಿಸಾನ್ ಯೋಜನೆಗೆ ಸಂಪೂರ್ಣ ಅರ್ಹರಾಗಿದ್ದೀರಿ! (Hallucination)",
        "english": "You are fully eligible for PM-KISAN! (Hallucination)",
        "explained_schemes": ["pm-kisan"]
    }

    with patch.object(LLMService, "_call_gemini_grounded", AsyncMock(return_value=mock_hallucinated_response)):
        with patch.object(settings, "DEMO_MODE", False):
            with patch.object(settings, "GEMINI_API_KEY", "mock_key"):
                res = await ConversationManager.process_message(
                    session_id=session_id,
                    message="ನಾನು ಗುತ್ತಿಗೆ ರೈತ, ನನಗೆ ಪಿಎಂ ಕಿಸಾನ್ ಸಿಗುತ್ತದೆಯೇ?",
                    language="kn"
                )

                # Find PM-KISAN in recommendations
                pmkisan_match = next((r for r in res.recommendations if r.scheme.id == "pm-kisan"), None)
                assert pmkisan_match is not None

                # CRITICAL ASSERTION: The rule engine MUST mark PM-KISAN as NOT_SUITABLE_BASED_ON_KNOWN_RULES
                # regardless of whatever the LLM text said!
                assert pmkisan_match.evaluation_status == SchemeStatus.NOT_SUITABLE_BASED_ON_KNOWN_RULES
                assert any(r.field == "ownership" and r.status.value == "NOT_SATISFIED" for r in pmkisan_match.unsatisfied_rules)

# 8. Chat Endpoint Live Metadata
def test_chat_api_response_metadata():
    """Verify that the FastAPI chat endpoint returns llm_provider and fallback indicators."""
    payload = {
        "message": "ನನ್ನ ಬಳಿ 4 ಎಕರೆ ಜಮೀನಿದೆ",
        "language": "kn"
    }
    resp = client.post("/api/chat", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "llm_provider" in data
    assert "is_fallback" in data
    assert data["llm_provider"] in ["gemini-live", "demo-deterministic"]
    assert "updated_profile" in data
    assert "recommendations" in data
