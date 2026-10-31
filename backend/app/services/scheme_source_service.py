import json
import logging
from pathlib import Path
from typing import List, Optional
from ..models.scheme import SchemeRecord

logger = logging.getLogger(__name__)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "schemes.json"

class SchemeSourceService:
    _schemes: Optional[List[SchemeRecord]] = None

    @classmethod
    def load_schemes(cls) -> List[SchemeRecord]:
        if cls._schemes is not None:
            return cls._schemes

        try:
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                raw = json.load(f)
                cls._schemes = [SchemeRecord.model_validate(item) for item in raw]
                logger.info(f"Loaded {len(cls._schemes)} scheme records from {DATA_PATH}")
                return cls._schemes
        except Exception as e:
            logger.error(f"Failed to load schemes from {DATA_PATH}: {e}")
            return []

    @classmethod
    def get_all(cls) -> List[SchemeRecord]:
        return cls.load_schemes()

    @classmethod
    def get_by_id(cls, scheme_id: str) -> Optional[SchemeRecord]:
        schemes = cls.load_schemes()
        for s in schemes:
            if s.id.lower() == scheme_id.lower():
                return s
        return None
