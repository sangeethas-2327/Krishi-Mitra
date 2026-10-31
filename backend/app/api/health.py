from fastapi import APIRouter
from ..config import settings

router = APIRouter(prefix="/api", tags=["health"])

@router.get("/health")
def get_health():
    api_key_configured = bool(settings.GEMINI_API_KEY.strip())
    is_live_gemini = api_key_configured and not settings.DEMO_MODE
    sarvam_configured = bool(settings.SARVAM_API_KEY.strip())
    is_live_sarvam = sarvam_configured and not settings.DEMO_MODE
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "demo_mode": settings.DEMO_MODE,
        "llm_provider": "gemini-live" if is_live_gemini else "demo-deterministic",
        "gemini_model": settings.GEMINI_MODEL,
        "voice_provider": "sarvam-live" if is_live_sarvam else "demo-synthetic",
        "sarvam_models": {
            "stt": settings.SARVAM_STT_MODEL,
            "tts": settings.SARVAM_TTS_MODEL,
            "speaker": settings.SARVAM_TTS_SPEAKER
        },
        "providers": {
            "gemini": api_key_configured,
            "sarvam": sarvam_configured
        }
    }
