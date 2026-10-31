#!/usr/bin/env python3
"""
Krishi Mitra — Cloud API Smoke Test & Credential Verification Suite
Phase 5B: Live API Activation & Offline Fallback Integrity Verification.

Performs live smoke-tests against Google Gemini and Sarvam AI when credentials exist.
If credentials are not configured, cleanly reports the unconfigured state, verifies
the fallback demo engine, and guarantees zero key exposure or simulated false passes.
"""

import os
import sys
import time
import asyncio
from pathlib import Path

# Fix Windows console UTF-8 output encoding for Kannada script
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# Ensure backend root is on sys.path
backend_path = Path(__file__).resolve().parent / "backend"
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))

from app.config import settings
from app.services.llm_service import LLMService
from app.services.speech_to_text import SpeechToTextService
from app.services.text_to_speech import TextToSpeechService
from app.models.farmer import FarmerProfile


def mask_key(key: str) -> str:
    if not key or len(key.strip()) < 8:
        return "[NOT_CONFIGURED]"
    k = key.strip()
    return f"{k[:4]}...{k[-4:]}"


async def test_gemini_smoke():
    print("\n--- 1. GOOGLE GEMINI SMOKE TEST ---")
    gemini_key = os.getenv("GEMINI_API_KEY") or settings.GEMINI_API_KEY
    model_name = os.getenv("GEMINI_MODEL") or settings.GEMINI_MODEL

    print(f"Configured Model : {model_name}")
    print(f"API Key Masked   : {mask_key(gemini_key)}")

    client = LLMService.get_client(gemini_key)
    
    if not client:
        print("[STATUS] GEMINI_API_KEY is not configured in backend/.env or environment.")
        print("[FALLBACK VERIFICATION] Testing offline deterministic Kannada explanation generator...")
        t0 = time.perf_counter()
        
        # Test fallback explanation generator
        explanation = await LLMService.generate_response(
            user_message="ನನಗೆ ಕೃಷಿ ಸಹಾಯಧನ ಬೇಕು",
            profile=FarmerProfile(),
            recommendations=[],
            next_question_en=None,
            next_question_kn=None,
            language="kn"
        )
        elapsed = (time.perf_counter() - t0) * 1000
        print(f"[PASS] Offline explanation generator responded in {elapsed:.1f}ms:")
        print(f"       Kannada Text: '{explanation.get('kannada', '')[:90]}...'")
        print("       (Note: Demo mode operational. To activate live Gemini, set GEMINI_API_KEY in backend/.env)")
        return "DEMO_FALLBACK"

    print("[STATUS] GEMINI_API_KEY detected. Initiating real cloud call to Google Gemini API...")
    t0 = time.perf_counter()
    try:
        from google.genai import types
        # Test minimal smoke call to Google Gemini
        response = await asyncio.to_thread(
            client.models.generate_content,
            model=model_name,
            contents="ದಯವಿಟ್ಟು ಒಂದು ಚಿಕ್ಕ ವಾಕ್ಯದಲ್ಲಿ ಕನ್ನಡದಲ್ಲಿ ನಮಸ್ಕಾರ ತಿಳಿಸಿ (Reply with a brief Kannada greeting)."
        )
        elapsed = (time.perf_counter() - t0) * 1000
        output_text = response.text.strip() if hasattr(response, "text") else str(response)
        print(f"[PASS] Real Gemini API call succeeded in {elapsed:.1f}ms!")
        print(f"       Model: {model_name}")
        print(f"       Live Kannada Response: '{output_text[:120]}'")
        return "LIVE_CLOUD_SUCCESS"
    except Exception as e:
        print(f"[FAIL] Real Gemini API call failed with error: {str(e)}")
        return "LIVE_CLOUD_FAILED"


async def test_sarvam_smoke():
    print("\n--- 2. SARVAM AI (SAARAS & BULBUL) SMOKE TEST ---")
    sarvam_key = os.getenv("SARVAM_API_KEY") or settings.SARVAM_API_KEY
    stt_model = os.getenv("SARVAM_STT_MODEL") or settings.SARVAM_STT_MODEL
    tts_model = os.getenv("SARVAM_TTS_MODEL") or settings.SARVAM_TTS_MODEL

    print(f"STT Model        : {stt_model}")
    print(f"TTS Model        : {tts_model}")
    print(f"API Key Masked   : {mask_key(sarvam_key)}")

    if not sarvam_key.strip():
        print("[STATUS] SARVAM_API_KEY is not configured in backend/.env or environment.")
        print("[FALLBACK VERIFICATION] Testing offline voice synthesis chime & demo recognizer...")
        
        # Test offline TTS synthesis
        t0 = time.perf_counter()
        synth_res = await TextToSpeechService.synthesize("ನಮಸ್ಕಾರ, ಕೃಷಿ ಮಿತ್ರ", language="kn")
        elapsed_tts = (time.perf_counter() - t0) * 1000
        
        # Test offline STT transcription
        dummy_wav = b"RIFF" + b"\x00" * 40
        stt_res = await SpeechToTextService.transcribe(dummy_wav, filename="audio.wav", language_code="kn-IN")
        
        print(f"[PASS] Offline TTS synthesized {len(synth_res.audio_base64 or '')} chars in {elapsed_tts:.1f}ms.")
        print(f"[PASS] Offline STT produced transcript: '{stt_res.transcript}' (confidence: {stt_res.confidence})")
        print("       (Note: Demo mode operational. To activate live Sarvam AI, set SARVAM_API_KEY in backend/.env)")
        return "DEMO_FALLBACK"

    print("[STATUS] SARVAM_API_KEY detected. Initiating real cloud call to Sarvam Bulbul TTS...")
    t0 = time.perf_counter()
    try:
        synth_res = await TextToSpeechService.synthesize("ನಮಸ್ಕಾರ, ನಾನು ಕೃಷಿ ಮಿತ್ರ", language="kn")
        elapsed_tts = (time.perf_counter() - t0) * 1000
        if synth_res.provider == "sarvam_bulbul":
            print(f"[PASS] Real Sarvam Bulbul TTS succeeded in {elapsed_tts:.1f}ms!")
            print(f"       Provider: {synth_res.provider}, Audio payload chars: {len(synth_res.audio_base64 or '')}")
            return "LIVE_CLOUD_SUCCESS"
        else:
            print(f"[INFO] Sarvam returned fallback chime (provider: {synth_res.provider})")
            return "FALLBACK_USED"
    except Exception as e:
        print(f"[FAIL] Real Sarvam API call failed with error: {str(e)}")
        return "LIVE_CLOUD_FAILED"


async def main():
    print("=" * 80)
    print("KRISHI MITRA — PHASE 5B CLOUD API & FALLBACK SMOKE TEST")
    print("=" * 80)
    gemini_status = await test_gemini_smoke()
    sarvam_status = await test_sarvam_smoke()
    print("\n" + "=" * 80)
    print("SMOKE TEST SUMMARY:")
    print(f"  * Gemini Status : {gemini_status}")
    print(f"  * Sarvam Status : {sarvam_status}")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
