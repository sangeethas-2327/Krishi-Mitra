import React from 'react';
import { ShieldCheck, Info, Lock } from 'lucide-react';
import { translations } from '../../utils/translations';

interface TrustBannerProps {
  language: 'kn' | 'en';
}

export const TrustBanner: React.FC<TrustBannerProps> = ({ language }) => {
  const t = translations[language];

  return (
    <div className="bg-[#183B2B] text-white rounded-[2rem] p-7 shadow-md mt-16 border border-[#23503B]">
      <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-5">
        
        <div className="flex items-start space-x-4">
          <div className="w-11 h-11 rounded-2xl bg-[#10261C] flex items-center justify-center flex-shrink-0 text-[#D7A85B] border border-[#D7A85B]/30">
            <ShieldCheck className="w-6 h-6 text-[#D7A85B]" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white font-kannada">
              {language === 'kn' ? 'ವಿಶ್ವಾಸಾರ್ಹತೆ ಮತ್ತು ಪಾರದರ್ಶಕತೆ (Trust, Privacy & Provenance)' : 'Trust, Privacy & Provenance'}
            </h3>
            <p className="text-xs text-[#DEE4D2] leading-relaxed font-kannada mt-1 max-w-3xl">
              {t.disclaimerText}
            </p>
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-2.5 text-[11px] font-mono text-[#DEE4D2]">
          <span className="flex items-center space-x-1.5 bg-[#10261C] px-3 py-1.5 rounded-full border border-[#23503B] text-white">
            <Lock className="w-3 h-3 text-[#D7A85B]" />
            <span>{language === 'kn' ? 'ಯಾವುದೇ ಖಾಸಗಿ ಡೇಟಾ ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ' : 'No Aadhaar or Bank PII Stored'}</span>
          </span>
          <span className="flex items-center space-x-1.5 bg-[#10261C] px-3 py-1.5 rounded-full border border-[#23503B] text-white">
            <Info className="w-3 h-3 text-[#D7A85B]" />
            <span>{language === 'kn' ? 'ಪಾರದರ್ಶಕ ಅರ್ಹತಾ ಪರಿಶೀಲನೆ' : 'Auditable Eligibility Check'}</span>
          </span>
        </div>

      </div>
    </div>
  );
};
