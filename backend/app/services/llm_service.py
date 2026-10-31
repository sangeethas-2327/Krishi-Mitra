import json
import logging
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from ..config import settings
from ..models.farmer import FarmerProfile, ExtractedFarmerInfo
from ..models.scheme import SchemeMatchResult, SchemeStatus

logger = logging.getLogger(__name__)

class GroundedResponseSchema(BaseModel):
    kannada: str = Field(description="Polite, conversational, natural Kannada response.")
    english: str = Field(description="Accurate English translation of the response.")
    explained_schemes: List[str] = Field(default_factory=list, description="IDs or names of schemes explained.")
    next_action_kn: Optional[str] = Field(default=None, description="Clear next action recommendation in Kannada.")
    next_action_en: Optional[str] = Field(default=None, description="Clear next action recommendation in English.")

class LLMService:
    @classmethod
    def get_client(cls, api_key: Optional[str] = None) -> Optional[Any]:
        """
        Initializes and returns the official Google Gen AI SDK client.
        Returns None if API key is missing or invalid.
        """
        key = (api_key or settings.GEMINI_API_KEY).strip()
        if not key:
            return None
        try:
            from google import genai
            return genai.Client(api_key=key)
        except Exception as e:
            logger.warning(f"Could not initialize Google Gen AI Client: {e}")
            return None

    @classmethod
    async def extract_farmer_profile_with_gemini(
        cls,
        message: str,
        current_profile: Optional[FarmerProfile] = None,
        language: str = "kn"
    ) -> Optional[ExtractedFarmerInfo]:
        """
        Uses Gemini with structured JSON output (Pydantic schema) to extract
        agricultural parameters from user messages in Kannada, English, or mixed phrases.
        Detects corrections vs new facts without overwriting unprompted.
        """
        if settings.DEMO_MODE or not settings.GEMINI_API_KEY.strip():
            return None

        client = cls.get_client()
        if not client:
            return None

        try:
            from google.genai import types

            system_instruction = (
                "You are an expert Kannada Agricultural Information Extractor for Krishi Mitra in Karnataka, India.\n"
                "Your objective is to extract structured farming facts from the farmer's utterance.\n\n"
                "RULES:\n"
                "1. Support Kannada, English, and Kannada-English code-mixed phrases (e.g., 'ನನ್ನ ಬಳಿ 3 acre land ide', 'I farm in Shivamogga').\n"
                "2. Standardize districts to Karnataka official district names (e.g., Shivamogga, Mandya, Mysuru, Belagavi, etc.).\n"
                "3. Standardize crops to canonical English names: 'arecanut', 'paddy', 'ragi', 'maize', 'sugarcane', 'coconut', 'cotton', 'groundnut', 'coffee', 'banana', 'chilli', 'pulses', 'vegetables', etc.\n"
                "4. Capture ALL crops mentioned in the message into the 'crops' array.\n"
                "5. Land measurement units: 'acre', 'gunta' (or 'guntha'/'gunte'), 'hectare', 'bigha'. Convert accurately to 'land_area_acres' (1 acre = 40 gunta, 1 hectare = 2.471 acres).\n"
                "6. Ownership types: 'owned', 'tenant', 'leased', 'sharecropper', 'joint_owned'.\n"
                "7. Season types: 'kharif', 'rabi', 'summer', 'annual', 'perennial'.\n"
                "8. Irrigation sources: 'borewell', 'open_well', 'canal', 'river', 'rainfed', 'none'.\n"
                "9. Assistance needs: 'micro_irrigation', 'crop_insurance', 'machinery_subsidy', 'soil_health', 'financial_support'.\n"
                "10. CORRECTION RECOGNITION: If the farmer is correcting or negating a previous fact (e.g. 'ನನ್ನದು 5 ಎಕರೆ ಅಲ್ಲ 2 ಎಕರೆ', 'not Mandya, it is Mysuru', 'alla', 'mistake'), set `is_correction: true` and specify which fields in `corrected_fields`.\n"
                "11. Never invent or hallucinate facts not stated by the farmer. Leave unknown fields as null or empty list."
            )

            current_facts = {}
            if current_profile:
                if current_profile.location.district:
                    current_facts["district"] = current_profile.location.district
                if current_profile.land_area.value_acres:
                    current_facts["land_area_acres"] = current_profile.land_area.value_acres
                if current_profile.crops:
                    current_facts["crops"] = current_profile.crops
                if current_profile.ownership:
                    current_facts["ownership"] = current_profile.ownership

            prompt_content = (
                f"Already confirmed farmer facts: {json.dumps(current_facts, ensure_ascii=False)}\n\n"
                f"Farmer's latest message: \"{message}\"\n\n"
                "Extract any agricultural facts from this message into structured ExtractedFarmerInfo JSON."
            )

            config = types.GenerateContentConfig(
                temperature=0.1,
                response_mime_type="application/json",
                response_schema=ExtractedFarmerInfo,
                system_instruction=system_instruction
            )

            response = await client.aio.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=prompt_content,
                config=config
            )

            if response and response.text:
                extracted = ExtractedFarmerInfo.model_validate_json(response.text)
                return extracted

        except Exception as e:
            logger.warning(f"Live Gemini extraction failed, falling back to deterministic extraction: {e}")

        return None

    @classmethod
    async def generate_response(
        cls,
        user_message: str,
        profile: FarmerProfile,
        recommendations: List[SchemeMatchResult],
        next_question_en: Optional[str],
        next_question_kn: Optional[str],
        language: str = "kn"
    ) -> Dict[str, Any]:
        """
        Generates contextual conversational response in Kannada and English.
        Uses Google Gen AI SDK if GEMINI_API_KEY is available and not in DEMO_MODE;
        otherwise uses a deterministic, rule-grounded response generator.
        """
        api_key = settings.GEMINI_API_KEY.strip()
        
        # Try live Gemini LLM if configured and not demo mode
        if api_key and not settings.DEMO_MODE:
            try:
                gemini_res = await cls._call_gemini_grounded(
                    api_key=api_key,
                    user_message=user_message,
                    profile=profile,
                    recommendations=recommendations,
                    next_question_en=next_question_en,
                    next_question_kn=next_question_kn,
                    language=language
                )
                if gemini_res:
                    return {
                        "kannada": gemini_res.get("kannada", ""),
                        "english": gemini_res.get("english", ""),
                        "llm_provider": "gemini-live",
                        "is_fallback": False,
                        "explained_schemes": gemini_res.get("explained_schemes", [])
                    }
            except Exception as e:
                logger.warning(f"Live Gemini API call failed, falling back to deterministic response: {e}")
                # Seamless fallback with is_fallback=True
                fallback_res = cls._generate_deterministic_response(
                    user_message=user_message,
                    profile=profile,
                    recommendations=recommendations,
                    next_question_en=next_question_en,
                    next_question_kn=next_question_kn,
                    language=language
                )
                fallback_res["is_fallback"] = True
                return fallback_res

        # Deterministic Grounded Fallback (Demo mode)
        return cls._generate_deterministic_response(
            user_message=user_message,
            profile=profile,
            recommendations=recommendations,
            next_question_en=next_question_en,
            next_question_kn=next_question_kn,
            language=language
        )

    @classmethod
    async def _call_gemini_grounded(
        cls,
        api_key: str,
        user_message: str,
        profile: FarmerProfile,
        recommendations: List[SchemeMatchResult],
        next_question_en: Optional[str],
        next_question_kn: Optional[str],
        language: str
    ) -> Optional[Dict[str, Any]]:
        client = cls.get_client(api_key=api_key)
        if not client:
            return None

        from google.genai import types

        system_instruction = (
            "You are Krishi Mitra (ಕೃಷಿ ಮಿತ್ರ), a warm, supportive, Kannada-first AI agricultural assistant for Karnataka farmers.\n\n"
            "CRITICAL ARCHITECTURAL CONSTRAINTS:\n"
            "1. Government scheme eligibility has ALREADY been calculated deterministically by our Python rule engine. NEVER override, recalculate, or invent eligibility rules.\n"
            "2. NEVER invent scheme benefits, criteria, or fake official application links.\n"
            "3. NEVER guarantee official approval or subsidy disbursement.\n"
            "4. Clearly distinguish real government schemes (PM-KISAN, PMFBY) from demonstration schemes (Demo Micro-Irrigation, Demo Agricultural Equipment, Demo Soil Improvement).\n\n"
            "GROUNDED EXPLANATION RULES:\n"
            "- Acknowledge the farmer's stated crops, land, and location with respect and warmth.\n"
            "- For POTENTIALLY_SUITABLE schemes: Explain clearly why they match based on the satisfied rules provided.\n"
            "- For NOT_SUITABLE_BASED_ON_KNOWN_RULES: Politely explain which condition was not met.\n"
            "- For INSUFFICIENT_INFORMATION: Note what details are still required.\n"
            "- For REQUIRES_OFFICIAL_VERIFICATION: Note that official documents (like RTC/Pahani or Aadhaar-bank link) require government verification.\n"
            "- ADAPTIVE FOLLOW-UP QUESTION: If a follow-up question is provided in the input, politely ask that exact question in natural Kannada and explain WHY it is required (using the justification provided).\n"
            "- Return strictly valid JSON conforming to GroundedResponseSchema."
        )

        evaluated_schemes_data = []
        for r in recommendations[:4]:
            evaluated_schemes_data.append({
                "id": r.scheme.id,
                "name": r.scheme.name,
                "name_kn": r.scheme.name_kn,
                "type": r.scheme.scheme_type,
                "status": r.evaluation_status.value,
                "satisfied_rules": [sr.description_kn or sr.description for sr in r.satisfied_rules],
                "unsatisfied_rules": [ur.description_kn or ur.description for ur in r.unsatisfied_rules],
                "unknown_rules": [uk.description_kn or uk.description for uk in r.unknown_rules],
                "needs_verification": [nv.description_kn or nv.description for nv in r.needs_verification_rules],
                "match_reason_kn": r.match_reason_kn,
                "match_reason_en": r.match_reason,
                "official_url": r.scheme.official_source_url
            })

        prompt_payload = {
            "farmer_profile": {
                "district": profile.location.district,
                "taluk": profile.location.taluk,
                "village": profile.location.village,
                "land_area_acres": profile.land_area.value_acres,
                "crops": profile.crops,
                "ownership": profile.ownership,
                "irrigation": profile.irrigation.model_dump(),
                "season": profile.season,
                "assistance_needs": profile.assistance_needs
            },
            "latest_user_message": user_message,
            "next_followup_question_kn": next_question_kn,
            "next_followup_question_en": next_question_en,
            "deterministic_rule_engine_results": evaluated_schemes_data
        }

        config = types.GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json",
            response_schema=GroundedResponseSchema,
            system_instruction=system_instruction
        )

        response = await client.aio.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=json.dumps(prompt_payload, ensure_ascii=False),
            config=config
        )

        if response and response.text:
            parsed = GroundedResponseSchema.model_validate_json(response.text)
            return parsed.model_dump()

        return None

    @classmethod
    def _generate_deterministic_response(
        cls,
        user_message: str,
        profile: FarmerProfile,
        recommendations: List[SchemeMatchResult],
        next_question_en: Optional[str],
        next_question_kn: Optional[str],
        language: str,
        is_fallback: bool = False
    ) -> Dict[str, Any]:
        """
        Deterministic, natural, polite Kannada and English response generator.
        Used in Demo Mode or when the live LLM API is unavailable.
        """
        kn_parts = []
        en_parts = []
        explained_schemes = []

        # Acknowledge extracted facts
        extracted_kn = []
        extracted_en = []
        if profile.crops:
            crops_str = ", ".join(profile.crops)
            extracted_kn.append(f"{crops_str} ಬೆಳೆ")
            extracted_en.append(f"growing {crops_str}")
        if profile.land_area.value_acres:
            extracted_kn.append(f"{profile.land_area.value_acres} ಎಕರೆ ಜಮೀನು")
            extracted_en.append(f"{profile.land_area.value_acres} acres land")
        if profile.location.district:
            extracted_kn.append(f"{profile.location.district} ಜಿಲ್ಲೆ")
            extracted_en.append(f"{profile.location.district} district")
        if profile.ownership:
            extracted_kn.append(f"{profile.ownership} ಸಾಗುವಳಿ")
            extracted_en.append(f"{profile.ownership} cultivation")

        if extracted_kn:
            kn_parts.append(f"ನಮಸ್ಕಾರ, ನಿಮ್ಮ ವಿವರಗಳನ್ನು ದಾಖಲಿಸಿಕೊಳ್ಳಲಾಗಿದೆ ({', '.join(extracted_kn)}).")
            en_parts.append(f"Greetings, your agricultural details have been noted ({', '.join(extracted_en)}).")
        else:
            kn_parts.append("ನಮಸ್ಕಾರ, ಕೃಷಿ ಮಿತ್ರಗೆ ಸ್ವಾಗತ.")
            en_parts.append("Greetings and welcome to Krishi Mitra.")

        # Check suitable schemes
        suitable = [r for r in recommendations if r.evaluation_status == SchemeStatus.POTENTIALLY_SUITABLE]

        if suitable:
            top = suitable[0]
            explained_schemes.append(top.scheme.id)
            kn_parts.append(f"ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ಪ್ರಕಾರ '{top.scheme.name_kn or top.scheme.name}' ಯೋಜನೆಗೆ ನೀವು ಪ್ರಾಥಮಿಕವಾಗಿ ಅರ್ಹರಾಗಿದ್ದೀರಿ.")
            en_parts.append(f"Based on your profile, you are preliminarily eligible for '{top.scheme.name}'.")

        # If follow-up question exists
        if next_question_kn:
            kn_parts.append(next_question_kn)
            en_parts.append(next_question_en or "Could you provide further information?")
        elif suitable:
            kn_parts.append("ಹೆಚ್ಚಿನ ವಿವರಗಳಿಗಾಗಿ ಮತ್ತು ಅರ್ಜಿ ವಿಧಾನ ತಿಳಿಯಲು ಕೆಳಗಿನ ಕಾರ್ಡ್‌ಗಳನ್ನು ನೋಡಿ.")
            en_parts.append("Please view the scheme cards below for application steps and benefits.")
        else:
            kn_parts.append("ದಯವಿಟ್ಟು ನಿಮ್ಮ ಜಿಲ್ಲೆ ಮತ್ತು ಬೆಳೆಯ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ಮಾಹಿತಿ ನೀಡಿ, ಇದರಿಂದ ಸೂಕ್ತ ಯೋಜನೆಯನ್ನು ಹುಡುಕಬಹುದು.")
            en_parts.append("Please share your district and crop details so we can find matching government assistance.")

        return {
            "kannada": " ".join(kn_parts),
            "english": " ".join(en_parts),
            "llm_provider": "demo-deterministic",
            "is_fallback": is_fallback,
            "explained_schemes": explained_schemes
        }
