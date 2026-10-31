import React, { useState, useEffect } from 'react';
import {
  X,
  Volume2,
  Square,
  ExternalLink,
  CheckCircle2,
  FileText,
  ListOrdered,
  AlertTriangle,
  ShieldCheck,
  HelpCircle,
  XCircle,
  Clock,
  Sparkles
} from 'lucide-react';
import { SchemeMatchResult, SchemeReadinessChecklist } from '../../types';
import { api } from '../../services/api';
import { translations } from '../../utils/translations';

interface SchemeModalProps {
  matchResult: SchemeMatchResult | null;
  language: 'kn' | 'en';
  isOpen: boolean;
  onClose: () => void;
  onPlayAudio: (text: string) => void;
  onStopAudio: () => void;
  isPlayingAudio: boolean;
  sessionId?: string;
}

export const SchemeModal: React.FC<SchemeModalProps> = ({
  matchResult,
  language,
  isOpen,
  onClose,
  onPlayAudio,
  onStopAudio,
  isPlayingAudio,
  sessionId
}) => {
  const t = translations[language];
  const [activeTab, setActiveTab] = useState<'overview' | 'rules' | 'checklist'>('overview');
  const [checklist, setChecklist] = useState<SchemeReadinessChecklist | null>(null);
  const [checkedItems, setCheckedItems] = useState<Record<string, boolean>>({});
  const [isLoadingChecklist, setIsLoadingChecklist] = useState<boolean>(false);

  useEffect(() => {
    if (isOpen && matchResult) {
      loadChecklist(matchResult.scheme.id);
    }
  }, [isOpen, matchResult]);

  const loadChecklist = async (schemeId: string) => {
    setIsLoadingChecklist(true);
    try {
      const data = await api.getSchemeChecklist(schemeId, sessionId);
      setChecklist(data);
      // Initialize checked items from backend
      const initial: Record<string, boolean> = {};
      data.items.forEach((item) => {
        initial[item.item_id] = item.is_completed;
      });
      setCheckedItems(initial);
    } catch (e) {
      console.warn('Could not load dynamic checklist:', e);
    } finally {
      setIsLoadingChecklist(false);
    }
  };

  if (!isOpen || !matchResult) return null;

  const { scheme, satisfied_rules, unsatisfied_rules, unknown_rules, needs_verification_rules } = matchResult;
  const isReal = scheme.scheme_type === 'real';

  const toggleItem = (itemId: string) => {
    setCheckedItems((prev) => ({
      ...prev,
      [itemId]: !prev[itemId]
    }));
  };

  const getSpokenSummaryText = () => {
    if (language === 'kn') {
      const name = scheme.name_kn || scheme.name;
      const desc = scheme.description_kn || scheme.description;
      const match = matchResult.match_reason_kn || matchResult.match_reason;
      return `${name}. ${desc}. ನಿಮ್ಮ ಅರ್ಹತಾ ಸ್ಥಿತಿ: ${match}`;
    }
    return `${scheme.name}. ${scheme.description}. Your eligibility: ${matchResult.match_reason}`;
  };

  const totalChecklistItems = checklist ? checklist.items.length : (scheme.required_documents || []).length;
  const readyCount = checklist
    ? checklist.items.filter((it) => checkedItems[it.item_id]).length
    : Object.values(checkedItems).filter(Boolean).length;
  const readyPct = totalChecklistItems > 0 ? Math.round((readyCount / totalChecklistItems) * 100) : 0;

  return (
    <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-3 sm:p-5">
      <div className="bg-white rounded-[2rem] shadow-2xl max-w-3xl w-full max-h-[94vh] overflow-hidden border border-ivory-border flex flex-col justify-between">

        {/* Modal Header */}
        <div className="p-6 border-b border-ivory-border bg-white">
          <div className="flex items-start justify-between">
            <div>
              <div className="flex items-center space-x-2 mb-1.5">
                <span
                  className={`text-[10px] font-mono font-bold tracking-wider px-2.5 py-0.5 rounded-full uppercase border ${isReal
                      ? 'bg-emerald-50 text-emerald-800 border-emerald-300'
                      : 'bg-harvest/15 text-harvest-dark border-harvest/40'
                    }`}
                >
                  {isReal ? t.realSchemeBadge : t.demoSchemeBadge}
                </span>
                <span className="text-xs font-mono text-charcoal-muted capitalize">
                  {language === 'kn' && scheme.category_kn ? scheme.category_kn : scheme.category.replace('_', ' ')}
                </span>
                {scheme.last_verified_at && (
                  <span className="text-[11px] font-mono text-charcoal-muted">
                    Verified: {scheme.last_verified_at}
                  </span>
                )}
              </div>
              <h2 className="text-xl font-bold text-charcoal font-kannada">
                {language === 'kn' && scheme.name_kn ? scheme.name_kn : scheme.name}
              </h2>
            </div>

            <button
              onClick={onClose}
              className="text-charcoal-muted hover:text-charcoal rounded-xl p-1.5 transition ml-2 hover:bg-ivory"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Voice Read-Aloud Bar */}
          <div className="mt-3.5 flex items-center justify-between p-3 rounded-xl bg-ivory border border-ivory-border">
            <div className="text-xs font-kannada text-charcoal font-medium flex items-center space-x-1.5">
              <Sparkles className="w-3.5 h-3.5 text-harvest-dark" />
              <span>{language === 'kn' ? 'ಕನ್ನಡ ಧ್ವನಿಯಲ್ಲಿ ವಿವರಣೆ ಕೇಳಿ:' : 'Listen to scheme explanation in voice:'}</span>
            </div>
            <button
              onClick={() => isPlayingAudio ? onStopAudio() : onPlayAudio(getSpokenSummaryText())}
              className="px-3.5 py-1.5 rounded-xl bg-forest hover:bg-forest-700 text-ivory text-xs font-bold font-mono flex items-center space-x-1.5 shadow-sm"
            >
              {isPlayingAudio ? (
                <>
                  <Square className="w-3.5 h-3.5 fill-current text-red-300" />
                  <span>{t.stopSpeaking}</span>
                </>
              ) : (
                <>
                  <Volume2 className="w-3.5 h-3.5" />
                  <span>{t.readAloud}</span>
                </>
              )}
            </button>
          </div>

          {/* Navigation Tabs */}
          <div className="flex space-x-4 border-b border-gray-200 mt-4 text-xs font-semibold">
            <button
              onClick={() => setActiveTab('overview')}
              className={`pb-2 border-b-2 font-kannada transition ${activeTab === 'overview'
                  ? 'border-forest-700 text-forest-800'
                  : 'border-transparent text-gray-500 hover:text-gray-700'
                }`}
            >
              {language === 'kn' ? 'ವಿವರ & ಪ್ರಯೋಜನಗಳು' : 'Overview & Benefits'}
            </button>
            <button
              onClick={() => setActiveTab('rules')}
              className={`pb-2 border-b-2 font-kannada transition flex items-center space-x-1 ${activeTab === 'rules'
                  ? 'border-forest-700 text-forest-800'
                  : 'border-transparent text-gray-500 hover:text-gray-700'
                }`}
            >
              <span>{language === 'kn' ? 'ಅರ್ಹತಾ ನಿಯಮಗಳ ಆಡಿಟ್' : 'Eligibility Rules Audit'}</span>
              <span className="text-[10px] bg-emerald-100 text-emerald-800 rounded-full px-1.5">
                {scheme.eligibility_rules.length}
              </span>
            </button>
            <button
              onClick={() => setActiveTab('checklist')}
              className={`pb-2 border-b-2 font-kannada transition flex items-center space-x-1 ${activeTab === 'checklist'
                  ? 'border-forest-700 text-forest-800'
                  : 'border-transparent text-gray-500 hover:text-gray-700'
                }`}
            >
              <span>{t.readinessTitle}</span>
              <span className="text-[10px] bg-emerald-700 text-white rounded-full px-1.5">
                {readyPct}%
              </span>
            </button>
          </div>
        </div>

        {/* Tab Content Area */}
        <div className="flex-1 overflow-y-auto p-5 text-xs font-kannada space-y-4">

          {/* TAB 1: OVERVIEW & BENEFITS */}
          {activeTab === 'overview' && (
            <div className="space-y-4">
              <div>
                <p className="text-sm text-ktext-primary leading-relaxed">
                  {language === 'kn' && scheme.description_kn ? scheme.description_kn : scheme.description}
                </p>
              </div>

              {/* Benefits */}
              <div className="p-3.5 bg-emerald-50/60 rounded-xl border border-emerald-100">
                <h4 className="font-bold text-forest-900 mb-2 flex items-center space-x-1.5 text-xs">
                  <ShieldCheck className="w-4 h-4 text-forest-700" />
                  <span>{t.benefits}</span>
                </h4>
                <ul className="space-y-1.5 list-disc list-inside text-ktext-primary">
                  {(language === 'kn' && scheme.benefits_kn ? scheme.benefits_kn : scheme.benefits).map((b, i) => (
                    <li key={i}>{b}</li>
                  ))}
                </ul>
              </div>

              {/* Application Steps */}
              <div>
                <h4 className="font-bold text-forest-900 mb-2 flex items-center space-x-1.5 text-xs">
                  <ListOrdered className="w-4 h-4 text-forest-700" />
                  <span>{t.applicationSteps}</span>
                </h4>
                <div className="space-y-2">
                  {(language === 'kn' && scheme.application_steps_kn ? scheme.application_steps_kn : scheme.application_steps).map((step, idx) => (
                    <div key={idx} className="p-2.5 rounded-lg bg-gray-50 border border-gray-200/80 text-ktext-primary">
                      {step}
                    </div>
                  ))}
                </div>
              </div>

              {/* Issuing Authority & Location */}
              <div className="p-3 bg-gray-50 rounded-xl border border-gray-200 text-gray-700 text-xs flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                  <span className="font-semibold">{language === 'kn' ? 'ಜಾರಿ ಪ್ರಾಧಿಕಾರ:' : 'Issuing Authority:'} </span>
                  <span>{scheme.issuing_authority || 'Designated Government Agency'}</span>
                </div>
                <div>
                  <span className="font-semibold">{language === 'kn' ? 'ವ್ಯಾಪ್ತಿ:' : 'Coverage:'} </span>
                  <span>{scheme.applicable_locations.join(', ')}</span>
                </div>
              </div>

              {/* Notes */}
              {scheme.notes && scheme.notes.length > 0 && (
                <div className="p-3 bg-amber-50 rounded-xl border border-amber-200 text-amber-900">
                  <h4 className="font-bold mb-1 flex items-center space-x-1">
                    <AlertTriangle className="w-3.5 h-3.5 text-amber-600" />
                    <span>{language === 'kn' ? 'ಮುಖ್ಯ ಇತಿಮಿತಿಗಳು ಮತ್ತು ಷರತ್ತುಗಳು:' : 'Important Limitations:'}</span>
                  </h4>
                  <ul className="list-disc list-inside space-y-0.5">
                    {(language === 'kn' && scheme.notes_kn ? scheme.notes_kn : scheme.notes).map((n, i) => (
                      <li key={i}>{n}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}

          {/* TAB 2: ELIGIBILITY RULES AUDIT */}
          {activeTab === 'rules' && (
            <div className="space-y-3">
              <p className="text-gray-600 text-xs font-kannada">
                {language === 'kn'
                  ? 'ಈ ಯೋಜನೆಯ ಪ್ರತಿಯೊಂದು ಅರ್ಹತಾ ಮಾನದಂಡವನ್ನು ನಿಮ್ಮ ಜಮೀನು ಮತ್ತು ಬೆಳೆ ವಿವರಗಳೊಂದಿಗೆ ಪಾರದರ್ಶಕವಾಗಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ:'
                  : 'Every eligibility criterion is verified against your profile with statutory justifications:'}
              </p>

              {/* Satisfied Rules */}
              {satisfied_rules.map((rule, idx) => (
                <div key={idx} className="p-3 rounded-xl bg-emerald-50/70 border border-emerald-200 flex flex-col gap-1">
                  <div className="flex items-center justify-between">
                    <span className="flex items-center space-x-1.5 font-bold text-emerald-900">
                      <CheckCircle2 className="w-4 h-4 text-emerald-600 flex-shrink-0" />
                      <span>{language === 'kn' && rule.description_kn ? rule.description_kn : rule.description}</span>
                    </span>
                    <span className="text-[10px] font-bold uppercase px-2 py-0.5 rounded-full bg-emerald-200 text-emerald-900">
                      Satisfied
                    </span>
                  </div>
                  <p className="text-emerald-800 text-xs mt-0.5">
                    {language === 'kn' && rule.reason_kn ? rule.reason_kn : rule.reason}
                  </p>
                  {(rule.why_needed || rule.why_needed_kn) && (
                    <p className="text-[11px] text-emerald-700 bg-white/70 p-1.5 rounded-md mt-1 border border-emerald-100">
                      <span className="font-semibold">{t.whyNeeded} </span>
                      {language === 'kn' && rule.why_needed_kn ? rule.why_needed_kn : rule.why_needed}
                    </p>
                  )}
                  {rule.source_reference && (
                    <span className="text-[10px] text-gray-500 font-sans mt-0.5">Ref: {rule.source_reference}</span>
                  )}
                </div>
              ))}

              {/* Unsatisfied Rules */}
              {unsatisfied_rules.map((rule, idx) => (
                <div key={idx} className="p-3 rounded-xl bg-red-50 border border-red-200 flex flex-col gap-1">
                  <div className="flex items-center justify-between">
                    <span className="flex items-center space-x-1.5 font-bold text-red-900">
                      <XCircle className="w-4 h-4 text-red-600 flex-shrink-0" />
                      <span>{language === 'kn' && rule.description_kn ? rule.description_kn : rule.description}</span>
                    </span>
                    <span className="text-[10px] font-bold uppercase px-2 py-0.5 rounded-full bg-red-200 text-red-900">
                      Not Satisfied
                    </span>
                  </div>
                  <p className="text-red-800 text-xs mt-0.5">
                    {language === 'kn' && rule.reason_kn ? rule.reason_kn : rule.reason}
                  </p>
                  {(rule.why_needed || rule.why_needed_kn) && (
                    <p className="text-[11px] text-red-700 bg-white/70 p-1.5 rounded-md mt-1 border border-red-100">
                      <span className="font-semibold">{t.whyNeeded} </span>
                      {language === 'kn' && rule.why_needed_kn ? rule.why_needed_kn : rule.why_needed}
                    </p>
                  )}
                  {rule.source_reference && (
                    <span className="text-[10px] text-gray-500 font-sans mt-0.5">Ref: {rule.source_reference}</span>
                  )}
                </div>
              ))}

              {/* Unknown Rules */}
              {unknown_rules.map((rule, idx) => (
                <div key={idx} className="p-3 rounded-xl bg-amber-50 border border-amber-200 flex flex-col gap-1">
                  <div className="flex items-center justify-between">
                    <span className="flex items-center space-x-1.5 font-bold text-amber-900">
                      <HelpCircle className="w-4 h-4 text-amber-600 flex-shrink-0" />
                      <span>{language === 'kn' && rule.description_kn ? rule.description_kn : rule.description}</span>
                    </span>
                    <span className="text-[10px] font-bold uppercase px-2 py-0.5 rounded-full bg-amber-200 text-amber-900">
                      Information Needed
                    </span>
                  </div>
                  <p className="text-amber-800 text-xs mt-0.5">
                    {language === 'kn' && rule.clarification_question_kn ? rule.clarification_question_kn : rule.clarification_question || rule.reason}
                  </p>
                  {(rule.why_needed || rule.why_needed_kn) && (
                    <p className="text-[11px] text-amber-700 bg-white/70 p-1.5 rounded-md mt-1 border border-amber-100">
                      <span className="font-semibold">{t.whyNeeded} </span>
                      {language === 'kn' && rule.why_needed_kn ? rule.why_needed_kn : rule.why_needed}
                    </p>
                  )}
                  {rule.source_reference && (
                    <span className="text-[10px] text-gray-500 font-sans mt-0.5">Ref: {rule.source_reference}</span>
                  )}
                </div>
              ))}

              {/* Needs Official Verification */}
              {needs_verification_rules.map((rule, idx) => (
                <div key={idx} className="p-3 rounded-xl bg-purple-50 border border-purple-200 flex flex-col gap-1">
                  <div className="flex items-center justify-between">
                    <span className="flex items-center space-x-1.5 font-bold text-purple-900">
                      <Clock className="w-4 h-4 text-purple-600 flex-shrink-0" />
                      <span>{language === 'kn' && rule.description_kn ? rule.description_kn : rule.description}</span>
                    </span>
                    <span className="text-[10px] font-bold uppercase px-2 py-0.5 rounded-full bg-purple-200 text-purple-900">
                      Official Check
                    </span>
                  </div>
                  <p className="text-purple-800 text-xs mt-0.5">
                    {language === 'kn' && rule.reason_kn ? rule.reason_kn : rule.reason}
                  </p>
                </div>
              ))}
            </div>
          )}

          {/* TAB 3: APPLICATION READINESS CHECKLIST */}
          {activeTab === 'checklist' && (
            <div className="space-y-4">

              {/* Readiness Progress Bar */}
              <div className="p-3.5 bg-emerald-50 rounded-xl border border-emerald-200 flex flex-col gap-2">
                <div className="flex items-center justify-between">
                  <span className="font-bold text-forest-900 text-xs">
                    {language === 'kn' ? 'ಅರ್ಜಿ ಸಿದ್ಧತಾ ಸ್ಥಿತಿ (Readiness Progress):' : 'Application Readiness Score:'}
                  </span>
                  <span className="font-extrabold text-forest-800 text-sm">{readyPct}%</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2.5 overflow-hidden">
                  <div
                    className={`h-2.5 rounded-full transition-all duration-500 ${readyPct >= 80 ? 'bg-forest-600' : readyPct >= 50 ? 'bg-amber-500' : 'bg-red-400'
                      }`}
                    style={{ width: `${readyPct}%` }}
                  />
                </div>
                <div className="flex items-center justify-between text-[11px] text-gray-600">
                  <span>{readyCount} of {totalChecklistItems} items ready</span>
                  <span>{readyPct === 100 ? 'All Documents Ready!' : 'Pending verification'}</span>
                </div>
              </div>

              {/* Checklist Items */}
              {isLoadingChecklist ? (
                <div className="p-6 text-center text-gray-500">Loading checklist items...</div>
              ) : checklist ? (
                <div className="space-y-2.5">
                  {checklist.items.map((item) => {
                    const isChecked = Boolean(checkedItems[item.item_id]);
                    return (
                      <div
                        key={item.item_id}
                        onClick={() => toggleItem(item.item_id)}
                        className={`p-3 rounded-xl border cursor-pointer transition flex items-start justify-between gap-3 ${isChecked
                            ? 'bg-emerald-50/80 border-emerald-300 text-emerald-950'
                            : 'bg-gray-50 border-gray-200 text-ktext-primary hover:bg-gray-100'
                          }`}
                      >
                        <div className="flex items-start space-x-2.5">
                          <FileText className={`w-4 h-4 mt-0.5 flex-shrink-0 ${isChecked ? 'text-forest-700' : 'text-gray-400'}`} />
                          <div>
                            <div className="flex items-center space-x-2">
                              <span className="font-semibold text-xs">
                                {language === 'kn' && item.title_kn ? item.title_kn : item.title}
                              </span>
                              <span className={`text-[10px] px-1.5 py-0.2 rounded font-semibold ${item.is_mandatory ? 'bg-red-100 text-red-800' : 'bg-gray-200 text-gray-700'}`}>
                                {item.is_mandatory ? (language === 'kn' ? 'ಕಡ್ಡಾಯ' : 'Mandatory') : (language === 'kn' ? 'ಐಚ್ಛಿಕ' : 'Optional')}
                              </span>
                            </div>
                            {(item.help_text || item.help_text_kn) && (
                              <p className="text-[11px] text-gray-500 mt-0.5">
                                {language === 'kn' && item.help_text_kn ? item.help_text_kn : item.help_text}
                              </p>
                            )}
                            {item.evidence_found && (
                              <p className="text-[10px] text-emerald-700 font-medium mt-0.5">
                                Verified: {item.evidence_found}
                              </p>
                            )}
                          </div>
                        </div>

                        <div
                          className={`w-5 h-5 rounded-md flex items-center justify-center border flex-shrink-0 mt-0.5 ${isChecked ? 'bg-forest-700 border-forest-700 text-white' : 'border-gray-300 bg-white'
                            }`}
                        >
                          {isChecked && <CheckCircle2 className="w-4 h-4" />}
                        </div>
                      </div>
                    );
                  })}
                </div>
              ) : null}

              {/* Next Steps Guidance */}
              {checklist && checklist.next_steps && (
                <div className="p-3 bg-gray-50 rounded-xl border border-gray-200 text-xs">
                  <h4 className="font-bold text-forest-900 mb-1.5 flex items-center space-x-1">
                    <ListOrdered className="w-3.5 h-3.5 text-forest-700" />
                    <span>{language === 'kn' ? 'ಮುಂದಿನ ಕ್ರಮಗಳು (Next Steps):' : 'Next Application Steps:'}</span>
                  </h4>
                  <ul className="space-y-1 list-disc list-inside text-gray-700">
                    {(language === 'kn' ? checklist.next_steps_kn : checklist.next_steps).map((step, idx) => (
                      <li key={idx}>{step}</li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Disclaimer */}
              <div className="p-3 bg-amber-50 rounded-xl border border-amber-200 text-amber-900 text-xs flex items-start space-x-2">
                <AlertTriangle className="w-4 h-4 text-amber-600 flex-shrink-0 mt-0.5" />
                <p>{checklist ? (language === 'kn' ? checklist.disclaimer_kn : checklist.disclaimer) : t.disclaimerText}</p>
              </div>

            </div>
          )}

        </div>

        {/* Modal Footer */}
        <div className="p-4 border-t border-gray-100 bg-gray-50 flex items-center justify-between text-xs">
          {scheme.official_source_url ? (
            <a
              href={scheme.official_source_url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-forest-700 hover:text-forest-900 font-semibold inline-flex items-center space-x-1"
            >
              <span>{language === 'kn' ? 'ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್ ತೆರೆಯಿರಿ' : 'Open Official Government Portal'}</span>
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          ) : (
            <span className="text-gray-400 italic">
              {language === 'kn' ? 'ಪ್ರಾಯೋಗಿಕ ಪ್ರದರ್ಶನ ಸಿಮ್ಯುಲೇಶನ್' : 'Demonstration Simulation Only'}
            </span>
          )}

          <button
            onClick={onClose}
            className="px-5 py-2 bg-gray-200 hover:bg-gray-300 text-gray-800 rounded-xl font-medium transition"
          >
            {t.close}
          </button>
        </div>

      </div>
    </div>
  );
};
