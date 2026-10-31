import React, { useState } from 'react';
import {
  Mic,
  BookOpenCheck,
  Sparkles,
  ShieldCheck,
  Scale,
  FileText,
  ArrowUpRight,
  Wheat,
  Layers,
  Info,
  Radio,
  PhoneCall
} from 'lucide-react';
import { translations } from '../../utils/translations';
import { NavTab } from '../layout/Navbar';
import { FarmerProfile } from '../../types';
import { LiveFarmWeatherCard } from '../weather/LiveFarmWeatherCard';
import { SarvamLiveVoiceModal } from '../voice/SarvamLiveVoiceModal';

interface DiscoverViewProps {
  language: 'kn' | 'en';
  onNavigate: (tab: NavTab) => void;
  onQuickPrompt: (promptText: string) => void;
  isDemoMode: boolean;
  suitableSchemesCount: number;
  profile: FarmerProfile;
}

export const DiscoverView: React.FC<DiscoverViewProps> = ({
  language,
  onNavigate,
  onQuickPrompt,
  suitableSchemesCount,
  profile
}) => {
  const t = translations[language];
  const [isLiveVoiceOpen, setIsLiveVoiceOpen] = useState(false);

  const quickSamples = [
    {
      kn: "ನನಗೆ 3 ಎಕರೆ ಅಡಿಕೆ ಜಮೀನಿದೆ, ಸಹಾಯಧನ ಬೇಕು",
      en: "I have 3 acres of arecanut, I need subsidy",
      tag: language === 'kn' ? 'ತೋಟಗಾರಿಕೆ' : 'Horticulture'
    },
    {
      kn: "ನಾನು ಗೇಣಿ ರೈತ, ಬೆಳೆ ವಿಮೆ ಯೋಜನೆ ಸಿಗುತ್ತದೆಯೇ?",
      en: "I am a tenant farmer, can I get crop insurance?",
      tag: language === 'kn' ? 'ವಿಮೆ / ಗೇಣಿ' : 'Insurance'
    },
    {
      kn: "ಮಂಡ್ಯದಲ್ಲಿ 4 ಎಕರೆ ಕಬ್ಬಿಗೆ ಹನಿ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿದೆಯೇ?",
      en: "Is drip irrigation available for 4 acres sugarcane in Mandya?",
      tag: language === 'kn' ? 'ನೀರಾವರಿ' : 'Irrigation'
    }
  ];

  return (
    <div className="space-y-12 pb-16 animate-fadeIn">

      {/* 1. Editorial Hero Section — High Contrast & Organic Agritech Layout */}
      <section className="relative overflow-hidden rounded-[2.5rem] bg-[#FAF7F0] p-8 sm:p-12 lg:p-14 border border-[#E2D9C8] shadow-md">

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">

          {/* Left Column: Bold Editorial Headline, Tagline & Actions */}
          <div className="lg:col-span-7 space-y-6">

            {/* Editorial Eyebrow Badge */}
            <div className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-white border border-[#E2D9C8] text-xs text-[#183B2B] font-mono tracking-wider uppercase shadow-sm">
              <Sparkles className="w-3.5 h-3.5 text-[#B08233] stroke-[2]" />
              <span className="font-bold">{t.livingCompanion}</span>
            </div>

            {/* Main High-Contrast Headline & Integrated Tagline */}
            <div className="space-y-3">
              <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold font-kannada tracking-tight leading-[1.25] text-[#183B2B]">
                {language === 'kn'
                  ? 'ನಿಮ್ಮ ಕೃಷಿಗೆ, ನಿಮ್ಮ ಧ್ವನಿಯಲ್ಲಿ ಸಹಾಯ'
                  : 'Support for your farming, in your own voice.'}
              </h1>

              {/* Tagline: Clear Visual Relationship with the Main Headline */}
              <div className="flex items-center space-x-2.5 pt-0.5">
                <span className="w-6 h-0.5 bg-[#D7A85B] rounded-full inline-block flex-shrink-0" />
                <p className="text-base sm:text-lg font-bold text-[#B08233] font-sans tracking-wide">
                  Your farm. Your voice. Your opportunities.
                </p>
              </div>
            </div>

            {/* Clear Subtitle */}
            <p className="text-base sm:text-lg text-[#4A5148] font-kannada max-w-xl leading-relaxed">
              {language === 'kn'
                ? 'ನೈಸರ್ಗಿಕವಾಗಿ ಮಾತನಾಡಿ. ಸೂಕ್ತ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳನ್ನು ಕಂಡುಕೊಳ್ಳಿ. ಅರ್ಹತೆಯ ನಿಯಮಗಳನ್ನು ಪಾರದರ್ಶಕವಾಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ.'
                : 'Talk naturally in Kannada. Discover relevant government schemes. Understand statutory eligibility rules with total clarity.'}
            </p>

            {/* Primary Action Buttons */}
            <div className="flex flex-wrap gap-4 pt-2">
              <button
                onClick={() => setIsLiveVoiceOpen(true)}
                className="group flex items-center space-x-3 px-7 py-4 rounded-2xl bg-[#183B2B] hover:bg-[#23503B] text-white font-extrabold text-sm sm:text-base transition-all shadow-md active:scale-95 border border-[#D7A85B]/40"
              >
                <div className="w-8 h-8 rounded-full bg-[#D7A85B] flex items-center justify-center group-hover:scale-110 transition-transform">
                  <Radio className="w-4 h-4 text-[#183B2B] stroke-[2.2] animate-pulse" />
                </div>
                <span className="font-kannada">
                  {language === 'kn' ? 'ಕೃಷಿ ಮಿತ್ರನೊಂದಿಗೆ ಮಾತನಾಡಿ (Live Voice)' : 'Talk to Krishi Mitra (Live Voice)'}
                </span>
                <PhoneCall className="w-4 h-4 text-[#D7A85B]" />
              </button>

              <button
                onClick={() => onNavigate('voice')}
                className="group flex items-center space-x-3 px-7 py-4 rounded-2xl bg-[#D7A85B] hover:bg-[#B08233] text-[#183B2B] font-extrabold text-sm sm:text-base transition-all shadow-md active:scale-95"
              >
                <div className="w-8 h-8 rounded-full bg-[#183B2B] flex items-center justify-center group-hover:scale-110 transition-transform">
                  <Mic className="w-4 h-4 text-[#D7A85B] stroke-[2.2]" />
                </div>
                <span className="font-kannada">{t.startConversation}</span>
                <ArrowUpRight className="w-4 h-4 text-[#183B2B] stroke-[2.2] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
              </button>

              <button
                onClick={() => onNavigate('schemes')}
                className="flex items-center space-x-2.5 px-7 py-4 rounded-2xl bg-white hover:bg-[#FAF7F0] text-[#183B2B] border-2 border-[#183B2B] font-bold text-sm sm:text-base transition-all shadow-sm active:scale-95"
              >
                <BookOpenCheck className="w-4 h-4 text-[#183B2B] stroke-[2.2]" />
                <span className="font-kannada">{t.exploreSchemes}</span>
              </button>
            </div>

            {/* Sample Voice Prompts Strip */}
            <div className="pt-4 border-t border-[#E2D9C8]">
              <span className="text-xs font-mono text-[#6B7468] block mb-2 font-semibold">
                {language === 'kn' ? 'ಪರೀಕ್ಷಿಸಲು ಒಂದು ಪ್ರಶ್ನೆ ಆರಿಸಿ (Click to test):' : 'Click a sample farmer query:'}
              </span>
              <div className="flex flex-wrap gap-2">
                {quickSamples.map((sample, idx) => (
                  <button
                    key={idx}
                    onClick={() => {
                      onQuickPrompt(language === 'kn' ? sample.kn : sample.en);
                      onNavigate('voice');
                    }}
                    className="inline-flex items-center space-x-2 px-3.5 py-2 rounded-xl bg-white hover:bg-[#EBE5D8] text-xs font-kannada text-[#282C27] border border-[#E2D9C8] transition-colors shadow-sm text-left"
                  >
                    <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-[#FAF7F0] text-[#B08233] font-bold border border-[#E2D9C8]">
                      {sample.tag}
                    </span>
                    <span className="font-medium">{language === 'kn' ? sample.kn : sample.en}</span>
                  </button>
                ))}
              </div>
            </div>

          </div>

          {/* Right Column: Live Farm Weather & Agronomic Insights */}
          <div className="lg:col-span-5">
            <LiveFarmWeatherCard profile={profile} language={language} />
          </div>

        </div>
      </section>

      {/* 2. Three Editorial Product Highlights (Pillars) */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-6">

        {/* Pillar 1: Vernacular Voice Studio */}
        <div className="rounded-[2rem] bg-white p-7 border border-[#E2D9C8] shadow-sm hover:shadow-md transition-all space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-[#F7E4DE] text-[#C66F4E] flex items-center justify-center font-bold">
            <Mic className="w-6 h-6 stroke-[2]" />
          </div>
          <div className="space-y-2">
            <span className="text-xs font-mono uppercase tracking-wider text-[#C66F4E] font-bold">01 / ASR & TTS</span>
            <h3 className="text-xl font-bold font-kannada text-[#183B2B]">
              {language === 'kn' ? 'ಕನ್ನಡ ಧ್ವನಿ ಬುದ್ಧಿಮತ್ತೆ' : 'Vernacular Voice AI'}
            </h3>
            <p className="text-xs sm:text-sm text-[#4A5148] font-kannada leading-relaxed">
              {language === 'kn'
                ? 'Sarvam Saaras ಮಾದರಿಯ ಮೂಲಕ ಗ್ರಾಮೀಣ ಕನ್ನಡ ಮತ್ತು ಸಂಕರ ಪದಗಳನ್ನು ನಿಖರವಾಗಿ ಅರ್ಥೈಸುತ್ತದೆ. ಧ್ವನಿ ಮೂಲಕವೇ ಮರು-ಉತ್ತರ ನೀಡುತ್ತದೆ.'
                : 'Powered by Sarvam Saaras for Kannada speech recognition and Bulbul for natural conversational speech synthesis.'}
            </p>
          </div>
        </div>

        {/* Pillar 2: Scheme Eligibility Check (Farmer Friendly Language) */}
        <div className="rounded-[2rem] bg-white p-7 border border-[#E2D9C8] shadow-sm hover:shadow-md transition-all space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-[#EBE5D8] text-[#183B2B] flex items-center justify-center font-bold">
            <Scale className="w-6 h-6 stroke-[2]" />
          </div>
          <div className="space-y-2">
            <span className="text-xs font-mono uppercase tracking-wider text-[#183B2B] font-bold">02 / Eligibility Assessment</span>
            <h3 className="text-xl font-bold font-kannada text-[#183B2B]">
              {language === 'kn' ? 'ಅಧಿಕೃತ ಅರ್ಹತಾ ಪರಿಶೀಲನೆ' : 'Scheme Eligibility Check'}
            </h3>
            <p className="text-xs sm:text-sm text-[#4A5148] font-kannada leading-relaxed">
              {language === 'kn'
                ? 'ನಿಮ್ಮ ಜಮೀನಿನ ಮಾಲೀಕತ್ವ, ಬೆಳೆಗಳು ಮತ್ತು ಅಧಿಸೂಚಿತ ಪ್ರದೇಶಗಳ ಅಧಿಕೃತ ಮಾನದಂಡಗಳನ್ನು ಆಧರಿಸಿ ಅರ್ಹತೆಯನ್ನು ನಿಖರವಾಗಿ ಪರಿಶೀಲಿಸಲಾಗುತ್ತದೆ.'
                : 'Transparently evaluates official rules for land ownership, notified crops, and welfare subsidies with verified accuracy.'}
            </p>
          </div>
        </div>

        {/* Pillar 3: Guided Application Journey */}
        <div className="rounded-[2rem] bg-white p-7 border border-[#E2D9C8] shadow-sm hover:shadow-md transition-all space-y-4">
          <div className="w-12 h-12 rounded-2xl bg-[#FBF4E4] text-[#B08233] flex items-center justify-center font-bold">
            <FileText className="w-6 h-6 stroke-[2]" />
          </div>
          <div className="space-y-2">
            <span className="text-xs font-mono uppercase tracking-wider text-[#B08233] font-bold">03 / Journey</span>
            <h3 className="text-xl font-bold font-kannada text-[#183B2B]">
              {language === 'kn' ? 'ಅರ್ಜಿ ಸಿದ್ಧತಾ ಪಯಣ' : 'Application Dossier'}
            </h3>
            <p className="text-xs sm:text-sm text-[#4A5148] font-kannada leading-relaxed">
              {language === 'kn'
                ? 'ಯಾವ ದಾಖಲೆಗಳು ಕೈಯಲ್ಲಿವೆ, ಯಾವುದು ಬಾಕಿಯಿದೆ ಎಂದು ಶೇಕಡಾವಾರು ಸಿದ್ಧತಾ ಕೋಷ್ಟಕ ನೀಡುತ್ತದೆ. ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್ ಕೊಂಡಿ ಒದಗಿಸುತ್ತದೆ.'
                : 'Dynamic document readiness scorecards, missing criteria checklists, and direct verified links to official portals.'}
            </p>
          </div>
        </div>

      </section>

      {/* 3. System Transparency Footer */}
      <section className="rounded-2xl bg-[#FAF7F0] p-5 border border-[#E2D9C8] flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-[#6B7468]">
        <div className="flex items-center space-x-2.5">
          <Info className="w-4 h-4 text-[#183B2B] stroke-[2] flex-shrink-0" />
          <span className="font-kannada">
            {language === 'kn'
              ? 'ಕೃಷಿ ಮಿತ್ರ ಪ್ರಾಥಮಿಕ ಅರ್ಹತಾ ಮಾರ್ಗದರ್ಶಿಯಾಗಿದೆ. ಅಂತಿಮ ಸಬ್ಸಿಡಿ ಮತ್ತು ವಿಮೆ ಅನುಮೋದನೆ ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್‌ಗಳಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತದೆ.'
              : 'Krishi Mitra provides advisory scheme matching. Final sanction rests with designated statutory agricultural departments.'}
          </span>
        </div>
        <div className="flex items-center space-x-3 font-mono text-[11px] flex-shrink-0">
          <span className="inline-flex items-center space-x-1 px-3 py-1 rounded-full bg-[#183B2B] text-white font-bold">
            <span className="w-2 h-2 rounded-full bg-emerald-400 mr-1 animate-pulse" />
            Backend 8000 Online
          </span>
          <span className="text-[#6B7468]">Python / Vite / React</span>
        </div>
      </section>

      {/* Real-time Official Sarvam Live Conversational AI Modal */}
      <SarvamLiveVoiceModal
        isOpen={isLiveVoiceOpen}
        onClose={() => setIsLiveVoiceOpen(false)}
        profile={profile}
        language={language}
      />

    </div>
  );
};
