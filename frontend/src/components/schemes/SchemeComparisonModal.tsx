import React, { useState, useEffect } from 'react';
import {
  X,
  Check,
  ShieldCheck,
  ExternalLink,
  Scale,
  AlertTriangle,
  Layers,
  Building2,
  FileText,
  CheckCircle2,
  XCircle,
  AlertCircle,
  HelpCircle,
  ArrowRight,
  Info
} from 'lucide-react';
import {
  SchemeComparisonResponse,
  SchemeComparisonItem,
  SchemeRecord,
  SchemeMatchResult
} from '../../types';
import { api } from '../../services/api';
import { translations } from '../../utils/translations';

interface SchemeComparisonModalProps {
  isOpen: boolean;
  onClose: () => void;
  language: 'kn' | 'en';
  allSchemes?: SchemeRecord[];
  availableSchemes?: SchemeRecord[];
  matchResults?: SchemeMatchResult[];
  initialSelectedIds?: string[];
}

export const SchemeComparisonModal: React.FC<SchemeComparisonModalProps> = ({
  isOpen,
  onClose,
  language,
  allSchemes = [],
  availableSchemes,
  matchResults = [],
  initialSelectedIds = ['pm-kisan', 'pmfby']
}) => {
  const schemesList = availableSchemes || allSchemes;
  const t = translations[language];
  const [selectedIds, setSelectedIds] = useState<string[]>(initialSelectedIds);
  const [comparisonData, setComparisonData] = useState<SchemeComparisonResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  // Modal dialog for portal redirection confirmation or offline application steps
  const [activeGuidance, setActiveGuidance] = useState<{
    scheme: SchemeComparisonItem;
    type: 'online_portal' | 'offline_process' | 'verification_warning';
  } | null>(null);

  useEffect(() => {
    if (isOpen && selectedIds.length > 0) {
      loadComparison(selectedIds);
    }
  }, [isOpen]);

  const loadComparison = async (ids: string[]) => {
    setIsLoading(true);
    try {
      const data = await api.compareSchemes(ids);
      setComparisonData(data);
    } catch (e) {
      console.error('Failed to load scheme comparison:', e);
    } finally {
      setIsLoading(false);
    }
  };

  const toggleScheme = (id: string) => {
    const next = selectedIds.includes(id)
      ? selectedIds.filter((s) => s !== id)
      : [...selectedIds, id];

    if (next.length > 0) {
      setSelectedIds(next);
      loadComparison(next);
    }
  };

  const getMatchResult = (schemeId: string): SchemeMatchResult | undefined => {
    return matchResults.find((m) => m.scheme.id === schemeId);
  };

  const handleApplyClick = (scheme: SchemeComparisonItem) => {
    if (scheme.official_url) {
      setActiveGuidance({
        scheme,
        type: 'online_portal'
      });
    } else {
      setActiveGuidance({
        scheme,
        type: 'offline_process'
      });
    }
  };

  const proceedToOfficialPortal = (url: string) => {
    window.open(url, '_blank', 'noopener,noreferrer');
    setActiveGuidance(null);
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-2 sm:p-4 md:p-6 overflow-hidden animate-fadeIn">
      <div className="bg-white rounded-[2rem] shadow-2xl max-w-7xl w-full h-[92vh] max-h-[92vh] flex flex-col border border-[#E2D9C8] overflow-hidden">

        {/* 1. Modal Header (Fixed at top) */}
        <div className="flex-shrink-0 px-6 py-4 border-b border-[#23503B] flex items-center justify-between bg-[#183B2B] text-white">
          <div className="flex items-center space-x-3.5">
            <div className="w-10 h-10 rounded-2xl bg-[#10261C] flex items-center justify-center text-[#D7A85B] border border-[#D7A85B]/30 shadow-xs">
              <Scale className="w-5 h-5 stroke-[2.2]" />
            </div>
            <div>
              <h2 className="text-lg sm:text-xl font-extrabold font-kannada text-white tracking-tight">
                {language === 'kn' ? 'ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಮುಖಾಮುಖಿ ಹೋಲಿಕೆ' : 'Side-by-Side Scheme Comparison'}
              </h2>
              <p className="text-xs text-[#A8B58A] font-sans">
                {language === 'kn'
                  ? 'ಕೇಂದ್ರ ಮತ್ತು ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಅಧಿಕೃತ ನಿಯಮಗಳು, ಮಾನದಂಡಗಳು ಮತ್ತು ಅರ್ಜಿ ಸಲ್ಲಿಕೆ ಮಾರ್ಗಗಳು'
                  : 'Factual statutory comparison of central and state programmes with live eligibility verification'}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="text-[#DEE4D2] hover:text-white rounded-xl p-2 transition-colors hover:bg-[#23503B]"
            aria-label="Close Comparison"
          >
            <X className="w-5 h-5 stroke-[2.2]" />
          </button>
        </div>

        {/* 2. Scheme Selector Pills Bar (Scrollable horizontally or compact wrap) */}
        <div className="flex-shrink-0 px-6 py-3 bg-[#FAF7F0] border-b border-[#E2D9C8] flex flex-wrap items-center gap-2 text-xs">
          <span className="font-bold text-[#183B2B] font-kannada flex items-center space-x-1.5 mr-1">
            <Layers className="w-4 h-4 text-[#B08233]" />
            <span>{language === 'kn' ? 'ಹೋಲಿಕೆಗೆ ಯೋಜನೆಗಳು:' : 'Select Schemes to Compare:'}</span>
          </span>
          <div className="flex flex-wrap gap-1.5 max-h-24 overflow-y-auto scrollbar-thin py-0.5">
            {schemesList.map((s) => {
              const isSelected = selectedIds.includes(s.id);
              const isReal = s.scheme_type === 'real';
              const isCentral = s.government_level === 'central';
              return (
                <button
                  key={s.id}
                  onClick={() => toggleScheme(s.id)}
                  className={`px-3 py-1 rounded-xl font-kannada text-xs font-semibold transition-all flex items-center space-x-1.5 border active:scale-95 ${isSelected
                      ? 'bg-[#183B2B] text-white border-[#183B2B] shadow-sm font-bold'
                      : 'bg-white border-[#E2D9C8] text-[#282C27] hover:bg-[#EBE5D8]'
                    }`}
                >
                  <span className="truncate max-w-[180px]">
                    {language === 'kn' && s.name_kn ? s.name_kn : s.name}
                  </span>
                  <span className={`text-[9px] font-mono px-1 py-0.2 rounded font-bold uppercase ${isCentral ? 'bg-blue-100 text-blue-900' : 'bg-emerald-100 text-emerald-900'
                    }`}>
                    {isCentral ? 'Central' : 'KA'}
                  </span>
                  {isSelected && <Check className="w-3.5 h-3.5 text-[#D7A85B] stroke-[2.5]" />}
                </button>
              );
            })}
          </div>
        </div>

        {/* 3. Comparison Content Matrix (Smooth Single-Container Scrolling) */}
        <div className="flex-1 min-h-0 overflow-auto p-4 sm:p-6 text-xs font-sans relative scrollbar-thin">
          {isLoading ? (
            <div className="h-64 flex flex-col items-center justify-center space-y-3 text-[#183B2B]">
              <div className="w-8 h-8 rounded-full border-3 border-[#D7A85B] border-t-transparent animate-spin" />
              <p className="font-kannada font-bold text-sm">
                {language === 'kn' ? 'ಯೋಜನಾ ಹೋಲಿಕಾ ಕೋಷ್ಟಕ ಸಿದ್ಧವಾಗುತ್ತಿದೆ...' : 'Loading statutory comparison matrix...'}
              </p>
            </div>
          ) : comparisonData && comparisonData.schemes.length > 0 ? (
            <div className="min-w-full inline-block align-middle">
              <table className="w-full border-separate border-spacing-0 border border-[#E2D9C8] rounded-2xl overflow-hidden shadow-xs">

                {/* Sticky Header Row: Scheme Titles & Top Action Buttons */}
                <thead>
                  <tr>
                    {/* Top-Left Corner Header Cell (Sticky both horizontally & vertically) */}
                    <th className="sticky top-0 left-0 z-30 p-4 text-left w-56 sm:w-64 bg-[#FAF7F0] border-b border-r border-[#E2D9C8] backdrop-blur-md">
                      <div className="text-xs font-mono uppercase tracking-wider font-extrabold text-[#183B2B]">
                        {language === 'kn' ? 'ಹೋಲಿಕಾ ನಿಯತಾಂಕಗಳು' : 'Comparison Dimension'}
                      </div>
                      <div className="text-[11px] font-sans font-normal text-[#6B7468] mt-0.5">
                        {language === 'kn' ? `${comparisonData.schemes.length} ಯೋಜನೆಗಳು` : `${comparisonData.schemes.length} Schemes Selected`}
                      </div>
                    </th>

                    {/* Scheme Column Headers (Sticky vertically at top) */}
                    {comparisonData.schemes.map((s) => {
                      const isReal = s.scheme_type === 'real';
                      const isCentral = s.government_level === 'central';
                      const match = getMatchResult(s.scheme_id);

                      return (
                        <th
                          key={s.scheme_id}
                          className="sticky top-0 z-20 p-4 text-left min-w-[280px] sm:min-w-[320px] max-w-[360px] bg-[#FAF7F0] border-b border-r border-[#E2D9C8] last:border-r-0 backdrop-blur-md shadow-xs align-top"
                        >
                          <div className="space-y-2">
                            {/* Government & Real/Demo Badges */}
                            <div className="flex flex-wrap items-center gap-1.5">
                              <span className={`text-[10px] font-mono font-bold px-2 py-0.5 rounded-full uppercase ${isCentral ? 'bg-blue-100 text-blue-900 border border-blue-200' : 'bg-emerald-100 text-emerald-900 border border-emerald-200'
                                }`}>
                                {isCentral
                                  ? (language === 'kn' ? 'ಕೇಂದ್ರ ಸರ್ಕಾರ' : 'Central Govt')
                                  : (language === 'kn' ? 'ಕರ್ನಾಟಕ ಸರ್ಕಾರ' : 'Karnataka State')}
                              </span>
                              <span className={`text-[10px] font-mono font-bold px-2 py-0.5 rounded-full uppercase ${isReal ? 'bg-emerald-50 text-emerald-800 border border-emerald-200' : 'bg-amber-100 text-amber-900 border border-amber-200'
                                }`}>
                                {isReal ? t.realSchemeBadge : t.demoSchemeBadge}
                              </span>
                            </div>

                            {/* Scheme Title */}
                            <h3 className="text-sm sm:text-base font-extrabold font-kannada text-[#183B2B] leading-tight">
                              {language === 'kn' && s.name_kn ? s.name_kn : s.name}
                            </h3>

                            {/* Top Functional Apply / Action Button */}
                            <div className="pt-1">
                              {s.official_url ? (
                                <button
                                  onClick={() => handleApplyClick(s)}
                                  className="w-full group flex items-center justify-center space-x-2 px-3 py-2 rounded-xl bg-[#D7A85B] hover:bg-[#B08233] text-[#183B2B] font-extrabold text-xs transition-all shadow-sm active:scale-95"
                                  title={s.official_url}
                                >
                                  <span className="font-kannada">
                                    {language === 'kn' ? 'ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ' : 'Apply on Official Portal'}
                                  </span>
                                  <ExternalLink className="w-3.5 h-3.5 stroke-[2.2] group-hover:translate-x-0.5 transition-transform" />
                                </button>
                              ) : isReal ? (
                                <button
                                  onClick={() => handleApplyClick(s)}
                                  className="w-full flex items-center justify-center space-x-2 px-3 py-2 rounded-xl bg-white hover:bg-[#FAF7F0] text-[#183B2B] border-2 border-[#183B2B] font-bold text-xs transition-all shadow-xs active:scale-95"
                                >
                                  <Building2 className="w-3.5 h-3.5 stroke-[2]" />
                                  <span className="font-kannada">
                                    {language === 'kn' ? 'ಕೃಷಿ ಕಚೇರಿ / ಅರ್ಜಿ ವಿಧಾನ' : 'Visit Office / How to Apply'}
                                  </span>
                                </button>
                              ) : (
                                <div className="px-3 py-2 rounded-xl bg-amber-50 border border-amber-200 text-amber-900 text-center text-[11px] font-mono font-bold">
                                  {language === 'kn' ? 'ಪ್ರಾಯೋಗಿಕ ಪರೀಕ್ಷಾರ್ಥ ಯೋಜನೆ' : 'Demonstration Simulation Only'}
                                </div>
                              )}
                            </div>
                          </div>
                        </th>
                      );
                    })}
                  </tr>
                </thead>

                {/* Table Body: Detailed Comparative Dimensions */}
                <tbody className="divide-y divide-[#E2D9C8] text-[#282C27] font-sans">

                  {/* 1. Farmer Live Eligibility Evaluation */}
                  {matchResults.length > 0 && (
                    <tr className="hover:bg-[#FAF7F0]/40 transition-colors">
                      <td className="sticky left-0 z-10 p-3.5 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                        {language === 'kn' ? 'ಅರ್ಹತಾ ಸ್ಥಿತಿ (Your Eligibility)' : 'Your Eligibility Status'}
                      </td>
                      {comparisonData.schemes.map((s) => {
                        const match = getMatchResult(s.scheme_id);
                        if (!match) {
                          return (
                            <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0 text-[#6B7468] italic">
                              {language === 'kn' ? 'ಪರಿಶೀಲನೆ ಲಭ್ಯವಿಲ್ಲ' : 'Evaluation not available'}
                            </td>
                          );
                        }

                        const isSuitable = match.evaluation_status === 'POTENTIALLY_SUITABLE';
                        const isNotSuitable = match.evaluation_status === 'NOT_SUITABLE_BASED_ON_KNOWN_RULES';

                        return (
                          <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0 space-y-2">
                            <div className="flex items-center space-x-2">
                              {isSuitable ? (
                                <div className="inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 font-bold text-xs">
                                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                                  <span>{language === 'kn' ? 'ಅರ್ಹತೆ ಸಾಧ್ಯತೆ ಇದೆ' : 'Potentially Suitable'}</span>
                                </div>
                              ) : isNotSuitable ? (
                                <div className="inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-full bg-[#F7E4DE] text-[#9E4E30] border border-[#C66F4E] font-bold text-xs">
                                  <XCircle className="w-3.5 h-3.5 text-[#C66F4E]" />
                                  <span>{language === 'kn' ? 'ಅರ್ಹತೆ ಹೊಂದಿಲ್ಲ' : 'Not Suitable'}</span>
                                </div>
                              ) : (
                                <div className="inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-full bg-[#FBF4E4] text-[#B08233] border border-[#D7A85B] font-bold text-xs">
                                  <AlertCircle className="w-3.5 h-3.5 text-[#B08233]" />
                                  <span>{language === 'kn' ? 'ಹೆಚ್ಚುವರಿ ಮಾಹಿತಿ ಅಗತ್ಯ' : 'Information Needed'}</span>
                                </div>
                              )}
                            </div>

                            <p className="text-[11px] text-[#4A5148] font-kannada leading-relaxed">
                              {language === 'kn' && match.match_reason_kn ? match.match_reason_kn : match.match_reason}
                            </p>

                            {/* Rules Summary Tally */}
                            <div className="flex flex-wrap gap-1.5 text-[10px] font-mono">
                              <span className="px-1.5 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200">
                                ✓ {match.satisfied_rules.length} Satisfied
                              </span>
                              {match.unsatisfied_rules.length > 0 && (
                                <span className="px-1.5 py-0.5 rounded bg-red-50 text-red-800 border border-red-200">
                                  ✕ {match.unsatisfied_rules.length} Failed
                                </span>
                              )}
                              {match.unknown_rules.length > 0 && (
                                <span className="px-1.5 py-0.5 rounded bg-amber-50 text-amber-800 border border-amber-200">
                                  ? {match.unknown_rules.length} Missing
                                </span>
                              )}
                            </div>
                          </td>
                        );
                      })}
                    </tr>
                  )}

                  {/* 2. Purpose */}
                  <tr className="hover:bg-[#FAF7F0]/40 transition-colors">
                    <td className="sticky left-0 z-10 p-3.5 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                      {language === 'kn' ? 'ಯೋಜನೆಯ ಉದ್ದೇಶ (Purpose)' : 'Scheme Purpose & Scope'}
                    </td>
                    {comparisonData.schemes.map((s) => (
                      <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0 leading-relaxed font-kannada">
                        {language === 'kn' && s.purpose_kn ? s.purpose_kn : s.purpose}
                      </td>
                    ))}
                  </tr>

                  {/* 3. Target Beneficiaries */}
                  <tr className="hover:bg-[#FAF7F0]/40 transition-colors">
                    <td className="sticky left-0 z-10 p-3.5 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                      {language === 'kn' ? 'ಅರ್ಹ ಫಲಾನುಭವಿಗಳು (Target)' : 'Target Beneficiaries'}
                    </td>
                    {comparisonData.schemes.map((s) => (
                      <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0 font-kannada leading-relaxed">
                        {language === 'kn' && s.target_beneficiaries_kn ? s.target_beneficiaries_kn : s.target_beneficiaries}
                      </td>
                    ))}
                  </tr>

                  {/* 4. Benefits Summary */}
                  <tr className="hover:bg-[#FAF7F0]/40 transition-colors">
                    <td className="sticky left-0 z-10 p-3.5 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                      {language === 'kn' ? 'ಲಭ್ಯವಿರುವ ಪ್ರಯೋಜನಗಳು (Benefits)' : 'Statutory Benefits & Subsidies'}
                    </td>
                    {comparisonData.schemes.map((s) => (
                      <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0 font-kannada">
                        <ul className="space-y-1.5">
                          {(language === 'kn' && s.benefits_summary_kn ? s.benefits_summary_kn : s.benefits_summary).map((b, i) => (
                            <li key={i} className="flex items-start space-x-1.5 leading-snug">
                              <span className="text-[#D7A85B] font-bold mt-0.5">•</span>
                              <span>{b}</span>
                            </li>
                          ))}
                        </ul>
                      </td>
                    ))}
                  </tr>

                  {/* 5. Key Eligibility Criteria */}
                  <tr className="hover:bg-[#FAF7F0]/40 transition-colors">
                    <td className="sticky left-0 z-10 p-3.5 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                      {language === 'kn' ? 'ಕಡ್ಡಾಯ ಅರ್ಹತಾ ಷರತ್ತುಗಳು (Eligibility)' : 'Mandatory Eligibility Criteria'}
                    </td>
                    {comparisonData.schemes.map((s) => (
                      <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0 font-kannada">
                        <ul className="space-y-1.5">
                          {(language === 'kn' && s.key_eligibility_kn ? s.key_eligibility_kn : s.key_eligibility).map((e, i) => (
                            <li key={i} className="flex items-start space-x-1.5 leading-snug">
                              <span className="text-emerald-700 font-bold mt-0.5">✓</span>
                              <span>{e}</span>
                            </li>
                          ))}
                        </ul>
                      </td>
                    ))}
                  </tr>

                  {/* 6. Required Documents */}
                  <tr className="hover:bg-[#FAF7F0]/40 transition-colors">
                    <td className="sticky left-0 z-10 p-3.5 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                      {language === 'kn' ? 'ಅಗತ್ಯ ದಾಖಲೆಗಳು (Documents)' : 'Required Documents'}
                    </td>
                    {comparisonData.schemes.map((s) => (
                      <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0 font-kannada">
                        <ul className="space-y-1.5">
                          {(language === 'kn' && s.required_documents_kn ? s.required_documents_kn : s.required_documents).map((d, i) => (
                            <li key={i} className="flex items-start space-x-1.5 leading-snug text-[#4A5148]">
                              <FileText className="w-3.5 h-3.5 text-[#B08233] flex-shrink-0 mt-0.5" />
                              <span>{d}</span>
                            </li>
                          ))}
                        </ul>
                      </td>
                    ))}
                  </tr>

                  {/* 7. Application Mode & Steps */}
                  <tr className="hover:bg-[#FAF7F0]/40 transition-colors">
                    <td className="sticky left-0 z-10 p-3.5 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                      {language === 'kn' ? 'ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ವಿಧಾನ (How to Apply)' : 'Application Mode & Process'}
                    </td>
                    {comparisonData.schemes.map((s) => (
                      <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0 font-kannada space-y-2">
                        <p className="font-semibold text-[#183B2B] leading-snug">
                          {language === 'kn' && s.application_mode_kn ? s.application_mode_kn : s.application_mode}
                        </p>
                        {s.application_steps && s.application_steps.length > 0 && (
                          <div className="pt-1 space-y-1 text-[11px] text-[#4A5148]">
                            {(language === 'kn' && s.application_steps_kn && s.application_steps_kn.length > 0
                              ? s.application_steps_kn
                              : s.application_steps
                            ).slice(0, 3).map((st, idx) => (
                              <div key={idx} className="flex items-start space-x-1.5">
                                <span className="font-mono font-bold text-[#B08233]">{idx + 1}.</span>
                                <span>{st}</span>
                              </div>
                            ))}
                          </div>
                        )}
                      </td>
                    ))}
                  </tr>

                  {/* 8. Issuing & Verification Authority */}
                  <tr className="hover:bg-[#FAF7F0]/40 transition-colors">
                    <td className="sticky left-0 z-10 p-3.5 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                      {language === 'kn' ? 'ಪರಿಶೀಲನಾ ಪ್ರಾಧಿಕಾರ (Authority)' : 'Implementing Department & Authority'}
                    </td>
                    {comparisonData.schemes.map((s) => (
                      <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0 text-[11px] text-[#4A5148]">
                        <div className="space-y-1">
                          {s.issuing_authority && (
                            <div>
                              <span className="font-bold text-[#183B2B] block">Issuing:</span>
                              <span>{s.issuing_authority}</span>
                            </div>
                          )}
                          {s.verification_authority && (
                            <div>
                              <span className="font-bold text-[#183B2B] block">Verification:</span>
                              <span>{s.verification_authority}</span>
                            </div>
                          )}
                        </div>
                      </td>
                    ))}
                  </tr>

                  {/* 9. Official Source Portal */}
                  <tr className="hover:bg-[#FAF7F0]/40 transition-colors">
                    <td className="sticky left-0 z-10 p-3.5 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                      {language === 'kn' ? 'ಅಧಿಕೃತ ಪೋರ್ಟಲ್ ಕೊಂಡಿ' : 'Official Portal URL'}
                    </td>
                    {comparisonData.schemes.map((s) => (
                      <td key={s.scheme_id} className="p-3.5 border-r border-[#E2D9C8] last:border-r-0">
                        {s.official_url ? (
                          <a
                            href={s.official_url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-[#183B2B] hover:text-[#B08233] inline-flex items-center space-x-1.5 font-bold font-mono underline break-all"
                          >
                            <span>{s.official_url}</span>
                            <ExternalLink className="w-3.5 h-3.5 flex-shrink-0" />
                          </a>
                        ) : (
                          <span className="text-[#6B7468] italic font-kannada text-[11px]">
                            {language === 'kn' ? 'ನೇರ ಪೋರ್ಟಲ್ ಇಲ್ಲ (ಸ್ಥಳೀಯ ಇಲಾಖಾ ಕಚೇರಿಗೆ ಭೇಟಿ ನೀಡಿ)' : 'No direct online portal (Office visit required)'}
                          </span>
                        )}
                      </td>
                    ))}
                  </tr>

                  {/* 10. Bottom Action Row (Apply / Check Process) */}
                  <tr className="bg-[#FAF7F0]/70">
                    <td className="sticky left-0 z-10 p-4 font-bold font-kannada bg-[#FAF7F0] border-r border-[#E2D9C8] text-[#183B2B]">
                      {language === 'kn' ? 'ಕ್ರಮ / ಅರ್ಜಿ ಸಲ್ಲಿಕೆ' : 'Action & Application'}
                    </td>
                    {comparisonData.schemes.map((s) => (
                      <td key={s.scheme_id} className="p-4 border-r border-[#E2D9C8] last:border-r-0">
                        {s.official_url ? (
                          <button
                            onClick={() => handleApplyClick(s)}
                            className="w-full flex items-center justify-center space-x-2 px-4 py-2.5 rounded-xl bg-[#D7A85B] hover:bg-[#B08233] text-[#183B2B] font-extrabold text-xs transition-all shadow-sm active:scale-95"
                          >
                            <span className="font-kannada">
                              {language === 'kn' ? 'ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ' : 'Apply on Official Portal'}
                            </span>
                            <ExternalLink className="w-4 h-4" />
                          </button>
                        ) : s.scheme_type === 'real' ? (
                          <button
                            onClick={() => handleApplyClick(s)}
                            className="w-full flex items-center justify-center space-x-2 px-4 py-2.5 rounded-xl bg-white hover:bg-[#FAF7F0] text-[#183B2B] border-2 border-[#183B2B] font-bold text-xs transition-all shadow-xs active:scale-95"
                          >
                            <Building2 className="w-4 h-4 text-[#183B2B]" />
                            <span className="font-kannada">
                              {language === 'kn' ? 'ಕೃಷಿ ಕಚೇರಿ / ಅರ್ಜಿ ವಿಧಾನ' : 'Visit Office / Process'}
                            </span>
                          </button>
                        ) : (
                          <div className="px-3 py-2 text-center text-[#6B7468] font-mono text-[11px]">
                            Demo Only
                          </div>
                        )}
                      </td>
                    ))}
                  </tr>

                </tbody>
              </table>

              {/* Statutory Disclaimer Box */}
              <div className="mt-5 p-4 bg-[#FBF4E4] rounded-2xl border border-[#D7A85B]/40 text-[#B08233] flex items-start space-x-3 text-xs leading-relaxed">
                <AlertTriangle className="w-5 h-5 text-[#B08233] flex-shrink-0 mt-0.5" />
                <div className="space-y-1">
                  <span className="font-extrabold font-mono uppercase tracking-wider block">
                    {language === 'kn' ? 'ಶಾಸನಬದ್ಧ ಸ್ಪಷ್ಟನೆ ಮತ್ತು ಎಚ್ಚರಿಕೆ' : 'Statutory Clarification & Public Disclaimer'}
                  </span>
                  <p className="font-kannada text-[#282C27] text-xs">
                    {language === 'kn' ? comparisonData.disclaimer_kn : comparisonData.disclaimer}
                  </p>
                </div>
              </div>

            </div>
          ) : (
            <div className="h-48 flex items-center justify-center text-[#6B7468] font-kannada">
              {language === 'kn' ? 'ಹೋಲಿಕೆಗೆ ಕನಿಷ್ಠ 2 ಯೋಜನೆಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ.' : 'Select at least 2 schemes to view comparison.'}
            </div>
          )}
        </div>

        {/* 4. Modal Footer (Fixed at bottom) */}
        <div className="flex-shrink-0 px-6 py-4 border-t border-[#E2D9C8] bg-[#FAF7F0] flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
          <div className="flex items-center space-x-2 text-[#4A5148] font-kannada text-xs">
            <ShieldCheck className="w-4 h-4 text-[#183B2B]" />
            <span>
              {language === 'kn'
                ? 'ಕೃಷಿ ಮಿತ್ರ ಕೇವಲ ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗಳಿಗೆ ಮಾತ್ರ ಸಂಪರ್ಕಿಸುತ್ತದೆ. ನಕಲಿ ಸಲ್ಲಿಕೆಗಳನ್ನು ಮಾಡುವುದಿಲ್ಲ.'
                : 'Krishi Mitra links directly to verified statutory portals without intermediaries.'}
            </span>
          </div>

          <button
            onClick={onClose}
            className="px-6 py-2.5 bg-[#183B2B] hover:bg-[#23503B] text-white rounded-xl text-xs font-bold transition-all shadow-sm active:scale-95"
          >
            {t.close}
          </button>
        </div>

      </div>

      {/* 5. Application Portal Redirection / Process Guidance Modal */}
      {activeGuidance && (
        <div className="fixed inset-0 z-60 bg-black/70 backdrop-blur-md flex items-center justify-center p-4 animate-fadeIn">
          <div className="bg-white rounded-[2rem] shadow-2xl max-w-lg w-full p-6 sm:p-7 border border-[#E2D9C8] space-y-5">

            {/* Header */}
            <div className="flex items-start justify-between">
              <div className="flex items-center space-x-3">
                <div className={`w-11 h-11 rounded-2xl flex items-center justify-center ${activeGuidance.type === 'online_portal'
                    ? 'bg-[#FBF4E4] text-[#B08233]'
                    : 'bg-[#DEE4D2] text-[#183B2B]'
                  }`}>
                  {activeGuidance.type === 'online_portal' ? (
                    <ExternalLink className="w-5 h-5 stroke-[2.2]" />
                  ) : (
                    <Building2 className="w-5 h-5 stroke-[2.2]" />
                  )}
                </div>
                <div>
                  <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-[#6B7468]">
                    {activeGuidance.type === 'online_portal' ? 'Official Portal Redirection' : 'Departmental Application'}
                  </span>
                  <h3 className="text-base sm:text-lg font-extrabold font-kannada text-[#183B2B]">
                    {language === 'kn' && activeGuidance.scheme.name_kn
                      ? activeGuidance.scheme.name_kn
                      : activeGuidance.scheme.name}
                  </h3>
                </div>
              </div>
              <button
                onClick={() => setActiveGuidance(null)}
                className="text-[#6B7468] hover:text-[#183B2B] p-1.5 rounded-lg hover:bg-[#FAF7F0]"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Content for Online Official Portal */}
            {activeGuidance.type === 'online_portal' && activeGuidance.scheme.official_url && (
              <div className="space-y-4">
                <div className="p-3.5 rounded-xl bg-[#FAF7F0] border border-[#E2D9C8] space-y-1.5 text-xs">
                  <span className="font-mono text-[10px] uppercase font-bold text-[#6B7468] block">
                    {language === 'kn' ? 'ಅಧಿಕೃತ ಸರ್ಕಾರಿ ವೆಬ್‌ಸೈಟ್ ವಿಳಾಸ:' : 'Official Government Portal Destination:'}
                  </span>
                  <p className="font-mono font-bold text-[#183B2B] break-all select-all text-xs bg-white p-2 rounded-lg border border-[#E2D9C8]">
                    {activeGuidance.scheme.official_url}
                  </p>
                </div>

                <div className="space-y-2 text-xs font-kannada text-[#4A5148] leading-relaxed">
                  <p className="font-bold text-[#183B2B]">
                    {language === 'kn' ? 'ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮುನ್ನ ನಿಮ್ಮ ಬಳಿ ಇರಬೇಕಾದ ದಾಖಲೆಗಳು:' : 'Keep the following ready before applying:'}
                  </p>
                  <ul className="space-y-1 list-disc list-inside text-[11px]">
                    <li>{language === 'kn' ? 'ಆಧಾರ್ ಕಾರ್ಡ್ (ಮೊಬೈಲ್ ಒಟಿಪಿ ಲಿಂಕ್)' : 'Aadhaar Card with mobile OTP'}</li>
                    <li>{language === 'kn' ? 'ಚಾಲ್ತಿ ಸಾಲಿನ ಪಹಣಿ (RTC / Pahani)' : 'Land RTC / Pahani record'}</li>
                    <li>{language === 'kn' ? 'ಆಧಾರ್ ಜೋಡಿತ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್' : 'Aadhaar-seeded bank passbook'}</li>
                  </ul>
                </div>

                <div className="p-3 bg-emerald-50 rounded-xl border border-emerald-200 text-emerald-900 text-xs flex items-center space-x-2">
                  <ShieldCheck className="w-4 h-4 text-emerald-600 flex-shrink-0" />
                  <span>
                    {language === 'kn'
                      ? 'ಕೃಷಿ ಮಿತ್ರ ನಿಮ್ಮನ್ನು ನೇರವಾಗಿ ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗೆ ಕೊಂಡೊಯ್ಯುತ್ತದೆ. ಯಾವುದೇ ಶುಲ್ಕವಿಲ್ಲ.'
                      : 'You will be redirected safely to the official statutory portal in a new tab.'}
                  </span>
                </div>

                <div className="flex space-x-3 pt-2">
                  <button
                    onClick={() => setActiveGuidance(null)}
                    className="flex-1 py-2.5 rounded-xl bg-[#FAF7F0] hover:bg-[#EBE5D8] text-[#282C27] font-bold text-xs font-kannada border border-[#E2D9C8]"
                  >
                    {language === 'kn' ? 'ರದ್ದುಮಾಡಿ' : 'Cancel'}
                  </button>
                  <button
                    onClick={() => proceedToOfficialPortal(activeGuidance.scheme.official_url!)}
                    className="flex-1 py-2.5 rounded-xl bg-[#D7A85B] hover:bg-[#B08233] text-[#183B2B] font-extrabold text-xs font-kannada flex items-center justify-center space-x-2 shadow-sm"
                  >
                    <span>{language === 'kn' ? 'ಪೋರ್ಟಲ್‌ಗೆ ಮುಂದುವರಿಯಿರಿ' : 'Proceed to Official Portal'}</span>
                    <ExternalLink className="w-3.5 h-3.5 stroke-[2.2]" />
                  </button>
                </div>
              </div>
            )}

            {/* Content for Offline / Departmental Application */}
            {activeGuidance.type === 'offline_process' && (
              <div className="space-y-4">
                <div className="p-3.5 rounded-xl bg-[#FAF7F0] border border-[#E2D9C8] space-y-1.5 text-xs">
                  <span className="font-mono text-[10px] uppercase font-bold text-[#6B7468] block">
                    {language === 'kn' ? 'ಅನುಷ್ಠಾನ ಇಲಾಖೆ / ಕಚೇರಿ:' : 'Implementing Department / Contact:'}
                  </span>
                  <p className="font-bold text-[#183B2B] text-xs">
                    {activeGuidance.scheme.issuing_authority || 'Department of Agriculture, Government of Karnataka'}
                  </p>
                  {activeGuidance.scheme.verification_authority && (
                    <p className="text-[11px] text-[#4A5148]">
                      Verification: {activeGuidance.scheme.verification_authority}
                    </p>
                  )}
                </div>

                {/* Application Steps */}
                <div className="space-y-2 text-xs font-kannada">
                  <span className="font-bold text-[#183B2B] block">
                    {language === 'kn' ? 'ಅರ್ಜಿ ಸಲ್ಲಿಕೆಯ ಹಂತಗಳು:' : 'Step-by-Step Application Steps:'}
                  </span>
                  <div className="space-y-1.5 text-[11px] text-[#282C27] max-h-48 overflow-y-auto pr-1">
                    {(language === 'kn' && activeGuidance.scheme.application_steps_kn && activeGuidance.scheme.application_steps_kn.length > 0
                      ? activeGuidance.scheme.application_steps_kn
                      : activeGuidance.scheme.application_steps && activeGuidance.scheme.application_steps.length > 0
                        ? activeGuidance.scheme.application_steps
                        : [activeGuidance.scheme.application_mode]
                    ).map((step, idx) => (
                      <div key={idx} className="flex items-start space-x-2 p-2 rounded-lg bg-[#FAF7F0] border border-[#E2D9C8]">
                        <span className="w-5 h-5 rounded-full bg-[#183B2B] text-[#D7A85B] flex items-center justify-center font-mono font-bold text-[10px] flex-shrink-0 mt-0.5">
                          {idx + 1}
                        </span>
                        <span className="leading-snug">{step}</span>
                      </div>
                    ))}
                  </div>
                </div>

                <div className="p-3 bg-amber-50 rounded-xl border border-amber-200 text-amber-900 text-xs flex items-center space-x-2">
                  <Info className="w-4 h-4 text-amber-700 flex-shrink-0" />
                  <span>
                    {language === 'kn'
                      ? 'ಈ ಯೋಜನೆಗೆ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಇರುವುದಿಲ್ಲ. ಅಗತ್ಯ ದಾಖಲೆಗಳೊಂದಿಗೆ ಸ್ಥಳೀಯ ಕಚೇರಿಗೆ ಭೇಟಿ ನೀಡಿ.'
                      : 'Physical application at your local department office / RSK is required for this component.'}
                  </span>
                </div>

                <button
                  onClick={() => setActiveGuidance(null)}
                  className="w-full py-2.5 rounded-xl bg-[#183B2B] text-white font-bold text-xs font-kannada hover:bg-[#23503B] transition-colors"
                >
                  {language === 'kn' ? 'ತಿಳಿದಿದೆ (ಮುಕ್ತಾಯ)' : 'Understood (Close)'}
                </button>
              </div>
            )}

          </div>
        </div>
      )}

    </div>
  );
};
