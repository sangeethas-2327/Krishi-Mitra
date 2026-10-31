import time
import httpx
from datetime import datetime
from typing import Optional, List, Dict, Tuple, Any

from app.models.weather import (
    FarmWeatherResponse,
    HourlyForecastItem,
    DailyForecastItem,
    AgronomicInsight
)

WMO_CODE_MAP = {
    0: ("Clear sky", "ಶುಭ್ರ ಆಕಾಶ"),
    1: ("Mainly clear", "ಹೆಚ್ಚಾಗಿ ಶುಭ್ರ ಆಕಾಶ"),
    2: ("Partly cloudy", "ಭಾಗಶಃ ಮೋಡ ಕವಿದಿದೆ"),
    3: ("Overcast", "ಮೋಡ ಕವಿದ ವಾತಾವರಣ"),
    45: ("Fog", "ದಟ್ಟ ಮಂಜು"),
    48: ("Depositing rime fog", "ತೇವಾಂಶ ಮಂಜು"),
    51: ("Light drizzle", "ಹಗುರ ತುಂತುರು ಮಳೆ"),
    53: ("Moderate drizzle", "ಸಾಧಾರಣ ತುಂತುರು ಮಳೆ"),
    55: ("Dense drizzle", "ದಟ್ಟ ತುಂತುರು ಮಳೆ"),
    61: ("Slight rain", "ಅಲ್ಪ ಮಳೆ"),
    63: ("Moderate rain", "ಸಾಧಾರಣ ಮಳೆ"),
    65: ("Heavy rain", "ಭಾರಿ ಮಳೆ"),
    80: ("Rain showers", "ಮಳೆ ಸುರಿಮಳೆ"),
    81: ("Moderate rain showers", "ಸಾಧಾರಣ ಮಳೆ ಸುರಿಮಳೆ"),
    82: ("Violent rain showers", "ಭಾರಿ ಬಿರುಸಿನ ಮಳೆ"),
    95: ("Thunderstorm", "ಗುಡುಗು ಸಹಿತ ಮಳೆ"),
    96: ("Thunderstorm with slight hail", "ಆಲಿಕಲ್ಲು ಸಹಿತ ಗುಡುಗು ಮಳೆ"),
    99: ("Thunderstorm with heavy hail", "ಭಾರಿ ಆಲಿಕಲ್ಲು ಸಹಿತ ಗುಡುಗು ಮಳೆ"),
}

DAYS_KN = {
    "Monday": "ಸೋಮವಾರ",
    "Tuesday": "ಮಂಗಳವಾರ",
    "Wednesday": "ಬುಧವಾರ",
    "Thursday": "ಗುರುವಾರ",
    "Friday": "ಶುಕ್ರವಾರ",
    "Saturday": "ಶನಿವಾರ",
    "Sunday": "ಭಾನುವಾರ"
}

