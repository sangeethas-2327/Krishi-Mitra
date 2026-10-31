import io
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"
    assert "Krishi Mitra" in data["app_name"]

def test_list_schemes():
    res = client.get("/api/schemes")
    assert res.status_code == 200
    data = res.json()
    assert len(data) >= 5
    ids = [s["id"] for s in data]
    assert "pm-kisan" in ids
    assert "pmfby" in ids
    assert "demo-micro-irrigation" in ids

def test_get_scheme_by_id():
    res = client.get("/api/schemes/pm-kisan")
    assert res.status_code == 200
    data = res.json()
    assert data["id"] == "pm-kisan"
    assert data["scheme_type"] == "real"
    assert len(data["eligibility_rules"]) > 0

def test_compare_schemes_api():
    # GET comparison
    res_get = client.get("/api/schemes/compare?ids=pm-kisan,pmfby")
    assert res_get.status_code == 200
    data_get = res_get.json()
    assert len(data_get["schemes"]) == 2
    assert "purpose" in data_get["comparison_matrix"]

    # POST comparison
    res_post = client.post("/api/schemes/compare", json=["pm-kisan", "demo-micro-irrigation"])
    assert res_post.status_code == 200
    data_post = res_post.json()
    assert len(data_post["schemes"]) == 2
    assert "pm-kisan" in data_post["comparison_matrix"]["purpose"]

def test_scheme_checklist_api():
    res = client.get("/api/schemes/pm-kisan/checklist")
    assert res.status_code == 200
    data = res.json()
    assert data["scheme_id"] == "pm-kisan"
    assert len(data["items"]) >= 4
    assert "disclaimer" in data
    assert "does NOT submit applications" in data["disclaimer"]

def test_chat_endpoint_e2e():
    payload = {
        "session_id": "test-api-session-1",
        "message": "ನನಗೆ ಕೃಷಿಗೆ ಸಹಾಯಧನ ಬೇಕು. ನಾನು ಮೂರು ಎಕರೆ ಅಡಿಕೆ ಬೆಳೆಯುತ್ತೇನೆ.",
        "language": "kn"
    }
    res = client.post("/api/chat", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["session_id"] == "test-api-session-1"
    assert data["updated_profile"]["land_area"]["value_acres"] == 3.0
    assert "arecanut" in data["updated_profile"]["crops"]
    assert len(data["recommendations"]) > 0

def test_voice_synthesize_endpoint():
    payload = {
        "text": "ನಮಸ್ಕಾರ, ನಿಮ್ಮ ವಿವರಗಳನ್ನು ದಾಖಲಿಸಿಕೊಳ್ಳಲಾಗಿದೆ.",
        "language": "kn"
    }
    res = client.post("/api/voice/synthesize", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["audio_base64"] is not None
    assert data["audio_base64"].startswith("data:audio/wav;base64,")

def test_voice_transcribe_endpoint():
    # Submit a dummy WAV file
    fake_wav = io.BytesIO(b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xac\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00")
    files = {"file": ("audio.wav", fake_wav, "audio/wav")}
    res = client.post("/api/voice/transcribe", files=files)
    assert res.status_code == 200
    data = res.json()
    assert "transcript" in data
    assert len(data["transcript"]) > 0

def test_profile_patch_and_reset():
    session_id = "test-patch-session"
    # 1. Patch profile with Phase 2 fields (taluk, irrigation, etc.)
    patch_payload = {
        "location": {"district": "Hassan", "taluk": "Belur"},
        "ownership": "owned",
        "irrigation": {"source": "borewell"}
    }
    res = client.patch(f"/api/farmer/profile?session_id={session_id}", json=patch_payload)
    assert res.status_code == 200
    p = res.json()
    assert p["location"]["district"] == "Hassan"
    assert p["location"]["taluk"] == "Belur"
    assert p["ownership"] == "owned"
    assert p["irrigation"]["source"] == "borewell"

    # 2. Reset session
    reset_res = client.post("/api/session/reset", json={"session_id": session_id})
    assert reset_res.status_code == 200

    # 3. Verify reset
    check_res = client.get(f"/api/farmer/profile?session_id={session_id}")
    p_reset = check_res.json()
    assert p_reset["location"]["district"] is None

def test_sarvam_proxy_missing_key_behavior(monkeypatch):
    from app.config import settings
    # Test proxy intercepts and requires SARVAM_API_KEY if unset
    monkeypatch.setattr(settings, "SARVAM_API_KEY", "")
    res = client.get("/api/sarvam/orgs/test/url")
    assert res.status_code == 401
    assert "SARVAM_API_KEY is not set" in res.json()["detail"]

def test_sarvam_proxy_forwarding_headers(monkeypatch):
    from app.config import settings
    import httpx
    
    monkeypatch.setattr(settings, "SARVAM_API_KEY", "test-secret-key-12345")
    
    captured_headers = {}
    
    async def mock_request(self, method, url, headers=None, **kwargs):
        captured_headers.update(headers or {})
        return httpx.Response(200, json={"url": "wss://apps.sarvam.ai/test", "reference_id": "ref-123"})
        
    monkeypatch.setattr(httpx.AsyncClient, "request", mock_request)
    
    res = client.get("/api/sarvam/orgs/my-org/workspaces/my-ws/apps/my-app/url?interaction_type=call")
    assert res.status_code == 200
    assert res.json()["reference_id"] == "ref-123"
    assert captured_headers.get("X-API-Key") == "test-secret-key-12345"
    assert captured_headers.get("api-subscription-key") == "test-secret-key-12345"

def test_mandi_prices_endpoints():
    # 1. Fetch all mandi prices
    res = client.get("/api/mandi")
    assert res.status_code == 200
    data = res.json()
    assert data["total_records"] > 0
    assert len(data["prices"]) > 0
    assert "KSAMB" in data["source"]

    # 2. Filter by district
    res_dist = client.get("/api/mandi?district=Mandya")
    assert res_dist.status_code == 200
    data_dist = res_dist.json()
    assert data_dist["total_records"] > 0
    for p in data_dist["prices"]:
        assert "mandya" in p["district"].lower()

    # 3. Filter by crop
    res_crop = client.get("/api/mandi?commodity=Ragi")
    assert res_crop.status_code == 200
    data_crop = res_crop.json()
    assert data_crop["total_records"] > 0
    for p in data_crop["prices"]:
        assert "ragi" in p["commodity"].lower()

    # 4. Commodities list
    res_comms = client.get("/api/mandi/commodities")
    assert res_comms.status_code == 200
    comms = res_comms.json()
    assert len(comms) > 0
    assert any(c["name_en"] == "Ragi" for c in comms)

    # 5. Markets list
    res_mkts = client.get("/api/mandi/markets")
    assert res_mkts.status_code == 200
    mkts = res_mkts.json()
    assert len(mkts) > 0
    assert any("Mandya" in m["market"] for m in mkts)


