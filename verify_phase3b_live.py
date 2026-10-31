#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Krishi Mitra Phase 3B Live End-to-End Voice Verification Script
Tests real HTTP endpoints against the running FastAPI backend and Vite frontend.
"""

import sys
import json
import httpx

BACKEND_URL = "http://127.0.0.1:8000"
FRONTEND_URL = "http://localhost:5173"

def create_dummy_wav(size_bytes: int = 120) -> bytes:
    return b"RIFF" + b"\x00" * (size_bytes - 4)

def main():
    print("=" * 70)
    print("KRISHI MITRA PHASE 3B LIVE VOICE INTERACTION VERIFICATION")
    print("=" * 70)

    client = httpx.Client(timeout=15.0)
    passed_tests = 0
    total_tests = 0

    # 1. Frontend Vite Server Check
    total_tests += 1
    try:
        r_fe = client.get(FRONTEND_URL)
        if r_fe.status_code == 200:
            print(f"[PASS] 1. Frontend Vite Server is running at {FRONTEND_URL} (Status 200)")
            passed_tests += 1
        else:
            print(f"[FAIL] 1. Frontend returned status {r_fe.status_code}")
    except Exception as e:
        print(f"[FAIL] 1. Could not connect to Frontend: {e}")

    # 2. Backend Health & Voice Provider Metadata
    total_tests += 1
    try:
        r_health = client.get(f"{BACKEND_URL}/api/health")
        if r_health.status_code == 200:
            h = r_health.json()
            assert h.get("status") == "healthy"
            assert "voice_provider" in h
            assert "sarvam_models" in h
            print(f"[PASS] 2. Backend Health Check: voice_provider='{h['voice_provider']}', STT='{h['sarvam_models']['stt']}', TTS='{h['sarvam_models']['tts']}'")
            passed_tests += 1
        else:
            print(f"[FAIL] 2. Backend Health failed: {r_health.status_code}")
    except Exception as e:
        print(f"[FAIL] 2. Backend Health exception: {e}")

    # 3. Audio Transcription Endpoint (WAV)
    total_tests += 1
    try:
        files = {"file": ("farmer_voice.wav", create_dummy_wav(200), "audio/wav")}
        r_trans = client.post(f"{BACKEND_URL}/api/voice/transcribe", files=files)
        if r_trans.status_code == 200:
            d = r_trans.json()
            assert "transcript" in d
            assert d.get("detected_language") == "kn"
            assert "provider_metadata" in d
            print(f"[PASS] 3. Audio Transcription (WAV): transcript='{d['transcript']}', provider='{d['provider_metadata']['provider']}'")
            passed_tests += 1
        else:
            print(f"[FAIL] 3. Audio transcription failed with status {r_trans.status_code}")
    except Exception as e:
        print(f"[FAIL] 3. Audio transcription exception: {e}")

    # 4. Audio Transcription Endpoint (WebM Browser Recording)
    total_tests += 1
    try:
        files = {"file": ("recording.webm", b"\x1a\x45\xdf\xa3" + b"\x00" * 120, "audio/webm")}
        r_webm = client.post(f"{BACKEND_URL}/api/voice/transcribe", files=files)
        if r_webm.status_code == 200:
            d = r_webm.json()
            assert "transcript" in d
            print(f"[PASS] 4. Audio Transcription (WebM): Successfully parsed browser recording")
            passed_tests += 1
        else:
            print(f"[FAIL] 4. WebM audio transcription failed: {r_webm.status_code}")
    except Exception as e:
        print(f"[FAIL] 4. WebM transcription exception: {e}")

    # 5. Speech Synthesis Endpoint (Kannada TTS)
    total_tests += 1
    try:
        synth_payload = {"text": "ನಮಸ್ಕಾರ, ಕೃಷಿ ಮಿತ್ರಗೆ ಸ್ವಾಗತ.", "language": "kn"}
        r_synth = client.post(f"{BACKEND_URL}/api/voice/synthesize", json=synth_payload)
        if r_synth.status_code == 200:
            d = r_synth.json()
            assert "audio_base64" in d
            assert d["audio_base64"].startswith("data:audio/wav;base64,")
            print(f"[PASS] 5. Speech Synthesis Endpoint: Generated {d['format']} audio (provider: {d['provider']})")
            passed_tests += 1
        else:
            print(f"[FAIL] 5. Speech synthesis failed: {r_synth.status_code}")
    except Exception as e:
        print(f"[FAIL] 5. Speech synthesis exception: {e}")

    # 6. End-to-End Voice Journey: Transcribe -> Chat with Pre-Synthesized Audio
    total_tests += 1
    try:
        session_id = "live_phase3b_journey"
        chat_payload = {
            "session_id": session_id,
            "message": "ನನಗೆ ಕೃಷಿಗೆ ಸಹಾಯಧನ ಬೇಕು. ನಾನು 3 ಎಕರೆ ಅಡಿಕೆ ಬೆಳೆಯುತ್ತೇನೆ.",
            "language": "kn"
        }
        r_chat = client.post(f"{BACKEND_URL}/api/chat", json=chat_payload)
        if r_chat.status_code == 200:
            d = r_chat.json()
            assert "audio_base64" in d and d["audio_base64"] is not None
            assert d["audio_base64"].startswith("data:audio/wav;base64,")
            assert "arecanut" in d["updated_profile"]["crops"]
            print(f"[PASS] 6. End-to-End Voice Journey: Chat response returned pre-synthesized audio for immediate playback!")
            print(f"       Audio Data URI length: {len(d['audio_base64'])} characters")
            passed_tests += 1
        else:
            print(f"[FAIL] 6. End-to-end voice journey failed: {r_chat.status_code}")
    except Exception as e:
        print(f"[FAIL] 6. End-to-end voice journey exception: {e}")

    # 7. Edge Case: Empty Audio Rejection
    total_tests += 1
    try:
        r_empty = client.post(f"{BACKEND_URL}/api/voice/transcribe", files={"file": ("empty.wav", b"", "audio/wav")})
        if r_empty.status_code == 400:
            print(f"[PASS] 7. Audio Validation: Correctly rejected 0-byte audio with HTTP 400")
            passed_tests += 1
        else:
            print(f"[FAIL] 7. Empty audio returned status {r_empty.status_code}")
    except Exception as e:
        print(f"[FAIL] 7. Empty audio exception: {e}")

    # 8. Edge Case: Empty Text Synthesis Rejection
    total_tests += 1
    try:
        r_empty_txt = client.post(f"{BACKEND_URL}/api/voice/synthesize", json={"text": "   ", "language": "kn"})
        if r_empty_txt.status_code == 400:
            print(f"[PASS] 8. Synthesis Validation: Correctly rejected empty text with HTTP 400")
            passed_tests += 1
        else:
            print(f"[FAIL] 8. Empty text synthesis returned status {r_empty_txt.status_code}")
    except Exception as e:
        print(f"[FAIL] 8. Empty text synthesis exception: {e}")

    print("=" * 70)
    print(f"PHASE 3B LIVE VERIFICATION SUMMARY: {passed_tests}/{total_tests} tests passed.")
    print("=" * 70)

    if passed_tests == total_tests:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

