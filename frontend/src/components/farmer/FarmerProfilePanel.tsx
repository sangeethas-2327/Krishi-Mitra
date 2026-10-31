import React, { useState } from 'react';
import {
  UserCheck,
  Edit3,
  CheckCircle,
  HelpCircle,
  AlertCircle,
  MapPin,
  Layers,
  Trees,
  ShieldAlert,
  Droplet,
  Info,
  History,
  AlertTriangle
} from 'lucide-react';
import { FarmerProfile } from '../../types';
import { translations } from '../../utils/translations';
import { ProfileEditorModal } from './ProfileEditorModal';

interface FarmerProfilePanelProps {
  profile: FarmerProfile;
  language: 'kn' | 'en';
  onUpdateProfile: (updates: Partial<FarmerProfile>) => Promise<void>;
}

export const FarmerProfilePanel: React.FC<FarmerProfilePanelProps> = ({
  profile,
  language,
  onUpdateProfile
}) => {
  const t = translations[language];
  const [isEditorOpen, setIsEditorOpen] = useState(false);
  const [showMetadata, setShowMetadata] = useState(false);

  // Critical fields completeness check
  const criticalFields = [
    Boolean(profile.location?.district),
    Boolean(profile.land_area?.value_acres),
    Boolean(profile.crops && profile.crops.length > 0),
    Boolean(profile.ownership),
    Boolean(profile.assistance_needs && profile.assistance_needs.length > 0)
  ];
  const completedCount = criticalFields.filter(Boolean).length;
  const completenessPct = Math.round((completedCount / criticalFields.length) * 100);

  const getStatusBadge = (isConfirmed: boolean, isKnown: boolean, source?: string) => {
    if (isConfirmed) {
      return (
        <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-100 text-emerald-800">
          <CheckCircle className="w-3 h-3 text-emerald-600" />
          <span>{t.confirmed}</span>
          {source && source === 'user_edit' && (
            <span className="text-[10px] text-emerald-600 font-normal">({t.userEdited})</span>
          )}
        </span>
      );
    }
    if (isKnown) {
      return (
        <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[11px] font-semibold bg-blue-100 text-blue-800">
          <HelpCircle className="w-3 h-3 text-blue-600" />
          <span>{t.needsClarification}</span>
        </span>
      );
    }
    return (
      <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[11px] font-semibold bg-amber-100 text-amber-800">
        <AlertCircle className="w-3 h-3 text-amber-600" />
        <span>{t.unknown}</span>
      </span>
    );
  };

  const hasConflicts = profile.conflict_fields && Object.keys(profile.conflict_fields).length > 0;

  return (
    <div className="bg-white rounded-2xl shadow-sm border border-emerald-100 p-5 mb-6">
      
      {/* Header & Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-gray-100 mb-4 gap-2">
        <div className="flex items-center space-x-2.5">
          <div className="w-9 h-9 rounded-xl bg-[#EBE5D8] text-[#183B2B] flex items-center justify-center shadow-inner">
            <UserCheck className="w-5 h-5 text-[#183B2B] stroke-[2]" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h2 className="text-base font-bold text-[#183B2B] font-kannada">
                {t.farmerProfileTitle}
              </h2>
              <span className="text-[11px] bg-emerald-50 text-[#183B2B] px-2 py-0.5 rounded-full border border-emerald-200">
                Phase 2
              </span>
            </div>
            <p className="text-xs text-[#6B7468]">
              {language === 'kn'
                ? 'ಧ್ವನಿ ಸಂಭಾಷಣೆಯಿಂದ ದಾಖಲಾದ ಪಾರದರ್ಶಕ ಕೃಷಿ ಮಾಹಿತಿ ಮತ್ತು ಆಡಿಟ್ ವಿವರಗಳು'
                : 'Auditable agricultural facts extracted from conversation with source tracking'}
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-2 self-end sm:self-auto">
          <button
            onClick={() => setShowMetadata(!showMetadata)}
            className="flex items-center space-x-1 text-xs px-2.5 py-1.5 rounded-lg border border-gray-200 text-gray-600 hover:bg-gray-50 transition"
            title="Toggle audit metadata"
          >
            <Info className="w-3.5 h-3.5 text-[#183B2B] stroke-[2]" />
            <span>{showMetadata ? (language === 'kn' ? 'ಆಡಿಟ್ ಮರೆಮಾಡಿ' : 'Hide Audit') : (language === 'kn' ? 'ಆಡಿಟ್ ವಿವರ' : 'Audit Data')}</span>
          </button>

          <button
            onClick={() => setIsEditorOpen(true)}
            className="flex items-center space-x-1 text-xs font-semibold px-3 py-1.5 rounded-lg bg-[#183B2B] hover:bg-[#23503B] text-white transition shadow-sm"
          >
            <Edit3 className="w-3.5 h-3.5 stroke-[2]" />
            <span>{t.editProfile}</span>
          </button>
        </div>
      </div>

      {/* Conflict / Correction Notification Banner if any */}
      {hasConflicts && (
        <div className="mb-4 p-3 bg-amber-50 border border-amber-200 rounded-xl flex items-start space-x-2 text-xs text-amber-900">
          <AlertTriangle className="w-4 h-4 text-amber-600 flex-shrink-0 mt-0.5" />
          <div>
            <span className="font-semibold font-kannada">
              {language === 'kn' ? 'ಮಾಹಿತಿ ತಿದ್ದುಪಡಿ ದಾಖಲಾಗಿದೆ (Conflict / Correction Handled):' : 'Information Update Handled:'}
            </span>
            <ul className="list-disc list-inside mt-1 space-y-0.5 text-[11px]">
              {Object.entries(profile.conflict_fields || {}).map(([field, logs]) => (
                <li key={field}>
                  Field <span className="font-mono font-semibold">{field}</span> updated from previous entry ({logs.length} changes recorded).
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}

      {/* Profile Completeness Meter */}
      <div className="mb-4 bg-emerald-50/50 rounded-xl p-3 border border-emerald-100/60">
        <div className="flex items-center justify-between text-xs mb-1.5 font-semibold text-forest-900">
          <span>{language === 'kn' ? 'ಯೋಜನಾ ಅರ್ಹತಾ ಪರಿಶೀಲನೆ ಸಿದ್ಧತೆ:' : 'Scheme Evaluation Readiness:'}</span>
          <span className="font-bold text-forest-800">{completenessPct}%</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
          <div
            className={`h-2 rounded-full transition-all duration-500 ${
              completenessPct >= 80 ? 'bg-forest-600' : completenessPct >= 40 ? 'bg-amber-500' : 'bg-red-400'
            }`}
            style={{ width: `${completenessPct}%` }}
          />
        </div>
        <div className="flex items-center justify-between mt-1.5 text-[11px] text-gray-600">
          <span>
            {completenessPct < 100
              ? (language === 'kn'
                  ? 'ಸೂಕ್ತ ಸರ್ಕಾರಿ ಯೋಜನೆಯನ್ನು ದೃಢೀಕರಿಸಲು ಕೃಷಿ ಮಿತ್ರ ಕೇಳುವ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿ.'
                  : 'Answer Krishi Mitra\'s questions to complete mandatory scheme criteria.')
              : (language === 'kn'
                  ? 'ಎಲ್ಲಾ ಮುಖ್ಯ ವಿವರಗಳು ದಾಖಲಾಗಿವೆ. ಕೆಳಗಿನ ಶಿಫಾರಸುಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.'
                  : 'All primary criteria confirmed. Review matched schemes below.')}
          </span>
          <span className="font-medium text-forest-800">
            {completedCount} / {criticalFields.length} {language === 'kn' ? 'ವಿವರಗಳು' : 'fields'}
          </span>
        </div>
      </div>

      {/* Grid of Extracted Fields */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
        
        {/* District, Taluk, Village */}
        <div className="p-3 bg-gray-50 rounded-xl border border-gray-100 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-ktext-muted flex items-center space-x-1">
              <MapPin className="w-3.5 h-3.5 text-forest-600" />
              <span>{t.district} & {t.taluk}</span>
            </span>
            {getStatusBadge(
              Boolean(profile.location?.district),
              Boolean(profile.location?.district),
              profile.fields_metadata?.['location.district']?.source
            )}
          </div>
          <div className="mt-1 font-kannada">
            <p className="text-sm font-bold text-ktext-primary">
              {profile.location?.district ? profile.location.district : (
                <span className="text-amber-700 font-normal italic text-xs">
                  {language === 'kn' ? 'ಜಿಲ್ಲೆ ತಿಳಿಸಿಲ್ಲ (Unknown)' : 'Not stated'}
                </span>
              )}
            </p>
            {(profile.location?.taluk || profile.location?.village) && (
              <p className="text-xs text-gray-600 mt-0.5">
                {[profile.location.taluk ? `${profile.location.taluk} Tk` : null, profile.location.village ? `${profile.location.village} Vlg` : null].filter(Boolean).join(', ')}
              </p>
            )}
            {showMetadata && profile.fields_metadata?.['location.district'] && (
              <p className="text-[10px] text-gray-400 mt-1 font-sans">
                Conf: {profile.fields_metadata['location.district'].confidence * 100}% | Src: {profile.fields_metadata['location.district'].source}
              </p>
            )}
          </div>
        </div>

        {/* Land Area */}
        <div className="p-3 bg-gray-50 rounded-xl border border-gray-100 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-ktext-muted flex items-center space-x-1">
              <Layers className="w-3.5 h-3.5 text-forest-600" />
              <span>{t.landArea}</span>
            </span>
            {getStatusBadge(
              Boolean(profile.land_area?.value_acres),
              Boolean(profile.land_area?.value_acres),
              profile.fields_metadata?.['land_area.value_acres']?.source
            )}
          </div>
          <div className="mt-1 font-kannada">
            <p className="text-sm font-bold text-ktext-primary">
              {profile.land_area?.value_acres ? (
                `${profile.land_area.value} ${profile.land_area.unit} (${profile.land_area.value_acres} acres)`
              ) : (
                <span className="text-amber-700 font-normal italic text-xs">
                  {language === 'kn' ? 'ವಿಸ್ತೀರ್ಣ ತಿಳಿಸಿಲ್ಲ (Unknown)' : 'Not stated'}
                </span>
              )}
            </p>
            {showMetadata && profile.fields_metadata?.['land_area.value_acres'] && (
              <p className="text-[10px] text-gray-400 mt-1 font-sans">
                Normalized: {profile.land_area.value_acres} ac | Conf: {profile.fields_metadata['land_area.value_acres'].confidence * 100}%
              </p>
            )}
          </div>
        </div>

        {/* Multiple Crops */}
        <div className="p-3 bg-gray-50 rounded-xl border border-gray-100 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-ktext-muted flex items-center space-x-1">
              <Trees className="w-3.5 h-3.5 text-forest-600" />
              <span>{t.crops} ({profile.crops.length})</span>
            </span>
            {getStatusBadge(
              Boolean(profile.crops && profile.crops.length > 0),
              Boolean(profile.crops && profile.crops.length > 0),
              profile.fields_metadata?.['crops']?.source
            )}
          </div>
          <div className="mt-1 flex flex-wrap gap-1">
            {profile.crops && profile.crops.length > 0 ? (
              profile.crops.map((crop, i) => (
                <span
                  key={i}
                  className="bg-forest-100 text-forest-800 text-xs font-semibold px-2 py-0.5 rounded-md capitalize font-kannada"
                >
                  {crop}
                </span>
              ))
            ) : (
              <span className="text-amber-700 font-normal italic text-xs font-kannada">
                {language === 'kn' ? 'ಬೆಳೆ ವಿವರ ಅಗತ್ಯವಿದೆ' : 'Not specified'}
              </span>
            )}
          </div>
        </div>

        {/* Ownership */}
        <div className="p-3 bg-gray-50 rounded-xl border border-gray-100 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-ktext-muted flex items-center space-x-1">
              <ShieldAlert className="w-3.5 h-3.5 text-forest-600" />
              <span>{t.ownership}</span>
            </span>
            {getStatusBadge(
              Boolean(profile.ownership),
              Boolean(profile.ownership),
              profile.fields_metadata?.['ownership']?.source
            )}
          </div>
          <p className="text-sm font-bold text-ktext-primary mt-1 capitalize font-kannada">
            {profile.ownership ? (
              profile.ownership === 'owned'
                ? (language === 'kn' ? 'ಸ್ವಂತ ಜಮೀನು (Owned)' : 'Owner Cultivator')
                : profile.ownership === 'joint_owned'
                ? (language === 'kn' ? 'ಜಂಟಿ ಮಾಲೀಕತ್ವ (Joint)' : 'Joint Family Owned')
                : profile.ownership === 'tenant'
                ? (language === 'kn' ? 'ಗುತ್ತಿಗೆ / ಕೌಲು (Tenant)' : 'Tenant Farmer')
                : (language === 'kn' ? 'ಪಾಲುದಾರಿಕೆ (Sharecropper)' : 'Sharecropper')
            ) : (
              <span className="text-amber-700 font-normal italic text-xs">
                {language === 'kn' ? 'ಹಕ್ಕು ವಿವರ ಅಗತ್ಯವಿದೆ' : 'Not specified'}
              </span>
            )}
          </p>
        </div>

        {/* Irrigation Facilities */}
        <div className="p-3 bg-gray-50 rounded-xl border border-gray-100 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-ktext-muted flex items-center space-x-1">
              <Droplet className="w-3.5 h-3.5 text-blue-600" />
              <span>{t.irrigation}</span>
            </span>
            {getStatusBadge(
              Boolean(profile.irrigation?.source),
              Boolean(profile.irrigation?.source)
            )}
          </div>
          <p className="text-sm font-bold text-ktext-primary mt-1 capitalize font-kannada">
            {profile.irrigation?.source ? (
              profile.irrigation.source === 'borewell'
                ? (language === 'kn' ? 'ಕೊಳವೆಬಾವಿ (Borewell)' : 'Borewell')
                : profile.irrigation.source === 'open_well'
                ? (language === 'kn' ? 'ತೆರೆದ ಬಾವಿ (Open Well)' : 'Open Well')
                : profile.irrigation.source === 'canal'
                ? (language === 'kn' ? 'ಕಾಲುವೆ ನೀರು (Canal)' : 'Canal Water')
                : profile.irrigation.source === 'drip'
                ? (language === 'kn' ? 'ಹನಿ ನೀರಾವರಿ (Drip)' : 'Drip Irrigation')
                : profile.irrigation.source === 'sprinkler'
                ? (language === 'kn' ? 'ತುಂತುರು (Sprinkler)' : 'Sprinkler')
                : (language === 'kn' ? 'ಮಳೆಯಾಶ್ರಿತ (Rainfed)' : 'Rainfed / Khushki')
            ) : (
              <span className="text-gray-400 font-normal italic text-xs">
                {language === 'kn' ? 'ತಿಳಿಸಿಲ್ಲ (Unknown)' : 'Not stated'}
              </span>
            )}
          </p>
        </div>

        {/* Season */}
        <div className="p-3 bg-gray-50 rounded-xl border border-gray-100 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-ktext-muted">
              <span>{t.season}</span>
            </span>
            {getStatusBadge(Boolean(profile.season), Boolean(profile.season))}
          </div>
          <p className="text-sm font-bold text-ktext-primary mt-1 capitalize font-kannada">
            {profile.season ? (
              profile.season === 'kharif'
                ? (language === 'kn' ? 'ಮುಂಗಾರು (Kharif)' : 'Kharif')
                : profile.season === 'rabi'
                ? (language === 'kn' ? 'ಹಿಂಗಾರು (Rabi)' : 'Rabi')
                : profile.season === 'summer'
                ? (language === 'kn' ? 'ಬೇಸಿಗೆ (Summer)' : 'Summer')
                : (language === 'kn' ? 'ವಾರ್ಷಿಕ (Annual)' : 'Annual')
            ) : (
              <span className="text-gray-400 font-normal italic text-xs">
                {language === 'kn' ? 'ಮುಂಗಾರು / ಸಾರ್ವಕಾಲಿಕ' : 'Kharif / Default'}
              </span>
            )}
          </p>
        </div>

        {/* Assistance Needs */}
        <div className="p-3 bg-gray-50 rounded-xl border border-gray-100 flex flex-col justify-between sm:col-span-2">
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs text-ktext-muted">
              <span>{t.needs}</span>
            </span>
            {getStatusBadge(
              Boolean(profile.assistance_needs && profile.assistance_needs.length > 0),
              Boolean(profile.assistance_needs && profile.assistance_needs.length > 0)
            )}
          </div>
          <div className="mt-1 flex flex-wrap gap-1">
            {profile.assistance_needs && profile.assistance_needs.length > 0 ? (
              <>
                {profile.assistance_needs.map((need, idx) => (
                  <span
                    key={idx}
                    className="bg-amber-100 text-amber-900 text-xs font-semibold px-2 py-0.5 rounded-md capitalize"
                  >
                    {need.replace(/_/g, ' ')}
                  </span>
                ))}
                {profile.additional_details?.custom_assistance && (
                  <span className="bg-emerald-100 text-emerald-900 text-xs font-semibold px-2 py-0.5 rounded-md flex items-center space-x-1">
                    <span className="text-[10px] bg-emerald-200 px-1 rounded text-emerald-800 font-mono">
                      {language === 'kn' ? 'ವಿಶೇಷ' : 'Custom'}
                    </span>
                    <span>{profile.additional_details.custom_assistance}</span>
                  </span>
                )}
              </>
            ) : (
              <span className="text-amber-700 font-normal italic text-xs font-kannada">
                {language === 'kn' ? 'ಸಾಮಾನ್ಯ ಕೃಷಿ ನೆರವು' : 'General support'}
              </span>
            )}
          </div>
        </div>

      </div>

      {/* Embedded Profile Editor Modal */}
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
