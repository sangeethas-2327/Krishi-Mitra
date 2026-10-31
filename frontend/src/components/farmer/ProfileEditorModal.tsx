import React, { useState, useEffect } from 'react';
import { X, Check, Lock, MapPin, Sparkles } from 'lucide-react';
import { FarmerProfile } from '../../types';
import { translations } from '../../utils/translations';
import { KARNATAKA_DISTRICTS, DistrictData, TalukData } from '../../data/karnatakaLocations';
import { CROP_CATEGORIES } from '../../data/cropCatalog';
import { ASSISTANCE_CATEGORIES } from '../../data/assistanceCatalog';
import { SearchableSelect, SelectOption } from '../common/SearchableSelect';
import { CategorizedMultiSelect } from '../common/CategorizedMultiSelect';

interface ProfileEditorModalProps {
  profile: FarmerProfile;
  language: 'kn' | 'en';
  isOpen: boolean;
  onClose: () => void;
  onSave: (updates: Partial<FarmerProfile>) => Promise<void>;
}

export const ProfileEditorModal: React.FC<ProfileEditorModalProps> = ({
  profile,
  language,
  isOpen,
  onClose,
  onSave
}) => {
  const t = translations[language];

  // Fixed State to Karnataka
  const fixedState = 'Karnataka';

  // Location States
  const [district, setDistrict] = useState(profile.location?.district || '');
  const [taluk, setTaluk] = useState(profile.location?.taluk || '');
  const [village, setVillage] = useState(profile.location?.village || '');

  // Land & Farming Details
  const [landValue, setLandValue] = useState(profile.land_area?.value?.toString() || '');
  const [landUnit, setLandUnit] = useState(profile.land_area?.unit || 'acre');
  const [crops, setCrops] = useState<string[]>(profile.crops || []);
  const [ownership, setOwnership] = useState(profile.ownership || 'owned');
  const [season, setSeason] = useState(profile.season || 'kharif');
  const [irrigationSource, setIrrigationSource] = useState(profile.irrigation?.source || 'borewell');
  const [assistanceNeeds, setAssistanceNeeds] = useState<string[]>(profile.assistance_needs || []);
  const [customAssistanceDetail, setCustomAssistanceDetail] = useState<string>(
    profile.additional_details?.custom_assistance || ''
  );

  const [isSaving, setIsSaving] = useState(false);

  // Sync internal state when profile prop updates or modal opens
  useEffect(() => {
    if (isOpen) {
      setDistrict(profile.location?.district || '');
      setTaluk(profile.location?.taluk || '');
      setVillage(profile.location?.village || '');
      setLandValue(profile.land_area?.value?.toString() || '');
      setLandUnit(profile.land_area?.unit || 'acre');
      setCrops(profile.crops || []);
      setOwnership(profile.ownership || 'owned');
      setSeason(profile.season || 'kharif');
      setIrrigationSource(profile.irrigation?.source || 'borewell');
      setAssistanceNeeds(profile.assistance_needs || []);
      setCustomAssistanceDetail(profile.additional_details?.custom_assistance || '');
    }
  }, [isOpen, profile]);

  if (!isOpen) return null;

  // 1. District options from authoritative Karnataka locations
  const districtOptions: SelectOption[] = KARNATAKA_DISTRICTS.map((d) => ({
    id: d.id,
    name_en: d.name_en,
    name_kn: d.name_kn,
    sublabel: 'ಕರ್ನಾಟಕ / Karnataka'
  }));

  // Find active district record
  const selectedDistrictObj: DistrictData | undefined = KARNATAKA_DISTRICTS.find(
    (d) =>
      d.id.toLowerCase() === district.toLowerCase() ||
      d.name_en.toLowerCase() === district.toLowerCase() ||
      d.name_kn === district
  );

  // 2. Dependent Taluk options based on selected district
  const talukOptions: SelectOption[] = selectedDistrictObj
    ? selectedDistrictObj.taluks.map((talukItem) => ({
        id: talukItem.id,
        name_en: talukItem.name_en,
        name_kn: talukItem.name_kn,
        sublabel: `${selectedDistrictObj.name_kn} ಜಿಲ್ಲೆ`
      }))
    : [];

  // Find active taluk record
  const selectedTalukObj: TalukData | undefined = selectedDistrictObj?.taluks.find(
    (tk) =>
      tk.id.toLowerCase() === taluk.toLowerCase() ||
      tk.name_en.toLowerCase() === taluk.toLowerCase() ||
      tk.name_kn === taluk
  );

  // 3. Dependent Village options based on selected taluk
  const villageOptions: SelectOption[] = selectedTalukObj
    ? selectedTalukObj.villages.map((v) => ({
        id: v.id,
        name_en: v.name_en,
        name_kn: v.name_kn,
        sublabel: `${selectedTalukObj.name_kn} ತಾಲೂಕು`
      }))
    : [];

  // District Change handler: clears dependent taluk & village
  const handleDistrictSelect = (option: SelectOption | null) => {
    if (!option) {
      setDistrict('');
      setTaluk('');
      setVillage('');
      return;
    }
    // Set standardized English district name for eligibility & weather
    setDistrict(option.name_en);
    // Reset dependent taluk and village
    setTaluk('');
    setVillage('');
  };

  // Taluk Change handler: clears dependent village
  const handleTalukSelect = (option: SelectOption | null) => {
    if (!option) {
      setTaluk('');
      setVillage('');
      return;
    }
    setTaluk(option.name_en);
    setVillage('');
  };

  // Village Change handler (supports custom entry)
  const handleVillageSelect = (option: SelectOption | null, customText?: string) => {
    if (!option && !customText) {
      setVillage('');
      return;
    }
    setVillage(customText || option?.name_en || option?.name_kn || '');
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSaving(true);

    const numLand = parseFloat(landValue) || undefined;
    const normalizedCrops = crops.map((c) => c.trim().toLowerCase()).filter(Boolean);
    const normalizedNeeds = assistanceNeeds.map((n) => n.trim().toLowerCase()).filter(Boolean);

    const updates: Partial<FarmerProfile> = {
      location: {
        state: fixedState,
        district: district.trim() || undefined,
        taluk: taluk.trim() || undefined,
        village: village.trim() || undefined
      },
      land_area: {
        value: numLand,
        unit: landUnit,
        value_acres: numLand
      },
      crops: normalizedCrops,
      ownership,
      season,
      irrigation: {
        source: irrigationSource,
        has_irrigation: irrigationSource !== 'rainfed'
      },
      assistance_needs: normalizedNeeds,
      additional_details: {
        ...(profile.additional_details || {}),
        custom_assistance: customAssistanceDetail.trim() || undefined
      }
    };

    try {
      await onSave(updates);
      onClose();
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-white rounded-[2rem] shadow-2xl max-w-lg w-full max-h-[92vh] flex flex-col border border-[#E2D9C8] overflow-hidden animate-fadeIn">
        
        {/* Header */}
        <div className="flex items-center justify-between p-6 sm:p-7 border-b border-[#E2D9C8] bg-[#FAF7F0] flex-shrink-0">
          <div>
            <div className="flex items-center space-x-2">
              <div className="w-7 h-7 rounded-lg bg-[#183B2B] flex items-center justify-center">
                <MapPin className="w-4 h-4 text-[#D7A85B]" />
              </div>
              <h3 className="text-xl font-bold text-[#282C27] font-kannada">
                {t.editProfile}
              </h3>
            </div>
            <p className="text-xs text-[#727B70] font-sans mt-1">
              {language === 'kn'
                ? 'ಸ್ಮಾರ್ಟ್ ಆಯ್ಕೆಗಳೊಂದಿಗೆ ನಿಮ್ಮ ಕೃಷಿ ವಿವರಗಳನ್ನು ತಿದ್ದಿ'
                : 'Update farm details with intelligent dropdowns for precise scheme matching'}
            </p>
          </div>
          <button
            onClick={onClose}
            className="text-[#727B70] hover:text-[#282C27] rounded-xl p-2 transition hover:bg-[#EBE5D8]"
            title="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Form Container (Smooth Vertically Scrollable Body) */}
        <div className="overflow-y-auto flex-1 p-6 sm:p-7 scrollbar-thin">
          <form id="profile-editor-form" onSubmit={handleSubmit} className="space-y-5 text-xs font-kannada">
            
            {/* 1. STATE (Fixed to Karnataka) & DISTRICT */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
              {/* Fixed State Input */}
              <div>
                <label className="block text-xs font-semibold text-[#282C27] mb-1 font-kannada flex items-center justify-between">
                  <span>{language === 'kn' ? 'ರಾಜ್ಯ (State)' : 'State'}</span>
                  <span className="text-[10px] text-[#183B2B] font-mono font-bold flex items-center space-x-0.5">
                    <Lock className="w-2.5 h-2.5 text-[#B08233]" />
                    <span>Fixed</span>
                  </span>
                </label>
                <div className="w-full bg-[#EBE5D8]/60 border border-[#E2D9C8] rounded-xl p-2.5 text-xs flex items-center justify-between text-[#183B2B] font-bold select-none cursor-not-allowed">
                  <div className="flex items-center space-x-2">
                    <span className="w-2 h-2 rounded-full bg-[#183B2B]" />
                    <span>{language === 'kn' ? 'ಕರ್ನಾಟಕ (Karnataka)' : 'Karnataka (ಕರ್ನಾಟಕ)'}</span>
                  </div>
                  <Lock className="w-3.5 h-3.5 text-[#727B70]" />
                </div>
              </div>

              {/* Searchable District Dropdown */}
              <div>
                <SearchableSelect
                  label={t.district}
                  placeholder={language === 'kn' ? 'ಜಿಲ್ಲೆ ಆರಿಸಿ...' : 'Select district...'}
                  options={districtOptions}
                  selectedValue={district}
                  onSelect={handleDistrictSelect}
                  language={language}
                />
              </div>
            </div>

            {/* 2. TALUK & VILLAGE (Dependent Cascading Dropdowns) */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
              {/* Dependent Taluk Dropdown */}
              <div>
                <SearchableSelect
                  label={t.taluk}
                  placeholder={language === 'kn' ? 'ತಾಲೂಕು ಆರಿಸಿ...' : 'Select taluk...'}
                  options={talukOptions}
                  selectedValue={taluk}
                  onSelect={handleTalukSelect}
                  disabled={!district}
                  disabledHint={
                    language === 'kn'
                      ? 'ಮೊದಲು ಜಿಲ್ಲೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ'
                      : 'Select a district first'
                  }
                  language={language}
                />
              </div>

              {/* Dependent Village Dropdown with Manual Entry Fallback */}
              <div>
                <SearchableSelect
                  label={t.village}
                  placeholder={language === 'kn' ? 'ಗ್ರಾಮ ಆರಿಸಿ / ಟೈಪ್ ಮಾಡಿ...' : 'Select or type village...'}
                  options={villageOptions}
                  selectedValue={village}
                  onSelect={handleVillageSelect}
                  disabled={!taluk}
                  disabledHint={
                    language === 'kn'
                      ? 'ಮೊದಲು ತಾಲೂಕನ್ನು ಆಯ್ಕೆಮಾಡಿ'
                      : 'Select a taluk first'
                  }
                  allowCustomEntry={true}
                  customEntryLabel={
                    language === 'kn'
                      ? '+ ಪಟ್ಟಿಯಲ್ಲಿಲ್ಲದ ಗ್ರಾಮ ನಮೂದಿಸಿ'
                      : '+ Enter village manually'
                  }
                  language={language}
                />
              </div>
            </div>

            {/* 3. LAND AREA & UNIT */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-1">
              <div>
                <label className="block text-xs font-semibold text-[#282C27] mb-1 font-kannada">
                  {t.landArea} ({language === 'kn' ? 'ವಿಸ್ತೀರ್ಣ ಸಂಖ್ಯೆ' : 'Numeric Value'})
                </label>
                <input
                  type="number"
                  step="0.1"
                  min="0"
                  value={landValue}
                  onChange={(e) => setLandValue(e.target.value)}
                  placeholder="3.0"
                  className="w-full bg-[#FAF7F0] border border-[#E2D9C8] rounded-xl p-2.5 text-[#282C27] font-mono focus:outline-none focus:border-[#183B2B] text-xs"
                />
              </div>
              <div>
                <label className="block text-xs font-semibold text-[#282C27] mb-1 font-kannada">
                  {language === 'kn' ? 'ಪ್ರಮಾಣ / Unit' : 'Unit of Measurement'}
                </label>
                <select
                  value={landUnit}
                  onChange={(e) => setLandUnit(e.target.value)}
                  className="w-full bg-[#FAF7F0] border border-[#E2D9C8] rounded-xl p-2.5 text-[#282C27] focus:outline-none focus:border-[#183B2B] text-xs font-sans"
                >
                  <option value="acre">ಎಕರೆ (Acre - 1.0)</option>
                  <option value="guntha">ಗುಂಟೆ (Guntha - 0.025 ac)</option>
                  <option value="hectare">ಹೆಕ್ಟೇರ್ (Hectare - 2.47 ac)</option>
                  <option value="cent">ಸೆಂಟ್ (Cent - 0.01 ac)</option>
                </select>
              </div>
            </div>

            {/* 4. CROPS (Intelligent Searchable Categorized Multi-Select across 8 Categories) */}
            <div className="pt-1">
              <CategorizedMultiSelect
                label={t.crops}
                placeholder={
                  language === 'kn'
                    ? 'ಬೆಳೆಗಳನ್ನು ಆರಿಸಿ (8 ವಿಭಾಗಗಳಲ್ಲಿ ಹುಡುಕಿ)...'
                    : 'Select crops across 8 categories...'
                }
                categories={CROP_CATEGORIES.map((c) => ({
                  id: c.id,
                  name_en: c.name_en,
                  name_kn: c.name_kn,
                  items: c.crops.map((crop) => ({
                    key: crop.key,
                    name_en: crop.name_en,
                    name_kn: crop.name_kn
                  }))
                }))}
                selectedKeys={crops}
                onChange={setCrops}
                language={language}
                allowOther={true}
              />
            </div>

            {/* 5. OWNERSHIP & SEASON */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-1">
              <div>
                <label className="block text-xs font-semibold text-[#282C27] mb-1 font-kannada">
                  {t.ownership}
                </label>
                <select
                  value={ownership}
                  onChange={(e) => setOwnership(e.target.value)}
                  className="w-full bg-[#FAF7F0] border border-[#E2D9C8] rounded-xl p-2.5 text-[#282C27] focus:outline-none focus:border-[#183B2B] text-xs font-sans"
                >
                  <option value="owned">ಸ್ವಂತ (Owner Cultivator)</option>
                  <option value="joint_owned">ಜಂಟಿ ಮಾಲೀಕತ್ವ (Joint Family)</option>
                  <option value="tenant">ಗುತ್ತಿಗೆ / ಕೌಲು (Tenant Farmer)</option>
                  <option value="leased">ಲೀಸ್ (Leased)</option>
                  <option value="sharecropper">ಪಾಲುದಾರಿಕೆ (Sharecropper)</option>
                </select>
              </div>
              <div>
                <label className="block text-xs font-semibold text-[#282C27] mb-1 font-kannada">
                  {t.season}
                </label>
                <select
                  value={season}
                  onChange={(e) => setSeason(e.target.value)}
                  className="w-full bg-[#FAF7F0] border border-[#E2D9C8] rounded-xl p-2.5 text-[#282C27] focus:outline-none focus:border-[#183B2B] text-xs font-sans"
                >
                  <option value="kharif">ಮುಂಗಾರು (Kharif)</option>
                  <option value="rabi">ಹಿಂಗಾರು (Rabi)</option>
                  <option value="summer">ಬೇಸಿಗೆ (Summer)</option>
                  <option value="annual">ವಾರ್ಷಿಕ (Annual)</option>
                  <option value="perennial">ಬಹುವಾರ್ಷಿಕ (Perennial)</option>
                </select>
              </div>
            </div>

            {/* 6. IRRIGATION SOURCE */}
            <div className="pt-1">
              <label className="block text-xs font-semibold text-[#282C27] mb-1 font-kannada">
                {t.irrigation}
              </label>
              <select
                value={irrigationSource}
                onChange={(e) => setIrrigationSource(e.target.value)}
                className="w-full bg-[#FAF7F0] border border-[#E2D9C8] rounded-xl p-2.5 text-[#282C27] focus:outline-none focus:border-[#183B2B] text-xs font-sans"
              >
                <option value="borewell">ಕೊಳವೆಬಾವಿ (Borewell)</option>
                <option value="open_well">ತೆರೆದ ಬಾವಿ (Open Well)</option>
                <option value="canal">ಕಾಲುವೆ / ನಾಲೆ (Canal)</option>
                <option value="drip">ಹನಿ ನೀರಾವರಿ (Drip Irrigation)</option>
                <option value="sprinkler">ತುಂತುರು ನೀರಾವರಿ (Sprinkler)</option>
                <option value="rainfed">ಮಳೆಯಾಶ್ರಿತ / ಖುಷ್ಕಿ (Rainfed / Dryland)</option>
              </select>
            </div>

            {/* 7. ASSISTANCE NEEDS (Categorized across 10 FAQ Domains + Custom Specification) */}
            <div className="pt-1">
              <CategorizedMultiSelect
                label={t.needs}
                placeholder={
                  language === 'kn'
                    ? 'ಅಗತ್ಯವಿರುವ ನೆರವು ಆರಿಸಿ (10 ವಿಭಾಗಗಳು)...'
                    : 'Select assistance needs across 10 domains...'
                }
                categories={ASSISTANCE_CATEGORIES.map((cat) => ({
                  id: cat.id,
                  name_en: cat.name_en,
                  name_kn: cat.name_kn,
                  items: cat.items.map((item) => ({
                    key: item.key,
                    name_en: item.name_en,
                    name_kn: item.name_kn
                  }))
                }))}
                selectedKeys={assistanceNeeds}
                onChange={setAssistanceNeeds}
                language={language}
                allowOther={true}
                otherKey="other"
                otherPromptText={
                  language === 'kn'
                    ? 'ದಯವಿಟ್ಟು ನಿಮಗೆ ಅಗತ್ಯವಿರುವ ನೆರವನ್ನು ನಮೂದಿಸಿ (Please specify assistance):'
                    : 'Please specify the assistance you need:'
                }
                customDetailValue={customAssistanceDetail}
                onCustomDetailChange={setCustomAssistanceDetail}
              />
            </div>

          </form>
        </div>

        {/* Modal Footer with Actions */}
        <div className="flex items-center justify-between p-5 sm:p-6 border-t border-[#E2D9C8] bg-[#FAF7F0] flex-shrink-0">
          <div className="flex items-center space-x-1.5 text-[11px] text-[#727B70] font-sans">
            <Sparkles className="w-3.5 h-3.5 text-[#B08233]" />
            <span>
              {language === 'kn'
                ? 'ಮಾಹಿತಿಯು ಅರ್ಹತಾ ಎಂಜಿನ್ ಅನ್ನು ನವೀಕರಿಸುತ್ತದೆ'
                : 'Profile changes update the deterministic engine'}
            </span>
          </div>

          <div className="flex items-center space-x-2.5">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 border border-[#E2D9C8] rounded-xl text-[#727B70] hover:text-[#282C27] hover:bg-[#EBE5D8] text-xs font-semibold transition"
            >
              {t.close}
            </button>
            <button
              type="submit"
              form="profile-editor-form"
              disabled={isSaving}
              className="px-6 py-2 bg-[#183B2B] hover:bg-[#10261C] text-[#FAF7F0] rounded-xl text-xs font-bold flex items-center space-x-2 shadow-sm transition active:scale-95 disabled:opacity-50"
            >
              <Check className="w-4 h-4 text-[#D7A85B]" />
              <span>{isSaving ? 'ಉಳಿಸಲಾಗುತ್ತಿದೆ...' : t.saveChanges}</span>
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};
