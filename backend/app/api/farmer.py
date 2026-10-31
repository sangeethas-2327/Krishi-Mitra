from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, Any
from ..models.farmer import FarmerProfile, FarmerProfileUpdate
from ..services.conversation_manager import ConversationManager

router = APIRouter(prefix="/api/farmer", tags=["farmer"])

@router.get("/profile", response_model=FarmerProfile)
def get_farmer_profile(session_id: str = Query(..., description="Unique session ID")):
    session = ConversationManager.get_or_create_session(session_id)
    return session.profile

@router.patch("/profile", response_model=FarmerProfile)
def update_farmer_profile(
    updates: FarmerProfileUpdate,
    session_id: str = Query(..., description="Unique session ID")
):
    session = ConversationManager.get_or_create_session(session_id)
    p = session.profile

    if updates.location:
        if "state" in updates.location and updates.location["state"]:
            p.location.state = updates.location["state"]
            p.set_field_value("location.state", p.location.state, source="user_edit")
        if "district" in updates.location and updates.location["district"]:
            p.location.district = updates.location["district"]
            p.set_field_value("location.district", p.location.district, source="user_edit")
        if "taluk" in updates.location and updates.location["taluk"]:
            p.location.taluk = updates.location["taluk"]
            p.set_field_value("location.taluk", p.location.taluk, source="user_edit")
        if "village" in updates.location and updates.location["village"]:
            p.location.village = updates.location["village"]
            p.set_field_value("location.village", p.location.village, source="user_edit")

    if updates.land_area:
        val = updates.land_area.get("value")
        unit = updates.land_area.get("unit", "acre")
        acres = updates.land_area.get("value_acres")
        if val is not None:
            p.land_area.value = float(val)
            p.land_area.unit = unit
            p.land_area.value_acres = float(acres) if acres is not None else float(val)
            p.set_field_value("land_area.value_acres", p.land_area.value_acres, source="user_edit")

    if updates.crops is not None:
        p.crops = updates.crops
        p.set_field_value("crops", p.crops, source="user_edit")

    if updates.ownership is not None:
        p.ownership = updates.ownership
        p.set_field_value("ownership", p.ownership, source="user_edit")

    if updates.season is not None:
        p.season = updates.season
        p.set_field_value("season", p.season, source="user_edit")

    if updates.irrigation:
        if "source" in updates.irrigation:
            src = updates.irrigation["source"]
            p.irrigation.source = src
            p.irrigation.has_irrigation = (src != "rainfed")
            p.set_field_value("irrigation.source", src, source="user_edit")
        if "type" in updates.irrigation:
            p.irrigation.type = updates.irrigation["type"]
        if "has_irrigation" in updates.irrigation:
            p.irrigation.has_irrigation = updates.irrigation["has_irrigation"]

    if updates.assistance_needs is not None:
        p.assistance_needs = updates.assistance_needs
        p.set_field_value("assistance_needs", p.assistance_needs, source="user_edit")

    if updates.additional_details is not None:
        p.additional_details.update(updates.additional_details)

    return p
