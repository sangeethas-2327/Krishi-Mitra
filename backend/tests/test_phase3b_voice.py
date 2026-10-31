import io
import json
import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from fastapi.testclient import TestClient

from app.main import app
from app.config import settings
from app.models.scheme import SchemeStatus
from app.services.speech_to_text import SpeechToTextService
from app.services.text_to_speech import TextToSpeechService
from app.services.conversation_manager import ConversationManager

client = TestClient(app)

def create_dummy_wav(size_bytes: int = 100) -> bytes:
    """Creates dummy bytes for audio testing."""
    return b"RIFF" + b"\x00" * (size_bytes - 4)

# 1. Audio Upload Validation Tests
def test_transcribe_empty_audio_fails():
    """Empty audio recording should return HTTP 400."""
    files = {"file": ("empty.wav", b"", "audio/wav")}
    resp = client.post("/api/voice/transcribe", files=files)
    assert resp.status_code == 400
    assert "Empty audio" in resp.json()["detail"]

def test_transcribe_unsupported_format_fails():
    """Unsupported non-audio format should return HTTP 400."""
    files = {"file": ("document.pdf", b"%PDF-1.4 dummy", "application/pdf")}
    resp = client.post("/api/voice/transcribe", files=files)
    assert resp.status_code == 400
    assert "Unsupported audio type" in resp.json()["detail"]

def test_transcribe_large_audio_fails():
    """Audio exceeding max allowed size should return HTTP 413."""
    with patch.object(settings, "MAX_AUDIO_UPLOAD_SIZE_MB", 1):
        big_bytes = b"RIFF" + b"\x00" * (2 * 1024 * 1024)  # 2MB > 1MB limit
        files = {"file": ("large_speech.wav", big_bytes, "audio/wav")}
        resp = client.post("/api/voice/transcribe", files=files)
        assert resp.status_code == 413
        assert "exceeds maximum size" in resp.json()["detail"]

# 2. Transcription with Supported Formats (WAV & WebM)
def test_transcribe_supported_wav():
    """Valid WAV recording returns successful structured transcript in demo mode."""
    files = {"file": ("farmer_voice.wav", create_dummy_wav(200), "audio/wav")}
    resp = client.post("/api/voice/transcribe", files=files)
    assert resp.status_code == 200
    data = resp.json()
    assert "transcript" in data
    assert len(data["transcript"]) > 0
    assert data["detected_language"] == "kn"
    assert data["provider_metadata"]["live"] is False

def test_transcribe_supported_webm():
    """Valid WebM browser recording returns successful structured transcript."""
    files = {"file": ("farmer_voice.webm", b"\x1a\x45\xdf\xa3" + b"\x00" * 150, "audio/webm")}
    resp = client.post("/api/voice/transcribe", files=files)
    assert resp.status_code == 200
    data = resp.json()
    assert "transcript" in data
    assert data["language_code"] == "kn-IN"

# 3. Live Sarvam Saaras ASR Integration Mock
@pytest.mark.asyncio
async def test_live_sarvam_saaras_transcription():
    """Tests live Sarvam AI Saaras speech recognition with mock response."""
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "transcript": "ನನಗೆ 3 ಎಕರೆ ಅಡಿಕೆ ತೋಟವಿದೆ",
        "language_code": "kn-IN",
        "duration": 2.8
    }

    with patch.object(settings, "DEMO_MODE", False):
        with patch.object(settings, "SARVAM_API_KEY", "mock_sarvam_key"):
            with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
                mock_post.return_value = mock_resp
                res = await SpeechToTextService.transcribe(
                    file_bytes=create_dummy_wav(250),
                    filename="speech.wav",
                    language_code="kn-IN"
                )
                assert res.transcript == "ನನಗೆ 3 ಎಕರೆ ಅಡಿಕೆ ತೋಟವಿದೆ"
                assert res.provider_metadata["provider"] == "sarvam_ai"
                assert res.provider_metadata["service"] == "saaras"
                assert res.provider_metadata["live"] is True

# 4. Text-to-Speech Synthesis Validation & Bulbul Mock
def test_synthesize_empty_text_fails():
    """Empty text for TTS synthesis should return HTTP 400."""
    resp = client.post("/api/voice/synthesize", json={"text": "", "language": "kn"})
    assert resp.status_code == 400
    assert "cannot be empty" in resp.json()["detail"]

