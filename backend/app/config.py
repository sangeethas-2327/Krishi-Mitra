from pathlib import Path
from typing import List, Union
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    _base_dir = Path(__file__).resolve().parents[1]
    _root_dir = Path(__file__).resolve().parents[2]

    model_config = SettingsConfigDict(
        env_file=[
            _base_dir / ".env",
            _root_dir / ".env",
            Path.cwd() / ".env",
            Path.cwd() / "backend" / ".env"
        ],
        env_file_encoding="utf-8",
        extra="ignore"
    )

    APP_NAME: str = "Krishi Mitra (ಕೃಷಿ ಮಿತ್ರ)"
    TAGLINE: str = "Your Voice. Our Support. Government Schemes Made Simple."
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    
    # AI & Speech Provider Keys
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.5-flash"
    OPENAI_API_KEY: str = ""
    SARVAM_API_KEY: str = ""
    SARVAM_BASE_URL: str = "https://api.sarvam.ai"
    SARVAM_STT_MODEL: str = "saaras:v2"
    SARVAM_TTS_MODEL: str = "bulbul:v1"
    SARVAM_TTS_SPEAKER: str = "meera"
    AUTO_SYNTHESIZE_SPEECH: bool = True
    
    # Mode Settings
    DEMO_MODE: bool = True
    
    # Server & Security
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    CORS_ORIGINS: Union[List[str], str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "*"
    ]
    MAX_AUDIO_UPLOAD_SIZE_MB: int = 15

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v):
        if isinstance(v, str):
            if v.startswith("[") and v.endswith("]"):
                import json
                try:
                    return json.loads(v)
                except Exception:
                    pass
            return [i.strip() for i in v.split(",") if i.strip()]
        elif isinstance(v, list):
            return v
        return ["*"]

settings = Settings()
