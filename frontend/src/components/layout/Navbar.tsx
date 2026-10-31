import React from 'react';
import {
  Compass,
  Mic,
  Sprout,
  BookOpenCheck,
  FileCheck2,
  Globe,
  RotateCcw,
  Radio
} from 'lucide-react';
import { translations } from '../../utils/translations';

export type NavTab = 'discover' | 'voice' | 'myfarm' | 'schemes' | 'journey';

interface NavbarProps {
  language: 'kn' | 'en';
  onToggleLanguage: () => void;
  onResetSession: () => void;
  isDemoMode: boolean;
  llmProvider?: string;
  geminiModel?: string;
  activeTab: NavTab;
  onTabChange: (tab: NavTab) => void;
  cropsCount?: number;
  landAcres?: number | null;
  suitableSchemesCount?: number;
  isVoiceActive?: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({
  language,
  onToggleLanguage,
  onResetSession,
  isDemoMode,
  llmProvider,
  activeTab,
  onTabChange,
  cropsCount = 0,
  landAcres = null,
  suitableSchemesCount = 0,
  isVoiceActive = false
}) => {
  const t = translations[language];
  const isLiveGemini = !isDemoMode && llmProvider === 'gemini-live';

  const navItems = [
    {
      id: 'discover' as NavTab,
      label: t.navDiscover,
      icon: Compass,
      badge: null,
    },
    {
      id: 'voice' as NavTab,
      label: t.navVoiceStudio,
      icon: Mic,
      isVoice: true,
      badge: null,
    },
    {
      id: 'myfarm' as NavTab,
      label: t.navMyFarm,
      icon: Sprout,
      badge: landAcres ? `${landAcres} ac` : (cropsCount > 0 ? `${cropsCount}` : null),
    },
    {
      id: 'schemes' as NavTab,
      label: t.navSchemes,
      icon: BookOpenCheck,
      badge: suitableSchemesCount > 0 ? `${suitableSchemesCount}` : null,
    },
    {
      id: 'journey' as NavTab,
      label: t.navJourney,
      icon: FileCheck2,
      badge: null,
    },
  ];

  return (
    <header className="sticky top-0 z-50 bg-[#FAF7F0] border-b border-[#E2D9C8] backdrop-blur-md shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">

          {/* Brand Mark — Clean Editorial Agritech */}
          <div
            onClick={() => onTabChange('discover')}
            className="flex items-center space-x-3 cursor-pointer group select-none flex-shrink-0"
          >
            <div className="w-11 h-11 sm:w-12 sm:h-12 rounded-xl overflow-hidden bg-[#FAF7F0] border border-[#E2D9C8] shadow-sm group-hover:scale-105 group-hover:shadow transition-all flex items-center justify-center flex-shrink-0 p-0.5">
              <img
                src="/krishi-mitra-logo.png"
                alt="Krishi Mitra Logo"
                className="w-full h-full object-contain"
                loading="eager"
              />
            </div>
            <div className="flex flex-col">
              <div className="flex items-center space-x-2">
                <span className="font-kannada text-xl sm:text-2xl font-extrabold tracking-tight text-[#183B2B]">
                  {language === 'kn' ? 'ಕೃಷಿ ಮಿತ್ರ' : 'Krishi Mitra'}
                </span>
                <span className="hidden sm:inline-block text-[10px] uppercase font-mono tracking-wider px-2 py-0.5 rounded-full bg-[#EBE5D8] text-[#183B2B] font-bold border border-[#E2D9C8]">
                  {t.livingCompanion}
                </span>
              </div>
              <span className="text-[11px] text-[#6B7468] tracking-wide font-sans hidden lg:block">
                {language === 'kn' ? 'ಬುದ್ಧಿವಂತ ಕೃಷಿ ಸಂವಾದ ವೇದಿಕೆ' : 'Intelligent Vernacular Agricultural Platform'}
              </span>
            </div>
          </div>

          {/* Center Navigation Tabs (Desktop & Tablet) */}
          <nav className="hidden md:flex items-center space-x-1 bg-[#EBE5D8]/70 p-1.5 rounded-2xl border border-[#E2D9C8]">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => onTabChange(item.id)}
                  className={`h-10 px-3 lg:px-3.5 rounded-xl text-xs font-semibold flex items-center transition-all ${isActive
                      ? 'bg-[#183B2B] text-white shadow-sm font-bold'
                      : 'text-[#282C27] hover:text-[#183B2B] hover:bg-white/70'
                    }`}
                >
                  <Icon className={`w-4 h-4 flex-shrink-0 mr-2 stroke-[2] ${isActive
                      ? 'text-[#D7A85B] stroke-[2.2]'
                      : 'text-[#5C645A]'
                    } ${item.isVoice && isVoiceActive ? 'text-[#C66F4E] animate-pulse' : ''}`} />

                  <span className="font-kannada text-[13px] whitespace-nowrap">{item.label}</span>

                  {/* Subtle active voice indicator */}
                  {item.isVoice && isVoiceActive && (
                    <span className="w-2 h-2 rounded-full bg-[#C66F4E] animate-pulse ml-2 flex-shrink-0" />
                  )}

                  {/* Clean, compact count/acreage badge */}
                  {item.badge && (
                    <span className={`ml-2 text-[10px] font-mono font-bold px-1.5 py-0.5 rounded-full flex items-center justify-center leading-none ${isActive
                        ? 'bg-[#D7A85B] text-[#183B2B]'
                        : 'bg-white text-[#183B2B] border border-[#E2D9C8]'
                      }`}>
                      {item.badge}
                    </span>
                  )}
                </button>
              );
            })}
          </nav>

          {/* Right Controls: Mode Badge, Language Switcher, Reset */}
          <div className="flex items-center space-x-2 sm:space-x-3 flex-shrink-0">

            {/* Operational Mode Badge — Farmer Friendly Terminology */}
            <div
              title={isLiveGemini ? 'Live Gemini 2.5 Flash connected' : 'Verified statutory eligibility assessment active'}
              className="hidden xl:flex items-center space-x-1.5 px-3 py-1.5 rounded-full text-[11px] font-mono bg-white border border-[#E2D9C8] text-[#183B2B]"
            >
              <Radio className={`w-3.5 h-3.5 ${isLiveGemini ? 'text-emerald-600 animate-pulse' : 'text-[#B08233]'}`} />
              <span className="font-bold">
                {isLiveGemini ? `Gemini AI` : (language === 'kn' ? 'ಅರ್ಹತಾ ಪರಿಶೀಲನೆ' : 'Eligibility Check')}
              </span>
            </div>

            {/* Language Switcher */}
            <button
              onClick={onToggleLanguage}
              className="flex items-center space-x-1.5 px-3 py-2 rounded-xl bg-white hover:bg-[#FAF7F0] border border-[#E2D9C8] text-xs font-bold text-[#183B2B] transition-all shadow-sm active:scale-95"
              aria-label="Toggle language"
            >
              <Globe className="w-3.5 h-3.5 text-[#B08233] stroke-[2]" />
              <span className="font-kannada">{language === 'kn' ? 'English' : 'ಕನ್ನಡ'}</span>
            </button>

            {/* Clear / New Session */}
            <button
              onClick={onResetSession}
              className="flex items-center justify-center w-9 h-9 rounded-xl bg-white hover:bg-[#F7E4DE] hover:text-[#C66F4E] border border-[#E2D9C8] text-[#6B7468] transition-colors"
              title={t.clearSession}
              aria-label={t.clearSession}
            >
              <RotateCcw className="w-4 h-4 stroke-[2]" />
            </button>

          </div>

        </div>
      </div>

      {/* Mobile Bottom Floating Navigation Bar — Clean, balanced 5-column grid */}
      <div className="md:hidden fixed bottom-0 left-0 right-0 z-50 bg-[#FAF7F0]/95 backdrop-blur-xl border-t border-[#E2D9C8] px-2 py-1.5 shadow-[0_-4px_24px_rgba(24,59,43,0.08)]">
        <div className="grid grid-cols-5 items-center max-w-md mx-auto">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;

            if (item.id === 'voice') {
              return (
                <button
                  key={item.id}
                  onClick={() => onTabChange(item.id)}
                  className="flex flex-col items-center justify-center py-1 -mt-5 group"
                  aria-label={item.label}
                >
                  <div className={`w-12 h-12 rounded-full flex items-center justify-center shadow-lg transition-transform active:scale-95 ${isVoiceActive
                      ? 'bg-[#C66F4E] text-white ring-4 ring-[#C66F4E]/30 animate-pulse'
                      : isActive
                        ? 'bg-[#183B2B] text-[#D7A85B] ring-2 ring-[#D7A85B]'
                        : 'bg-[#D7A85B] text-[#183B2B] hover:scale-105'
                    }`}>
                    <Icon className="w-5 h-5 stroke-[2.2]" />
                  </div>
                  <span className={`text-[10px] font-kannada mt-1 leading-none ${isActive ? 'text-[#183B2B] font-bold' : 'text-[#5C645A]'
                    }`}>
                    {item.label}
                  </span>
                </button>
              );
            }

            return (
              <button
                key={item.id}
                onClick={() => onTabChange(item.id)}
                className={`flex flex-col items-center justify-center py-1.5 px-1 rounded-xl transition-colors relative ${isActive ? 'text-[#183B2B] font-bold' : 'text-[#6B7468] hover:text-[#183B2B]'
                  }`}
              >
                <div className="relative">
                  <Icon className={`w-5 h-5 stroke-[2] ${isActive ? 'text-[#183B2B]' : 'text-[#6B7468]'}`} />
                  {item.badge && (
                    <span className="absolute -top-1 -right-2 min-w-[14px] h-[14px] px-0.5 rounded-full bg-[#D7A85B] text-[#183B2B] text-[9px] font-mono font-bold flex items-center justify-center leading-none">
                      {item.badge}
                    </span>
                  )}
                </div>
                <span className="text-[10px] font-kannada mt-1 truncate max-w-full text-center leading-none">
                  {item.label}
                </span>
                {isActive && (
                  <span className="w-1 h-1 rounded-full bg-[#183B2B] mt-1" />
                )}
              </button>
            );
          })}
        </div>
      </div>
    </header>
  );
};
