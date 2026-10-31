from fastapi import APIRouter, HTTPException, Query, Body
from typing import List, Optional
from ..models.scheme import (
    SchemeRecord,
    SchemeMatchResult,
    SchemeComparisonResponse,
    SchemeReadinessChecklist
)
from ..models.farmer import FarmerProfile
from ..services.scheme_source_service import SchemeSourceService
from ..services.scheme_recommender import SchemeRecommender
from ..services.scheme_comparison import SchemeComparisonService
from ..services.checklist_service import ChecklistService
from ..services.conversation_manager import ConversationManager

router = APIRouter(prefix="/api/schemes", tags=["schemes"])

@router.get("", response_model=List[SchemeRecord])
def list_schemes(category: Optional[str] = Query(None, description="Filter by scheme category")):
    schemes = SchemeSourceService.get_all()
    if category and category.lower() != "all":
        return [s for s in schemes if s.category.lower() == category.lower()]
    return schemes

@router.get("/compare", response_model=SchemeComparisonResponse)
def compare_schemes_get(ids: Optional[str] = Query(None, description="Comma-separated scheme IDs to compare")):
    scheme_ids = [s.strip() for s in ids.split(",")] if ids else ["pm-kisan", "pmfby"]
    return SchemeComparisonService.compare_schemes(scheme_ids)

@router.post("/compare", response_model=SchemeComparisonResponse)
def compare_schemes_post(scheme_ids: List[str] = Body(..., description="List of scheme IDs to compare")):
    if not scheme_ids:
        scheme_ids = ["pm-kisan", "pmfby"]
    return SchemeComparisonService.compare_schemes(scheme_ids)

@router.get("/{scheme_id}/checklist", response_model=SchemeReadinessChecklist)
def get_scheme_checklist(scheme_id: str, session_id: Optional[str] = Query(None)):
    scheme = SchemeSourceService.get_by_id(scheme_id)
    if not scheme:
        raise HTTPException(status_code=404, detail=f"Scheme '{scheme_id}' not found.")

    profile = None
    if session_id:
        session = ConversationManager.get_or_create_session(session_id)
        profile = session.profile

    return ChecklistService.generate_checklist(scheme, profile)

@router.get("/{scheme_id}", response_model=SchemeRecord)
def get_scheme_detail(scheme_id: str):
    scheme = SchemeSourceService.get_by_id(scheme_id)
    if not scheme:
        raise HTTPException(status_code=404, detail=f"Scheme '{scheme_id}' not found.")
    return scheme

@router.post("/match", response_model=List[SchemeMatchResult])
def match_schemes(profile: FarmerProfile, category: Optional[str] = Query(None)):
    try:
        recommendations = SchemeRecommender.get_recommendations(profile=profile, category=category)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Matching failed: {str(e)}")
