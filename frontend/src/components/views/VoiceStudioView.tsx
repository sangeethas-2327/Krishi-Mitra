import React, { useState, useEffect } from 'react';
import {
  Mic,
  Square,
  Loader2,
  Send,
  Volume2,
  VolumeX,
  RotateCcw,
  Check,
  Edit3,
  Sparkles,
  AlertCircle,
  MessageSquare,
  ChevronRight,
  ChevronDown,
  ChevronUp,
  History,
  Layers,
  MapPin,
  Wheat,
  Scale,
  RefreshCw,
  PhoneCall,
  Radio
} from 'lucide-react';
import { translations } from '../../utils/translations';
import { FarmerProfile, ChatMessage, SchemeMatchResult } from '../../types';
import { useVoiceRecorder } from '../../hooks/useVoiceRecorder';
import { SarvamLiveVoiceModal } from '../voice/SarvamLiveVoiceModal';

interface VoiceStudioViewProps {
  language: 'kn' | 'en';
  onSendMessage: (text: string) => Promise<void>;
  isLoading: boolean;
  voiceProvider?: string;
  llmProvider?: string;
  profile: FarmerProfile;
  messages: ChatMessage[];
  recommendations: SchemeMatchResult[];
  onPlayAudio: (text: string, audioBase64?: string) => void;
  onStopAudio: () => void;
  isPlayingAudio: boolean;
  onNavigateToSchemes: () => void;
  onNavigateToFarm: () => void;
}

