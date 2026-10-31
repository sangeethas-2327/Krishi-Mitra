from typing import Optional, List, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field
from .farmer import FarmerProfile, FarmerProfileUpdate
from .scheme import SchemeMatchResult

class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class ChatMessage(BaseModel):
    id: str
    role: MessageRole
    content: str
    audio_url: Optional[str] = None
    created_at: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    message: str
    language: str = "kn"  # "kn" (Kannada) or "en" (English)
    corrected_fields: Optional[Dict[str, Any]] = None

class ChatResponse(BaseModel):
    session_id: str
    response_text: str
    response_text_kn: Optional[str] = None
    response_text_en: Optional[str] = None
    audio_url: Optional[str] = None
    audio_base64: Optional[str] = None
    voice_provider: Optional[str] = None
    updated_profile: FarmerProfile
    next_question: Optional[str] = None
    next_question_kn: Optional[str] = None
    conversation_status: str = "in_progress"  # in_progress, awaiting_clarification, ready_with_recommendations
    recommendations: List[SchemeMatchResult] = Field(default_factory=list)
    source_references: List[str] = Field(default_factory=list)
    uncertainty_notes: List[str] = Field(default_factory=list)
    llm_provider: str = "demo-deterministic"  # "gemini-live" or "demo-deterministic"
    is_fallback: bool = False
    explained_schemes: List[str] = Field(default_factory=list)

class TranscribeResponse(BaseModel):
    transcript: str
    detected_language: str = "kn"
    language_code: Optional[str] = "kn-IN"
    confidence: float = 1.0
    duration_seconds: Optional[float] = None
    provider_metadata: Dict[str, Any] = Field(default_factory=dict)

class SynthesizeRequest(BaseModel):
    text: str
    language: str = "kn"
    voice_id: Optional[str] = None

class SynthesizeResponse(BaseModel):
    audio_base64: Optional[str] = None
    audio_url: Optional[str] = None
    format: str = "audio/wav"
    duration_seconds: Optional[float] = None
    provider: str = "mock"
    live: bool = False
    format: str = "audio/wav"
    duration_seconds: Optional[float] = None
    provider: str = "mock"
