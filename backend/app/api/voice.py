from fastapi import APIRouter, UploadFile, File, HTTPException
from ..models.conversation import TranscribeResponse, SynthesizeRequest, SynthesizeResponse
from ..services.speech_to_text import SpeechToTextService
from ..services.text_to_speech import TextToSpeechService
from ..config import settings

router = APIRouter(prefix="/api/voice", tags=["voice"])

@router.post("/transcribe", response_model=TranscribeResponse)
async def transcribe_audio(file: UploadFile = File(...)):
    # Validate content type / extension
    allowed_types = ["audio/wav", "audio/wave", "audio/x-wav", "audio/webm", "audio/ogg", "audio/mpeg", "audio/mp4", "audio/m4a", "audio/aac"]
    if file.content_type and file.content_type.lower() not in allowed_types:
        # Fallback check file extension
        if not any(file.filename.lower().endswith(ext) for ext in [".wav", ".webm", ".ogg", ".mp3", ".m4a"]):
            raise HTTPException(status_code=400, detail=f"Unsupported audio type: {file.content_type}")

    file_bytes = await file.read()
    max_bytes = settings.MAX_AUDIO_UPLOAD_SIZE_MB * 1024 * 1024
    if len(file_bytes) > max_bytes:
        raise HTTPException(status_code=413, detail=f"Audio file exceeds maximum size of {settings.MAX_AUDIO_UPLOAD_SIZE_MB}MB.")

    if len(file_bytes) == 0:
        raise HTTPException(status_code=400, detail="Empty audio recording submitted.")

    try:
        res = await SpeechToTextService.transcribe(file_bytes, file.filename or "audio.wav")
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")

@router.post("/synthesize", response_model=SynthesizeResponse)
async def synthesize_speech(request: SynthesizeRequest):
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Text for speech synthesis cannot be empty.")

    try:
        res = await TextToSpeechService.synthesize(request.text, request.language)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Speech synthesis failed: {str(e)}")
