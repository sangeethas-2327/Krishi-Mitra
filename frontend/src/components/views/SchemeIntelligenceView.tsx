import React, { useState } from 'react';
import { 
  BookOpenCheck, 
  CheckCircle2, 
  XCircle, 
  AlertCircle, 
  Clock, 
  ExternalLink, 
  ArrowRight, 
  Scale, 
  Filter, 
  Search, 
  ChevronRight, 
  ShieldCheck, 
  FileText,
  FileCheck,
  Building2,
  Calendar
} from 'lucide-react';
import { translations } from '../../utils/translations';
import { SchemeMatchResult, SchemeRecord } from '../../types';
import { SchemeModal } from '../schemes/SchemeModal';
import { SchemeComparisonModal } from '../schemes/SchemeComparisonModal';

interface SchemeIntelligenceViewProps {
  recommendations: SchemeMatchResult[];
  language: 'kn' | 'en';
  onPlayAudio: (text: string) => void;
  onStopAudio: () => void;
  isPlayingAudio: boolean;
  sessionId: string;
  onNavigateToJourney: (scheme: SchemeMatchResult) => void;
}

export const SchemeIntelligenceView: React.FC<SchemeIntelligenceViewProps> = ({
  recommendations,
  language,
  onPlayAudio,
  onStopAudio,
  isPlayingAudio,
  sessionId,
  onNavigateToJourney
}) => {
  const t = translations[language];
  const [selectedScheme, setSelectedScheme] = useState<SchemeMatchResult | null>(null);
  const [isCompareOpen, setIsCompareOpen] = useState(false);
  const [activeCategory, setActiveCategory] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');

  // Categories list
  const categories = [
    { id: 'all', label: language === 'kn' ? 'ಎಲ್ಲಾ ಯೋಜನೆಗಳು' : 'All Schemes' },
    { id: 'income_support', label: language === 'kn' ? 'ಆದಾಯ ನೆರವು (Income)' : 'Income Support' },
    { id: 'crop_insurance', label: language === 'kn' ? 'ಬೆಳೆ ವಿಮೆ (Insurance)' : 'Crop Insurance' },
    { id: 'micro_irrigation', label: language === 'kn' ? 'ಹನಿ ನೀರಾವರಿ (Drip)' : 'Irrigation' },
    { id: 'horticulture', label: language === 'kn' ? 'ತೋಟಗಾರಿಕೆ (Horticulture)' : 'Horticulture' },
    { id: 'seeds_inputs', label: language === 'kn' ? 'ಬೀಜ ಸಬ್ಸಿಡಿ (Seeds)' : 'Seeds & Inputs' }
  ];

  // Filtering
  const filtered = recommendations.filter((item) => {
    const matchCat = activeCategory === 'all' || item.scheme.category === activeCategory;
    const nameMatch = item.scheme.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                      (item.scheme.name_kn && item.scheme.name_kn.includes(searchQuery));
    return matchCat && nameMatch;
  });

  const getStatusDisplay = (status: string) => {
    switch (status) {
      case 'POTENTIALLY_SUITABLE':
        return {
          label: language === 'kn' ? 'ಪ್ರಾಥಮಿಕವಾಗಿ ಅರ್ಹ (Suitable)' : 'Potentially Suitable',
          badge: 'bg-emerald-50 text-emerald-800 border-emerald-300',
          dot: 'bg-emerald-500'
        };
      case 'INSUFFICIENT_INFORMATION':
        return {
          label: language === 'kn' ? 'ಮಾಹಿತಿ ಅಪೂರ್ಣ (Info Needed)' : 'Info Needed',
          badge: 'bg-harvest/15 text-harvest-dark border-harvest/40',
          dot: 'bg-harvest'
        };
      case 'REQUIRES_OFFICIAL_VERIFICATION':
        return {
          label: language === 'kn' ? 'ದಾಖಲೆ ಪರಿಶೀಲನೆ ಅಗತ್ಯ (Verify)' : 'Requires Verification',
          badge: 'bg-purple-50 text-purple-800 border-purple-200',
          dot: 'bg-purple-500'
        };
      case 'NOT_SUITABLE_BASED_ON_KNOWN_RULES':
        return {
          label: language === 'kn' ? 'ಅರ್ಹತೆ ಹೊಂದಿಲ್ಲ (Not Suitable)' : 'Not Suitable',
          badge: 'bg-terracotta/10 text-terracotta border-terracotta/30',
          dot: 'bg-terracotta'
        };
      default:
        return {
          label: status,
          badge: 'bg-ivory text-charcoal border-ivory-border',
          dot: 'bg-charcoal'
        };
    }
  };

  return (
    <div className="max-w-6xl mx-auto space-y-8 pb-20 animate-fadeIn">
      
      {/* 1. Header & Compare Trigger */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 p-8 rounded-[2rem] bg-white border border-ivory-border shadow-editorial">
        <div className="space-y-1.5">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-forest text-ivory text-xs font-mono tracking-wider uppercase">
            <BookOpenCheck className="w-3.5 h-3.5 text-harvest" />
            <span>Editorial Scheme Intelligence</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold font-kannada text-charcoal">
            {language === 'kn' ? 'ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಸಮಗ್ರ ಪರಿಶೀಲನಾ ಕೋಷ್ಟಕ' : 'Statutory Government Scheme Dossiers'}
          </h2>
          <p className="text-xs sm:text-sm text-charcoal-muted font-kannada">
            {language === 'kn'
              ? 'ಪ್ರತಿಯೊಂದು ಯೋಜನೆಯ ಮಾನದಂಡಗಳನ್ನು ರೈತರ ಜಮೀನು ಮತ್ತು ಬೆಳೆ ವಿವರಗಳೊಂದಿಗೆ ಪರಿಶೀಲಿಸಿದ ಪಾರದರ್ಶಕ ವರದಿ.'
              : 'Audit dossiers evaluated against verified farmer profile facts with complete statutory transparency.'}
          </p>
        </div>

        <button
          onClick={() => setIsCompareOpen(true)}
          className="flex items-center space-x-2.5 px-6 py-3.5 rounded-xl bg-forest hover:bg-forest-700 text-ivory font-bold text-xs font-kannada transition-all shadow-sm hover:border-harvest active:scale-95"
        >
          <Scale className="w-4 h-4 text-harvest" />
          <span>{t.compareSchemes}</span>
        </button>
      </div>

      {/* 2. Filter & Search Toolbar */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 p-4 rounded-2xl bg-white border border-ivory-border shadow-sm">
        
        {/* Category Filter Pills */}
        <div className="flex items-center space-x-2 overflow-x-auto w-full sm:w-auto pb-2 sm:pb-0">
          <Filter className="w-4 h-4 text-charcoal-muted flex-shrink-0 ml-1" />
          {categories.map((cat) => (
            <button
              key={cat.id}
              onClick={() => setActiveCategory(cat.id)}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-kannada whitespace-nowrap transition-all ${
                activeCategory === cat.id
                  ? 'bg-forest text-ivory font-bold shadow-sm'
                  : 'bg-ivory text-charcoal hover:bg-ivory-dark border border-ivory-border'
              }`}
            >
              {cat.label}
            </button>
          ))}
        </div>

        {/* Search input */}
        <div className="relative w-full sm:w-64">
          <Search className="w-4 h-4 text-charcoal-muted absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder={language === 'kn' ? 'ಯೋಜನೆ ಹುಡುಕಿ...' : 'Search scheme name...'}
            className="w-full bg-ivory text-charcoal text-xs font-kannada pl-9 pr-3 py-2 rounded-xl border border-ivory-border focus:outline-none focus:border-forest"
          />
        </div>

      </div>

      {/* 3. Scheme Dossiers Layout */}
      <div className="space-y-6">
        {filtered.length === 0 ? (
          <div className="p-12 rounded-[2rem] bg-white text-center border border-dashed border-ivory-border space-y-3">
            <BookOpenCheck className="w-10 h-10 text-charcoal-muted mx-auto" />
            <p className="text-sm font-kannada text-charcoal">
              {language === 'kn' ? 'ಈ ವಿಭಾಗದಲ್ಲಿ ಯಾವುದೇ ಯೋಜನೆಗಳು ಹೊಂದಿಕೆಯಾಗಿಲ್ಲ.' : 'No schemes match the selected category filter.'}
            </p>
          </div>
        ) : (
          filtered.map((match) => {
            const { scheme, evaluation_status, satisfied_rules, unsatisfied_rules, unknown_rules, needs_verification_rules } = match;
            const isReal = scheme.scheme_type === 'real';
            const statusMeta = getStatusDisplay(evaluation_status);

            return (
              <div
                key={scheme.id}
                className="rounded-[2rem] bg-white border border-ivory-border p-6 sm:p-8 shadow-editorial hover:shadow-editorial-hover transition-all space-y-6"
              >
                {/* Dossier Header */}
                <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-4 pb-5 border-b border-ivory-border">
                  <div className="space-y-2">
                    <div className="flex flex-wrap items-center gap-2">
                      <span className={`text-[10px] font-mono px-2.5 py-0.5 rounded-full uppercase border font-bold ${
                        isReal 
                          ? 'bg-emerald-50 text-emerald-800 border-emerald-200' 
                          : 'bg-harvest/15 text-harvest-dark border-harvest/30'
                      }`}>
                        {isReal ? t.realSchemeBadge : t.demoSchemeBadge}
                      </span>
                      <span className="text-[11px] font-mono text-charcoal-muted uppercase bg-ivory px-2 py-0.5 rounded-full border border-ivory-border">
                        {scheme.category.replace('_', ' ')}
                      </span>
                      {scheme.last_verified_at && (
                        <span className="text-[11px] font-mono text-charcoal-muted flex items-center space-x-1">
                          <Calendar className="w-3.5 h-3.5 stroke-[2]" />
                          <span>Verified: {scheme.last_verified_at}</span>
                        </span>
                      )}
                    </div>

                    <h3 className="text-xl sm:text-2xl font-bold font-kannada text-charcoal">
                      {language === 'kn' && scheme.name_kn ? scheme.name_kn : scheme.name}
                    </h3>
                    
                    {scheme.name_kn && language !== 'kn' && (
                      <p className="text-xs font-kannada text-charcoal-muted">{scheme.name_kn}</p>
                    )}

                    {scheme.issuing_authority && (
                      <p className="text-xs text-charcoal-muted flex items-center space-x-1.5 font-sans">
                        <Building2 className="w-3.5 h-3.5 text-forest" />
                        <span>{scheme.issuing_authority}</span>
                      </p>
                    )}
                  </div>

                  {/* Eligibility Status Badge */}
                  <div className="flex flex-col sm:items-end space-y-1">
                    <span className={`inline-flex items-center space-x-1.5 text-xs font-bold font-mono px-3 py-1.5 rounded-full border ${statusMeta.badge}`}>
                      <span className={`w-2 h-2 rounded-full ${statusMeta.dot}`} />
                      <span>{statusMeta.label}</span>
                    </span>
                  </div>
                </div>

                {/* Match Reason Banner */}
                <div className="p-4 rounded-xl bg-ivory border border-ivory-border text-xs font-kannada text-charcoal">
                  <span className="font-bold text-forest mr-2">
                    {language === 'kn' ? 'ಹೊಂದಾಣಿಕೆ ವಿವರಣೆ:' : 'Match Reason:'}
                  </span>
                  <span>{language === 'kn' && match.match_reason_kn ? match.match_reason_kn : match.match_reason}</span>
                </div>

                {/* 4-State Rule Evaluation Breakdown */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs font-kannada">
                  
                  {/* Satisfied Rules */}
                  <div className="p-3.5 rounded-xl bg-emerald-50/60 border border-emerald-100 space-y-1.5">
                    <div className="flex items-center space-x-1.5 text-emerald-800 font-bold">
                      <CheckCircle2 className="w-4 h-4 text-emerald-600 flex-shrink-0" />
                      <span>{language === 'kn' ? `ಪೂರೈಸಿದ ಷರತ್ತುಗಳು (${satisfied_rules.length})` : `Satisfied (${satisfied_rules.length})`}</span>
                    </div>
                    {satisfied_rules.slice(0, 2).map((r, i) => (
                      <p key={i} className="text-[11px] text-emerald-900 leading-snug">
                        • {language === 'kn' && r.description_kn ? r.description_kn : r.description}
                      </p>
                    ))}
                  </div>

                  {/* Unsatisfied Rules */}
                  <div className="p-3.5 rounded-xl bg-terracotta/10 border border-terracotta/20 space-y-1.5">
                    <div className="flex items-center space-x-1.5 text-terracotta font-bold">
                      <XCircle className="w-4 h-4 text-terracotta flex-shrink-0" />
                      <span>{language === 'kn' ? `ಹೊಂದಿಕೆಯಾಗದ ಷರತ್ತುಗಳು (${unsatisfied_rules.length})` : `Unsatisfied (${unsatisfied_rules.length})`}</span>
                    </div>
                    {unsatisfied_rules.length === 0 ? (
                      <p className="text-[11px] text-charcoal-muted italic">ಯಾವುದೂ ಇಲ್ಲ / None</p>
                    ) : (
                      unsatisfied_rules.map((r, i) => (
                        <p key={i} className="text-[11px] text-terracotta-dark leading-snug">
                          • {language === 'kn' && r.description_kn ? r.description_kn : r.description}
                        </p>
                      ))
                    )}
                  </div>

                  {/* Unknown / Info Needed */}
                  <div className="p-3.5 rounded-xl bg-harvest/15 border border-harvest/30 space-y-1.5">
                    <div className="flex items-center space-x-1.5 text-harvest-dark font-bold">
                      <AlertCircle className="w-4 h-4 text-harvest-dark flex-shrink-0" />
                      <span>{language === 'kn' ? `ಮಾಹಿತಿ ಅಗತ್ಯ (${unknown_rules.length})` : `Missing Info (${unknown_rules.length})`}</span>
                    </div>
                    {unknown_rules.slice(0, 2).map((r, i) => (
                      <p key={i} className="text-[11px] text-charcoal-dark leading-snug">
                        • {language === 'kn' && r.clarification_question_kn ? r.clarification_question_kn : r.description}
                      </p>
                    ))}
                  </div>

                  {/* Offline Verification */}
                  <div className="p-3.5 rounded-xl bg-purple-50/70 border border-purple-100 space-y-1.5">
                    <div className="flex items-center space-x-1.5 text-purple-900 font-bold">
                      <Clock className="w-4 h-4 text-purple-700 flex-shrink-0" />
                      <span>{language === 'kn' ? `ದಾಖಲೆ ಪರಿಶೀಲನೆ (${needs_verification_rules.length})` : `Verify Offline (${needs_verification_rules.length})`}</span>
                    </div>
                    {needs_verification_rules.slice(0, 2).map((r, i) => (
                      <p key={i} className="text-[11px] text-purple-950 leading-snug">
                        • {language === 'kn' && r.description_kn ? r.description_kn : r.description}
                      </p>
                    ))}
                  </div>

                </div>

                {/* Dossier Footer & Action Links */}
                <div className="pt-4 border-t border-ivory-border flex flex-col sm:flex-row items-center justify-between gap-3">
                  <div className="flex items-center space-x-4">
                    {scheme.official_source_url ? (
                      <a
                        href={scheme.official_source_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-xs text-forest hover:text-harvest inline-flex items-center space-x-1.5 font-bold font-mono"
                      >
                        <span>{t.officialSource}</span>
                        <ExternalLink className="w-3.5 h-3.5" />
                      </a>
                    ) : (
                      <span className="text-[11px] text-charcoal-muted italic">
                        {language === 'kn' ? 'ಪ್ರಾಯೋಗಿಕ ಪ್ರದರ್ಶನ ಯೋಜನೆ' : 'Synthetic Reference Scheme'}
                      </span>
                    )}

                    <button
                      onClick={() => onNavigateToJourney(match)}
                      className="text-xs text-forest hover:text-harvest inline-flex items-center space-x-1 font-semibold font-kannada"
                    >
                      <FileCheck className="w-3.5 h-3.5 text-harvest" />
                      <span>{language === 'kn' ? 'ದಾಖಲೆ ಸಿದ್ಧತೆ (Checklist)' : 'Prepare Documents'}</span>
                    </button>
                  </div>

                  <button
                    onClick={() => setSelectedScheme(match)}
                    className="flex items-center space-x-2 px-5 py-2.5 rounded-xl bg-forest hover:bg-forest-700 text-ivory text-xs font-bold font-kannada transition-all shadow-sm"
                  >
                    <span>{t.viewDetails}</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>

              </div>
            );
          })
        )}
      </div>

      {/* Scheme Details Modal */}
      <SchemeModal
        matchResult={selectedScheme}
        language={language}
        isOpen={Boolean(selectedScheme)}
        onClose={() => setSelectedScheme(null)}
        onPlayAudio={onPlayAudio}
        onStopAudio={onStopAudio}
        isPlayingAudio={isPlayingAudio}
        sessionId={sessionId}
      />

      {/* Side-by-Side Scheme Comparison Matrix Modal */}
      <SchemeComparisonModal
        language={language}
        isOpen={isCompareOpen}
        onClose={() => setIsCompareOpen(false)}
        availableSchemes={recommendations.map(r => r.scheme)}
        matchResults={recommendations}
      />

    </div>
  );
};

