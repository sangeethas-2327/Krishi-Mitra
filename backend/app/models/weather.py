from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class HourlyForecastItem(BaseModel):
    time: str
    temperature: float
    weather_code: int
    weather_desc: str
    weather_desc_kn: str
    precipitation_prob: int
    is_day: bool

class DailyForecastItem(BaseModel):
    date: str
    day_name: str
    day_name_kn: str
    min_temp: float
    max_temp: float
    weather_code: int
    weather_desc: str
    weather_desc_kn: str
    precipitation_prob: int

class AgronomicInsight(BaseModel):
    alert_level: Literal["optimal", "advisory", "warning"]
    title: str
    title_kn: str
    advice: str
    advice_kn: str

class FarmWeatherResponse(BaseModel):
    location_name: str
    location_name_kn: str
    precision_level: Literal["village", "taluk", "district", "state_default"]
    precision_label: str
    precision_label_kn: str
    latitude: float
    longitude: float
    current_temp: float
    feels_like: float
    humidity: int
    wind_speed: float
    wind_direction: str
    wind_direction_kn: str
    precipitation: float
    precipitation_prob: int
    cloud_cover: int
    weather_code: int
    weather_desc: str
    weather_desc_kn: str
    is_day: bool
    today_min_temp: float
    today_max_temp: float
    hourly_forecast: List[HourlyForecastItem]
    daily_forecast: List[DailyForecastItem]
    agronomic_insight: AgronomicInsight
    fetched_at: str
    is_cached: bool = False

