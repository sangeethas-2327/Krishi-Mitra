import React, { useEffect } from 'react';
import {
  Mic,
  MicOff,
  PhoneOff,
  Radio,
  Volume2,
  Loader2,
  AlertCircle,
  X,
  Sparkles,
  MapPin,
  Trees,
  CheckCircle2
} from 'lucide-react';
import { AgentState } from 'sarvam-conv-ai-sdk/browser';
import { FarmerProfile } from '../../types';
import { useSarvamConversation } from '../../hooks/useSarvamConversation';

interface SarvamLiveVoiceModalProps {
  isOpen: boolean;
  onClose: () => void;
  profile: FarmerProfile;
  language: 'kn' | 'en';
}

export const SarvamLiveVoiceModal: React.FC<SarvamLiveVoiceModalProps> = ({
  isOpen,
  onClose,
  profile,
  language
}) => {
  const {
    agentState,
    isProcessing,
    isMuted,
    error,
    currentAssistantText,
    currentUserText,
    conversationHistory,
    audioLevel,
    startConversation,
    stopConversation,
    toggleMute,
    isConnected
  } = useSarvamConversation();

  // Auto-start voice call when modal opens
  useEffect(() => {
    if (isOpen && agentState === AgentState.IDLE) {
      startConversation(profile, language);
    }
    // Cleanup when modal closes
    return () => {
      if (isOpen) {
        stopConversation();
      }
    };
  }, [isOpen]);

  if (!isOpen) return null;

  const handleEndCall = async () => {
    await stopConversation();
    onClose();
  };

  // State badge styling and label
  const renderStateBadge = () => {
    if (error) {
      return (
        <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-red-100 text-red-800 text-xs font-bold font-kannada">
          <AlertCircle className="w-3.5 h-3.5 text-red-600" />
          <span>{language === 'kn' ? 'ದೋಷ ಕಂಡುಬಂದಿದೆ' : 'Connection Error'}</span>
        </span>
      );
    }

    if (agentState === AgentState.CONNECTING) {
      return (
        <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-amber-100 text-amber-800 text-xs font-bold font-kannada animate-pulse">
          <Loader2 className="w-3.5 h-3.5 animate-spin text-amber-600" />
          <span>{language === 'kn' ? 'ಸರ್ವರ್ ಸಂಪರ್ಕಿಸಲಾಗುತ್ತಿದೆ (Connecting...)' : 'Connecting to Krishi Mitra...'}</span>
        </span>
      );
    }

    if (isProcessing) {
      return (
        <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-[#D7A85B]/20 text-[#B08233] text-xs font-bold font-kannada animate-pulse">
          <Sparkles className="w-3.5 h-3.5 text-[#B08233]" />
          <span>{language === 'kn' ? 'ಯೋಚಿಸುತ್ತಿದೆ (Processing...)' : 'Thinking / Processing...'}</span>
        </span>
      );
    }

    if (agentState === AgentState.SPEAKING) {
      return (
        <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold font-kannada">
          <Volume2 className="w-3.5 h-3.5 text-emerald-600 animate-bounce" />
          <span>{language === 'kn' ? 'ಕೃಷಿ ಮಿತ್ರ ಮಾತನಾಡುತ್ತಿದೆ (Speaking...)' : 'Krishi Mitra is speaking...'}</span>
        </span>
      );
    }

    if (agentState === AgentState.LISTENING || agentState === AgentState.CONNECTED) {
      return (
        <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-emerald-100 text-[#183B2B] text-xs font-bold font-kannada">
          <Radio className="w-3.5 h-3.5 text-emerald-600 animate-pulse" />
          <span>{language === 'kn' ? 'ಕೇಳಿಸಿಕೊಳ್ಳುತ್ತಿದೆ (Listening... ಮಾತನಾಡಿ)' : 'Listening... Speak naturally'}</span>
        </span>
      );
    }

    return (
      <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-gray-100 text-gray-700 text-xs font-medium font-kannada">
        <span>{language === 'kn' ? 'ಸಿದ್ಧವಾಗಿದೆ (Ready)' : 'Ready'}</span>
      </span>
    );
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/70 backdrop-blur-md flex items-center justify-center p-4">
      <div className="bg-[#FAF7F0] rounded-[2.5rem] shadow-2xl max-w-lg w-full max-h-[92vh] flex flex-col border border-[#E2D9C8] overflow-hidden animate-fadeIn">
        
        {/* Header */}
        <div className="p-6 pb-4 border-b border-[#E2D9C8] flex items-center justify-between bg-white flex-shrink-0">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-2xl bg-[#183B2B] flex items-center justify-center shadow-sm">
              <Radio className="w-5 h-5 text-[#D7A85B] animate-pulse" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h3 className="text-lg font-extrabold text-[#183B2B] font-kannada">
                  {language === 'kn' ? 'ಸರ್ವಂ ಲೈವ್ ಕೃಷಿ ಮಿತ್ರ' : 'Sarvam Live Krishi Mitra'}
                </h3>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-[#EBE5D8] text-[#183B2B] font-bold border border-[#E2D9C8]">
                  Web SDK
                </span>
              </div>
              <p className="text-xs text-[#6B7468] font-sans">
                {language === 'kn' ? 'ನೈಜ-ಸಮಯದ ಧ್ವನಿ ಸಂಭಾಷಣೆ • ಕನ್ನಡ' : 'Real-Time Full-Duplex Voice Conversation'}
              </p>
            </div>
          </div>

          <button
            onClick={handleEndCall}
            className="p-2 rounded-xl text-[#6B7468] hover:text-[#183B2B] hover:bg-[#FAF7F0] transition"
            title="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6 flex flex-col items-center justify-between space-y-6 scrollbar-thin">
          
          {/* Active Context Banner */}
          <div className="w-full bg-white border border-[#E2D9C8] rounded-2xl p-3 flex items-center justify-between text-xs text-[#282C27] shadow-xs">
            <div className="flex items-center space-x-2 truncate">
              <MapPin className="w-4 h-4 text-[#183B2B] flex-shrink-0" />
              <span className="font-semibold truncate">
                {profile.location?.district ? `${profile.location.district}` : 'Karnataka'}
                {profile.location?.taluk ? `, ${profile.location.taluk}` : ''}
              </span>
            </div>
            <div className="flex items-center space-x-1.5 flex-shrink-0">
              <Trees className="w-3.5 h-3.5 text-[#B08233]" />
              <span className="text-[11px] text-[#6B7468] capitalize">
                {profile.crops && profile.crops.length > 0 ? profile.crops.slice(0, 2).join(', ') : 'All crops'}
              </span>
            </div>
          </div>

          {/* Central Pulsing Audio Visualizer */}
          <div className="relative my-4 flex items-center justify-center">
            {/* Outer animated ripple rings */}
            {agentState === AgentState.SPEAKING && (
              <div className="absolute w-44 h-44 rounded-full bg-emerald-400/20 animate-ping" />
            )}
            {agentState === AgentState.LISTENING && (
              <div className="absolute w-40 h-40 rounded-full bg-[#D7A85B]/25 animate-pulse" />
            )}
            {isProcessing && (
              <div className="absolute w-40 h-40 rounded-full bg-amber-400/25 animate-spin" />
            )}

            {/* Central Circle Orb */}
            <div
              className={`relative z-10 w-28 h-28 rounded-full flex flex-col items-center justify-center shadow-lg transition-transform duration-300 ${
                agentState === AgentState.SPEAKING
                  ? 'bg-[#183B2B] text-emerald-300 scale-105 ring-4 ring-emerald-200'
                  : agentState === AgentState.LISTENING
                  ? 'bg-[#183B2B] text-[#D7A85B] ring-4 ring-[#D7A85B]/40'
                  : agentState === AgentState.CONNECTING || isProcessing
                  ? 'bg-amber-700 text-white animate-pulse'
                  : error
                  ? 'bg-red-700 text-white'
                  : 'bg-[#183B2B] text-white'
              }`}
            >
              {error ? (
                <AlertCircle className="w-10 h-10" />
              ) : isProcessing ? (
                <Loader2 className="w-10 h-10 animate-spin text-[#D7A85B]" />
              ) : agentState === AgentState.SPEAKING ? (
                <Volume2 className="w-10 h-10 animate-bounce text-emerald-400" />
              ) : isMuted ? (
                <MicOff className="w-10 h-10 text-red-300" />
              ) : (
                <Mic className="w-10 h-10 text-[#D7A85B]" />
              )}

              {/* Dynamic waveform simulation ticks */}
              <div className="flex items-center space-x-1 mt-1">
                <span className="w-1 h-2 bg-current rounded-full animate-pulse" />
                <span className="w-1 h-3.5 bg-current rounded-full animate-pulse delay-75" />
                <span className="w-1 h-2 bg-current rounded-full animate-pulse delay-150" />
              </div>
            </div>
          </div>

          {/* Current State Badge */}
          <div className="flex justify-center">{renderStateBadge()}</div>

          {/* Real-time Streaming Transcript & Turn History */}
          <div className="w-full bg-white border border-[#E2D9C8] rounded-2xl p-4 shadow-inner min-h-[140px] max-h-52 overflow-y-auto space-y-3 text-xs scrollbar-thin">
            {conversationHistory.length > 0 && (
              <div className="space-y-2">
                {conversationHistory.map((msg) => (
                  <div key={msg.id} className="space-y-1 animate-fadeIn">
                    <span className="text-[10px] font-bold text-[#6B7468]">
                      {msg.role === 'user' ? (language === 'kn' ? 'ನೀವು (Farmer):' : 'You:') : (language === 'kn' ? 'ಕೃಷಿ ಮಿತ್ರ:' : 'Krishi Mitra:')}
                    </span>
                    <p className={`text-xs p-2.5 rounded-xl border ${
                      msg.role === 'user'
                        ? 'bg-emerald-50/60 text-[#183B2B] border-emerald-100 font-sans'
                        : 'bg-[#FAF7F0] text-[#282C27] border-[#E2D9C8] font-kannada'
                    }`}>
                      {msg.text}
                    </p>
                  </div>
                ))}
              </div>
            )}

            {/* Currently speaking turn */}
            {currentAssistantText && (!conversationHistory.length || conversationHistory[conversationHistory.length - 1]?.text !== currentAssistantText) && (
              <div className="space-y-1 animate-fadeIn">
                <div className="flex items-center space-x-1.5 text-[11px] font-bold text-[#183B2B] font-kannada">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#B08233]" />
                  <span>{language === 'kn' ? 'ಕೃಷಿ ಮಿತ್ರ ಉತ್ತರ:' : 'Krishi Mitra:'}</span>
                </div>
                <p className="text-xs text-[#282C27] font-kannada leading-relaxed bg-[#FAF7F0] p-2.5 rounded-xl border border-[#E2D9C8]">
                  {currentAssistantText}
                </p>
              </div>
            )}

            {currentUserText && (!conversationHistory.length || conversationHistory[conversationHistory.length - 1]?.text !== currentUserText) && (
              <div className="space-y-1 animate-fadeIn">
                <span className="text-[11px] font-bold text-[#6B7468]">
                  {language === 'kn' ? 'ನೀವು ಹೇಳುತ್ತಿದ್ದೀರಿ:' : 'You are saying:'}
                </span>
                <p className="text-xs text-[#183B2B] italic bg-emerald-50/70 p-2.5 rounded-xl border border-emerald-200">
                  "{currentUserText}"
                </p>
              </div>
            )}

            {!conversationHistory.length && !currentAssistantText && !currentUserText && (
              <div className="h-full flex flex-col items-center justify-center text-center py-6 text-[#6B7468]">
                <p className="font-kannada text-xs font-medium">
                  {language === 'kn'
                    ? 'ನೈಸರ್ಗಿಕವಾಗಿ ಕನ್ನಡದಲ್ಲಿ ಮಾತನಾಡಿ. ಯೋಜನೆಗಳು, ಹವಾಮಾನ ಅಥವಾ ಬೆಳೆಗಳ ಬಗ್ಗೆ ಕೇಳಿ...'
                    : 'Speak naturally in Kannada or English. Ask about schemes, weather, or crops...'}
                </p>
                <span className="text-[10px] text-[#A8B58A] mt-1 font-mono">
                  sarvam-conv-ai-sdk • Full-Duplex Audio
                </span>
              </div>
            )}
          </div>

          {/* Error Banner with Retry */}
          {error && (
            <div className="w-full bg-red-50 border border-red-200 rounded-2xl p-3.5 flex flex-col space-y-2 text-xs text-red-900 animate-fadeIn">
              <div className="flex items-start space-x-2">
                <AlertCircle className="w-4 h-4 text-red-600 flex-shrink-0 mt-0.5" />
                <span className="font-medium">{error}</span>
              </div>
              <button
                onClick={() => startConversation(profile, language)}
                className="self-end px-3 py-1 bg-red-600 hover:bg-red-700 text-white text-[11px] font-bold rounded-lg transition"
              >
                {language === 'kn' ? 'ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ (Retry)' : 'Retry Call'}
              </button>
            </div>
          )}

        </div>

        {/* Footer Controls: Mute, End Call */}
        <div className="p-6 pt-4 border-t border-[#E2D9C8] bg-white flex items-center justify-around flex-shrink-0">
          
          {/* Mute / Unmute Button */}
          <button
            onClick={toggleMute}
            disabled={!isConnected}
            className={`flex flex-col items-center space-y-1 p-3 rounded-2xl transition disabled:opacity-40 ${
              isMuted
                ? 'bg-red-100 text-red-800 hover:bg-red-200'
                : 'bg-[#FAF7F0] text-[#183B2B] hover:bg-[#EBE5D8]'
            }`}
          >
            {isMuted ? <MicOff className="w-6 h-6 text-red-600" /> : <Mic className="w-6 h-6 text-[#183B2B]" />}
            <span className="text-[11px] font-semibold font-kannada">
              {isMuted
                ? (language === 'kn' ? 'ಅನ್‌ಮ್ಯೂಟ್' : 'Unmute')
                : (language === 'kn' ? 'ಮ್ಯೂಟ್' : 'Mute')}
            </span>
          </button>

          {/* End Call Button */}
          <button
            onClick={handleEndCall}
            className="flex items-center space-x-2.5 px-7 py-3.5 rounded-2xl bg-red-600 hover:bg-red-700 text-white font-extrabold text-sm shadow-md transition active:scale-95"
          >
            <PhoneOff className="w-5 h-5" />
            <span className="font-kannada">
              {language === 'kn' ? 'ಸಂಭಾಷಣೆ ಮುಕ್ತಾಯ (End)' : 'End Call'}
            </span>
          </button>

        </div>

      </div>
    </div>
  );
};

