import React from 'react';
import { CheckCircle2, XCircle, AlertCircle, ShieldAlert, ExternalLink, ArrowRight, Clock, HelpCircle } from 'lucide-react';
import { SchemeMatchResult } from '../../types';
import { translations } from '../../utils/translations';

interface SchemeCardProps {
  matchResult: SchemeMatchResult;
  language: 'kn' | 'en';
  onViewDetails: (scheme: SchemeMatchResult) => void;
}

export const SchemeCard: React.FC<SchemeCardProps> = ({
  matchResult,
  language,
  onViewDetails
}) => {
  const t = translations[language];
  const { scheme, evaluation_status, satisfied_rules, unsatisfied_rules, unknown_rules, needs_verification_rules } = matchResult;

  const isReal = scheme.scheme_type === 'real';

  const getStatusDisplay = () => {
    switch (evaluation_status) {
      case 'POTENTIALLY_SUITABLE':
        return {
          bg: 'bg-emerald-50 border-emerald-300',
          badgeBg: 'bg-emerald-600 text-white',
          label: language === 'kn' ? 'ಪ್ರಾಥಮಿಕವಾಗಿ ಅರ್ಹ (Potentially Suitable)' : 'Potentially Suitable'
        };
      case 'INSUFFICIENT_INFORMATION':
        return {
          bg: 'bg-amber-50/70 border-amber-300',
          badgeBg: 'bg-amber-600 text-white',
          label: language === 'kn' ? 'ಮಾಹಿತಿ ಅಗತ್ಯ (Info Needed)' : 'Info Needed'
        };
      case 'REQUIRES_OFFICIAL_VERIFICATION':
        return {
          bg: 'bg-purple-50 border-purple-300',
          badgeBg: 'bg-purple-700 text-white',
          label: language === 'kn' ? 'ದಾಖಲೆ ಪರಿಶೀಲನೆ ಬಾಕಿ (Verify Offline)' : 'Requires Verification'
        };
      case 'NOT_SUITABLE_BASED_ON_KNOWN_RULES':
        return {
          bg: 'bg-red-50/50 border-red-200',
          badgeBg: 'bg-red-700 text-white',
          label: language === 'kn' ? 'ಅರ್ಹತೆ ಹೊಂದಿಲ್ಲ (Not Suitable)' : 'Not Suitable'
        };
      default:
        return {
          bg: 'bg-gray-50 border-gray-200',
          badgeBg: 'bg-gray-600 text-white',
          label: evaluation_status
        };
    }
  };

  const statusStyle = getStatusDisplay();

  return (
    <div className={`rounded-2xl border ${statusStyle.bg} p-5 shadow-sm hover:shadow-md transition flex flex-col justify-between bg-white`}>

      <div>
        {/* Real vs Synthetic Demo Banner */}
        <div className="flex items-center justify-between mb-2.5">
          <span
            className={`text-[10px] font-bold tracking-wider px-2.5 py-0.5 rounded-full uppercase border ${isReal
                ? 'bg-emerald-100 text-emerald-800 border-emerald-300'
                : 'bg-amber-100 text-amber-900 border-amber-300'
              }`}
          >
            {isReal ? t.realSchemeBadge : t.demoSchemeBadge}
          </span>
          <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-full ${statusStyle.badgeBg}`}>
            {statusStyle.label}
          </span>
        </div>

        {/* Scheme Name */}
        <h3 className="text-base font-bold text-forest-950 font-kannada leading-snug">
          {language === 'kn' && scheme.name_kn ? scheme.name_kn : scheme.name}
        </h3>
        {scheme.name_kn && language !== 'kn' && (
          <p className="text-xs text-gray-500 font-kannada mt-0.5">
            {scheme.name_kn}
          </p>
        )}

        {/* Category & Authority */}
        <div className="flex flex-wrap items-center gap-1.5 mt-1.5 text-xs text-ktext-muted">
          <span className="bg-gray-100 px-2 py-0.5 rounded text-gray-700 font-medium capitalize">
            {language === 'kn' && scheme.category_kn ? scheme.category_kn : scheme.category.replace('_', ' ')}
          </span>
          {scheme.last_verified_at && (
            <span className="text-[11px] text-gray-400">
              Verified: {scheme.last_verified_at}
            </span>
          )}
        </div>

        {/* Match Reason explanation */}
        <div className="my-3 p-2.5 rounded-xl bg-gray-50 text-xs font-kannada text-ktext-primary border border-gray-100">
          <p className="font-semibold text-forest-900 mb-0.5">
            {language === 'kn' ? 'ಹೊಂದಾಣಿಕೆ ವಿವರ:' : 'Match Reason:'}
          </p>
          <p>{language === 'kn' && matchResult.match_reason_kn ? matchResult.match_reason_kn : matchResult.match_reason}</p>
        </div>

        {/* Transparent Rule Evaluation Breakdown */}
        <div className="space-y-1.5 my-3 text-xs">
          {/* Satisfied Rules */}
          {satisfied_rules.slice(0, 3).map((r, i) => (
            <div key={i} className="flex items-start space-x-1.5 text-emerald-800 font-kannada">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 flex-shrink-0 mt-0.5" />
              <span>{language === 'kn' && r.description_kn ? r.description_kn : r.description}</span>
            </div>
          ))}

          {/* Unsatisfied Rules */}
          {unsatisfied_rules.map((r, i) => (
            <div key={i} className="flex items-start space-x-1.5 text-red-700 font-kannada">
              <XCircle className="w-3.5 h-3.5 text-red-500 flex-shrink-0 mt-0.5" />
              <span>{language === 'kn' && r.description_kn ? r.description_kn : r.description}</span>
            </div>
          ))}

          {/* Unknown Rules */}
          {unknown_rules.slice(0, 2).map((r, i) => (
            <div key={i} className="flex items-start space-x-1.5 text-amber-700 font-kannada">
              <AlertCircle className="w-3.5 h-3.5 text-amber-500 flex-shrink-0 mt-0.5" />
              <span>{language === 'kn' && r.clarification_question_kn ? r.clarification_question_kn : r.description}</span>
            </div>
          ))}

          {/* Needs Verification */}
          {needs_verification_rules.map((r, i) => (
            <div key={i} className="flex items-start space-x-1.5 text-purple-700 font-kannada">
              <Clock className="w-3.5 h-3.5 text-purple-500 flex-shrink-0 mt-0.5" />
              <span>{language === 'kn' && r.description_kn ? r.description_kn : r.description}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Card Footer: Portal Link & View Details */}
      <div className="pt-3 border-t border-gray-100 flex items-center justify-between">
        {scheme.official_source_url ? (
          <a
            href={scheme.official_source_url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-xs text-[#183B2B] hover:text-[#23503B] inline-flex items-center space-x-1 font-semibold"
          >
            <span>{t.officialSource}</span>
            <ExternalLink className="w-3.5 h-3.5 stroke-[2]" />
          </a>
        ) : (
          <span className="text-[11px] text-gray-400 italic">
            {language === 'kn' ? 'ಪ್ರಾಯೋಗಿಕ ಯೋಜನೆ' : 'Synthetic Scheme'}
          </span>
        )}

        <button
          onClick={() => onViewDetails(matchResult)}
          className="text-xs font-bold bg-[#183B2B] hover:bg-[#23503B] text-white px-3.5 py-1.5 rounded-xl flex items-center space-x-1.5 transition shadow-sm"
        >
          <span>{t.viewDetails}</span>
          <ArrowRight className="w-3.5 h-3.5 stroke-[2.2]" />
        </button>
      </div>

    </div>
  );
};
