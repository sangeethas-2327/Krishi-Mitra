import React, { useState } from 'react';
import { Mic, Square, Loader2, Send, CheckCircle2, AlertCircle } from 'lucide-react';
import { useVoiceRecorder } from '../../hooks/useVoiceRecorder';
import { translations } from '../../utils/translations';

interface VoiceRecorderPanelProps {
  language: 'kn' | 'en';
  onSendMessage: (text: string) => Promise<void>;
  isLoading: boolean;
  voiceProvider?: string;
}

export const VoiceRecorderPanel: React.FC<VoiceRecorderPanelProps> = ({
  language,
  onSendMessage,
  isLoading,
  voiceProvider
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

  const [textInput, setTextInput] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleMicClick = async () => {
    if (isRecording) {
      const recognized = await stopRecording();
      if (recognized) {
        setTextInput(recognized);
      }
    } else {
      await startRecording();
    }
  };

  const handleSend = async (textToSend: string) => {
    const trimmed = textToSend.trim();
    if (!trimmed || isLoading || isSubmitting) return;

    setIsSubmitting(true);
    try {
      await onSendMessage(trimmed);
      setTextInput('');
      setTranscript('');
    } finally {
      setIsSubmitting(false);
    }
  };

  const formatSeconds = (sec: number) => {
    const mins = Math.floor(sec / 60);
    const secs = sec % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="bg-white rounded-2xl shadow-sm border border-emerald-100 p-5 mb-6 transition-all">
      <div className="flex flex-col items-center justify-center text-center">
        
        {/* Large Accessible Microphone Button */}
        <div className="relative mb-3">
          {/* Animated Pulse Ring during recording */}
          {isRecording && (
            <div className="absolute inset-0 rounded-full bg-red-400 opacity-75 animate-ping" />
          )}

          <button
            onClick={handleMicClick}
            disabled={isProcessing || isLoading || isSubmitting}
            className={`relative z-10 w-24 h-24 rounded-full flex flex-col items-center justify-center shadow-lg transition-all transform active:scale-95 focus:outline-none focus:ring-4 ${
              isRecording
                ? 'bg-red-600 hover:bg-red-700 text-white focus:ring-red-200'
                : isProcessing
                ? 'bg-amber-500 text-white cursor-wait'
                : 'bg-forest-700 hover:bg-forest-800 text-white focus:ring-forest-200 hover:shadow-xl'
            }`}
            aria-label={isRecording ? t.stopSpeaking : t.startSpeaking}
          >
            {isProcessing ? (
              <Loader2 className="w-10 h-10 animate-spin" />
            ) : isRecording ? (
              <Square className="w-9 h-9 fill-current" />
            ) : (
              <Mic className="w-10 h-10" />
            )}
          </button>
        </div>

        {/* State label & Timer */}
        <div className="mb-4">
          <div className="inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[11px] font-medium bg-emerald-50 text-forest-800 border border-emerald-200 mb-2">
            <span>{voiceProvider === 'sarvam-live' ? 'Sarvam Saaras Voice ASR' : (language === 'kn' ? 'ಕನ್ನಡ ಧ್ವನಿ ಸಹಾಯಕ' : 'Kannada Voice Assistant')}</span>
          </div>

          <p className="text-base font-semibold text-ktext-primary">
            {isRecording
              ? `${t.recording} (${formatSeconds(recordingSeconds)})`
              : isProcessing
              ? t.processingAudio
              : t.startSpeaking}
          </p>

          {/* Sound Wave Animation when recording */}
          {isRecording && (
            <div className="flex items-center justify-center space-x-1 my-2">
              <span className="w-1.5 h-4 bg-red-500 rounded-full animate-bounce [animation-delay:-0.3s]" />
              <span className="w-1.5 h-6 bg-red-600 rounded-full animate-bounce [animation-delay:-0.15s]" />
              <span className="w-1.5 h-8 bg-red-700 rounded-full animate-bounce" />
              <span className="w-1.5 h-6 bg-red-600 rounded-full animate-bounce [animation-delay:-0.15s]" />
              <span className="w-1.5 h-4 bg-red-500 rounded-full animate-bounce [animation-delay:-0.3s]" />
            </div>
          )}

          <p className="text-xs text-ktext-muted mt-0.5">
            {language === 'kn'
              ? 'ಕನ್ನಡದಲ್ಲಿ ಮಾತನಾಡಿ (ಉದಾ: "ನನಗೆ ಕೃಷಿಗೆ ಸಹಾಯಧನ ಬೇಕು...")'
              : 'Speak naturally in Kannada or English'}
          </p>
        </div>

        {/* Error notification if mic fails */}
        {recorderError && (
          <div className="w-full max-w-lg mb-3 p-3 bg-red-50 border border-red-200 rounded-xl flex items-center space-x-2 text-xs text-red-700 text-left">
            <AlertCircle className="w-4 h-4 flex-shrink-0" />
            <span>{recorderError}</span>
          </div>
        )}

        {/* Transcript Review Box (if speech was recognized) */}
        {transcript && (
          <div className="w-full max-w-2xl mb-4 bg-emerald-50/70 border border-emerald-200 rounded-xl p-3 text-left">
            <div className="flex items-center justify-between mb-1.5">
              <span className="text-xs font-semibold text-forest-800 flex items-center space-x-1">
                <CheckCircle2 className="w-3.5 h-3.5 text-forest-600" />
                <span>{language === 'kn' ? 'ಗುರುತಿಸಲಾದ ಧ್ವನಿ (ಪರಿಶೀಲಿಸಿ ಅಥವಾ ತಿದ್ದಿ):' : 'Recognized Voice (Review or Edit):'}</span>
              </span>
              <button
                onClick={() => handleSend(transcript)}
                className="text-xs font-medium text-forest-700 hover:text-forest-900 underline"
              >
                {t.send}
              </button>
            </div>
            <textarea
              value={transcript}
              onChange={(e) => setTranscript(e.target.value)}
              rows={2}
              className="w-full text-sm bg-white border border-emerald-300 rounded-lg p-2 text-ktext-primary focus:outline-none focus:ring-2 focus:ring-forest-500 font-kannada"
            />
            <div className="flex justify-end mt-2 space-x-2">
              <button
                onClick={cancelRecording}
                className="text-xs text-gray-500 hover:text-gray-700 px-2 py-1"
              >
                {language === 'kn' ? 'ರದ್ದುಮಾಡಿ' : 'Cancel'}
              </button>
              <button
                onClick={() => handleSend(transcript)}
                disabled={isSubmitting}
                className="text-xs bg-forest-700 hover:bg-forest-800 text-white px-3 py-1.5 rounded-lg flex items-center space-x-1"
              >
                <span>{language === 'kn' ? 'ಪ್ರಶ್ನೆ ಸಲ್ಲಿಸಿ' : 'Submit Voice'}</span>
                <Send className="w-3 h-3" />
              </button>
            </div>
          </div>
        )}

        {/* Text Input Fallback Bar */}
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSend(textInput);
          }}
          className="w-full max-w-2xl flex items-center space-x-2"
        >
          <input
            type="text"
            value={textInput}
            onChange={(e) => setTextInput(e.target.value)}
            placeholder={t.typeMessagePlaceholder}
            disabled={isLoading || isSubmitting}
            className="flex-1 text-sm bg-gray-50 border border-gray-300 rounded-xl px-4 py-2.5 text-ktext-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-forest-600 font-kannada shadow-inner"
          />
          <button
            type="submit"
            disabled={!textInput.trim() || isLoading || isSubmitting}
            className="bg-forest-700 hover:bg-forest-800 disabled:opacity-50 text-white rounded-xl px-5 py-2.5 text-sm font-medium flex items-center space-x-1.5 transition shadow"
          >
            {isSubmitting || isLoading ? (
              <Loader2 className="w-4 h-4 animate-spin" />
            ) : (
              <>
                <span>{t.send}</span>
                <Send className="w-4 h-4" />
              </>
            )}
          </button>
        </form>

      </div>
    </div>
  );
};
