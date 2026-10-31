import React, { useState, useEffect } from 'react';
import {
  FileCheck2,
  CheckCircle2,
  Circle,
  AlertCircle,
  Clock,
  ExternalLink,
  ShieldAlert,
  ArrowRight,
  Sparkles,
  Layers,
  ChevronRight,
  Info,
  Loader2,
  CheckSquare,
  Square
} from 'lucide-react';
import { translations } from '../../utils/translations';
import { SchemeMatchResult, SchemeReadinessChecklist, ChecklistItem } from '../../types';
import { api } from '../../services/api';

interface ApplicationJourneyViewProps {
  recommendations: SchemeMatchResult[];
  language: 'kn' | 'en';
  sessionId: string;
  selectedSchemeTarget?: SchemeMatchResult | null;
  onNavigateToVoice: () => void;
  onNavigateToSchemes: () => void;
}

export const ApplicationJourneyView: React.FC<ApplicationJourneyViewProps> = ({
  recommendations,
  language,
  sessionId,
  selectedSchemeTarget,
  onNavigateToVoice,
  onNavigateToSchemes
}) => {
  const t = translations[language];

  // Default active scheme to user selected, or first potentially suitable scheme, or first scheme
  const defaultSchemeId = selectedSchemeTarget?.scheme.id ||
    recommendations.find(r => r.evaluation_status === 'POTENTIALLY_SUITABLE')?.scheme.id ||
    recommendations[0]?.scheme.id ||
    'PM-KISAN';

  const [activeSchemeId, setActiveSchemeId] = useState<string>(defaultSchemeId);
  const [checklist, setChecklist] = useState<SchemeReadinessChecklist | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [userCheckedItems, setUserCheckedItems] = useState<Record<string, boolean>>({});

  // Sync when selectedSchemeTarget changes
  useEffect(() => {
    if (selectedSchemeTarget) {
      setActiveSchemeId(selectedSchemeTarget.scheme.id);
    }
  }, [selectedSchemeTarget]);

  // Load checklist from backend API
  useEffect(() => {
    const fetchChecklist = async () => {
      setIsLoading(true);
      try {
        const data = await api.getSchemeChecklist(activeSchemeId, sessionId);
        setChecklist(data);
        // Initialize checked items from backend evidence
        const initialChecked: Record<string, boolean> = {};
        data.items.forEach(item => {
          if (item.is_completed) {
            initialChecked[item.item_id] = true;
          }
        });
        setUserCheckedItems(initialChecked);
      } catch (err) {
        console.warn('Could not load checklist from API:', err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchChecklist();
  }, [activeSchemeId, sessionId]);

  const toggleCheck = (itemId: string) => {
    setUserCheckedItems(prev => ({
      ...prev,
      [itemId]: !prev[itemId]
    }));
  };

  // Compute local progress
  const totalItems = checklist?.items.length || 1;
  const completedCount = checklist?.items.filter(i => userCheckedItems[i.item_id]).length || 0;
  const progressPercent = Math.round((completedCount / totalItems) * 100);

  const steps = [
    { num: '01', title: language === 'kn' ? 'ಅರ್ಹತೆ ಪರೀಕ್ಷಿಸಿ' : 'Check Eligibility', desc: language === 'kn' ? 'ಅರ್ಹತಾ ಮೌಲ್ಯಮಾಪನ' : 'Eligibility Assessment', done: true },
    { num: '02', title: language === 'kn' ? 'ಷರತ್ತು ಪರಿಶೀಲನೆ' : 'Review Requirements', desc: language === 'kn' ? 'ಜಮೀನು ಮತ್ತು ಬೆಳೆ ಮಾನದಂಡ' : 'Land & Crop Verification', done: true },
    { num: '03', title: language === 'kn' ? 'ದಾಖಲೆ ಸಿದ್ಧತೆ' : 'Prepare Documents', desc: language === 'kn' ? 'ಆರ್ಟಿಸಿ, ಆಧಾರ್, ಪಾಸ್ ಬುಕ್' : 'RTC, Aadhaar, Passbook', active: true },
    { num: '04', title: language === 'kn' ? 'ಬಾಕಿ ಮಾಹಿತಿ ಭರ್ತಿ' : 'Fill Missing Info', desc: language === 'kn' ? 'ಸ್ಪಷ್ಟೀಕರಣ ಒದಗಿಸಿ' : 'Resolve Clarifications', done: false },
    { num: '05', title: language === 'kn' ? 'ಅಧಿಕೃತ ಪೋರ್ಟಲ್' : 'Official Portal', desc: language === 'kn' ? 'ಅರ್ಜಿ ಸಲ್ಲಿಕೆ' : 'Submit on Portal', done: false }
  ];

  const activeSchemeObj = recommendations.find(r => r.scheme.id === activeSchemeId)?.scheme;

  return (
    <div className="max-w-6xl mx-auto space-y-8 pb-20 animate-fadeIn">

      {/* 1. Header & Stage Tracker */}
      <div className="p-8 rounded-[2rem] bg-white border border-ivory-border shadow-editorial space-y-6">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="space-y-1.5">
            <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-forest text-ivory text-xs font-mono tracking-wider uppercase">
              <FileCheck2 className="w-3.5 h-3.5 text-harvest" />
              <span>Step-by-Step Guided Application Journey</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-extrabold font-kannada text-charcoal">
              {language === 'kn' ? 'ಯೋಜನಾ ಅರ್ಜಿ ಪೂರ್ವ ಸಿದ್ಧತಾ ಮಾರ್ಗ' : 'Pre-Application Readiness Journey'}
            </h2>
            <p className="text-xs sm:text-sm text-charcoal-muted font-kannada">
              {language === 'kn'
                ? 'ಕೃಷಿ ಇಲಾಖೆಗೆ ಭೇಟಿ ನೀಡುವ ಮುನ್ನ ನಿಮ್ಮ ಎಲ್ಲಾ ದಾಖಲೆಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ಹಂತ-ಹಂತದ ಮಾರ್ಗದರ್ಶಿ.'
                : 'Guided visual steps to assemble mandatory records before visiting the official government portal.'}
            </p>
          </div>

          {/* Target Scheme Dropdown / Selector */}
          <div className="flex items-center space-x-2">
            <span className="text-xs font-mono text-charcoal-muted whitespace-nowrap">
              {language === 'kn' ? 'ಯೋಜನೆ:' : 'Target:'}
            </span>
            <select
              value={activeSchemeId}
              onChange={(e) => setActiveSchemeId(e.target.value)}
              className="bg-ivory border border-ivory-border text-xs font-kannada font-bold text-forest px-4 py-2.5 rounded-xl focus:outline-none focus:border-forest"
            >
              {recommendations.map((r) => (
                <option key={r.scheme.id} value={r.scheme.id}>
                  {language === 'kn' && r.scheme.name_kn ? r.scheme.name_kn : r.scheme.name}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Visual 5-Stage Journey Stepper */}
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3 pt-4 border-t border-ivory-border">
          {steps.map((step, idx) => (
            <div
              key={idx}
              className={`p-3 rounded-xl border flex flex-col justify-between space-y-1 transition-all ${step.done
                  ? 'bg-emerald-50/80 border-emerald-200 text-emerald-950'
                  : step.active
                    ? 'bg-harvest/15 border-harvest/50 text-forest shadow-sm'
                    : 'bg-ivory border-ivory-border text-charcoal-muted opacity-80'
                }`}
            >
              <div className="flex items-center justify-between">
                <span className="font-mono text-xs font-bold">{step.num}</span>
                {step.done ? (
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                ) : (
                  <Circle className="w-3 h-3 text-harvest" />
                )}
              </div>
              <div>
                <p className="font-bold text-xs font-kannada leading-tight">{step.title}</p>
                <p className="text-[10px] font-kannada text-charcoal-muted mt-0.5 line-clamp-1">{step.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 2. Readiness Scorecard & Document Checklist */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">

        {/* Left Column: Progress Scorecard & Official Portal CTA */}
        <div className="lg:col-span-4 space-y-6">

          <div className="rounded-[2rem] bg-white p-6 border border-ivory-border shadow-editorial space-y-5 text-center">
            <span className="text-xs font-mono uppercase tracking-wider text-charcoal-muted font-semibold">
              {language === 'kn' ? 'ದಾಖಲೆ ಸಿದ್ಧತಾ ಪ್ರಮಾಣ' : 'Document Readiness Score'}
            </span>

            {/* Circular Progress Display */}
            <div className="relative w-36 h-36 mx-auto flex items-center justify-center">
              <svg className="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                <path
                  className="text-ivory-border"
                  strokeWidth="3.5"
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  className="text-harvest transition-all duration-700 ease-out"
                  strokeDasharray={`${progressPercent}, 100`}
                  strokeWidth="3.5"
                  strokeLinecap="round"
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
              </svg>
              <div className="absolute flex flex-col items-center">
                <span className="text-3xl font-extrabold font-mono text-forest">{progressPercent}%</span>
                <span className="text-[10px] font-mono text-charcoal-muted uppercase">Ready</span>
              </div>
            </div>

            <p className="text-xs font-kannada text-charcoal leading-relaxed">
              {language === 'kn'
                ? `${totalItems} ದಾಖಲೆಗಳಲ್ಲಿ ${completedCount} ಸಿದ್ಧವಾಗಿವೆ.`
                : `${completedCount} of ${totalItems} required documents verified.`}
            </p>

            {/* Official Portal Outlink Button */}
            {activeSchemeObj?.official_source_url && (
              <a
                href={activeSchemeObj.official_source_url}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full flex items-center justify-center space-x-2 py-3 px-4 rounded-xl bg-forest hover:bg-forest-700 text-ivory text-xs font-bold font-mono transition-all shadow-sm"
              >
                <span>{language === 'kn' ? 'ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ' : 'Visit Official Portal'}</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            )}
          </div>

          {/* Clear Non-Submission Disclaimer Notice */}
          <div className="p-4 rounded-2xl bg-ivory border border-ivory-border text-xs text-charcoal-muted space-y-2">
            <div className="flex items-center space-x-2 text-forest font-bold">
              <ShieldAlert className="w-4 h-4 text-harvest-dark" />
              <span className="font-kannada">{language === 'kn' ? 'ಪ್ರಾಮಾಣಿಕ ಮಾರ್ಗದರ್ಶಿ ಸೂಚನೆ' : 'Statutory Disclaimer'}</span>
            </div>
            <p className="font-kannada text-[11px] leading-relaxed">
              {language === 'kn'
                ? 'ಕೃಷಿ ಮಿತ್ರ ನೇರವಾಗಿ ಯಾವುದೇ ಅರ್ಜಿಯನ್ನು ಸರ್ಕಾರಕ್ಕೆ ಸಲ್ಲಿಸುವುದಿಲ್ಲ. ಇದು ರೈತರಿಗೆ ಅರ್ಜಿ ಸಿದ್ಧತೆಗೆ ನೆರವಾಗುವ ಮಾರ್ಗದರ್ಶಿಯಾಗಿದೆ.'
                : 'Krishi Mitra does not submit official applications. All welfare applications must be lodged on the designated government portals.'}
            </p>
          </div>

        </div>

        {/* Right Column: Interactive Document & Requirement Checklist */}
        <div className="lg:col-span-8 space-y-4">
          <div className="rounded-[2rem] bg-white p-6 sm:p-8 border border-ivory-border shadow-editorial space-y-6">

            <div className="flex items-center justify-between pb-4 border-b border-ivory-border">
              <h3 className="text-lg font-bold font-kannada text-charcoal">
                {language === 'kn' ? 'ಪರಿಶೀಲನಾ ಪಟ್ಟಿ (Checklist Items)' : 'Document & Verification Checklist'}
              </h3>
              <span className="text-xs font-mono text-charcoal-muted">
                {completedCount} / {totalItems} Completed
              </span>
            </div>

            {isLoading ? (
              <div className="py-12 text-center text-charcoal-muted space-y-2">
                <Loader2 className="w-8 h-8 animate-spin mx-auto text-forest" />
                <p className="text-xs font-kannada">ದಾಖಲೆಗಳ ಪಟ್ಟಿ ಲೋಡ್ ಆಗುತ್ತಿದೆ...</p>
              </div>
            ) : (
              <div className="space-y-3">
                {checklist?.items.map((item) => {
                  const isChecked = Boolean(userCheckedItems[item.item_id]);
                  return (
                    <div
                      key={item.item_id}
                      onClick={() => toggleCheck(item.item_id)}
                      className={`p-4 rounded-2xl border transition-all cursor-pointer flex items-start space-x-3.5 select-none ${isChecked
                          ? 'bg-emerald-50/50 border-emerald-200'
                          : 'bg-ivory/60 border-ivory-border hover:border-harvest'
                        }`}
                    >
                      <button className="mt-0.5 text-forest">
                        {isChecked ? (
                          <CheckSquare className="w-5 h-5 text-emerald-600 fill-emerald-100" />
                        ) : (
                          <Square className="w-5 h-5 text-charcoal-muted" />
                        )}
                      </button>

                      <div className="flex-1 space-y-1">
                        <div className="flex items-center justify-between">
                          <h4 className={`text-sm font-bold font-kannada ${isChecked ? 'text-emerald-950 line-through opacity-85' : 'text-charcoal'
                            }`}>
                            {language === 'kn' && item.title_kn ? item.title_kn : item.title}
                          </h4>
                          <span className={`text-[10px] font-mono px-2 py-0.5 rounded-full ${item.is_mandatory ? 'bg-terracotta/10 text-terracotta' : 'bg-ivory text-charcoal-muted'
                            }`}>
                            {item.is_mandatory ? 'Mandatory' : 'Optional'}
                          </span>
                        </div>

                        {(item.help_text_kn || item.help_text) && (
                          <p className="text-xs font-kannada text-charcoal-muted">
                            {language === 'kn' && item.help_text_kn ? item.help_text_kn : item.help_text}
                          </p>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            )}

            {/* Next Action Steps */}
            {checklist?.next_steps && checklist.next_steps.length > 0 && (
              <div className="pt-4 border-t border-ivory-border space-y-2">
                <span className="text-xs font-mono font-bold uppercase text-forest tracking-wider">
                  {language === 'kn' ? 'ಮುಂದಿನ ಕ್ರಮಗಳು:' : 'Recommended Next Steps:'}
                </span>
                <ul className="space-y-1 text-xs font-kannada text-charcoal-muted">
                  {(language === 'kn' && checklist.next_steps_kn ? checklist.next_steps_kn : checklist.next_steps).map((s, idx) => (
                    <li key={idx} className="flex items-start space-x-2">
                      <span className="text-harvest font-bold">•</span>
                      <span>{s}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

          </div>
        </div>

      </div>

    </div>
  );
};

