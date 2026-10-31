import React from 'react';
import { Volume2, Square, User, Bot, Sparkles, RefreshCw, AlertCircle, Cpu } from 'lucide-react';
import { ChatMessage } from '../../types';
import { translations } from '../../utils/translations';

interface ChatWorkspaceProps {
  messages: ChatMessage[];
  language: 'kn' | 'en';
  onPlayAudio: (text: string, audioBase64?: string) => void;
  onStopAudio: () => void;
  isPlayingAudio: boolean;
  onSelectPrompt: (prompt: string) => void;
  isLoading: boolean;
  onRetry?: (text: string) => void;
  llmProvider?: string;
}

const SAMPLE_PROMPTS = [
  {
    kn: "ನನಗೆ ಕೃಷಿಗೆ ಸಹಾಯಧನ ಬೇಕು. ನಾನು ಮೂರು ಎಕರೆ ಅಡಿಕೆ ಬೆಳೆಯುತ್ತೇನೆ.",
    en: "I need agricultural assistance. I grow arecanut on 3 acres.",
    label_kn: "ಅಡಿಕೆ & ಸಹಾಯಧನ (ಪ್ರಾಥಮಿಕ ಸನ್ನಿವೇಶ)",
    label_en: "Arecanut & Subsidy (Primary Acceptance)"
  },
  {
    kn: "ನನ್ನ ಜಮೀನು ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯಲ್ಲಿದೆ ಮತ್ತು ಇದು ನನ್ನ ಸ್ವಂತ ಜಮೀನು.",
    en: "My land is in Shivamogga district and it is owned.",
    label_kn: "ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆ & ಸ್ವಂತ ಜಮೀನು",
    label_en: "Shivamogga District & Owned Land"
  },
  {
    kn: "ನಾನು ಗುತ್ತಿಗೆ ರೈತ, ನನಗೆ ಬೆಳೆ ವಿಮೆ ಯೋಜನೆ ಅನ್ವಯಿಸುತ್ತದೆಯೇ?",
    en: "I am a tenant farmer, does crop insurance apply to me?",
    label_kn: "ಗುತ್ತಿಗೆ ರೈತರ ಬೆಳೆ ವಿಮೆ (PMFBY)",
    label_en: "Tenant Farmer Crop Insurance"
  },
  {
    kn: "ನನ್ನ ಬಳಿ 4 ಎಕರೆ ಕಬ್ಬಿನ ತೋಟವಿದೆ, ಹನಿ ನೀರಾವರಿಗೆ ಸಹಾಯಧನ ಸಿಗುತ್ತದೆಯೇ?",
    en: "I have 4 acres of sugarcane, can I get a drip irrigation subsidy?",
    label_kn: "ಹನಿ ನೀರಾವರಿ ಸಲಕರಣೆ ನೆರವು",
    label_en: "Micro-Irrigation Assistance"
  }
];