DISTRICT_COORDS_KA: Dict[str, Tuple[float, float, str]] = {
    "bagalkot": (16.1804, 75.6960, "ಬಾಗಲಕೋಟೆ"),
    "ballari": (15.1394, 76.9214, "ಬಳ್ಳಾರಿ"),
    "bellary": (15.1394, 76.9214, "ಬಳ್ಳಾರಿ"),
    "belagavi": (15.8497, 74.4977, "ಬೆಳಗಾವಿ"),
    "belgaum": (15.8497, 74.4977, "ಬೆಳಗಾವಿ"),
    "bengaluru": (12.9716, 77.5946, "ಬೆಂಗಳೂರು"),
    "bangalore": (12.9716, 77.5946, "ಬೆಂಗಳೂರು"),
    "bengaluru rural": (13.2269, 77.5753, "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ"),
    "bidar": (17.9104, 77.5199, "ಬೀದರ್"),
    "chamarajanagar": (11.9261, 76.9437, "ಚಾಮರಾಜನಗರ"),
    "chikkaballapur": (13.4325, 77.7275, "ಚಿಕ್ಕಬಳ್ಳಾಪುರ"),
    "chikkamagaluru": (13.3161, 75.7720, "ಚಿಕ್ಕಮಗಳೂರು"),
    "chitradurga": (14.2251, 76.3980, "ಚಿತ್ರದುರ್ಗ"),
    "dakshina kannada": (12.8703, 74.8806, "ದಕ್ಷಿಣ ಕನ್ನಡ"),
    "mangalore": (12.9141, 74.8560, "ಮಂಗಳೂರು"),
    "davanagere": (14.4644, 75.9218, "ದಾವಣಗೆರೆ"),
    "dharwad": (15.4589, 75.0078, "ಧಾರವಾಡ"),
    "gadag": (15.4313, 75.6358, "ಗದಗ"),
    "hassan": (13.0072, 76.1030, "ಹಾಸನ"),
    "haveri": (14.7972, 75.4026, "ಹಾವೇರಿ"),
    "kalaburagi": (17.3297, 76.8343, "ಕಲಬುರಗಿ"),
    "gulbarga": (17.3297, 76.8343, "ಕಲಬುರಗಿ"),
    "kodagu": (12.4244, 75.7382, "ಕೊಡಗು"),
    "madikeri": (12.4244, 75.7382, "ಮಡಿಕೇರಿ"),
    "kolar": (13.1367, 78.1291, "ಕೋಲಾರ"),
    "koppal": (15.3456, 76.1553, "ಕೊಪ್ಪಳ"),
    "mandya": (12.5218, 76.8951, "ಮಂಡ್ಯ"),
    "mysuru": (12.2958, 76.6394, "ಮೈಸೂರು"),
    "mysore": (12.2958, 76.6394, "ಮೈಸೂರು"),
    "raichur": (16.2076, 77.3463, "ರಾಯಚೂರು"),
    "ramanagara": (12.7209, 77.2799, "ರಾಮನಗರ"),
    "shivamogga": (13.9299, 75.5681, "ಶಿವಮೊಗ್ಗ"),
    "shimoga": (13.9299, 75.5681, "ಶಿವಮೊಗ್ಗ"),
    "tumakuru": (13.3392, 77.1017, "ತುಮಕೂರು"),
    "tumkur": (13.3392, 77.1017, "ತುಮಕೂರು"),
    "udupi": (13.3409, 74.7421, "ಉಡುಪಿ"),
    "uttara kannada": (14.8136, 74.1297, "ಉತ್ತರ ಕನ್ನಡ"),
    "karwar": (14.8136, 74.1297, "ಕಾರವಾರ"),
    "vijayanagara": (15.2736, 76.3916, "ವಿಜಯನಗರ"),
    "hosapete": (15.2736, 76.3916, "ಹೊಸಪೇಟೆ"),
    "vijayapura": (16.8302, 75.7100, "ವಿಜಯಪುರ"),
    "bijapur": (16.8302, 75.7100, "ವಿಜಯಪುರ"),
    "yadgir": (16.7644, 77.1378, "ಯಾದಗಿರಿ")
}

_WEATHER_CACHE: Dict[str, Tuple[float, FarmWeatherResponse]] = {}
CACHE_TTL_SECONDS = 900  # 15 minutes

