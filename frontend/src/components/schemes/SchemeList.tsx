import React, { useState } from 'react';
import { Award, Filter, Scale } from 'lucide-react';
import { SchemeMatchResult, SchemeRecord } from '../../types';
import { SchemeCard } from './SchemeCard';
import { SchemeComparisonModal } from './SchemeComparisonModal';
import { translations } from '../../utils/translations';

interface SchemeListProps {
  recommendations: SchemeMatchResult[];
  language: 'kn' | 'en';
  onViewDetails: (scheme: SchemeMatchResult) => void;
}

const CATEGORIES = [
  { id: 'all', kn: 'ಎಲ್ಲಾ ಯೋಜನೆಗಳು', en: 'All Categories' },
  { id: 'income_support', kn: 'ಆದಾಯ ಬೆಂಬಲ', en: 'Income Support' },
  { id: 'crop_insurance', kn: 'ಬೆಳೆ ವಿಮೆ', en: 'Crop Insurance' },
  { id: 'irrigation', kn: 'ನೀರಾವರಿ & ಡ್ರಿಪ್', en: 'Irrigation' },
  { id: 'equipment', kn: 'ಯಂತ್ರೋಪಕರಣ', en: 'Farm Equipment' },
  { id: 'soil_health', kn: 'ಮಣ್ಣಿನ ಆರೋಗ್ಯ', en: 'Soil Health' }
];

export const SchemeList: React.FC<SchemeListProps> = ({
  recommendations,
  language,
  onViewDetails
}) => {
  const t = translations[language];
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [statusFilter, setStatusFilter] = useState('all');
  const [isCompareOpen, setIsCompareOpen] = useState(false);

  const filteredSchemes = recommendations.filter((item) => {
    if (selectedCategory !== 'all' && item.scheme.category !== selectedCategory) {
      return false;
    }
    if (statusFilter !== 'all' && item.evaluation_status !== statusFilter) {
      return false;
    }
    return true;
  });

  const allSchemeRecords: SchemeRecord[] = recommendations.map((r) => r.scheme);

  return (
    <div className="mt-8">
      
      {/* Section Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-gray-200 mb-5 gap-3">
        <div className="flex items-center space-x-2.5">
          <div className="w-10 h-10 rounded-xl bg-[#EBE5D8] text-[#183B2B] flex items-center justify-center">
            <Award className="w-5 h-5 text-[#183B2B] stroke-[2]" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-[#183B2B] font-kannada">
              {t.recommendedSchemes}
            </h2>
            <p className="text-xs text-[#6B7468]">
              {language === 'kn'
                ? 'ಪಾರದರ್ಶಕ ನಿಯಮಗಳ ಮೂಲಕ ಪರಿಶೀಲಿಸಲಾದ ಅಧಿಕೃತ ಮತ್ತು ಪ್ರಾಯೋಗಿಕ ಯೋಜನೆಗಳು'
                : 'Auditable government and simulated schemes matched to your profile'}
            </p>
          </div>
        </div>

        {/* Right side: Filter & Compare buttons */}
        <div className="flex items-center space-x-2.5">
          {/* Compare Schemes Button */}
          <button
            onClick={() => setIsCompareOpen(true)}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-emerald-700 hover:bg-emerald-800 text-white text-xs font-semibold shadow-sm transition"
          >
            <Scale className="w-3.5 h-3.5" />
            <span>{t.compareSchemes}</span>
          </button>

          {/* Status Filter */}
          <div className="flex items-center space-x-1.5">
            <Filter className="w-3.5 h-3.5 text-gray-500" />
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              className="text-xs bg-white border border-gray-300 rounded-lg px-2.5 py-1.5 text-gray-700 focus:ring-2 focus:ring-forest-600 font-kannada"
            >
              <option value="all">{language === 'kn' ? 'ಎಲ್ಲಾ ಅರ್ಹತಾ ಸ್ಥಿತಿ' : 'All Statuses'}</option>
              <option value="POTENTIALLY_SUITABLE">{language === 'kn' ? 'ಪ್ರಾಥಮಿಕವಾಗಿ ಅರ್ಹ' : 'Potentially Suitable'}</option>
              <option value="INSUFFICIENT_INFORMATION">{language === 'kn' ? 'ಮಾಹಿತಿ ಅಗತ್ಯವಿದೆ' : 'Information Needed'}</option>
              <option value="REQUIRES_OFFICIAL_VERIFICATION">{language === 'kn' ? 'ದಾಖಲೆ ಪರಿಶೀಲನೆ ಬಾಕಿ' : 'Requires Verification'}</option>
              <option value="NOT_SUITABLE_BASED_ON_KNOWN_RULES">{language === 'kn' ? 'ಅರ್ಹತೆ ಹೊಂದಿಲ್ಲ' : 'Not Suitable'}</option>
            </select>
          </div>
        </div>
      </div>

      {/* Category Pills */}
      <div className="flex flex-wrap gap-2 mb-6">
        {CATEGORIES.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setSelectedCategory(cat.id)}
            className={`text-xs px-3.5 py-1.5 rounded-full font-medium transition font-kannada ${
              selectedCategory === cat.id
                ? 'bg-forest-700 text-white shadow'
                : 'bg-white border border-gray-200 text-gray-700 hover:bg-gray-50'
            }`}
          >
            {language === 'kn' ? cat.kn : cat.en}
          </button>
        ))}
      </div>

      {/* Scheme Cards Grid */}
      {filteredSchemes.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {filteredSchemes.map((item) => (
            <SchemeCard
              key={item.scheme.id}
              matchResult={item}
              language={language}
              onViewDetails={onViewDetails}
            />
          ))}
        </div>
      ) : (
        <div className="bg-white rounded-2xl p-8 border border-gray-200 text-center text-ktext-muted">
          <p className="text-sm font-medium text-ktext-primary font-kannada mb-1">
            {language === 'kn' ? 'ಆಯ್ಕೆಮಾಡಿದ ವರ್ಗದಲ್ಲಿ ಯಾವುದೇ ಯೋಜನೆಗಳು ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ.' : 'No schemes match the selected filter.'}
          </p>
          <p className="text-xs">
            {language === 'kn' ? 'ಬೇರೆ ವರ್ಗವನ್ನು ಆಯ್ಕೆಮಾಡಿ ಅಥವಾ ಫಿಲ್ಟರ್ ತೆರವುಗೊಳಿಸಿ.' : 'Try changing your category or filter selection.'}
          </p>
        </div>
      )}

      {/* Scheme Comparison Modal */}
      <SchemeComparisonModal
        isOpen={isCompareOpen}
        onClose={() => setIsCompareOpen(false)}
        language={language}
        allSchemes={allSchemeRecords}
      />

    </div>
  );
};
