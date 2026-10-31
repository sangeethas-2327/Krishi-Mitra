import React, { useState } from 'react';
import { Sparkles, Mic, FileText, CheckCircle2, ChevronDown, ChevronUp, HelpCircle } from 'lucide-react';
import { translations } from '../../utils/translations';

interface QuickStartGuideProps {
  language: 'kn' | 'en';
  onSelectPrompt: (promptText: string) => void;
  disabled?: boolean;
}

export const QuickStartGuide: React.FC<QuickStartGuideProps> = ({
  language,
  onSelectPrompt,
  disabled
}) => {
  const [isOpen, setIsOpen] = useState(true);
  const t = translations[language];

  const quickPrompts = [
    {
      kn: 'ನನಗೆ 3 ಎಕರೆ ಅಡಿಕೆ ಜಮೀನಿದೆ, ಸಹಾಯಧನ ಬೇಕು',
      en: 'I have 3 acres of arecanut land, I need financial assistance',
      category: language === 'kn' ? 'ತೋಟಗಾರಿಕೆ / ತೋಟ' : 'Horticulture'
    },
    {
      kn: 'ನಾನು ಮಂಡ್ಯದಲ್ಲಿ ಕಬ್ಬು ಬೆಳೆಯುತ್ತೇನೆ, 4 ಎಕರೆಗೆ ಹನಿ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿದೆಯೇ?',
      en: 'I grow sugarcane in Mandya, is drip irrigation subsidy available for 4 acres?',
      category: language === 'kn' ? 'ನೀರಾವರಿ ನೆರವು' : 'Irrigation'
    },
    {
      kn: 'ನಾನು ಗೇಣಿ ರೈತ, ನನಗೆ ಬೆಳೆ ವಿಮೆ ಸಿಗುತ್ತದೆಯೇ?',
      en: 'I am a tenant farmer, am I eligible for crop insurance (PMFBY)?',
      category: language === 'kn' ? 'ಗೇಣಿ ರೈತರು / ವಿಮೆ' : 'Tenant / Insurance'
    }
  ];

  return (
    <div className="bg-gradient-to-r from-forest-800 to-forest-900 rounded-2xl shadow-sm text-white mb-6 border border-forest-700/60 overflow-hidden transition-all">
      {/* Header bar with toggle */}
      <div
        onClick={() => setIsOpen(!isOpen)}
        className="px-5 py-3.5 flex items-center justify-between cursor-pointer hover:bg-forest-800/40 select-none"
      >
        <div className="flex items-center space-x-2.5">
          <div className="w-8 h-8 rounded-lg bg-forest-700/80 flex items-center justify-center border border-forest-600">
            <Sparkles className="w-4 h-4 text-emerald-300" />
          </div>
          <div>
            <h2 className="text-sm font-bold font-kannada flex items-center space-x-2 text-white">
              <span>{language === 'kn' ? 'ಕೃಷಿ ಮಿತ್ರ ಹೇಗೆ ಬಳಸಬೇಕು? (ತ್ವರಿತ ಮಾರ್ಗದರ್ಶಿ)' : 'How Krishi Mitra Works (Quick Guide)'}</span>
              <span className="text-[10px] bg-emerald-700/70 text-emerald-100 px-2 py-0.5 rounded-full font-sans uppercase tracking-wider font-semibold">
                Voice-First AI
              </span>
            </h2>
            <p className="text-xs text-emerald-200/90 font-kannada">
              {language === 'kn'
                ? 'ಕನ್ನಡ ಧ್ವನಿ ಸಂಭಾಷಣೆ ಮತ್ತು ಅಧಿಕೃತ ಅರ್ಹತಾ ಪರಿಶೀಲನೆ'
                : 'Kannada conversational AI paired with verified government scheme eligibility assessment'}
            </p>
          </div>
        </div>

        <button
          className="text-emerald-300 hover:text-white p-1 rounded-lg transition"
          aria-label={isOpen ? 'Collapse Guide' : 'Expand Guide'}
        >
          {isOpen ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
        </button>
      </div>

      {/* Expandable 3-step walk-through and sample prompts */}
      {isOpen && (
        <div className="px-5 pb-5 pt-1 border-t border-forest-700/50">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3 my-3">
            {/* Step 1 */}
            <div className="bg-forest-950/40 rounded-xl p-3 border border-forest-700/40 flex items-start space-x-2.5">
              <div className="w-7 h-7 rounded-full bg-emerald-600/30 text-emerald-300 flex items-center justify-center font-bold text-xs flex-shrink-0">
                1
              </div>
              <div>
                <p className="text-xs font-bold text-emerald-200 font-kannada flex items-center space-x-1">
                  <Mic className="w-3.5 h-3.5 text-emerald-400" />
                  <span>{language === 'kn' ? 'ಧ್ವನಿ ಮೂಲಕ ಮಾತನಾಡಿ' : 'Speak Naturally'}</span>
                </p>
                <p className="text-[11px] text-gray-300 font-kannada mt-0.5">
                  {language === 'kn'
                    ? 'ಮೈಕ್ರೋಫೋನ್ ಒತ್ತಿ ನಿಮ್ಮ ಜಮೀನು, ಬೆಳೆ ಮತ್ತು ಅಗತ್ಯಗಳ ಬಗ್ಗೆ ಕನ್ನಡದಲ್ಲಿ ಮಾತನಾಡಿ.'
                    : 'Tap the microphone to speak your land size, crops, and district in Kannada.'}
                </p>
              </div>
            </div>

            {/* Step 2 */}
            <div className="bg-forest-950/40 rounded-xl p-3 border border-forest-700/40 flex items-start space-x-2.5">
              <div className="w-7 h-7 rounded-full bg-emerald-600/30 text-emerald-300 flex items-center justify-center font-bold text-xs flex-shrink-0">
                2
              </div>
              <div>
                <p className="text-xs font-bold text-emerald-200 font-kannada flex items-center space-x-1">
                  <FileText className="w-3.5 h-3.5 text-emerald-400" />
                  <span>{language === 'kn' ? 'ಸ್ವಯಂ ಪ್ರೊಫೈಲ್ ರಚನೆ' : 'Automatic Profile'}</span>
                </p>
                <p className="text-[11px] text-gray-300 font-kannada mt-0.5">
                  {language === 'kn'
                    ? 'AI ನಿಮ್ಮ ವಿವರಗಳನ್ನು ಪಾರದರ್ಶಕವಾಗಿ ಗುರುತಿಸುತ್ತದೆ (ತಪ್ಪಿದ್ದರೆ ತಿದ್ದಲು ಅವಕಾಶವಿದೆ).'
                    : 'AI extracts structured parameters transparently with full edit provenance.'}
                </p>
              </div>
            </div>

            {/* Step 3 */}
            <div className="bg-forest-950/40 rounded-xl p-3 border border-forest-700/40 flex items-start space-x-2.5">
              <div className="w-7 h-7 rounded-full bg-emerald-600/30 text-emerald-300 flex items-center justify-center font-bold text-xs flex-shrink-0">
                3
              </div>
              <div>
                <p className="text-xs font-bold text-emerald-200 font-kannada flex items-center space-x-1">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                  <span>{language === 'kn' ? 'ಖಚಿತ ಅರ್ಹತಾ ಪರಿಶೀಲನೆ' : 'Scheme Eligibility Check'}</span>
                </p>
                <p className="text-[11px] text-gray-300 font-kannada mt-0.5">
                  {language === 'kn'
                    ? 'ಯಾವ ಯೋಜನೆಗಳಿಗೆ ನೀವು ಅರ್ಹರು ಎಂದು ನಿಖರ ನಿಯಮಗಳೊಂದಿಗೆ ಪರಿಶೀಲಿಸಿ.'
                    : 'Matches official schemes with exact rule breakdowns and application checklists.'}
                </p>
              </div>
            </div>
          </div>

          {/* Quick-start sample prompts */}
          <div className="mt-3 pt-3 border-t border-forest-800/80">
            <span className="text-[11px] text-emerald-300/80 font-medium font-kannada mr-2 block sm:inline mb-1.5 sm:mb-0">
              {language === 'kn' ? 'ಪರೀಕ್ಷಿಸಲು ತ್ವರಿತ ಪ್ರಶ್ನೆಗಳನ್ನು ಆರಿಸಿ:' : 'Try clicking a sample farmer prompt:'}
            </span>
            <div className="flex flex-wrap gap-2">
              {quickPrompts.map((p, idx) => (
                <button
                  key={idx}
                  onClick={() => onSelectPrompt(language === 'kn' ? p.kn : p.en)}
                  disabled={disabled}
                  className="bg-forest-950/60 hover:bg-forest-800 border border-emerald-600/40 hover:border-emerald-400 text-xs px-3 py-1.5 rounded-xl text-left text-emerald-100 transition shadow-sm font-kannada disabled:opacity-50"
                >
                  <span className="font-semibold text-emerald-300 mr-1.5 text-[10px] bg-forest-900 px-1.5 py-0.5 rounded">
                    {p.category}
                  </span>
                  <span>{language === 'kn' ? p.kn : p.en}</span>
                </button>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

