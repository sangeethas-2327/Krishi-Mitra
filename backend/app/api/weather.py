import logging
from typing import Optional, List
from fastapi import APIRouter, Query, HTTPException
from app.models.weather import FarmWeatherResponse
from app.services.weather_service import WeatherService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/weather", tags=["weather"])

@router.get("", response_model=FarmWeatherResponse)
async def get_farm_weather(
    village: Optional[str] = Query(None, description="Village name"),
    taluk: Optional[str] = Query(None, description="Taluk / Sub-district name"),
    district: Optional[str] = Query(None, description="District name"),
    state: Optional[str] = Query("Karnataka", description="State name"),
    lat: Optional[float] = Query(None, description="Optional manual latitude"),
    lon: Optional[float] = Query(None, description="Optional manual longitude"),
    crops: Optional[str] = Query(None, description="Comma-separated crops for agronomic insights"),
    refresh: bool = Query(False, description="Bypass cache and force refresh")
):
    """
    Returns live farm weather, 24-hour hourly forecast, 7-day daily forecast,
    and contextual agronomic advisories based on farmer location and crops.
    """
    try:
        crop_list = [c.strip() for c in crops.split(",")] if crops else []
        weather_data = await WeatherService.get_farm_weather(
            village=village,
            taluk=taluk,
            district=district,
            state=state,
            lat=lat,
            lon=lon,
            crops=crop_list,
            force_refresh=refresh
        )
        return weather_data
    except Exception as e:
        logger.error(f"Error fetching farm weather: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to fetch farm weather: {str(e)}")

