import math
import wave
import struct
import base64
import io
import logging
import httpx
from typing import Optional
from ..config import settings
from ..models.conversation import SynthesizeResponse

logger = logging.getLogger(__name__)

class TextToSpeechService:
    @classmethod
    async def synthesize(cls, text: str, language: str = "kn") -> SynthesizeResponse:
        """
        Synthesizes speech into playable audio using Sarvam AI Bulbul model
        if SARVAM_API_KEY is configured. Otherwise generates a valid playable WAV audio
        chime and signals browser speech synthesis.
        """
        api_key = settings.SARVAM_API_KEY.strip()
        clean_text = text.strip()

        # 1. Live Sarvam AI TTS (Bulbul)
        if api_key and not settings.DEMO_MODE:
            try:
                url = f"{settings.SARVAM_BASE_URL.rstrip('/')}/text-to-speech"
                headers = {
                    "api-subscription-key": api_key,
                    "Content-Type": "application/json"
                }
                payload = {
                    "inputs": [clean_text[:500]],  # Safe limit per request chunk
                    "target_language_code": "kn-IN" if language == "kn" else "en-IN",
                    "speaker": settings.SARVAM_TTS_SPEAKER,
                    "model": settings.SARVAM_TTS_MODEL,
                    "pace": 1.0,
                    "speech_sample_rate": 22050,
                    "enable_preprocessing": True
                }

                async with httpx.AsyncClient(timeout=25.0, verify=False) as client:
                    resp = await client.post(url, headers=headers, json=payload)
                    if resp.status_code == 200:
                        res_json = resp.json()
                        audios = res_json.get("audios", [])
                        if audios and len(audios) > 0:
                            base64_audio = audios[0]
                            # Detect or format base64 URI
                            audio_uri = base64_audio if base64_audio.startswith("data:") else f"data:audio/wav;base64,{base64_audio}"
                            return SynthesizeResponse(
                                audio_base64=audio_uri,
                                audio_url=None,
                                format="audio/wav",
                                duration_seconds=max(2.0, len(clean_text) * 0.08),
                                provider="sarvam_bulbul",
                                live=True
                            )
                    else:
                        logger.warning(f"Sarvam AI TTS returned status {resp.status_code}: {resp.text}")
            except Exception as e:
                logger.error(f"Sarvam AI TTS request failed: {e}")

        # 2. Demo Mode Playable WAV Generation (Valid 16-bit PCM Audio Chime)
        wav_base64 = cls._generate_harmonic_audio()
        return SynthesizeResponse(
            audio_base64=wav_base64,
            audio_url=None,
            format="audio/wav",
            duration_seconds=1.2,
            provider="demo_harmonic_synth",
            live=False
        )

    @classmethod
    def _generate_harmonic_audio(cls) -> str:
        """
        Generates a valid, pure-Python 16-bit PCM WAV audio chime (523Hz -> 659Hz)
        that browsers can play directly without external assets.
        """
        sample_rate = 22050
        duration = 1.0  # seconds
        num_samples = int(sample_rate * duration)
        
        buffer = io.BytesIO()
        with wave.open(buffer, "wb") as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 16-bit
            wav_file.setframerate(sample_rate)

            samples = []
            for i in range(num_samples):
                t = i / sample_rate
                # Envelope: smooth rise and decay
                envelope = math.sin(math.pi * (i / num_samples))
                # Harmonic frequency chord (Agricultural calm tone)
                freq = 523.25 if t < 0.5 else 659.25
                val = int(32767.0 * 0.4 * envelope * math.sin(2.0 * math.pi * freq * t))
                samples.append(struct.pack("<h", max(-32768, min(32767, val))))

            wav_file.writeframes(b"".join(samples))

        raw_bytes = buffer.getvalue()
        b64 = base64.b64encode(raw_bytes).decode("ascii")
        return f"data:audio/wav;base64,{b64}"