def test_synthesize_demo_audio_chime():
    """Demo TTS generates playable 16-bit PCM WAV audio."""
    resp = client.post("/api/voice/synthesize", json={"text": "ನಮಸ್ಕಾರ", "language": "kn"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["audio_base64"].startswith("data:audio/wav;base64,")
    assert data["provider"] == "demo_harmonic_synth"
    assert data["format"] == "audio/wav"
    assert data["live"] is False

@pytest.mark.asyncio
async def test_live_sarvam_bulbul_synthesis():
    """Tests live Sarvam AI Bulbul speech synthesis with mock response."""
    dummy_audio_b64 = "UklGRigAAABXQVZFZm10IBIAAAABAAEAQB8AAEAfAAABAAgAAABmYWN0BAAAAAAAAABkYXRhAAAAAA=="
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "audios": [dummy_audio_b64]
    }

    with patch.object(settings, "DEMO_MODE", False):
        with patch.object(settings, "SARVAM_API_KEY", "mock_sarvam_key"):
            with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
                mock_post.return_value = mock_resp
                res = await TextToSpeechService.synthesize(
                    text="ನಮಸ್ಕಾರ, ಕೃಷಿ ಮಿತ್ರಗೆ ಸ್ವಾಗತ",
                    language="kn"
                )
                assert res.audio_base64.startswith("data:audio/wav;base64,")
                assert res.provider == "sarvam_bulbul"
                assert res.live is True

# 5. Representative Agricultural Audio Corpus Matching in Demo Mode
@pytest.mark.asyncio
async def test_kannada_agricultural_corpus_scenarios():
    """Verify demo mode provides verified agricultural phrases for representative scenarios."""
    scenarios = [
        ("scenario_1.wav", "ಅಡಿಕೆ ಬೆಳೆಯುತ್ತೇನೆ"),
        ("scenario_2.wav", "ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯಲ್ಲಿದೆ"),
        ("scenario_tenant.wav", "ಗುತ್ತಿಗೆ ರೈತ"),
        ("scenario_irrigation.wav", "ಹನಿ ನೀರಾವರಿಗೆ"),
        ("scenario_correction.wav", "2 ಎಕರೆ ಜಮೀನಿದೆ")
    ]
    for fname, expected_phrase in scenarios:
        res = await SpeechToTextService.transcribe(
            file_bytes=create_dummy_wav(150),
            filename=fname
        )
        assert expected_phrase in res.transcript

# 6. End-to-End Voice Journey with Profile Update, Scheme Match & TTS
@pytest.mark.asyncio
async def test_end_to_end_voice_journey():
    """
    Tests complete voice interaction flow:
    Voice Audio Upload -> Transcription -> ConversationManager -> Gemini/Engine ->
    Profile Update -> Scheme Evaluation -> TTS Audio Generation in ChatResponse.
    """
    session_id = "test_sess_voice_journey"
    ConversationManager.reset_session(session_id)

    # 1. Voice Upload
    audio_file = {"file": ("scenario_1.wav", create_dummy_wav(200), "audio/wav")}
    trans_resp = client.post("/api/voice/transcribe", files=audio_file)
    assert trans_resp.status_code == 200
    transcript = trans_resp.json()["transcript"]
    assert "ಅಡಿಕೆ" in transcript

    # 2. Conversational Processing of Transcript
    chat_payload = {
        "session_id": session_id,
        "message": transcript,
        "language": "kn"
    }
    chat_resp = client.post("/api/chat", json=chat_payload)
    assert chat_resp.status_code == 200
    chat_data = chat_resp.json()

    # 3. Verify Farmer Profile Updated
    assert "arecanut" in chat_data["updated_profile"]["crops"]
    assert chat_data["updated_profile"]["land_area"]["value_acres"] == 3.0

    # 4. Verify Schemes Evaluated
    assert len(chat_data["recommendations"]) > 0

    # 5. Verify Real-time TTS Audio Generated in ChatResponse
    assert chat_data.get("audio_base64") is not None
    assert chat_data["audio_base64"].startswith("data:audio/wav;base64,")

# 7. Consecutive Voice Turns Context Preservation
@pytest.mark.asyncio
async def test_consecutive_voice_turns_context_preservation():
    """Farmer conducts multiple voice dialogue turns without resetting session."""
    session_id = "test_sess_consecutive_voice"
    ConversationManager.reset_session(session_id)

    # Turn 1: Voice Crop & Land
    t1 = await SpeechToTextService.transcribe(create_dummy_wav(100), filename="scenario_1.wav")
    r1 = await ConversationManager.process_message(session_id=session_id, message=t1.transcript, language="kn")
    assert "arecanut" in r1.updated_profile.crops
    assert r1.updated_profile.land_area.value_acres == 3.0

    # Turn 2: Voice District & Ownership
    t2 = await SpeechToTextService.transcribe(create_dummy_wav(100), filename="scenario_2.wav")
    r2 = await ConversationManager.process_message(session_id=session_id, message=t2.transcript, language="kn")
    assert r2.updated_profile.location.district == "Shivamogga"
    assert r2.updated_profile.ownership == "owned"
    # Turn 1 facts must be preserved!
    assert "arecanut" in r2.updated_profile.crops
    assert r2.updated_profile.land_area.value_acres == 3.0

    # Turn 3: Voice Correction
    t3 = await SpeechToTextService.transcribe(create_dummy_wav(100), filename="scenario_correction.wav")
    r3 = await ConversationManager.process_message(session_id=session_id, message=t3.transcript, language="kn")
    assert r3.updated_profile.land_area.value_acres == 2.0
    # Location and crops preserved
    assert r3.updated_profile.location.district == "Shivamogga"
    assert "arecanut" in r3.updated_profile.crops
