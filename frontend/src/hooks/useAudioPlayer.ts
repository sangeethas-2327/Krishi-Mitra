import { useState, useRef, useCallback } from 'react';
import { api } from '../services/api';

export function useAudioPlayer() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [currentText, setCurrentText] = useState<string>('');
  const audioRef = useRef<HTMLAudioElement | null>(null);

  const stop = useCallback(() => {
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
      audioRef.current = null;
    }
    setIsPlaying(false);
    setIsPaused(false);
  }, []);

  const pause = useCallback(() => {
    if (audioRef.current && isPlaying) {
      audioRef.current.pause();
      setIsPaused(true);
      setIsPlaying(false);
    }
  }, [isPlaying]);

  const resume = useCallback(() => {
    if (audioRef.current && isPaused) {
      audioRef.current.play().catch(() => {});
      setIsPaused(false);
      setIsPlaying(true);
    }
  }, [isPaused]);

  const playText = useCallback(async (text: string, language: string = 'kn', existingAudioBase64?: string) => {
    stop();
    setIsPlaying(true);
    setIsPaused(false);
    setCurrentText(text);

    const onAudioEnd = () => {
      setIsPlaying(false);
      setIsPaused(false);
    };

    try {
      let audioUri = existingAudioBase64;

      if (!audioUri) {
        // Synthesize on-demand from backend using existing Sarvam Bulbul TTS
        const res = await api.synthesizeSpeech(text, language);
        audioUri = res.audio_base64;
      }

      if (audioUri && !audioUri.includes('demo_harmonic')) {
        const audio = new Audio(audioUri);
        audioRef.current = audio;

        audio.onended = onAudioEnd;
        audio.onerror = () => {
          setIsPlaying(false);
          setIsPaused(false);
        };

        await audio.play().catch((e) => {
          console.warn('[AudioPlayer] Playback notice:', e);
          setIsPlaying(false);
          setIsPaused(false);
        });
      } else {
        // No browser speech synthesis fallback; keep playback state clean
        setIsPlaying(false);
        setIsPaused(false);
      }
    } catch (err) {
      console.warn('[AudioPlayer] Synthesis notice:', err);
      setIsPlaying(false);
      setIsPaused(false);
    }
  }, [stop]);

  return {
    isPlaying,
    isPaused,
    currentText,
    playText,
    pause,
    resume,
    stop
  };
}
