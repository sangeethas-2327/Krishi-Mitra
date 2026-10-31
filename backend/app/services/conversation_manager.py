import uuid
import logging
from typing import Dict, Optional, Tuple, List, Any
from ..models.farmer import FarmerProfile
from ..models.scheme import SchemeMatchResult, SchemeStatus
from ..models.conversation import ChatMessage, MessageRole, ChatResponse
from .profile_extractor import ProfileExtractor
from .scheme_recommender import SchemeRecommender
from .llm_service import LLMService
from .text_to_speech import TextToSpeechService
from ..config import settings

logger = logging.getLogger(__name__)

# Scheme field justification map for explaining WHY a field is needed
FIELD_JUSTIFICATIONS = {
    "ownership": {
        "why_en": "Needed to verify PM-KISAN, as it specifically supports landholding owner-cultivator families.",
        "why_kn": "ಪಿಎಂ-ಕಿಸಾನ್ ಯೋಜನೆಗೆ ನೀವು ಜಮೀನಿನ ಮಾಲೀಕರಾಗಿದ್ದೀರಾ ಎಂದು ತಿಳಿಯಲು ನಿಮ್ಮ ಭೂಮಿ ಹಕ್ಕು (ಸ್ವಂತವೇ ಅಥವಾ ಗುತ್ತಿಗೆಯೇ) ಅಗತ್ಯವಿದೆ."
    },
    "land_area.value_acres": {
        "why_en": "Required to calculate subsidy slabs for micro-irrigation and farm mechanization equipment.",
        "why_kn": "ಹನಿ ನೀರಾವರಿ ಮತ್ತು ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ಸಹಾಯಧನದ ಶ್ರೇಣಿಯನ್ನು ನಿರ್ಧರಿಸಲು ಭೂಮಿ ವಿಸ್ತೀರ್ಣ ಅಗತ್ಯವಿದೆ."
    },
    "location.district": {
        "why_en": "Required because crop insurance (PMFBY) and regional micro-irrigation schemes apply to notified districts.",
        "why_kn": "ಬೆಳೆ ವಿಮೆ (PMFBY) ಮತ್ತು ನೀರಾವರಿ ಯೋಜನೆಗಳು ಅಧಿಸೂಚಿತ ಜಿಲ್ಲೆಗಳಿಗೆ ಮಾತ್ರ ಅನ್ವಯಿಸುವುದರಿಂದ ನಿಮ್ಮ ಜಿಲ್ಲೆ ಅಗತ್ಯವಿದೆ."
    },
    "crops": {
        "why_en": "Crop insurance and soil enhancement assistance depend on the specific notified crops grown.",
        "why_kn": "ಬೆಳೆ ವಿಮೆ (PMFBY) ಮತ್ತು ಮಣ್ಣು ಸುಧಾರಣೆ ನೆರವು ನೀವು ಬೆಳೆಯುವ ನಿರ್ದಿಷ್ಟ ಬೆಳೆಯನ್ನು ಆಧರಿಸಿರುತ್ತದೆ."
    },
    "irrigation.source": {
        "why_en": "Micro-irrigation schemes require an assured water source (borewell, well, or canal).",
        "why_kn": "ಹನಿ ನೀರಾವರಿ ಸಹಾಯಧನ ಪಡೆಯಲು ನಿಮ್ಮ ಜಮೀನಿನಲ್ಲಿ ಖಚಿತ ನೀರಿನ ಮೂಲ (ಕೊಳವೆಬಾವಿ ಅಥವಾ ಬಾವಿ) ಇರುವುದನ್ನು ದೃಢೀಕರಿಸಬೇಕು."
    },
    "season": {
        "why_en": "PMFBY premium rates and enrollment cut-off dates depend on the crop season (Kharif or Rabi).",
        "why_kn": "ಬೆಳೆ ವಿಮೆ ಪ್ರೀಮಿಯಂ ದರ ಹಾಗೂ ಕೊನೆಯ ದಿನಾಂಕಗಳು ಮುಂಗಾರು ಅಥವಾ ಹಿಂಗಾರು ಹಂಗಾಮಿನ ಮೇಲೆ ಆಧಾರಿತವಾಗಿರುತ್ತವೆ."
    }
}

class ConversationSession:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.profile = FarmerProfile()
        self.history: List[ChatMessage] = []
        self.asked_questions: List[str] = []
        self.status = "in_progress"

