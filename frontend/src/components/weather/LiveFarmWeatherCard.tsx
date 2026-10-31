import React, { useState, useEffect, useCallback } from 'react';
import {
  Cloud,
  CloudRain,
  Sun,
  CloudLightning,
  CloudDrizzle,
  Wind,
  Droplets,
  Thermometer,
  RotateCcw,
  MapPin,
  Sparkles,
  AlertTriangle,
  CheckCircle2,
  ChevronRight,
  ChevronDown
} from 'lucide-react';
import { FarmWeatherResponse, FarmerProfile } from '../../types';
import { api } from '../../services/api';

interface LiveFarmWeatherCardProps {
  profile: FarmerProfile;
  language: 'kn' | 'en';
}

const KARNATAKA_DISTRICTS = [
  'Bagalkot', 'Ballari', 'Belagavi', 'Bengaluru Urban', 'Bengaluru Rural',
  'Bidar', 'Chamarajanagar', 'Chikkaballapur', 'Chikkamagaluru', 'Chitradurga',
  'Dakshina Kannada', 'Davanagere', 'Dharwad', 'Gadag', 'Hassan',
  'Haveri', 'Kalaburagi', 'Kodagu', 'Kolar', 'Koppal',
  'Mandya', 'Mysuru', 'Raichur', 'Ramanagara', 'Shivamogga',
  'Tumakuru', 'Udupi', 'Uttara Kannada', 'Vijayanagara', 'Vijayapura', 'Yadgir'
];

