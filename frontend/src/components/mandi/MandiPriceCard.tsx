import React, { useState, useEffect, useCallback } from 'react';
import {
  TrendingUp,
  TrendingDown,
  Minus,
  RefreshCw,
  Store,
  MapPin,
  Wheat,
  ShieldCheck,
  Calendar,
  AlertCircle,
  Filter
} from 'lucide-react';
import { MandiPriceItem, MandiPricesResponse, FarmerProfile } from '../../types';
import { api } from '../../services/api';

interface MandiPriceCardProps {
  profile: FarmerProfile;
  language: 'kn' | 'en';
}

export const MandiPriceCard: React.FC<MandiPriceCardProps> = ({
  profile,
  language
}) => {
  const [data, setData] = useState<MandiPricesResponse | null>(null);
  const [commodities, setCommodities] = useState<Array<{ name_en: string; name_kn: string }>>([]);
  const [selectedCommodity, setSelectedCommodity] = useState<string>('all');
  const [selectedDistrict, setSelectedDistrict] = useState<string>(profile.location.district || 'all');
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [isRefreshing, setIsRefreshing] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Load available commodities on mount
  useEffect(() => {
    api.getMandiCommodities()
      .then(setCommodities)
      .catch((e) => console.warn('Could not load commodities list:', e));
  }, []);

  // Update selected district when profile updates
  useEffect(() => {
    if (profile.location.district) {
      setSelectedDistrict(profile.location.district);
    }
  }, [profile.location.district]);

  const loadPrices = useCallback(async (force: boolean = false) => {
    if (force) setIsRefreshing(true);
    else setIsLoading(true);
    setError(null);

    try {
      const res = await api.getMandiPrices({
        district: selectedDistrict !== 'all' ? selectedDistrict : undefined,
        commodity: selectedCommodity !== 'all' ? selectedCommodity : undefined
      });
      setData(res);
    } catch (err: any) {
      console.error('Failed to load mandi prices:', err);
      setError(
        language === 'kn'
          ? 'ಮಂಡಿ ಧಾರಣೆ ಮಾಹಿತಿ ಪಡೆಯಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ಮರುಪ್ರಯತ್ನಿಸಿ.'
          : 'Unable to load APMC Mandi prices. Please retry.'
      );
    } finally {
      setIsLoading(false);
      setIsRefreshing(false);
    }
  }, [selectedDistrict, selectedCommodity, language]);

  useEffect(() => {
    loadPrices(false);
  }, [loadPrices]);

  const getTrendIcon = (trend: string) => {
    if (trend === 'rising') {
      return (
        <span className="inline-flex items-center space-x-1 text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full text-[11px] font-bold font-mono">
          <TrendingUp className="w-3.5 h-3.5 stroke-[2.5]" />
          <span>{language === 'kn' ? 'ಏರಿಕೆ' : 'Rising'}</span>
        </span>
      );
    }
    if (trend === 'falling') {
      return (
        <span className="inline-flex items-center space-x-1 text-amber-700 bg-amber-50 px-2 py-0.5 rounded-full text-[11px] font-bold font-mono">
          <TrendingDown className="w-3.5 h-3.5 stroke-[2.5]" />
          <span>{language === 'kn' ? 'ಇಳಿಕೆ' : 'Falling'}</span>
        </span>
      );
    }
    return (
      <span className="inline-flex items-center space-x-1 text-gray-600 bg-gray-100 px-2 py-0.5 rounded-full text-[11px] font-bold font-mono">
        <Minus className="w-3.5 h-3.5 stroke-[2.5]" />
        <span>{language === 'kn' ? 'ಸ್ಥಿರ' : 'Stable'}</span>
      </span>
    );
  };

  return (
    <div className="rounded-[2rem] bg-white border border-[#E2D9C8] p-6 sm:p-7 shadow-sm hover:shadow-md transition-all space-y-6">
      
      {/* 1. Header & Source Badge */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-[#E2D9C8]">
        <div className="flex items-center space-x-3.5">
          <div className="w-12 h-12 rounded-2xl bg-[#183B2B] text-[#D7A85B] flex items-center justify-center flex-shrink-0 shadow-sm">
            <Store className="w-6 h-6 stroke-[2]" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-[10px] font-mono uppercase tracking-wider px-2 py-0.5 rounded-full bg-[#FAF7F0] text-[#B08233] font-bold border border-[#E2D9C8]">
                APMC Live Market Rates
              </span>
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            </div>
            <h3 className="text-xl font-extrabold font-kannada text-[#183B2B]">
              {language === 'kn' ? 'ಕರ್ನಾಟಕ ಎ.ಪಿ.ಎಂ.ಸಿ ಮಂಡಿ ಧಾರಣೆ' : 'Karnataka APMC Mandi Prices'}
            </h3>
          </div>
        </div>

        {/* Refresh & Provenance */}
        <div className="flex items-center space-x-3 self-end sm:self-auto text-xs text-[#6B7468]">
          <span className="font-mono text-[11px] hidden sm:inline">
            {data?.last_updated ? `${data.last_updated}` : ''}
          </span>
          <button
            onClick={() => loadPrices(true)}
            disabled={isRefreshing || isLoading}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-[#FAF7F0] hover:bg-[#EBE5D8] border border-[#E2D9C8] text-[#183B2B] font-semibold transition active:scale-95 disabled:opacity-50"
            title="Refresh Mandi Rates"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${isRefreshing ? 'animate-spin' : ''}`} />
            <span className="text-xs">{language === 'kn' ? 'ನವೀಕರಿಸಿ' : 'Refresh'}</span>
          </button>
        </div>
      </div>

      {/* 2. Filter Bar (Commodity & Market/District) */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5 bg-[#FAF7F0] p-3.5 rounded-2xl border border-[#E2D9C8]">
        
        {/* Commodity Selector */}
        <div className="space-y-1">
          <label className="text-[11px] font-mono text-[#6B7468] uppercase font-bold flex items-center space-x-1">
            <Wheat className="w-3 h-3 text-[#B08233]" />
            <span>{language === 'kn' ? 'ಬೆಳೆ / ಧಾನ್ಯ ಆಯ್ಕೆ:' : 'Filter by Crop:'}</span>
          </label>
          <select
            value={selectedCommodity}
            onChange={(e) => setSelectedCommodity(e.target.value)}
            className="w-full bg-white border border-[#E2D9C8] rounded-xl px-3 py-2 text-xs font-kannada text-[#183B2B] font-semibold focus:outline-none focus:border-[#D7A85B]"
          >
            <option value="all">
              {language === 'kn' ? 'ಎಲ್ಲಾ ಬೆಳೆಗಳು (All Crops)' : 'All Tracked Crops'}
            </option>
            {commodities.map((c) => (
              <option key={c.name_en} value={c.name_en}>
                {language === 'kn' ? `${c.name_kn} (${c.name_en})` : `${c.name_en} (${c.name_kn})`}
              </option>
            ))}
          </select>
        </div>

        {/* District Filter */}
        <div className="space-y-1">
          <label className="text-[11px] font-mono text-[#6B7468] uppercase font-bold flex items-center space-x-1">
            <MapPin className="w-3 h-3 text-[#B08233]" />
            <span>{language === 'kn' ? 'ಜಿಲ್ಲೆ / ಮಾರುಕಟ್ಟೆ:' : 'District / APMC:'}</span>
          </label>
          <select
            value={selectedDistrict}
            onChange={(e) => setSelectedDistrict(e.target.value)}
            className="w-full bg-white border border-[#E2D9C8] rounded-xl px-3 py-2 text-xs font-kannada text-[#183B2B] font-semibold focus:outline-none focus:border-[#D7A85B]"
          >
            <option value="all">
              {language === 'kn' ? 'ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳು (All Karnataka)' : 'All Karnataka Districts'}
            </option>
            <option value="Mandya">{language === 'kn' ? 'ಮಂಡ್ಯ (Mandya)' : 'Mandya'}</option>
            <option value="Mysuru">{language === 'kn' ? 'ಮೈಸೂರು (Mysuru)' : 'Mysuru'}</option>
            <option value="Shivamogga">{language === 'kn' ? 'ಶಿವಮೊಗ್ಗ (Shivamogga)' : 'Shivamogga'}</option>
            <option value="Hassan">{language === 'kn' ? 'ಹಾಸನ (Hassan)' : 'Hassan'}</option>
            <option value="Davanagere">{language === 'kn' ? 'ದಾವಣಗೆರೆ (Davanagere)' : 'Davanagere'}</option>
            <option value="Kalaburagi">{language === 'kn' ? 'ಕಲಬುರಗಿ (Kalaburagi)' : 'Kalaburagi'}</option>
            <option value="Dharwad">{language === 'kn' ? 'ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ (Hubballi)' : 'Dharwad / Hubballi'}</option>
            <option value="Raichur">{language === 'kn' ? 'ರಾಯಚೂರು (Raichur)' : 'Raichur'}</option>
            <option value="Tumakuru">{language === 'kn' ? 'ತುಮಕೂರು / ತಿಪಟೂರು (Tiptur)' : 'Tumakuru / Tiptur'}</option>
            <option value="Bengaluru Urban">{language === 'kn' ? 'ಬೆಂಗಳೂರು (Yeshwanthpur)' : 'Bengaluru (Yeshwanthpur)'}</option>
            <option value="Belagavi">{language === 'kn' ? 'ಬೆಳಗಾವಿ (Belagavi)' : 'Belagavi'}</option>
            <option value="Kolar">{language === 'kn' ? 'ಕೋಲಾರ (Kolar)' : 'Kolar'}</option>
          </select>
        </div>

      </div>

      {/* 3. Error State */}
      {error && (
        <div className="p-4 rounded-xl bg-red-50 border border-red-200 text-xs text-red-800 flex items-center space-x-2">
          <AlertCircle className="w-4 h-4 text-red-600 flex-shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {/* 4. Price Table / Cards Grid */}
      {isLoading ? (
        <div className="py-12 flex flex-col items-center justify-center space-y-2 text-[#6B7468]">
          <RefreshCw className="w-6 h-6 animate-spin text-[#D7A85B]" />
          <span className="text-xs font-kannada">
            {language === 'kn' ? 'ಮಂಡಿ ಧಾರಣೆ ಪಡೆಯಲಾಗುತ್ತಿದೆ...' : 'Loading APMC market prices...'}
          </span>
        </div>
      ) : !data || data.prices.length === 0 ? (
        <div className="py-10 text-center space-y-2 bg-[#FAF7F0] rounded-2xl border border-dashed border-[#E2D9C8]">
          <Store className="w-8 h-8 text-[#A8B58A] mx-auto" />
          <p className="text-xs text-[#6B7468] font-kannada">
            {language === 'kn'
              ? 'ಆಯ್ಕೆಮಾಡಿದ ಫಿಲ್ಟರ್‌ಗೆ ಯಾವುದೇ ದರಗಳು ಲಭ್ಯವಿಲ್ಲ. ದಯವಿಟ್ಟು ಬೇರೆ ಬೆಳೆ ಅಥವಾ ಜಿಲ್ಲೆ ಆಯ್ಕೆಮಾಡಿ.'
              : 'No mandi prices found for the selected filter. Try selecting another crop or district.'}
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {data.prices.map((item, idx) => (
            <div
              key={idx}
              className="rounded-2xl p-4 bg-[#FAF7F0] border border-[#E2D9C8] hover:border-[#D7A85B] transition-all space-y-3 flex flex-col justify-between"
            >
              {/* Header: Commodity & Trend */}
              <div className="flex items-start justify-between">
                <div>
                  <h4 className="text-base font-extrabold font-kannada text-[#183B2B]">
                    {language === 'kn' ? item.commodity_kn : item.commodity}
                  </h4>
                  <span className="text-[11px] text-[#6B7468] font-mono">
                    {item.variety}
                  </span>
                </div>
                {getTrendIcon(item.trend)}
              </div>

              {/* Market Yard & District */}
              <div className="flex items-center space-x-1.5 text-xs text-[#4A5148] font-kannada">
                <MapPin className="w-3.5 h-3.5 text-[#B08233] flex-shrink-0" />
                <span className="font-semibold">
                  {language === 'kn' ? item.market_kn : item.market}
                </span>
              </div>

              {/* Price Numbers Box */}
              <div className="p-3 bg-white rounded-xl border border-[#E2D9C8] space-y-1.5">
                <div className="flex items-baseline justify-between">
                  <span className="text-[10px] font-mono uppercase text-[#6B7468] font-bold">
                    {language === 'kn' ? 'ಮಾದರಿ ಬೆಲೆ (Modal):' : 'Modal Price:'}
                  </span>
                  <span className="font-mono text-lg font-extrabold text-[#183B2B]">
                    ₹{item.modal_price.toLocaleString('en-IN')}
                    <span className="text-[10px] text-[#6B7468] font-normal ml-1">/ ಕ್ವಿಂಟಾಲ್</span>
                  </span>
                </div>

                <div className="flex items-center justify-between text-[11px] text-[#6B7468] font-mono pt-1 border-t border-dashed border-[#E2D9C8]">
                  <span>Min: ₹{item.min_price.toLocaleString('en-IN')}</span>
                  <span>Max: ₹{item.max_price.toLocaleString('en-IN')}</span>
                </div>
              </div>

              {/* MSP Reference Banner */}
              {item.msp && (
                <div className="flex items-center justify-between text-[10px] font-mono px-2 py-1 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200">
                  <span className="font-bold">Govt MSP: ₹{item.msp.toLocaleString('en-IN')}</span>
                  <span className="text-emerald-700 font-semibold">
                    {item.modal_price >= item.msp ? '✓ Above MSP' : '⚠ Below MSP'}
                  </span>
                </div>
              )}

            </div>
          ))}
        </div>
      )}

      {/* 5. Footer Provenance Notice */}
      <div className="flex items-center justify-between text-[11px] text-[#6B7468] pt-2 border-t border-[#E2D9C8]">
        <div className="flex items-center space-x-1.5">
          <ShieldCheck className="w-3.5 h-3.5 text-[#183B2B]" />
          <span>Karnataka State Agricultural Marketing Board (KSAMB) & Agmarknet</span>
        </div>
        <span className="font-mono text-[10px]">
          {data?.total_records || 0} Mandi entries
        </span>
      </div>

    </div>
  );
};