class ConversationManager:
    _sessions: Dict[str, ConversationSession] = {}

    @classmethod
    def get_or_create_session(cls, session_id: Optional[str] = None) -> ConversationSession:
        if not session_id or session_id not in cls._sessions:
            new_id = session_id or str(uuid.uuid4())
            cls._sessions[new_id] = ConversationSession(new_id)
            return cls._sessions[new_id]
        return cls._sessions[session_id]

    @classmethod
    def reset_session(cls, session_id: str) -> None:
        if session_id in cls._sessions:
            cls._sessions[session_id] = ConversationSession(session_id)

    @classmethod
    def select_adaptive_followup_question(
        cls,
        profile: FarmerProfile,
        recommendations: List[SchemeMatchResult],
        asked_questions: List[str]
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        Adaptive Question Engine:
        1. Clarifies ambiguous terms first if any pending.
        2. Driven by actual candidate scheme rules.
        3. Asks one useful question at a time.
        4. Explains WHY the requested information is necessary.
        5. Avoids repeating previously asked questions.
        """
        # 1. Check for pending ambiguities first (e.g. "ಜೋಳ" ambiguous between Sorghum and Maize)
        pending_ambiguities = profile.additional_details.get("pending_ambiguities", [])
        if pending_ambiguities:
            for ambig in pending_ambiguities:
                term = ambig.get("term")
                if term and term not in asked_questions:
                    asked_questions.append(term)
                    return ambig.get("question_en"), ambig.get("question_kn")

        # 2. Look for schemes with INSUFFICIENT_INFORMATION
        candidate_schemes = [
            r for r in recommendations
            if r.evaluation_status == SchemeStatus.INSUFFICIENT_INFORMATION
        ]

        # Prioritize real schemes first, then higher matching scores
        sorted_candidates = sorted(
            candidate_schemes,
            key=lambda x: (x.scheme.scheme_type == "real", x.score),
            reverse=True
        )

        for match_res in sorted_candidates:
            for rule_res in match_res.unknown_rules:
                if rule_res.is_mandatory:
                    field = rule_res.field
                    if field not in asked_questions:
                        justification = FIELD_JUSTIFICATIONS.get(field, {})
                        why_en = rule_res.why_needed or justification.get("why_en") or f"This is required to check your eligibility for {match_res.scheme.name}."
                        why_kn = rule_res.why_needed_kn or justification.get("why_kn") or f"{match_res.scheme.name_kn or match_res.scheme.name} ಯೋಜನೆಯ ಅರ್ಹತೆಯನ್ನು ಪರಿಶೀಲಿಸಲು ಈ ವಿವರ ಅಗತ್ಯವಿದೆ."

                        base_q_en = rule_res.clarification_question or f"Could you please specify your {rule_res.description or field}?"
                        base_q_kn = rule_res.clarification_question_kn or f"ದಯವಿಟ್ಟು ನಿಮ್ಮ {rule_res.description_kn or field} ಬಗ್ಗೆ ತಿಳಿಸುವಿರಾ?"

                        full_q_en = f"{base_q_en} ({why_en})"
                        full_q_kn = f"{base_q_kn} ({why_kn})"

                        asked_questions.append(field)
                        return full_q_en, full_q_kn

        return None, None

    @classmethod
    async def process_message(
        cls,
        session_id: Optional[str],
        message: str,
        language: str = "kn",
        corrected_fields: Optional[Dict[str, Any]] = None
    ) -> ChatResponse:
        session = cls.get_or_create_session(session_id)

        # 1. Apply any manual user corrections directly with provenance tracking
        if corrected_fields:
            for k, v in corrected_fields.items():
                if k == "crops" and isinstance(v, list):
                    session.profile.crops = v
                    session.profile.set_field_value("crops", v, source="user_edit")
                elif k == "district":
                    session.profile.location.district = v
                    session.profile.set_field_value("location.district", v, source="user_edit")
                elif k == "taluk":
                    session.profile.location.taluk = v
                    session.profile.set_field_value("location.taluk", v, source="user_edit")
                elif k == "ownership":
                    session.profile.ownership = v
                    session.profile.set_field_value("ownership", v, source="user_edit")
                elif k == "land_area_acres":
                    try:
                        val = float(v)
                        session.profile.land_area.value = val
                        session.profile.land_area.unit = "acre"
                        session.profile.land_area.value_acres = val
                        session.profile.set_field_value("land_area.value_acres", val, source="user_edit")
                    except ValueError:
                        pass
                elif k == "season":
                    session.profile.season = v
                    session.profile.set_field_value("season", v, source="user_edit")
                elif k == "irrigation_source":
                    session.profile.irrigation.source = v
                    session.profile.irrigation.has_irrigation = (v != "rainfed")
                    session.profile.set_field_value("irrigation.source", v, source="user_edit")
                elif k == "assistance_needs" and isinstance(v, list):
                    session.profile.assistance_needs = v
                    session.profile.set_field_value("assistance_needs", v, source="user_edit")

        # 2. Extract profile details: First attempt Gemini LLM extraction (if available), then combine with deterministic extractor
        gemini_extracted = await LLMService.extract_farmer_profile_with_gemini(
            message=message,
            current_profile=session.profile,
            language=language
        )

        # Run deterministic extractor as foundation / vocabulary validator
        updated_profile, extracted_info = ProfileExtractor.extract_from_text(
            text=message,
            existing_profile=session.profile
        )
        session.profile = updated_profile

        # If Gemini successfully extracted structured data, merge safely while respecting confirmed fields
        if gemini_extracted:
            is_explicit_corr = gemini_extracted.is_correction or any(
                neg in message for neg in ["ಅಲ್ಲ", "ತಪ್ಪು", "not", "mistake", "actually", "ಬದಲಿಗೆ", "instead"]
            )
            corr_set = set(gemini_extracted.corrected_fields)

            # District
            if gemini_extracted.district:
                if "location.district" in session.profile.confirmed_fields and not is_explicit_corr and "district" not in corr_set:
                    pass  # Keep confirmed value
                else:
                    session.profile.location.district = gemini_extracted.district
                    session.profile.set_field_value(
                        "location.district",
                        gemini_extracted.district,
                        confidence=0.96,
                        source="gemini_correction" if is_explicit_corr else "gemini_extracted"
                    )

            # Taluk
            if gemini_extracted.taluk:
                if "location.taluk" in session.profile.confirmed_fields and not is_explicit_corr and "taluk" not in corr_set:
                    pass
                else:
                    session.profile.location.taluk = gemini_extracted.taluk
                    session.profile.set_field_value(
                        "location.taluk",
                        gemini_extracted.taluk,
                        confidence=0.95,
                        source="gemini_correction" if is_explicit_corr else "gemini_extracted"
                    )

            # Village
            if gemini_extracted.village:
                session.profile.location.village = gemini_extracted.village

            # Land Area
            if gemini_extracted.land_area is not None or gemini_extracted.land_area_acres is not None:
                val_acres = (
                    gemini_extracted.land_area_acres
                    if gemini_extracted.land_area_acres is not None
                    else ProfileExtractor.convert_to_acres(gemini_extracted.land_area, gemini_extracted.land_unit or "acre")
                )
                if val_acres is None and gemini_extracted.land_area is not None:
                    val_acres = float(gemini_extracted.land_area)

                if "land_area.value_acres" in session.profile.confirmed_fields and not is_explicit_corr and "land_area" not in corr_set:
                    pass
                elif val_acres is not None:
                    session.profile.land_area.value = gemini_extracted.land_area or val_acres
                    session.profile.land_area.unit = gemini_extracted.land_unit or "acre"
                    session.profile.land_area.value_acres = val_acres
                    session.profile.set_field_value(
                        "land_area.value_acres",
                        val_acres,
                        confidence=0.98,
                        source="gemini_correction" if is_explicit_corr else "gemini_extracted"
                    )

            # Crops (Supporting Multiple Crops)
            if gemini_extracted.crops:
                if is_explicit_corr and any(c in message for c in ["ಅಲ್ಲ", "not", "replace", "ಬದಲಿಗೆ"]):
                    session.profile.crops = gemini_extracted.crops
                else:
                    for c in gemini_extracted.crops:
                        if c not in session.profile.crops:
                            session.profile.crops.append(c)
                session.profile.set_field_value(
                    "crops",
                    session.profile.crops,
                    confidence=0.97,
                    source="gemini_correction" if is_explicit_corr else "gemini_extracted"
                )

            # Ownership
            if gemini_extracted.ownership:
                if "ownership" in session.profile.confirmed_fields and not is_explicit_corr and "ownership" not in corr_set:
                    pass
                else:
                    session.profile.ownership = gemini_extracted.ownership
                    session.profile.set_field_value(
                        "ownership",
                        gemini_extracted.ownership,
                        confidence=0.95,
                        source="gemini_correction" if is_explicit_corr else "gemini_extracted"
                    )

            # Season
            if gemini_extracted.season:
                if "season" in session.profile.confirmed_fields and not is_explicit_corr and "season" not in corr_set:
                    pass
                else:
                    session.profile.season = gemini_extracted.season
                    session.profile.set_field_value(
                        "season",
                        gemini_extracted.season,
                        confidence=0.95,
                        source="gemini_correction" if is_explicit_corr else "gemini_extracted"
                    )

            # Irrigation
            if gemini_extracted.irrigation_source:
                session.profile.irrigation.source = gemini_extracted.irrigation_source
                session.profile.irrigation.has_irrigation = (
                    gemini_extracted.irrigation_source != "rainfed" and gemini_extracted.irrigation_source != "none"
                )
                session.profile.set_field_value(
                    "irrigation.source",
                    gemini_extracted.irrigation_source,
                    confidence=0.95,
                    source="gemini_correction" if is_explicit_corr else "gemini_extracted"
                )
            elif gemini_extracted.has_irrigation is not None:
                session.profile.irrigation.has_irrigation = gemini_extracted.has_irrigation

            # Assistance Needs
            if gemini_extracted.assistance_needs:
                for an in gemini_extracted.assistance_needs:
                    if an not in session.profile.assistance_needs:
                        session.profile.assistance_needs.append(an)
                session.profile.set_field_value(
                    "assistance_needs",
                    session.profile.assistance_needs,
                    confidence=0.95,
                    source="gemini_extracted"
                )

        # 3. Evaluate schemes using deterministic recommender (SOLE AUTHORITY FOR ELIGIBILITY)
        recommendations = SchemeRecommender.get_recommendations(session.profile)

        # 4. Adaptive follow-up question generation with explanation
        next_q_en, next_q_kn = cls.select_adaptive_followup_question(
            profile=session.profile,
            recommendations=recommendations,
            asked_questions=session.asked_questions
        )

        # 5. Determine conversation status
        has_suitable = any(r.evaluation_status == SchemeStatus.POTENTIALLY_SUITABLE for r in recommendations)
        if has_suitable and not next_q_en:
            session.status = "ready_with_recommendations"
        elif next_q_en:
            session.status = "awaiting_clarification"
        else:
            session.status = "in_progress"

        # 6. Generate contextual explanation via LLM Service (or deterministic fallback)
        llm_response = await LLMService.generate_response(
            user_message=message,
            profile=session.profile,
            recommendations=recommendations,
            next_question_en=next_q_en,
            next_question_kn=next_q_kn,
            language=language
        )

        resp_text = llm_response.get("kannada" if language == "kn" else "english", "")
        resp_kn = llm_response.get("kannada", "")
        resp_en = llm_response.get("english", "")

        # 7. Collect sources and uncertainty notes
        sources = []
        uncertainties = []
        for r in recommendations:
            if r.scheme.official_source_url:
                sources.append(f"{r.scheme.name}: {r.scheme.official_source_url} (Verified: {r.scheme.last_verified_at})")
            elif r.scheme.scheme_type == "demonstration":
                sources.append(f"{r.scheme.name}: Synthetic Demonstration Specification (Not official)")

            if r.needs_verification_rules:
                uncertainties.append(f"{r.scheme.name} requires official offline RTC/caste verification.")

        # Record messages in session history
        session.history.append(ChatMessage(
            id=str(uuid.uuid4()),
            role=MessageRole.USER,
            content=message,
            created_at="now",
            metadata={"extracted": extracted_info}
        ))
        session.history.append(ChatMessage(
            id=str(uuid.uuid4()),
            role=MessageRole.ASSISTANT,
            content=resp_text,
            created_at="now",
            metadata={"status": session.status}
        ))

        # 8. Synthesize audio for real-time voice feedback
        audio_base64 = None
        voice_provider = None
        if settings.AUTO_SYNTHESIZE_SPEECH:
            try:
                synth_target = resp_kn if resp_kn else resp_text
                synth_res = await TextToSpeechService.synthesize(synth_target, language=language)
                audio_base64 = synth_res.audio_base64
                voice_provider = synth_res.provider
            except Exception as e:
                logger.warning(f"Speech pre-synthesis skipped: {e}")

        return ChatResponse(
            session_id=session.session_id,
            response_text=resp_text,
            response_text_kn=resp_kn,
            response_text_en=resp_en,
            audio_url=None,
            audio_base64=audio_base64,
            voice_provider=voice_provider,
            updated_profile=session.profile,
            next_question=next_q_en,
            next_question_kn=next_q_kn,
            conversation_status=session.status,
            recommendations=recommendations,
            source_references=list(set(sources)),
            uncertainty_notes=uncertainties,
            llm_provider=llm_response.get("llm_provider", "demo-deterministic"),
            is_fallback=bool(llm_response.get("is_fallback", False)),
            explained_schemes=llm_response.get("explained_schemes", [])
        )