export const LiveFarmWeatherCard: React.FC<LiveFarmWeatherCardProps> = ({
  profile,
  language
}) => {
  const [weather, setWeather] = useState<FarmWeatherResponse | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [isRefreshing, setIsRefreshing] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [selectedDistrict, setSelectedDistrict] = useState<string>(
    profile.location.district || 'Shivamogga'
  );
  const [isChangingLocation, setIsChangingLocation] = useState<boolean>(false);
  const [activeTab, setActiveTab] = useState<'hourly' | 'daily'>('hourly');

  const fetchWeather = useCallback(async (districtName: string, force: boolean = false) => {
    if (force) setIsRefreshing(true);
    else setIsLoading(true);
    setError(null);

    try {
      const data = await api.getWeather({
        village: profile.location.village,
        taluk: profile.location.taluk,
        district: districtName,
        state: profile.location.state || 'Karnataka',
        crops: profile.crops,
        refresh: force
      });
      setWeather(data);
    } catch (err: any) {
      console.error('Failed to load weather:', err);
      setError(
        language === 'kn'
          ? 'ಹವಾಮಾನ ಮಾಹಿತಿ ಲೋಡ್ ಮಾಡಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ಮರುಪ್ರಯತ್ನಿಸಿ.'
          : 'Unable to load live weather. Please retry.'
      );
    } finally {
      setIsLoading(false);
      setIsRefreshing(false);
    }
  }, [profile.location.village, profile.location.taluk, profile.location.state, profile.crops, language]);

  useEffect(() => {
    const targetDistrict = profile.location.district || selectedDistrict || 'Shivamogga';
    setSelectedDistrict(targetDistrict);
    fetchWeather(targetDistrict, false);
  }, [profile.location.district]);

  const handleRefresh = () => {
    fetchWeather(selectedDistrict, true);
  };

  const handleSelectDistrict = (d: string) => {
    setSelectedDistrict(d);
    setIsChangingLocation(false);
    fetchWeather(d, true);
  };

  const getWeatherIcon = (code: number, isDay: boolean = true) => {
    if (code === 0) return <Sun className="w-8 h-8 text-[#D7A85B] animate-pulse" />;
    if ([1, 2, 3].includes(code)) return <Cloud className="w-8 h-8 text-[#4A6B5B]" />;
    if ([51, 53, 55].includes(code)) return <CloudDrizzle className="w-8 h-8 text-cyan-600" />;
    if ([61, 63, 65, 80, 81, 82].includes(code)) return <CloudRain className="w-8 h-8 text-blue-600" />;
    if ([95, 96, 99].includes(code)) return <CloudLightning className="w-8 h-8 text-amber-600" />;
    return isDay ? <Sun className="w-8 h-8 text-[#D7A85B]" /> : <Cloud className="w-8 h-8 text-[#4A6B5B]" />;
  };

  if (isLoading && !weather) {
    return (
      <div className="rounded-3xl bg-white p-7 border border-[#E2D9C8] shadow-md animate-pulse">
        <div className="flex items-center justify-between pb-4 border-b border-[#E2D9C8]">
          <div className="h-5 bg-[#EBE5D8] rounded w-1/3" />
          <div className="h-4 bg-[#EBE5D8] rounded w-1/4" />
        </div>
        <div className="py-6 space-y-4">
          <div className="h-10 bg-[#EBE5D8] rounded w-1/2" />
          <div className="grid grid-cols-3 gap-3">
            <div className="h-14 bg-[#EBE5D8] rounded-xl" />
            <div className="h-14 bg-[#EBE5D8] rounded-xl" />
            <div className="h-14 bg-[#EBE5D8] rounded-xl" />
          </div>
        </div>
      </div>
    );
  }

  if (error || !weather) {
    return (
      <div className="rounded-3xl bg-white p-6 border border-[#E2D9C8] shadow-sm text-center space-y-3">
        <AlertTriangle className="w-8 h-8 text-[#C66F4E] mx-auto" />
        <p className="text-xs text-[#6B7468] font-kannada">{error || 'Weather temporarily unavailable'}</p>
        <button
          onClick={() => handleRefresh()}
          className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-[#FAF7F0] border border-[#E2D9C8] text-xs font-bold text-[#183B2B] hover:bg-[#EBE5D8]"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>{language === 'kn' ? 'ಮರುಪ್ರಯತ್ನಿಸಿ' : 'Retry'}</span>
        </button>
      </div>
    );
  }

  const insight = weather.agronomic_insight;

  return (
    <div className="rounded-3xl bg-white p-6 sm:p-7 border border-[#E2D9C8] shadow-lg space-y-5 transition-all">
      
      {/* Header: Title, Precision Pill & Refresh Action */}
      <div className="flex items-start justify-between pb-4 border-b border-[#E2D9C8]">
        <div className="space-y-1">
          <div className="flex items-center space-x-2">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse" />
            <span className="text-xs font-mono uppercase tracking-wider text-[#183B2B] font-extrabold">
              {language === 'kn' ? 'ನಿಮ್ಮ ಹೊಲದ ಸ್ಥಳೀಯ ಹವಾಮಾನ' : 'Your Farm, Right Now'}
            </span>
          </div>
          
          {/* Location Selector Pill */}
          <div className="relative">
            <button
              onClick={() => setIsChangingLocation(!isChangingLocation)}
              className="group flex items-center space-x-1.5 text-xs text-[#282C27] hover:text-[#183B2B] font-bold bg-[#FAF7F0] hover:bg-[#EBE5D8] px-2.5 py-1 rounded-lg border border-[#E2D9C8] transition-colors"
              title={language === 'kn' ? 'ಸ್ಥಳ ಬದಲಾಯಿಸಿ' : 'Change location'}
            >
              <MapPin className="w-3.5 h-3.5 text-[#C66F4E]" />
              <span className="font-kannada">
                {language === 'kn' ? weather.location_name_kn : weather.location_name}
              </span>
              <ChevronDown className="w-3 h-3 text-[#6B7468] group-hover:text-[#183B2B]" />
            </button>

            {/* District Dropdown Selector */}
            {isChangingLocation && (
              <div className="absolute top-8 left-0 z-50 w-60 max-h-60 overflow-y-auto rounded-2xl bg-white border border-[#E2D9C8] shadow-2xl p-2 space-y-1">
                <span className="text-[10px] font-mono text-[#6B7468] px-2 font-bold uppercase block">
                  {language === 'kn' ? 'ಜಿಲ್ಲೆ ಆಯ್ಕೆಮಾಡಿ:' : 'Select Karnataka District:'}
                </span>
                {KARNATAKA_DISTRICTS.map((dist) => (
                  <button
                    key={dist}
                    onClick={() => handleSelectDistrict(dist)}
                    className={`w-full text-left px-2.5 py-1.5 rounded-lg text-xs font-kannada transition-colors ${
                      selectedDistrict.toLowerCase() === dist.toLowerCase()
                        ? 'bg-[#183B2B] text-white font-bold'
                        : 'hover:bg-[#FAF7F0] text-[#282C27]'
                    }`}
                  >
                    {dist}
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Precision Badge & Refresh Button */}
        <div className="flex items-center space-x-2 flex-shrink-0">
          <span
            className="text-[10px] font-mono font-bold px-2.5 py-1 rounded-full bg-[#FAF7F0] border border-[#E2D9C8] text-[#183B2B]"
            title={language === 'kn' ? weather.precision_label_kn : weather.precision_label}
          >
            {language === 'kn' ? weather.precision_label_kn : weather.precision_label}
          </span>
          <button
            onClick={handleRefresh}
            disabled={isRefreshing}
            className="w-7 h-7 rounded-lg bg-[#FAF7F0] hover:bg-[#EBE5D8] border border-[#E2D9C8] flex items-center justify-center text-[#183B2B] transition-transform active:scale-95 disabled:opacity-50"
            title={language === 'kn' ? 'ಹವಾಮಾನ ಅಪ್ಡೇಟ್ ಮಾಡಿ' : 'Refresh live weather'}
          >
            <RotateCcw className={`w-3.5 h-3.5 ${isRefreshing ? 'animate-spin text-[#B08233]' : ''}`} />
          </button>
        </div>
      </div>

      {/* Primary Current Metrics Box */}
      <div className="grid grid-cols-12 gap-4 items-center bg-[#FAF7F0] rounded-2xl p-4 border border-[#E2D9C8]">
        {/* Left: Big Temp & Condition */}
        <div className="col-span-6 sm:col-span-7 flex items-center space-x-3.5">
          <div className="w-14 h-14 rounded-2xl bg-white border border-[#E2D9C8] flex items-center justify-center shadow-sm flex-shrink-0">
            {getWeatherIcon(weather.weather_code, weather.is_day)}
          </div>
          <div>
            <div className="flex items-baseline space-x-1">
              <span className="text-3xl sm:text-4xl font-extrabold font-mono text-[#183B2B] tracking-tight">
                {Math.round(weather.current_temp)}°
              </span>
              <span className="text-xs font-mono font-bold text-[#6B7468]">C</span>
            </div>
            <p className="text-xs font-bold font-kannada text-[#183B2B] line-clamp-1">
              {language === 'kn' ? weather.weather_desc_kn : weather.weather_desc}
            </p>
            <span className="text-[10px] text-[#6B7468] font-sans">
              {language === 'kn'
                ? `ಅನಿಸುವುದು ${Math.round(weather.feels_like)}°C • ಕನಿಷ್ಠ ${Math.round(weather.today_min_temp)}° / ಗರಿಷ್ಠ ${Math.round(weather.today_max_temp)}°`
                : `Feels ${Math.round(weather.feels_like)}°C • Min ${Math.round(weather.today_min_temp)}° / Max ${Math.round(weather.today_max_temp)}°`}
            </span>
          </div>
        </div>

        {/* Right: Key Agronomic Parameters */}
        <div className="col-span-6 sm:col-span-5 grid grid-cols-2 gap-2 text-center text-xs">
          <div className="p-2 rounded-xl bg-white border border-[#E2D9C8] shadow-xs">
            <div className="flex items-center justify-center space-x-1 text-[#6B7468] mb-0.5">
              <Droplets className="w-3 h-3 text-cyan-600" />
              <span className="text-[10px] font-mono">{language === 'kn' ? 'ಆರ್ದ್ರತೆ' : 'Humidity'}</span>
            </div>
            <span className="font-mono font-bold text-[#183B2B] text-xs">{weather.humidity}%</span>
          </div>

          <div className="p-2 rounded-xl bg-white border border-[#E2D9C8] shadow-xs">
            <div className="flex items-center justify-center space-x-1 text-[#6B7468] mb-0.5">
              <CloudRain className="w-3 h-3 text-blue-600" />
              <span className="text-[10px] font-mono">{language === 'kn' ? 'ಮಳೆ ಸಂಭವ' : 'Rain'}</span>
            </div>
            <span className="font-mono font-bold text-[#183B2B] text-xs">{weather.precipitation_prob}%</span>
          </div>

          <div className="p-2 rounded-xl bg-white border border-[#E2D9C8] shadow-xs">
            <div className="flex items-center justify-center space-x-1 text-[#6B7468] mb-0.5">
              <Wind className="w-3 h-3 text-[#B08233]" />
              <span className="text-[10px] font-mono">{language === 'kn' ? 'ಗಾಳಿ' : 'Wind'}</span>
            </div>
            <span className="font-mono font-bold text-[#183B2B] text-[11px]">
              {Math.round(weather.wind_speed)} km/h
            </span>
          </div>

          <div className="p-2 rounded-xl bg-white border border-[#E2D9C8] shadow-xs">
            <div className="flex items-center justify-center space-x-1 text-[#6B7468] mb-0.5">
              <Cloud className="w-3 h-3 text-[#4A6B5B]" />
              <span className="text-[10px] font-mono">{language === 'kn' ? 'ಮೋಡ' : 'Cloud'}</span>
            </div>
            <span className="font-mono font-bold text-[#183B2B] text-xs">{weather.cloud_cover}%</span>
          </div>
        </div>
      </div>

      {/* Tabs: 24h Hourly vs 7-Day Forecast */}
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <div className="inline-flex rounded-xl bg-[#FAF7F0] p-1 border border-[#E2D9C8] text-xs font-bold">
            <button
              onClick={() => setActiveTab('hourly')}
              className={`px-3 py-1 rounded-lg transition-all ${
                activeTab === 'hourly'
                  ? 'bg-white text-[#183B2B] shadow-xs'
                  : 'text-[#6B7468] hover:text-[#183B2B]'
              }`}
            >
              {language === 'kn' ? '24 ಗಂಟೆ ಮುನ್ಸೂಚನೆ' : '24h Hourly'}
            </button>
            <button
              onClick={() => setActiveTab('daily')}
              className={`px-3 py-1 rounded-lg transition-all ${
                activeTab === 'daily'
                  ? 'bg-white text-[#183B2B] shadow-xs'
                  : 'text-[#6B7468] hover:text-[#183B2B]'
              }`}
            >
              {language === 'kn' ? '7 ದಿನಗಳ ಮುನ್ಸೂಚನೆ' : '7-Day Outlook'}
            </button>
          </div>
          <span className="text-[10px] font-mono text-[#6B7468]">
            {language === 'kn' ? `ಅಪ್ಡೇಟ್: ${weather.fetched_at}` : `Updated: ${weather.fetched_at}`}
          </span>
        </div>

        {/* A. 24h Hourly Horizontal Strip */}
        {activeTab === 'hourly' && (
          <div className="flex space-x-2.5 overflow-x-auto pb-2 scrollbar-thin">
            {weather.hourly_forecast.slice(0, 16).map((item, idx) => (
              <div
                key={idx}
                className="flex-shrink-0 w-16 p-2 rounded-xl bg-[#FAF7F0] border border-[#E2D9C8] text-center space-y-1 hover:border-[#183B2B] transition-colors"
              >
                <span className="text-[10px] font-mono text-[#6B7468] block">{item.time}</span>
                <div className="flex justify-center py-0.5">
                  <span className="text-base">
                    {item.weather_code === 0 ? '☀️' : [1, 2, 3].includes(item.weather_code) ? '⛅' : '🌧️'}
                  </span>
                </div>
                <span className="font-mono font-bold text-xs text-[#183B2B] block">
                  {Math.round(item.temperature)}°
                </span>
                {item.precipitation_prob > 0 && (
                  <span className="text-[9px] font-mono font-bold text-blue-600 block">
                    {item.precipitation_prob}%
                  </span>
                )}
              </div>
            ))}
          </div>
        )}

        {/* B. 7-Day Forecast Grid */}
        {activeTab === 'daily' && (
          <div className="space-y-1.5">
            {weather.daily_forecast.map((d, idx) => (
              <div
                key={idx}
                className="flex items-center justify-between p-2.5 rounded-xl bg-[#FAF7F0] border border-[#E2D9C8] text-xs"
              >
                <div className="flex items-center space-x-2.5 w-24">
                  <span className="font-kannada font-bold text-[#183B2B]">
                    {language === 'kn' ? d.day_name_kn : d.day_name}
                  </span>
                </div>
                <div className="flex items-center space-x-2 flex-1 justify-center">
                  <span className="text-sm">
                    {d.weather_code === 0 ? '☀️' : [1, 2, 3].includes(d.weather_code) ? '⛅' : '🌧️'}
                  </span>
                  <span className="text-[11px] text-[#4A5148] font-kannada line-clamp-1">
                    {language === 'kn' ? d.weather_desc_kn : d.weather_desc}
                  </span>
                </div>
                <div className="flex items-center space-x-3 w-28 justify-end">
                  {d.precipitation_prob > 10 && (
                    <span className="text-[10px] font-mono font-bold text-blue-600 bg-blue-50 px-1.5 py-0.5 rounded">
                      {d.precipitation_prob}%
                    </span>
                  )}
                  <span className="font-mono font-bold text-[#183B2B]">
                    {Math.round(d.max_temp)}° / <span className="text-[#6B7468]">{Math.round(d.min_temp)}°</span>
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Contextual Agronomic Suggestion Box */}
      <div
        className={`rounded-2xl p-4 border transition-all ${
          insight.alert_level === 'warning'
            ? 'bg-[#F7E4DE] border-[#C66F4E] text-[#9E4E30]'
            : insight.alert_level === 'advisory'
            ? 'bg-[#FBF4E4] border-[#D7A85B] text-[#B08233]'
            : 'bg-[#DEE4D2]/40 border-[#A8B58A] text-[#183B2B]'
        }`}
      >
        <div className="flex items-start space-x-3">
          <div className="w-7 h-7 rounded-lg bg-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
            {insight.alert_level === 'warning' ? (
              <AlertTriangle className="w-4 h-4 text-[#C66F4E]" />
            ) : insight.alert_level === 'advisory' ? (
              <Sparkles className="w-4 h-4 text-[#B08233]" />
            ) : (
              <CheckCircle2 className="w-4 h-4 text-emerald-600" />
            )}
          </div>
          <div className="space-y-1 text-xs">
            <span className="font-extrabold uppercase font-mono tracking-wider block">
              {language === 'kn' ? insight.title_kn : insight.title}
            </span>
            <p className="font-kannada leading-relaxed text-[#282C27] text-[12px]">
              {language === 'kn' ? insight.advice_kn : insight.advice}
            </p>
          </div>
        </div>
      </div>

    </div>
  );
};