export const ChatWorkspace: React.FC<ChatWorkspaceProps> = ({
  messages,
  language,
  onPlayAudio,
  onStopAudio,
  isPlayingAudio,
  onSelectPrompt,
  isLoading,
  onRetry,
  llmProvider
}) => {
  const t = translations[language];

  return (
    <div className="bg-white rounded-2xl shadow-sm border border-emerald-100 p-5 flex flex-col h-[520px]">
      
      {/* Header */}
      <div className="flex items-center justify-between pb-3 border-b border-gray-100">
        <div className="flex items-center space-x-2">
          <Bot className="w-5 h-5 text-forest-700" />
          <h2 className="text-base font-bold text-forest-900 font-kannada">
            {language === 'kn' ? 'ಸಂಭಾಷಣಾ ಇತಿಹಾಸ' : 'Conversational Dialogue'}
          </h2>
        </div>
        <span className="text-xs text-ktext-muted">
          {messages.length} {language === 'kn' ? 'ಸಂದೇಶಗಳು' : 'messages'}
        </span>
      </div>

      {/* Messages Scroll Area */}
      <div className="flex-1 overflow-y-auto py-4 space-y-4 pr-1">
        {messages.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-center p-6 text-ktext-muted">
            <div className="w-14 h-14 rounded-full bg-emerald-50 flex items-center justify-center mb-3 text-forest-700">
              <Sparkles className="w-7 h-7" />
            </div>
            <p className="text-sm font-medium text-ktext-primary mb-1 font-kannada">
              {language === 'kn' ? 'ಸ್ವಾಗತ! ಮಾತನಾಡಲು ಮೈಕ್ ಒತ್ತಿ ಅಥವಾ ಕೆಳಗಿನ ಪ್ರಶ್ನೆ ಆರಿಸಿ' : 'Welcome! Tap microphone or choose a sample question below'}
            </p>
            <p className="text-xs max-w-sm">
              {language === 'kn'
                ? 'ನಿಮ್ಮ ಕೃಷಿ ಭೂಮಿ, ಬೆಳೆ ಮತ್ತು ಅಗತ್ಯ ನೆರವಿನ ಬಗ್ಗೆ ತಿಳಿಸಿ. ಕೃಷಿ ಮಿತ್ರ ನಿಮಗೆ ಸರಿಹೊಂದುವ ಯೋಜನೆಗಳನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ.'
                : 'Share your land size, crop, and needed support. Krishi Mitra will match verified government schemes.'}
            </p>
          </div>
        ) : (
          messages.map((msg) => (
            <div
              key={msg.id}
              className={`flex items-start space-x-3 ${
                msg.role === 'user' ? 'flex-row-reverse space-x-reverse' : 'flex-row'
              }`}
            >
              {/* Avatar */}
              <div
                className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 text-white ${
                  msg.role === 'user' ? 'bg-earth-700' : 'bg-forest-700'
                }`}
              >
                {msg.role === 'user' ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
              </div>

              {/* Message Content */}
              <div
                className={`max-w-[82%] rounded-2xl p-4 shadow-sm text-sm font-kannada leading-relaxed ${
                  msg.role === 'user'
                    ? 'bg-emerald-700 text-white rounded-tr-none'
                    : msg.isError
                    ? 'bg-red-50/90 border border-red-200 text-red-900 rounded-tl-none'
                    : 'bg-emerald-50/70 border border-emerald-100 text-ktext-primary rounded-tl-none'
                }`}
              >
                {/* Provider Badge if assistant */}
                {msg.role === 'assistant' && !msg.isError && (
                  <div className="flex items-center space-x-1 mb-1.5 text-[10px] text-forest-700 font-sans font-medium">
                    <Cpu className="w-3 h-3 text-forest-600" />
                    <span>
                      {msg.llm_provider === 'gemini-live' ? 'Gemini 2.5 Flash' : 'Krishi Mitra Engine'}
                    </span>
                  </div>
                )}

                <p className="text-sm">{msg.content}</p>

                {/* English translation subtitle if in Kannada mode */}
                {msg.role === 'assistant' && msg.content_en && language === 'kn' && !msg.isError && (
                  <p className="text-xs text-gray-500 mt-2 pt-2 border-t border-emerald-200/60 font-sans italic">
                    EN: {msg.content_en}
                  </p>
                )}

                {/* Spoken Audio Listen Button or Retry on Error */}
                {msg.role === 'assistant' && (
                  <div className="mt-2.5 pt-2 border-t border-emerald-200/60 flex items-center justify-between text-xs">
                    {msg.isError && msg.retryText && onRetry ? (
                      <button
                        onClick={() => onRetry(msg.retryText!)}
                        className="inline-flex items-center space-x-1.5 text-red-700 hover:text-red-900 font-medium px-2.5 py-1 rounded bg-white border border-red-200 transition shadow-sm text-xs"
                      >
                        <RefreshCw className="w-3.5 h-3.5" />
                        <span>{language === 'kn' ? 'ಮರುಪ್ರಯತ್ನಿಸಿ' : 'Retry'}</span>
                      </button>
                    ) : (
                      <button
                        onClick={() => isPlayingAudio ? onStopAudio() : onPlayAudio(msg.content, msg.audio_base64)}
                        className="inline-flex items-center space-x-1.5 text-forest-800 hover:text-forest-950 font-medium px-2 py-1 rounded bg-white border border-emerald-200 transition"
                      >
                        {isPlayingAudio ? (
                          <>
                            <Square className="w-3.5 h-3.5 fill-current text-red-600" />
                            <span>{t.stopSpeaking}</span>
                          </>
                        ) : (
                          <>
                            <Volume2 className="w-3.5 h-3.5 text-forest-700" />
                            <span>{t.readAloud}</span>
                          </>
                        )}
                      </button>
                    )}
                    <span className="text-[11px] text-gray-400">
                      {msg.created_at}
                    </span>
                  </div>
                )}
              </div>
            </div>
          ))
        )}

        {isLoading && (
          <div className="flex items-center space-x-2 text-forest-800 text-xs py-2 px-3 bg-emerald-50/80 border border-emerald-200/60 rounded-xl w-max animate-pulse">
            <Bot className="w-4 h-4 text-forest-700 animate-bounce" />
            <span className="font-kannada font-medium">
              {language === 'kn'
                ? 'ಕೃಷಿ ಮಿತ್ರ (Gemini AI) ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸುತ್ತಿದೆ...'
                : 'Krishi Mitra (Gemini AI) is evaluating eligibility rules...'}
            </span>
          </div>
        )}
      </div>

      {/* Quick Suggestion Chips */}
      <div className="pt-3 border-t border-gray-100">
        <p className="text-xs text-ktext-muted mb-2 font-medium">
          {language === 'kn' ? 'ಉದಾಹರಣೆ ಪ್ರಶ್ನೆಗಳು (ಪರೀಕ್ಷಿಸಲು ಒತ್ತಿ):' : 'Sample Scenarios (Tap to test):'}
        </p>
        <div className="flex flex-wrap gap-1.5">
          {SAMPLE_PROMPTS.map((prompt, idx) => (
            <button
              key={idx}
              onClick={() => onSelectPrompt(language === 'kn' ? prompt.kn : prompt.en)}
              className="text-xs bg-emerald-50 hover:bg-emerald-100 text-forest-900 border border-emerald-200 rounded-lg px-2.5 py-1 text-left transition font-kannada flex items-center space-x-1"
            >
              <Sparkles className="w-3 h-3 text-forest-600 flex-shrink-0" />
              <span>{language === 'kn' ? prompt.label_kn : prompt.label_en}</span>
            </button>
          ))}
        </div>
      </div>

    </div>
  );
};
