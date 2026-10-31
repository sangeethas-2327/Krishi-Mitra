import React, { useState } from 'react';
import { 
  Sprout, 
  MapPin, 
  Layers, 
  Wheat, 
  Trees,
  Droplets, 
  SunMedium, 
  HelpCircle, 
  CheckCircle2, 
  AlertCircle, 
  Clock, 
  Edit3, 
  ChevronRight,
  ShieldCheck,
  History,
  Info
} from 'lucide-react';
import { translations } from '../../utils/translations';
import { FarmerProfile } from '../../types';
import { ProfileEditorModal } from '../farmer/ProfileEditorModal';
import { MandiPriceCard } from '../mandi/MandiPriceCard';

interface MyFarmViewProps {
  profile: FarmerProfile;
  language: 'kn' | 'en';
  onUpdateProfile: (updates: Partial<FarmerProfile>) => Promise<void>;
  onNavigateToVoice: () => void;
  onNavigateToSchemes: () => void;
}

export const MyFarmView: React.FC<MyFarmViewProps> = ({
  profile,
  language,
  onUpdateProfile,
  onNavigateToVoice,
  onNavigateToSchemes
}) => {
  const t = translations[language];
  const [isEditorOpen, setIsEditorOpen] = useState(false);

  // Field status helper: confirmed | needs_clarification | not_provided
  const getFieldStatus = (fieldName: string, value: any) => {
    if (value === null || value === undefined || value === '' || (Array.isArray(value) && value.length === 0)) {
      return {
        label: language === 'kn' ? 'ಮಾಹಿತಿ ಅಗತ್ಯವಿದೆ' : 'Not provided',
        bg: 'bg-ivory border-ivory-border text-charcoal-muted',
        icon: AlertCircle,
        color: 'text-charcoal-muted'
      };
    }
    if (profile.confirmed_fields && profile.confirmed_fields.includes(fieldName)) {
      return {
        label: language === 'kn' ? 'ದೃಢೀಕರಿಸಲಾಗಿದೆ' : 'Confirmed',
        bg: 'bg-emerald-50 border-emerald-200 text-emerald-800',
        icon: CheckCircle2,
        color: 'text-emerald-600'
      };
    }
    return {
      label: language === 'kn' ? 'ಪರಿಶೀಲಿಸಿ' : 'Inferred',
      bg: 'bg-harvest/15 border-harvest/30 text-harvest-dark',
      icon: Clock,
      color: 'text-harvest-dark'
    };
  };

  // Botanical crop metadata helper (Lucide icon setup, no emojis)
  const getCropMeta = (cropName: string) => {
    const lower = cropName.toLowerCase();
    if (lower.includes('arecanut') || lower.includes('adike')) {
      return { icon: Trees, kannada: 'ಅಡಿಕೆ', en: 'Arecanut', tag: 'Perennial' };
    }
    if (lower.includes('paddy') || lower.includes('bhatta') || lower.includes('rice')) {
      return { icon: Wheat, kannada: 'ಭತ್ತ', en: 'Paddy', tag: 'Food Grain' };
    }
    if (lower.includes('coconut') || lower.includes('tengu')) {
      return { icon: Trees, kannada: 'ತೆಂಗು', en: 'Coconut', tag: 'Perennial' };
    }
    if (lower.includes('sugarcane') || lower.includes('kabbu')) {
      return { icon: Sprout, kannada: 'ಕಬ್ಬು', en: 'Sugarcane', tag: 'Commercial' };
    }
    if (lower.includes('ragi')) {
      return { icon: Wheat, kannada: 'ರಾಗಿ', en: 'Finger Millet', tag: 'Dryland' };
    }
    if (lower.includes('maize') || lower.includes('jola')) {
      return { icon: Wheat, kannada: 'ಮೆಕ್ಕೆಜೋಳ / ಜೋಳ', en: 'Maize / Sorghum', tag: 'Grain' };
    }
    return { icon: Sprout, kannada: cropName, en: cropName, tag: 'Crop' };
  };

  const districtStatus = getFieldStatus('location.district', profile.location.district);
  const landStatus = getFieldStatus('land_area.value_acres', profile.land_area.value_acres);
  const cropsStatus = getFieldStatus('crops', profile.crops);
  const ownershipStatus = getFieldStatus('ownership', profile.ownership);
  const irrigationStatus = getFieldStatus('irrigation', profile.irrigation?.has_irrigation);

  return (
    <div className="max-w-6xl mx-auto space-y-8 pb-20 animate-fadeIn">
      
      {/* 1. Farm Header & Action Bar */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 p-8 rounded-[2rem] bg-white border border-ivory-border shadow-editorial">
        <div className="space-y-1.5">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-forest text-ivory text-xs font-mono tracking-wider uppercase">
            <Sprout className="w-3.5 h-3.5 text-harvest" />
            <span>Digital Agricultural Identity</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold font-kannada text-charcoal">
            {language === 'kn' ? 'ನನ್ನ ಕೃಷಿ ವಿವರ (ಫಾರ್ಮ್ ಪ್ರೊಫೈಲ್)' : 'My Farm Agricultural Identity'}
          </h2>
          <p className="text-xs sm:text-sm text-charcoal-muted font-kannada">
            {language === 'kn'
              ? 'ಧ್ವನಿ ಸಂಭಾಷಣೆಯಿಂದ ಗುರುತಿಸಲಾದ ಎಲ್ಲಾ ಜಮೀನು, ಬೆಳೆ ಮತ್ತು ನೀರಾವರಿ ಸೌಲಭ್ಯಗಳ ಪಾರದರ್ಶಕ ವಿವರ.'
              : 'Structured parameters extracted from conversational speech with full provenance and edit history.'}
          </p>
        </div>

        <div className="flex items-center space-x-3">
          <button
            onClick={() => setIsEditorOpen(true)}
            className="flex items-center space-x-2 px-5 py-3 rounded-xl bg-forest hover:bg-forest-700 text-ivory text-xs font-semibold font-kannada transition-all shadow-sm"
          >
            <Edit3 className="w-4 h-4 text-harvest" />
            <span>{t.editProfile}</span>
          </button>

          <button
            onClick={onNavigateToSchemes}
            className="flex items-center space-x-2 px-5 py-3 rounded-xl bg-harvest hover:bg-[#B08233] text-forest-950 text-xs font-bold font-kannada transition-all shadow-sm"
          >
            <span>{language === 'kn' ? 'ಯೋಜನೆಗಳಿಗೆ ಹೋಲಿಸಿ' : 'Match Schemes'}</span>
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* 2. Visual Farm Identity Grid */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-6">
        
        {/* Farm Location Dossier */}
        <div className="md:col-span-6 lg:col-span-4 rounded-2xl bg-white p-6 border border-ivory-border shadow-editorial space-y-4">
          <div className="flex items-center justify-between pb-3 border-b border-ivory-border">
            <div className="flex items-center space-x-2.5">
              <div className="w-8 h-8 rounded-xl bg-terracotta/10 text-terracotta flex items-center justify-center">
                <MapPin className="w-4 h-4" />
              </div>
              <h3 className="font-bold text-sm text-charcoal font-kannada">{t.district} / {t.taluk}</h3>
            </div>
            <span className={`text-[10px] font-mono px-2 py-0.5 rounded-full border ${districtStatus.bg}`}>
              {districtStatus.label}
            </span>
          </div>

          <div className="space-y-3 font-kannada text-xs">
            <div className="flex justify-between py-1 border-b border-dashed border-ivory-border">
              <span className="text-charcoal-muted">ರಾಜ್ಯ / State:</span>
              <span className="font-semibold text-charcoal">{profile.location.state || 'Karnataka'}</span>
            </div>
            <div className="flex justify-between py-1 border-b border-dashed border-ivory-border">
              <span className="text-charcoal-muted">ಜಿಲ್ಲೆ / District:</span>
              <span className="font-semibold text-charcoal text-sm">
                {profile.location.district || (
                  <span className="text-charcoal-muted italic">ಮಾಹಿತಿ ಅಗತ್ಯವಿದೆ</span>
                )}
              </span>
            </div>
            <div className="flex justify-between py-1 border-b border-dashed border-ivory-border">
              <span className="text-charcoal-muted">ತಾಲೂಕು / Taluk:</span>
              <span className="font-semibold text-charcoal">{profile.location.taluk || '—'}</span>
            </div>
            <div className="flex justify-between py-1">
              <span className="text-charcoal-muted">ಗ್ರಾಮ / Village:</span>
              <span className="font-semibold text-charcoal">{profile.location.village || '—'}</span>
            </div>
          </div>
        </div>

        {/* Land Holding & Ownership */}
        <div className="md:col-span-6 lg:col-span-4 rounded-2xl bg-white p-6 border border-ivory-border shadow-editorial space-y-4">
          <div className="flex items-center justify-between pb-3 border-b border-ivory-border">
            <div className="flex items-center space-x-2.5">
              <div className="w-8 h-8 rounded-xl bg-harvest/15 text-harvest-dark flex items-center justify-center">
                <Layers className="w-4 h-4" />
              </div>
              <h3 className="font-bold text-sm text-charcoal font-kannada">{t.landArea} & {t.ownership}</h3>
            </div>
            <span className={`text-[10px] font-mono px-2 py-0.5 rounded-full border ${landStatus.bg}`}>
              {landStatus.label}
            </span>
          </div>

          <div className="space-y-3 text-xs">
            <div className="flex justify-between py-1 border-b border-dashed border-ivory-border font-kannada">
              <span className="text-charcoal-muted">ವಿಸ್ತೀರ್ಣ (Acres):</span>
              <span className="font-mono text-base font-bold text-forest">
                {profile.land_area.value_acres 
                  ? `${profile.land_area.value_acres} Acres` 
                  : (profile.land_area.value ? `${profile.land_area.value} ${profile.land_area.unit}` : '—')}
              </span>
            </div>

            {/* Gunta Conversion Note if available */}
            {profile.land_area.value_acres && (
              <div className="p-2 rounded-xl bg-ivory text-[11px] font-mono text-charcoal-muted flex justify-between">
                <span>Equivalent Guntas:</span>
                <span className="font-bold text-charcoal">{(profile.land_area.value_acres * 40).toFixed(0)} Gunta</span>
              </div>
            )}

            <div className="flex justify-between py-1 border-b border-dashed border-ivory-border font-kannada">
              <span className="text-charcoal-muted">ಭೂಮಿ ಹಕ್ಕು / Ownership:</span>
              <span className="font-semibold text-charcoal capitalize">
                {profile.ownership 
                  ? (profile.ownership === 'owned' ? 'ಸ್ವಂತ ಭೂಮಿ (Owner)' : 'ಗೇಣಿ / ಗುತ್ತಿಗೆ (Tenant)') 
                  : '—'}
              </span>
            </div>
            <div className="flex justify-between py-1 font-kannada">
              <span className="text-charcoal-muted">ಹಂಗಾಮು / Season:</span>
              <span className="font-semibold text-charcoal capitalize">{profile.season || 'Kharif'}</span>
            </div>
          </div>
        </div>

        {/* Irrigation Facilities & Water Resources */}
        <div className="md:col-span-12 lg:col-span-4 rounded-2xl bg-white p-6 border border-ivory-border shadow-editorial space-y-4">
          <div className="flex items-center justify-between pb-3 border-b border-ivory-border">
            <div className="flex items-center space-x-2.5">
              <div className="w-8 h-8 rounded-xl bg-forest/10 text-forest flex items-center justify-center">
                <Droplets className="w-4 h-4" />
              </div>
              <h3 className="font-bold text-sm text-charcoal font-kannada">{t.irrigation}</h3>
            </div>
            <span className={`text-[10px] font-mono px-2 py-0.5 rounded-full border ${irrigationStatus.bg}`}>
              {irrigationStatus.label}
            </span>
          </div>

          <div className="space-y-3 font-kannada text-xs">
            <div className="flex justify-between py-1 border-b border-dashed border-ivory-border">
              <span className="text-charcoal-muted">ಸೌಲಭ್ಯ ಲಭ್ಯತೆ:</span>
              <span className="font-semibold text-charcoal">
                {profile.irrigation?.has_irrigation === true
                  ? 'ಲಭ್ಯವಿದೆ (Yes)'
                  : profile.irrigation?.has_irrigation === false
                  ? 'ಮಳೆ ಆಶ್ರಿತ (Rainfed)'
                  : 'ತಿಳಿಸಿಲ್ಲ (Unknown)'}
              </span>
            </div>
            <div className="flex justify-between py-1 border-b border-dashed border-ivory-border">
              <span className="text-charcoal-muted">ನೀರಿನ ಮೂಲ / Source:</span>
              <span className="font-semibold text-charcoal capitalize">{profile.irrigation?.source || '—'}</span>
            </div>
            <div className="flex justify-between py-1">
              <span className="text-charcoal-muted">ನೀರಾವರಿ ವಿಧಾನ / Type:</span>
              <span className="font-semibold text-charcoal capitalize">{profile.irrigation?.type || '—'}</span>
            </div>
          </div>
        </div>

      </div>

      {/* 3. Crops Cultivated Section (Visual Botanical Tiles) */}
      <div className="rounded-[2rem] bg-white p-8 border border-ivory-border shadow-editorial space-y-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-2xl bg-forest text-harvest flex items-center justify-center">
              <Wheat className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-lg font-bold font-kannada text-charcoal">
                {language === 'kn' ? 'ಬೆಳೆಯುತ್ತಿರುವ ಬೆಳೆಗಳು (Crops Cultivated)' : 'Cultivated Crops & Horticulture'}
              </h3>
              <p className="text-xs text-charcoal-muted font-kannada">
                {language === 'kn' ? 'ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತೆಗೆ ಪರಿಶೀಲಿಸಲಾದ ಬೆಳೆಗಳ ಪಟ್ಟಿ.' : 'Approved crop entries evaluated for scheme eligibility assessment.'}
              </p>
            </div>
          </div>
          <span className={`text-[10px] font-mono px-2.5 py-1 rounded-full border ${cropsStatus.bg}`}>
            {cropsStatus.label}
          </span>
        </div>

        {profile.crops.length === 0 ? (
          <div className="p-8 rounded-2xl bg-ivory text-center space-y-3 border border-dashed border-ivory-border">
            <Sprout className="w-8 h-8 text-charcoal-muted mx-auto" />
            <p className="text-xs text-charcoal font-kannada">
              {language === 'kn' 
                ? 'ಯಾವುದೇ ಬೆಳೆಗಳನ್ನು ನಮೂದಿಸಿಲ್ಲ. ಧ್ವನಿ ಮೂಲಕ ಹೇಳಿ (ಉದಾ: "ನಾನು ಅಡಿಕೆ ಮತ್ತು ಭತ್ತ ಬೆಳೆಯುತ್ತೇನೆ").' 
                : 'No crops added yet. Speak naturally (e.g. "I grow arecanut and paddy").'}
            </p>
            <button
              onClick={onNavigateToVoice}
              className="px-4 py-2 rounded-xl bg-forest text-ivory text-xs font-kannada hover:bg-forest-700 transition"
            >
              ಧ್ವನಿ ಮೂಲಕ ಸೇರಿಸಿ (Add via Voice)
            </button>
          </div>
        ) : (
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
            {profile.crops.map((crop, idx) => {
              const meta = getCropMeta(crop);
              const CropIcon = meta.icon;
              return (
                <div 
                  key={idx}
                  className="rounded-2xl p-4 bg-ivory border border-ivory-border flex flex-col justify-between space-y-3 hover:border-harvest transition-all"
                >
                  <div className="flex items-start justify-between">
                    <div className="w-10 h-10 rounded-xl bg-forest/10 text-forest flex items-center justify-center">
                      <CropIcon className="w-5 h-5 text-forest stroke-[2]" />
                    </div>
                    <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-white border border-ivory-border text-charcoal-muted font-bold">
                      {meta.tag}
                    </span>
                  </div>
                  <div>
                    <h4 className="font-bold text-sm text-charcoal font-kannada">{meta.kannada}</h4>
                    <p className="text-xs text-charcoal-muted font-sans capitalize">{meta.en}</p>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>

      {/* 4. Live Karnataka APMC Mandi Market Prices */}
      <MandiPriceCard profile={profile} language={language} />

      {/* 5. Provenance & Conflict History Note */}
      {profile.conflict_fields && Object.keys(profile.conflict_fields).length > 0 && (
        <div className="p-4 rounded-2xl bg-harvest/15 border border-harvest/30 text-xs font-kannada flex items-start space-x-3 text-charcoal">
          <History className="w-4 h-4 text-harvest-dark flex-shrink-0 mt-0.5" />
          <div>
            <p className="font-semibold text-forest">
              {language === 'kn' ? 'ತಿದ್ದಿದ ಮಾಹಿತಿ ಇತಿಹಾಸ (Conversational Corrections Log):' : 'Conversational Corrections History:'}
            </p>
            <p className="text-[11px] text-charcoal-muted mt-0.5">
              {language === 'kn'
                ? 'ಸಂಭಾಷಣೆಯಲ್ಲಿ ನೀವು ತಿದ್ದಿದ ಮೌಲ್ಯಗಳನ್ನು (ಉದಾ: 3 ಎಕರೆ ಅಲ್ಲ 2 ಎಕರೆ) ನಿಖರವಾಗಿ ನವೀಕರಿಸಿ ಹಿಂದಿನ ಮೌಲ್ಯವನ್ನು ಇತಿಹಾಸದಲ್ಲಿ ದಾಖಲಿಸಲಾಗಿದೆ.'
                : 'Values you corrected during dialogue (e.g. not 3 acres, 2 acres) have been updated with full audit provenance.'}
            </p>
          </div>
        </div>
      )}

      {/* Profile Edit Modal */}
      <ProfileEditorModal
        profile={profile}
        language={language}
        isOpen={isEditorOpen}
        onClose={() => setIsEditorOpen(false)}
        onSave={onUpdateProfile}
      />

    </div>
  );
};

