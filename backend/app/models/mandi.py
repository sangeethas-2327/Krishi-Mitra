from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class MandiPriceItem(BaseModel):
    commodity: str = Field(..., description="Crop / Commodity name (e.g., Ragi, Paddy, Arecanut)")
    commodity_kn: str = Field(..., description="Kannada name of commodity")
    variety: Optional[str] = Field("FAQ / Standard", description="Variety / Grade")
    market: str = Field(..., description="APMC Market Yard (e.g., Mandya, Mysuru, Shimoga)")
    market_kn: str = Field(..., description="Kannada name of APMC Market Yard")
    district: str = Field(..., description="District in Karnataka")
    district_kn: str = Field(..., description="Kannada district name")
    min_price: float = Field(..., description="Minimum price in INR per quintal")
    max_price: float = Field(..., description="Maximum price in INR per quintal")
    modal_price: float = Field(..., description="Modal / Most common prevailing price in INR per quintal")
    unit: str = Field("₹ / Quintal", description="Measurement unit")
    price_date: str = Field(..., description="Date of price reporting")
    trend: str = Field("stable", description="Price trend: rising, falling, or stable")
    msp: Optional[float] = Field(None, description="Official Minimum Support Price if applicable")

class MandiPricesResponse(BaseModel):
    source: str = Field(
        "Karnataka State Agricultural Marketing Board (KSAMB) & Agmarknet",
        description="Data provenance source"
    )
    last_updated: str = Field(..., description="Timestamp of data report")
    filter_district: Optional[str] = None
    filter_commodity: Optional[str] = None
    total_records: int
    prices: List[MandiPriceItem]