class WeatherService:
    @staticmethod
    def _wind_dir_to_text(degree: float) -> Tuple[str, str]:
        dirs = [
            ("N", "ಉತ್ತರ"), ("NE", "ಈಶಾನ್ಯ"), ("E", "ಪೂರ್ವ"), ("SE", "ಆಗ್ನೇಯ"),
            ("S", "ದಕ್ಷಿಣ"), ("SW", "ನೈಋತ್ಯ"), ("W", "ಪಶ್ಚಿಮ"), ("NW", "ವಾಯುವ್ಯ")
        ]
        idx = int((degree + 22.5) / 45.0) % 8
        return dirs[idx]

    @staticmethod
    def _generate_insight(
        temp: float,
        humidity: int,
        rain_prob: int,
        wind_speed: float,
        weather_code: int,
        crops: Optional[List[str]] = None
    ) -> AgronomicInsight:
        crops = [c.lower() for c in (crops or [])]
        is_horticulture = any(c in crops for c in ["arecanut", "banana", "mango", "pomegranate", "pepper", "coconut", "onion", "tomato"])
        is_paddy_sugarcane = any(c in crops for c in ["paddy", "rice", "sugarcane", "maize"])

        # Severe rain / thunderstorm
        if weather_code in [65, 82, 95, 96, 99] or rain_prob >= 75:
            return AgronomicInsight(
                alert_level="warning",
                title="Heavy Rain Forecast — Suspend Spraying & Drainage Alert",
                title_kn="ಭಾರಿ ಮಳೆ ಮುನ್ಸೂಚನೆ — ಕೀಟನಾಶಕ ಸಿಂಪಡಣೆ ಮುಂದೂಡಿ",
                advice="Hold off all pesticide spraying, top-dress fertilizer applications, and post-harvest drying. Ensure drainage channels in low-lying plots are cleared to avoid root inundation.",
                advice_kn="ಭಾರಿ ಮಳೆ ಸಾಧ್ಯತೆ ಇರುವುದರಿಂದ ಕೀಟನಾಶಕ ಸಿಂಪಡಣೆ ಮತ್ತು ಮೇಲುಗೊಬ್ಬರ ನೀಡುವುದನ್ನು ತಕ್ಷಣ ಮುಂದೂಡಿ. ತಗ್ಗು ಜಮೀನುಗಳಲ್ಲಿ ನೀರು ನಿಲ್ಲದಂತೆ ಬಸಿಗಾಲುವೆಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ."
            )

        # High humidity + moderate heat -> Fungal disease alert
        if humidity >= 80 and temp >= 24:
            crop_mention = "arecanut koleroga and fungal leaf spot" if is_horticulture else "blast and fungal infections"
            crop_mention_kn = "ಅಡಿಕೆ ಕೊಳೆರೋಗ ಮತ್ತು ಎಲೆಚುಕ್ಕಿ ರೋಗ" if is_horticulture else "ಬೆಂಕಿ ರೋಗ ಮತ್ತು ಶಿಲೀಂಧ್ರ ಬಾಧೆ"
            return AgronomicInsight(
                alert_level="advisory",
                title="High Humidity Advisory — Fungal Vigilance Required",
                title_kn="ಹೆಚ್ಚಿನ ಆರ್ದ್ರತೆ ಎಚ್ಚರಿಕೆ — ಶಿಲೀಂಧ್ರ ರೋಗಗಳ ಬಗ್ಗೆ ಎಚ್ಚರ",
                advice=f"High ambient moisture ({humidity}%) creates favourable conditions for {crop_mention}. Inspect foliage undersides for spores; plan prophylactic biological sprays (Trichoderma/Bordeaux) on rain-free breaks.",
                advice_kn=f"ವಾತಾವರಣದಲ್ಲಿ ಶೇ. {humidity} ರಷ್ಟು ತೇವಾಂಶ ಇರುವುದರಿಂದ {crop_mention_kn} ಕಾಣಿಸಿಕೊಳ್ಳುವ ಸಾಧ್ಯತೆಯಿದೆ. ಮಳೆ ಇಲ್ಲದ ಶುಭ್ರ ಸಮಯದಲ್ಲಿ ಮುಂಜಾಗ್ರತಾ ಬೋರ್ಡೋ ಅಥವಾ ಜೈವಿಕ ಔಷಧ ಸಿಂಪಡಣೆಗೆ ಸಿದ್ಧತೆ ಮಾಡಿಕೊಳ್ಳಿ."
            )

        # High wind speed (> 25 km/h) -> Spraying drift and lodging alert
        if wind_speed >= 25:
            return AgronomicInsight(
                alert_level="advisory",
                title="Brisk Winds — Avoid Foliar Spraying & Prop Tall Crops",
                title_kn="ಬಿರುಸಿನ ಗಾಳಿ — ಸಿಂಪಡಣೆ ಬೇಡ & ಬೆಳೆಗಳಿಗೆ ಆಸರೆ ನೀಡಿ",
                advice=f"Wind speeds reaching {wind_speed:.1f} km/h cause chemical spray drift and poor droplet adherence. Provide staking/earthing up for banana, sugarcane, and young orchard saplings.",
                advice_kn=f"ಗಾಳಿಯ ವೇಗ {wind_speed:.1f} ಕಿಮೀ/ಗಂಟೆ ಇರುವುದರಿಂದ ಕೀಟನಾಶಕಗಳು ಪೋಲಾಗುತ್ತವೆ. ಬಾಳೆ ಮತ್ತು ಕಬ್ಬಿನ ಬೆಳೆಗಳಿಗೆ ಆಸರೆ ನೀಡಿ ಗಾಳಿಯಿಂದ ಮುರಿಯದಂತೆ ರಕ್ಷಿಸಿ."
            )

        # Optimal weather (clear sky, moderate temp, low rain prob)
        if rain_prob <= 20 and humidity < 75:
            harvest_tip = "ideal for drying harvested grain, arecanut, and field sowing" if not is_paddy_sugarcane else "optimal for scheduled irrigation and nutrient uptake"
            harvest_tip_kn = "ಧಾನ್ಯ ಒಣಗಿಸಲು, ಅಡಿಕೆ ಸಂಸ್ಕರಣೆಗೆ ಮತ್ತು ಕಟಾವಿಗೆ ಅತ್ಯುತ್ತಮ" if not is_paddy_sugarcane else "ನೀರಾವರಿ ಒದಗಿಸಲು ಮತ್ತು ರಸಗೊಬ್ಬರ ನೀಡಲು ಸೂಕ್ತ"
            return AgronomicInsight(
                alert_level="optimal",
                title="Favourable Clear Weather — Recommended Field Operations",
                title_kn="ಅನುಕೂಲಕರ ಹವಾಮಾನ — ಕೃಷಿ ಕೆಲಸಗಳಿಗೆ ಸಕಾಲ",
                advice=f"Fair conditions today ({temp:.1f}°C, rain chance {rain_prob}%). Window is {harvest_tip}. Continue planned farm operations with confidence.",
                advice_kn=f"ಇಂದು ಹವಾಮಾನ ಅನುಕೂಲಕರವಾಗಿದೆ ({temp:.1f}°C, ಮಳೆ ಸಂಭವ {rain_prob}%). ಈ ಸಮಯವು {harvest_tip_kn}. ನಿಮ್ಮ ಹೊಲದ ಕೆಲಸಗಳನ್ನು ಸುಲಲಿತವಾಗಿ ಮುಂದುವರಿಸಿ."
            )

        # Default advisory
        return AgronomicInsight(
            alert_level="optimal",
            title="Stable Weather Conditions",
            title_kn="ಸ್ಥಿರ ಹವಾಮಾನ ಪರಿಸ್ಥಿತಿ",
            advice=f"Moderate conditions ({temp:.1f}°C, humidity {humidity}%). Monitor morning soil moisture before irrigating.",
            advice_kn=f"ಸಾಧಾರಣ ಹವಾಮಾನವಿದೆ ({temp:.1f}°C, ತೇವಾಂಶ ಶೇ. {humidity}). ನೀರು ಹಾಯಿಸುವ ಮುನ್ನ ಜಮೀನಿನ ತೇವಾಂಶವನ್ನು ಪರೀಕ್ಷಿಸಿಕೊಳ್ಳಿ."
        )

    @classmethod
    async def resolve_location(
        cls,
        village: Optional[str] = None,
        taluk: Optional[str] = None,
        district: Optional[str] = None,
        state: Optional[str] = "Karnataka"
    ) -> Tuple[float, float, str, str, str, str]:
        """
        Returns: (lat, lon, location_name, location_name_kn, precision_level, precision_label)
        Fallback hierarchy: Village -> Taluk -> District -> State default
        """
        client = httpx.AsyncClient(timeout=6.0, verify=False)

        # 1. Try Village + Taluk + District
        if village and (taluk or district):
            query = f"{village}, {taluk or district}, Karnataka, India"
            try:
                res = await client.get(
                    "https://geocoding-api.open-meteo.com/v1/search",
                    params={"name": village, "count": 5, "language": "en", "format": "json"}
                )
                if res.status_code == 200:
                    data = res.json()
                    results = data.get("results") or []
                    for r in results:
                        if r.get("country_code") == "IN" and "karnataka" in str(r.get("admin1", "")).lower():
                            return (
                                float(r["latitude"]),
                                float(r["longitude"]),
                                f"{village.title()}, {r.get('admin2', district or 'Karnataka')}",
                                f"{village.title()}, {district or 'ಕರ್ನಾಟಕ'}",
                                "village",
                                "Village-level (GPS/Local)",
                            )
            except Exception:
                pass

        # 2. Try Taluk
        if taluk:
            try:
                res = await client.get(
                    "https://geocoding-api.open-meteo.com/v1/search",
                    params={"name": taluk, "count": 5, "language": "en", "format": "json"}
                )
                if res.status_code == 200:
                    data = res.json()
                    results = data.get("results") or []
                    for r in results:
                        if r.get("country_code") == "IN" and "karnataka" in str(r.get("admin1", "")).lower():
                            return (
                                float(r["latitude"]),
                                float(r["longitude"]),
                                f"{taluk.title()} Taluk, {district or 'Karnataka'}",
                                f"{taluk.title()} ತಾಲೂಕು, {district or 'ಕರ್ನಾಟಕ'}",
                                "taluk",
                                "Taluk-level",
                            )
            except Exception:
                pass

        # 3. Try District (from fast local lookup or geocoding)
        if district:
            clean_d = district.lower().strip()
            if clean_d in DISTRICT_COORDS_KA:
                lat, lon, name_kn = DISTRICT_COORDS_KA[clean_d]
                return (
                    lat, lon,
                    f"{district.title()} District, Karnataka",
                    f"{name_kn} ಜಿಲ್ಲೆ, ಕರ್ನಾಟಕ",
                    "district",
                    "District-level",
                )
            # Try geocoding district
            try:
                res = await client.get(
                    "https://geocoding-api.open-meteo.com/v1/search",
                    params={"name": district, "count": 3, "language": "en", "format": "json"}
                )
                if res.status_code == 200:
                    results = res.json().get("results") or []
                    if results:
                        r = results[0]
                        return (
                            float(r["latitude"]),
                            float(r["longitude"]),
                            f"{district.title()} District, Karnataka",
                            f"{district.title()} ಜಿಲ್ಲೆ, ಕರ್ನಾಟಕ",
                            "district",
                            "District-level",
                        )
            except Exception:
                pass

        # 4. State Default Fallback: Shivamogga, Karnataka (central agricultural district)
        lat, lon, name_kn = DISTRICT_COORDS_KA["shivamogga"]
        return (
            lat, lon,
            "Shivamogga (Central Karnataka)",
            "ಶಿವಮೊಗ್ಗ (ಕೇಂದ್ರ ಕರ್ನಾಟಕ)",
            "state_default",
            "State default (Central KA)",
        )

    @classmethod
    async def get_farm_weather(
        cls,
        village: Optional[str] = None,
        taluk: Optional[str] = None,
        district: Optional[str] = None,
        state: Optional[str] = "Karnataka",
        lat: Optional[float] = None,
        lon: Optional[float] = None,
        location_label: Optional[str] = None,
        crops: Optional[List[str]] = None,
        force_refresh: bool = False
    ) -> FarmWeatherResponse:
        # Resolve coordinates if not directly provided
        if lat is None or lon is None:
            resolved_lat, resolved_lon, loc_name, loc_name_kn, prec_level, prec_label = await cls.resolve_location(
                village=village, taluk=taluk, district=district, state=state
            )
        else:
            resolved_lat, resolved_lon = lat, lon
            loc_name = location_label or f"Lat: {lat:.2f}, Lon: {lon:.2f}"
            loc_name_kn = loc_name
            prec_level = "village" if village else ("taluk" if taluk else ("district" if district else "state_default"))
            prec_label = f"{prec_level.title()}-level"

        cache_key = f"{round(resolved_lat, 2)}_{round(resolved_lon, 2)}"
        now = time.time()

        # Check Cache
        if not force_refresh and cache_key in _WEATHER_CACHE:
            cached_time, cached_resp = _WEATHER_CACHE[cache_key]
            if now - cached_time < CACHE_TTL_SECONDS:
                resp = cached_resp.model_copy()
                resp.is_cached = True
                return resp

        # Fetch from Open-Meteo API
        async with httpx.AsyncClient(timeout=10.0, verify=False) as client:
            resp = await client.get(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": resolved_lat,
                    "longitude": resolved_lon,
                    "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,cloud_cover,wind_speed_10m,wind_direction_10m,is_day",
                    "hourly": "temperature_2m,precipitation_probability,weather_code,is_day",
                    "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max",
                    "timezone": "Asia/Kolkata",
                    "forecast_days": 7
                }
            )
            resp.raise_for_status()
            data = resp.json()

        current = data.get("current", {})
        hourly = data.get("hourly", {})
        daily = data.get("daily", {})

        current_temp = float(current.get("temperature_2m", 28.0))
        feels_like = float(current.get("apparent_temperature", current_temp))
        humidity = int(current.get("relative_humidity_2m", 65))
        precip = float(current.get("precipitation", 0.0))
        cloud = int(current.get("cloud_cover", 30))
        wind_spd = float(current.get("wind_speed_10m", 12.0))
        wind_deg = float(current.get("wind_direction_10m", 90.0))
        w_code = int(current.get("weather_code", 1))
        is_day = bool(current.get("is_day", 1))

        wind_dir_en, wind_dir_kn = cls._wind_dir_to_text(wind_deg)
        desc_en, desc_kn = WMO_CODE_MAP.get(w_code, ("Fair", "ಸಾಧಾರಣ"))

        # Hourly forecast (next 24 hours)
        hourly_times = hourly.get("time", [])
        hourly_temps = hourly.get("temperature_2m", [])
        hourly_probs = hourly.get("precipitation_probability", [])
        hourly_codes = hourly.get("weather_code", [])
        hourly_is_day = hourly.get("is_day", [])

        # Find current hour index
        current_iso_hour = datetime.now().strftime("%Y-%m-%dT%H:00")
        start_idx = 0
        for i, t_str in enumerate(hourly_times):
            if t_str >= current_iso_hour:
                start_idx = i
                break

        hourly_items: List[HourlyForecastItem] = []
        for i in range(start_idx, min(start_idx + 24, len(hourly_times))):
            h_code = hourly_codes[i] if i < len(hourly_codes) else 0
            h_desc_en, h_desc_kn = WMO_CODE_MAP.get(h_code, ("Fair", "ಸಾಧಾರಣ"))
            t_obj = datetime.fromisoformat(hourly_times[i])
            hourly_items.append(
                HourlyForecastItem(
                    time=t_obj.strftime("%I %p"),
                    temperature=float(hourly_temps[i]),
                    weather_code=h_code,
                    weather_desc=h_desc_en,
                    weather_desc_kn=h_desc_kn,
                    precipitation_prob=int(hourly_probs[i]) if i < len(hourly_probs) else 0,
                    is_day=bool(hourly_is_day[i]) if i < len(hourly_is_day) else True
                )
            )

        # Daily forecast (next 7 days)
        daily_times = daily.get("time", [])
        daily_max = daily.get("temperature_2m_max", [])
        daily_min = daily.get("temperature_2m_min", [])
        daily_probs = daily.get("precipitation_probability_max", [])
        daily_codes = daily.get("weather_code", [])

        daily_items: List[DailyForecastItem] = []
        for i in range(min(7, len(daily_times))):
            d_code = daily_codes[i] if i < len(daily_codes) else 0
            d_desc_en, d_desc_kn = WMO_CODE_MAP.get(d_code, ("Fair", "ಸಾಧಾರಣ"))
            d_date = datetime.strptime(daily_times[i], "%Y-%m-%d")
            day_name = "Today" if i == 0 else d_date.strftime("%a")
            day_name_kn = "ಇಂದು" if i == 0 else DAYS_KN.get(d_date.strftime("%A"), d_date.strftime("%a"))

            daily_items.append(
                DailyForecastItem(
                    date=daily_times[i],
                    day_name=day_name,
                    day_name_kn=day_name_kn,
                    min_temp=float(daily_min[i]),
                    max_temp=float(daily_max[i]),
                    weather_code=d_code,
                    weather_desc=d_desc_en,
                    weather_desc_kn=d_desc_kn,
                    precipitation_prob=int(daily_probs[i]) if i < len(daily_probs) else 0
                )
            )

        today_min = float(daily_min[0]) if daily_min else current_temp - 5
        today_max = float(daily_max[0]) if daily_max else current_temp + 5
        today_rain_prob = int(daily_probs[0]) if daily_probs else 10

        insight = cls._generate_insight(
            temp=current_temp,
            humidity=humidity,
            rain_prob=today_rain_prob,
            wind_speed=wind_spd,
            weather_code=w_code,
            crops=crops
        )

        prec_labels_kn = {
            "village": "ಗ್ರಾಮ ಮಟ್ಟ (ಸ್ಥಳೀಯ)",
            "taluk": "ತಾಲೂಕು ಮಟ್ಟ",
            "district": "ಜಿಲ್ಲಾ ಮಟ್ಟ",
            "state_default": "ರಾಜ್ಯ ಡೀಫಾಲ್ಟ್ (ಮಧ್ಯ ಕರ್ನಾಟಕ)"
        }

        weather_resp = FarmWeatherResponse(
            location_name=loc_name,
            location_name_kn=loc_name_kn,
            precision_level=prec_level, # type: ignore
            precision_label=prec_label,
            precision_label_kn=prec_labels_kn.get(prec_level, "ಜಿಲ್ಲಾ ಮಟ್ಟ"),
            latitude=resolved_lat,
            longitude=resolved_lon,
            current_temp=current_temp,
            feels_like=feels_like,
            humidity=humidity,
            wind_speed=wind_spd,
            wind_direction=wind_dir_en,
            wind_direction_kn=wind_dir_kn,
            precipitation=precip,
            precipitation_prob=today_rain_prob,
            cloud_cover=cloud,
            weather_code=w_code,
            weather_desc=desc_en,
            weather_desc_kn=desc_kn,
            is_day=is_day,
            today_min_temp=today_min,
            today_max_temp=today_max,
            hourly_forecast=hourly_items,
            daily_forecast=daily_items,
            agronomic_insight=insight,
            fetched_at=datetime.now().strftime("%I:%M %p"),
            is_cached=False
        )

        _WEATHER_CACHE[cache_key] = (now, weather_resp)
        return weather_resp

