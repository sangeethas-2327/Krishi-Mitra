import logging
from typing import Optional, List, Dict
from fastapi import APIRouter, Query, HTTPException
from ..models.mandi import MandiPricesResponse
from ..services.mandi_service import MandiService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/mandi", tags=["mandi-prices"])

@router.get("", response_model=MandiPricesResponse)
def get_mandi_prices(
    district: Optional[str] = Query(None, description="Optional district name in Karnataka"),
    commodity: Optional[str] = Query(None, description="Optional crop/commodity name"),
    market: Optional[str] = Query(None, description="Optional APMC market yard name")
):
    """
    Returns official Karnataka APMC mandi prices with min, max, modal prices,
    Minimum Support Price (MSP) comparisons, and price trend indicators.
    """
    try:
        return MandiService.get_prices(district=district, commodity=commodity, market=market)
    except Exception as e:
        logger.error(f"Error fetching mandi prices: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to fetch mandi prices: {str(e)}")

@router.get("/commodities", response_model=List[Dict[str, str]])
def get_mandi_commodities():
    """
    Returns list of all available crops/commodities tracked across Karnataka APMCs.
    """
    return MandiService.get_available_commodities()

@router.get("/markets", response_model=List[Dict[str, str]])
def get_mandi_markets():
    """
    Returns list of all monitored APMC market yards across Karnataka.
    """
    return MandiService.get_available_markets()