export const VoiceStudioView: React.FC<VoiceStudioViewProps> = ({
  language,
  onSendMessage,
  isLoading,
  voiceProvider,
  llmProvider,
  profile,
  messages,
  recommendations,
  onPlayAudio,
  onStopAudio,
  isPlayingAudio,
  onNavigateToSchemes,
  onNavigateToFarm
}) => {
  const t = translations[language];

  const {
    isRecording,
    isProcessing,
    recordingSeconds,
    transcript,
    error: recorderError,
    startRecording,
    stopRecording,
    cancelRecording,
    setTranscript
  } = useVoiceRecorder();

  const [editableTranscript, setEditableTranscript] = useState('');
  const [isEditingTranscript, setIsEditingTranscript] = useState(false);
  const [showHistory, setShowHistory] = useState(false);
  const [textInput, setTextInput] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isLiveCallOpen, setIsLiveCallOpen] = useState(false);

  // Sync transcribed text to editable buffer
  useEffect(() => {
    if (transcript) {
      setEditableTranscript(transcript);
    }
  }, [transcript]);

  // Determine current interaction state
  type StudioState = 'IDLE' | 'LISTENING' | 'PROCESSING' | 'TRANSCRIBED' | 'RESPONDING' | 'ERROR';

  const getStudioState = (): StudioState => {
    if (recorderError) return 'ERROR';
    if (isRecording) return 'LISTENING';
    if (isProcessing || isLoading || isSubmitting) return 'PROCESSING';
    if (transcript && !isSubmitting) return 'TRANSCRIBED';
    if (isPlayingAudio) return 'RESPONDING';
    return 'IDLE';
  };

  const studioState = getStudioState();

  const formatSeconds = (sec: number) => {
    const mins = Math.floor(sec / 60);
    const secs = sec % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const handleMicToggle = async () => {
    if (isRecording) {
      const recognized = await stopRecording();
      if (recognized) {
        setEditableTranscript(recognized);
      }
    } else {
      setEditableTranscript('');
      setIsEditingTranscript(false);
      await startRecording();
    }
  };

  const handleConfirmAndSend = async (textToSend: string) => {
    const trimmed = textToSend.trim();
    if (!trimmed || isSubmitting || isLoading) return;

    setIsSubmitting(true);
    try {
      await onSendMessage(trimmed);
      setEditableTranscript('');
      setTranscript('');
      setIsEditingTranscript(false);
      setTextInput('');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Get latest assistant message for responding state
  const latestAssistantMessage = [...messages].reverse().find(m => m.role === 'assistant');

  return (
    <div className="max-w-5xl mx-auto space-y-6 pb-20 animate-fadeIn">

      {/* 1. Contextual Farmer Identity Chips Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 p-3.5 rounded-2xl bg-white border border-ivory-border shadow-sm">
        <div className="flex flex-wrap items-center gap-2">
          <span className="text-[11px] font-mono uppercase text-charcoal-muted tracking-wider font-semibold mr-1">
            {language === 'kn' ? 'ಸಕ್ರಿಯ ವಿವರಗಳು:' : 'Active Context:'}
          </span>

          {/* Location Chip */}
          <button
            onClick={onNavigateToFarm}
            className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-xl bg-ivory text-forest text-xs font-kannada border border-ivory-border hover:border-harvest transition-colors"
          >
            <MapPin className="w-3.5 h-3.5 text-terracotta" />
            <span>
              {profile.location.district
                ? `${profile.location.district}${profile.location.taluk ? `, ${profile.location.taluk}` : ''}`
                : (language === 'kn' ? 'ಜಿಲ್ಲೆ: ನಮೂದಿಸಿಲ್ಲ' : 'District: Not set')}
            </span>
          </button>

          {/* Land Area Chip */}
          <button
            onClick={onNavigateToFarm}
            className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-xl bg-ivory text-forest text-xs font-mono font-medium border border-ivory-border hover:border-harvest transition-colors"
          >
            <Layers className="w-3.5 h-3.5 text-harvest-dark" />
            <span>
              {profile.land_area.value_acres
                ? `${profile.land_area.value_acres} Acres`
                : (language === 'kn' ? 'ಭೂಮಿ: ಅಗತ್ಯವಿದೆ' : 'Land: Needed')}
            </span>
          </button>

          {/* Crops Chip */}
          <button
            onClick={onNavigateToFarm}
            className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-xl bg-ivory text-forest text-xs font-kannada border border-ivory-border hover:border-harvest transition-colors"
          >
            <Wheat className="w-3.5 h-3.5 text-forest-500" />
            <span>
              {profile.crops.length > 0
                ? profile.crops.join(', ')
                : (language === 'kn' ? 'ಬೆಳೆಗಳು: ಸೇರಿಸಿ' : 'Crops: Add')}
            </span>
          </button>
        </div>

        {/* Suitable Schemes Quick Link Badge */}
        {recommendations.length > 0 && (
          <button
            onClick={onNavigateToSchemes}
            className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-xl bg-harvest/15 text-forest font-semibold text-xs border border-harvest/40 hover:bg-harvest/25 transition-all"
          >
            <Scale className="w-3.5 h-3.5 text-harvest-dark" />
            <span>
              {language === 'kn'
                ? `${recommendations.filter(r => r.evaluation_status === 'POTENTIALLY_SUITABLE').length} ಅರ್ಹ ಯೋಜನೆಗಳು`
                : `${recommendations.filter(r => r.evaluation_status === 'POTENTIALLY_SUITABLE').length} Suitable Schemes`}
            </span>
            <ChevronRight className="w-3.5 h-3.5 text-forest-muted" />
          </button>
        )}
      </div>

      {/* Real-time Sarvam AI Live Voice Call Banner */}
      <div className="relative overflow-hidden rounded-[2rem] bg-gradient-to-r from-[#FAF7F0] to-[#F5EFE0] p-6 border-2 border-[#D7A85B] shadow-sm flex flex-col sm:flex-row items-center justify-between gap-5">
        <div className="flex items-center space-x-4">
          <div className="w-14 h-14 rounded-2xl bg-[#183B2B] flex items-center justify-center flex-shrink-0 shadow-md">
            <Radio className="w-7 h-7 text-[#D7A85B] animate-pulse" />
          </div>
          <div className="text-left space-y-1">
            <div className="flex items-center space-x-2">
              <span className="px-2.5 py-0.5 rounded-full bg-[#183B2B] text-white text-[10px] font-mono font-bold tracking-wider uppercase">
                SARVAM CONV-AI LIVE
              </span>
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
              <span className="text-xs font-semibold text-emerald-700">Official Agent Connected</span>
            </div>
            <h3 className="text-lg font-extrabold font-kannada text-[#183B2B]">
              {language === 'kn' ? 'ಲೈವ್ ಧ್ವನಿ ಕರೆ: ಕೃಷಿ ಮಿತ್ರನೊಂದಿಗೆ ನೇರವಾಗಿ ಮಾತನಾಡಿ' : 'Live Call: Talk directly with Krishi Mitra'}
            </h3>
            <p className="text-xs text-[#4A5148] font-kannada max-w-xl">
              {language === 'kn'
                ? 'ಯಾವುದೇ ಬಟನ್ ಒತ್ತಿ ಹಿಡಿಯುವ ಅಗತ್ಯವಿಲ್ಲ. ನೈಸರ್ಗಿಕವಾಗಿ ಮಾತನಾಡಿ, ಕೃಷಿ ಮಿತ್ರ ನೇರವಾಗಿ ಧ್ವನಿಯಲ್ಲೇ ಉತ್ತರಿಸುತ್ತದೆ.'
                : 'Full-duplex real-time voice conversation powered by official Sarvam Conv-AI Web SDK.'}
            </p>
          </div>
        </div>

        <button
          onClick={() => setIsLiveCallOpen(true)}
          className="flex-shrink-0 flex items-center space-x-2.5 px-6 py-3.5 rounded-xl bg-[#183B2B] hover:bg-[#23503B] text-white font-bold text-sm font-kannada shadow-md hover:shadow-lg transition-all active:scale-95 group"
        >
          <PhoneCall className="w-4 h-4 text-[#D7A85B] group-hover:rotate-12 transition-transform" />
          <span>{language === 'kn' ? 'ಲೈವ್ ಕರೆ ಪ್ರಾರಂಭಿಸಿ' : 'Start Live Call'}</span>
        </button>
      </div>

      {/* 2. Signature Voice Studio Canvas */}
      <div className="relative rounded-[2.5rem] bg-[#183B2B] text-white p-8 sm:p-12 lg:p-16 border border-[#23503B] shadow-dossier overflow-hidden flex flex-col items-center justify-center text-center min-h-[460px]">

        {/* Ambient Studio Lighting Glow */}
        <div className={`absolute inset-0 transition-opacity duration-700 pointer-events-none ${studioState === 'LISTENING'
            ? 'bg-[#C66F4E]/20 opacity-100'
            : studioState === 'RESPONDING'
              ? 'bg-[#D7A85B]/20 opacity-100'
              : 'bg-[#23503B]/30 opacity-60'
          }`} />

        {/* State Indicator Pill */}
        <div className="relative z-10 mb-6">
          <div className="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-[#10261C] border border-[#23503B] text-xs font-mono tracking-wider uppercase text-white shadow-sm">
            {studioState === 'LISTENING' && (
              <>
                <span className="w-2.5 h-2.5 rounded-full bg-[#C66F4E] animate-ping" />
                <span className="text-[#C66F4E] font-bold">
                  {language === 'kn' ? `ಕೇಳಿಸಿಕೊಳ್ಳುತ್ತಿದ್ದೇವೆ (${formatSeconds(recordingSeconds)})` : `Listening (${formatSeconds(recordingSeconds)})`}
                </span>
              </>
            )}
            {studioState === 'PROCESSING' && (
              <>
                <Loader2 className="w-3.5 h-3.5 text-[#D7A85B] animate-spin" />
                <span className="text-[#D7A85B] font-bold">
                  {language === 'kn' ? 'ತಿಳಿದುಕೊಳ್ಳಲಾಗುತ್ತಿದೆ...' : 'Processing Vernacular Speech...'}
                </span>
              </>
            )}
            {studioState === 'TRANSCRIBED' && (
              <>
                <Check className="w-3.5 h-3.5 text-emerald-400" />
                <span className="text-emerald-400 font-bold">
                  {language === 'kn' ? 'ಧ್ವನಿ ಗುರುತಿಸಲಾಗಿದೆ' : 'Speech Transcribed'}
                </span>
              </>
            )}
            {studioState === 'RESPONDING' && (
              <>
                <Volume2 className="w-3.5 h-3.5 text-[#D7A85B] animate-bounce" />
                <span className="text-[#D7A85B] font-bold">
                  {language === 'kn' ? 'ಕೃಷಿ ಮಿತ್ರ ಮಾತನಾಡುತ್ತಿದೆ' : 'Krishi Mitra Speaking'}
                </span>
              </>
            )}
            {studioState === 'IDLE' && (
              <>
                <Sparkles className="w-3.5 h-3.5 text-[#D7A85B]" />
                <span className="text-[#EBE5D8] font-bold">{voiceProvider === 'sarvam-live' ? 'Sarvam Saaras Voice ASR Ready' : 'Voice Studio Ready'}</span>
              </>
            )}
            {studioState === 'ERROR' && (
              <>
                <AlertCircle className="w-3.5 h-3.5 text-[#C66F4E]" />
                <span className="text-[#C66F4E] font-bold">Microphone Notice</span>
              </>
            )}
          </div>
        </div>

        {/* The Central Iconic Microphone Orb */}
        <div className="relative z-10 my-4 flex flex-col items-center">

          {/* Animated sound ripple rings while recording */}
          {studioState === 'LISTENING' && (
            <>
              <div className="absolute -inset-8 rounded-full border-2 border-[#C66F4E]/50 animate-ping pointer-events-none" />
              <div className="absolute -inset-16 rounded-full border border-[#C66F4E]/30 animate-pulse pointer-events-none" />
            </>
          )}

          {/* Active Audio Waveform bars while listening */}
          {studioState === 'LISTENING' && (
            <div className="flex items-center justify-center space-x-1.5 h-12 mb-4">
              <span className="w-2 h-10 bg-[#C66F4E] rounded-full animate-voice-bar-1" />
              <span className="w-2 h-12 bg-[#C66F4E] rounded-full animate-voice-bar-2" />
              <span className="w-2 h-14 bg-[#D7A85B] rounded-full animate-voice-bar-3" />
              <span className="w-2 h-12 bg-[#C66F4E] rounded-full animate-voice-bar-4" />
              <span className="w-2 h-8 bg-[#C66F4E] rounded-full animate-voice-bar-5" />
            </div>
          )}

          {/* Main Action Microphone Control */}
          <button
            onClick={handleMicToggle}
            disabled={isProcessing || isLoading || isSubmitting}
            className={`w-28 h-28 sm:w-32 sm:h-32 rounded-full flex flex-col items-center justify-center shadow-2xl transition-all transform active:scale-95 focus:outline-none ${studioState === 'LISTENING'
                ? 'bg-[#C66F4E] hover:bg-[#9E4E30] text-white ring-8 ring-[#C66F4E]/30'
                : studioState === 'PROCESSING'
                  ? 'bg-[#10261C] border-2 border-[#D7A85B] text-[#D7A85B] cursor-wait'
                  : 'bg-[#D7A85B] hover:bg-[#B08233] text-[#183B2B] hover:shadow-2xl'
              }`}
            aria-label={isRecording ? t.stopSpeaking : t.startSpeaking}
          >
            {studioState === 'PROCESSING' ? (
              <Loader2 className="w-12 h-12 animate-spin text-[#D7A85B]" />
            ) : studioState === 'LISTENING' ? (
              <Square className="w-10 h-10 fill-current text-white" />
            ) : (
              <Mic className="w-12 h-12 text-[#183B2B]" />
            )}
          </button>

          {/* Guidance Caption with 100% Crisp Contrast */}
          <p className="mt-5 text-sm sm:text-base font-kannada text-[#FAF7F0] max-w-md font-medium">
            {studioState === 'LISTENING'
              ? (language === 'kn' ? 'ನಿಮ್ಮ ಬೆಳೆ ಮತ್ತು ಜಮೀನಿನ ಬಗ್ಗೆ ಮಾತನಾಡಿ, ಮುಗಿದ ನಂತರ ನಿಲ್ಲಿಸಿ ಒತ್ತಿ...' : 'Speak your crops, acreage, and location. Tap to stop...')
              : studioState === 'PROCESSING'
                ? (language === 'kn' ? 'ನಿಮ್ಮ ಕನ್ನಡ ಸಂಭಾಷಣೆಯನ್ನು ಅರ್ಥೈಸಲಾಗುತ್ತಿದೆ...' : 'Interpreting your voice query...')
                : (language === 'kn' ? 'ಧ್ವನಿ ಸಂಭಾಷಣೆ ಪ್ರಾರಂಭಿಸಲು ಮೈಕ್ರೋಫೋನ್ ಒತ್ತಿ' : 'Tap the microphone to speak naturally in Kannada or English')}
          </p>
        </div>

        {/* Error Notification */}
        {recorderError && (
          <div className="relative z-10 mt-4 max-w-md p-3.5 rounded-xl bg-terracotta/20 border border-terracotta/50 text-xs text-ivory text-left flex items-start space-x-2">
            <AlertCircle className="w-4 h-4 text-terracotta flex-shrink-0 mt-0.5" />
            <div className="flex-1">
              <p className="font-semibold text-terracotta-light">Microphone Notice</p>
              <p className="text-[11px] text-ivory/80">{recorderError}</p>
            </div>
            <button
              onClick={() => cancelRecording()}
              className="text-xs text-sage hover:text-white underline"
            >
              Dismiss
            </button>
          </div>
        )}

        {/* 3. Transcribed Review & Edit Box (State: TRANSCRIBED) */}
        {editableTranscript && studioState !== 'LISTENING' && (
          <div className="relative z-10 w-full max-w-xl mt-6 p-4 rounded-2xl bg-[#10261C] border border-[#A8B58A]/30 text-left space-y-3 shadow-xl">
            <div className="flex items-center justify-between text-xs text-sage">
              <span className="font-semibold font-kannada flex items-center space-x-1.5 text-harvest">
                <Check className="w-3.5 h-3.5" />
                <span>{language === 'kn' ? 'ಗುರುತಿಸಲಾದ ಮಾತು (ಪರಿಶೀಲಿಸಿ ಅಥವಾ ತಿದ್ದಿ):' : 'Recognized Voice (Review or Edit):'}</span>
              </span>
              <button
                onClick={() => setIsEditingTranscript(!isEditingTranscript)}
                className="inline-flex items-center space-x-1 text-xs text-sage hover:text-white"
              >
                <Edit3 className="w-3.5 h-3.5 stroke-[2]" />
                <span>{isEditingTranscript ? 'Done' : 'Edit'}</span>
              </button>
            </div>

            <textarea
              value={editableTranscript}
              onChange={(e) => setEditableTranscript(e.target.value)}
              rows={2}
              className="w-full bg-[#183B2B] text-ivory text-sm font-kannada p-3 rounded-xl border border-[#23503B] focus:outline-none focus:border-harvest transition-colors resize-none"
            />

            <div className="flex items-center justify-end space-x-3 pt-1">
              <button
                onClick={() => {
                  setEditableTranscript('');
                  cancelRecording();
                }}
                className="text-xs text-sage hover:text-white px-3 py-1.5"
              >
                {language === 'kn' ? 'ರದ್ದುಮಾಡಿ' : 'Cancel'}
              </button>
              <button
                onClick={() => handleConfirmAndSend(editableTranscript)}
                disabled={isSubmitting || !editableTranscript.trim()}
                className="flex items-center space-x-2 px-5 py-2 rounded-xl bg-harvest hover:bg-[#B08233] text-forest-950 font-bold text-xs font-kannada transition-all shadow-sm active:scale-95 disabled:opacity-50"
              >
                <span>{language === 'kn' ? 'ಪ್ರಶ್ನೆ ಸಲ್ಲಿಸಿ' : 'Confirm & Ask'}</span>
                <Send className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        )}

        {/* 4. Responding & Audio Playback Active Banner */}
        {latestAssistantMessage && studioState === 'RESPONDING' && (
          <div className="relative z-10 w-full max-w-xl mt-6 p-4 rounded-2xl bg-forest-950/90 border border-harvest/40 text-left space-y-2">
            <div className="flex items-center justify-between text-xs text-harvest">
              <span className="font-semibold font-kannada flex items-center space-x-1.5">
                <Volume2 className="w-4 h-4 text-harvest animate-pulse" />
                <span>{language === 'kn' ? 'ಧ್ವನಿ ಪ್ರತಿಕ್ರಿಯೆ ಕೇಳಿ:' : 'Listening to Assistant Response:'}</span>
              </span>
              <button
                onClick={onStopAudio}
                className="inline-flex items-center space-x-1 text-xs text-terracotta hover:underline font-mono"
              >
                <VolumeX className="w-3.5 h-3.5" />
                <span>Stop</span>
              </button>
            </div>
            <p className="text-xs text-ivory font-kannada line-clamp-2">
              {latestAssistantMessage.content_kn || latestAssistantMessage.content}
            </p>
          </div>
        )}

      </div>

      {/* 3. Text Fallback Input Bar */}
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleConfirmAndSend(textInput);
        }}
        className="flex items-center space-x-2 p-2 rounded-2xl bg-white border border-ivory-border shadow-sm"
      >
        <input
          type="text"
          value={textInput}
          onChange={(e) => setTextInput(e.target.value)}
          placeholder={t.typeMessagePlaceholder}
          disabled={isLoading || isSubmitting}
          className="flex-1 bg-transparent px-4 py-2.5 text-sm font-kannada text-charcoal placeholder:text-charcoal-muted focus:outline-none"
        />
        <button
          type="submit"
          disabled={!textInput.trim() || isLoading || isSubmitting}
          className="flex items-center space-x-1.5 px-5 py-2.5 rounded-xl bg-forest hover:bg-forest-700 text-ivory text-xs font-bold font-kannada transition-all disabled:opacity-40"
        >
          {isSubmitting || isLoading ? (
            <Loader2 className="w-4 h-4 animate-spin" />
          ) : (
            <>
              <span>{t.send}</span>
              <Send className="w-3.5 h-3.5" />
            </>
          )}
        </button>
      </form>

      {/* 4. Collapsible Conversation Timeline & Audio Replay */}
      {messages.length > 0 && (
        <div className="rounded-2xl bg-white border border-ivory-border shadow-sm overflow-hidden">
          <button
            onClick={() => setShowHistory(!showHistory)}
            className="w-full px-5 py-3.5 flex items-center justify-between text-xs font-semibold text-charcoal hover:bg-ivory/50 transition-colors select-none"
          >
            <div className="flex items-center space-x-2">
              <History className="w-4 h-4 text-forest" />
              <span className="font-kannada">
                {language === 'kn'
                  ? `ಸಂಭಾಷಣಾ ಇತಿಹಾಸ (${messages.length} ಸಂದೇಶಗಳು)`
                  : `Conversation Timeline (${messages.length} messages)`}
              </span>
            </div>
            {showHistory ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
          </button>

          {showHistory && (
            <div className="px-5 pb-5 pt-2 border-t border-ivory-border space-y-4 max-h-96 overflow-y-auto">
              {messages.map((msg) => (
                <div
                  key={msg.id}
                  className={`flex flex-col ${msg.role === 'user' ? 'items-end' : 'items-start'
                    }`}
                >
                  <div
                    className={`max-w-xl p-4 rounded-2xl text-xs font-kannada ${msg.role === 'user'
                        ? 'bg-forest text-ivory rounded-br-none'
                        : 'bg-ivory text-charcoal border border-ivory-border rounded-bl-none'
                      }`}
                  >
                    <p className="leading-relaxed">
                      {language === 'kn' ? (msg.content_kn || msg.content) : (msg.content_en || msg.content)}
                    </p>

                    <div className="mt-2 flex items-center justify-between text-[10px] text-charcoal-muted pt-1 border-t border-black/5">
                      <span>{msg.created_at}</span>
                      {msg.role === 'assistant' && (
                        <button
                          onClick={() => onPlayAudio(msg.content_kn || msg.content, msg.audio_base64)}
                          className="flex items-center space-x-1 text-forest hover:text-harvest font-semibold"
                        >
                          <Volume2 className="w-3.5 h-3.5 stroke-[2]" />
                          <span>{language === 'kn' ? 'ಧ್ವನಿ ಕೇಳಿ' : 'Listen'}</span>
                        </button>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Sarvam AI Live Voice Conversation Modal */}
      <SarvamLiveVoiceModal
        isOpen={isLiveCallOpen}
        onClose={() => setIsLiveCallOpen(false)}
        profile={profile}
        language={language}
      />

    </div>
  );
};

