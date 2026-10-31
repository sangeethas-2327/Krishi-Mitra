import { useState, useRef, useCallback, useEffect } from 'react';
import {
  ConversationAgent,
  BrowserAudioInterface,
  InteractionType,
  AgentState,
  type ServerTextMsgType,
  type ServerTextChunkMsg,
  type ServerTranscriptMsg,
  type ServerEventBase,
  type AudioLevel
} from 'sarvam-conv-ai-sdk/browser';
import { FarmerProfile } from '../types';

export interface SarvamConversationMessage {
  id: string;
  role: 'user' | 'assistant';
  text: string;
  timestamp: string;
}

export interface UseSarvamConversationOptions {
  onSessionEnded?: () => void;
  onTranscriptUpdate?: (text: string) => void;
}

export function useSarvamConversation(options: UseSarvamConversationOptions = {}) {
  const [agentState, setAgentState] = useState<AgentState>(AgentState.IDLE);
  const [isProcessing, setIsProcessing] = useState<boolean>(false);
  const [isMuted, setIsMuted] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [currentAssistantText, setCurrentAssistantText] = useState<string>('');
  const [currentUserText, setCurrentUserText] = useState<string>('');
  const [conversationHistory, setConversationHistory] = useState<SarvamConversationMessage[]>([]);
  const [audioLevel, setAudioLevel] = useState<number>(0);

  const agentRef = useRef<ConversationAgent | null>(null);
  const audioInterfaceRef = useRef<BrowserAudioInterface | null>(null);
  const assistantBufferRef = useRef<string>('');

  // Clean up on component unmount
  useEffect(() => {
    return () => {
      if (agentRef.current) {
        agentRef.current.stop().catch((err) => console.warn('[Sarvam] Stop error on unmount:', err));
        agentRef.current = null;
      }
    };
  }, []);

  const startConversation = useCallback(
    async (profile: FarmerProfile, language: 'kn' | 'en' = 'kn', customSessionId?: string) => {
      setError(null);
      setCurrentAssistantText('');
      setCurrentUserText('');
      assistantBufferRef.current = '';
      setIsProcessing(false);
      setIsMuted(false);

      // Verify browser microphone support
      if (typeof navigator === 'undefined' || !navigator.mediaDevices?.getUserMedia) {
        setError('ಮೈಕ್ರೊಫೋನ್ ಸೌಲಭ್ಯ ಲಭ್ಯವಿಲ್ಲ (Microphone is not supported in this browser environment).');
        setAgentState(AgentState.ERROR);
        return;
      }

      try {
        setAgentState(AgentState.CONNECTING);

        // Pre-check microphone permission
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        // Close test stream immediately, BrowserAudioInterface will manage capture
        stream.getTracks().forEach((track) => track.stop());

        // Prepare exact farmer variables matching Sarvam agent dashboard configuration
        const farmerVariables: Record<string, any> = {
          // Standard and dashboard variable keys
          Name: profile.additional_details?.farmer_name || 'ರೈತರು (Farmer)',
          name: profile.additional_details?.farmer_name || 'Farmer',
          State: profile.location?.state || 'Karnataka',
          state: profile.location?.state || 'Karnataka',
          District: profile.location?.district || '',
          district: profile.location?.district || '',
          Taluk: profile.location?.taluk || '',
          taluk: profile.location?.taluk || '',
          Village: profile.location?.village || '',
          village: profile.location?.village || '',
          'Land size': profile.land_area?.value_acres
            ? `${profile.land_area.value_acres} acres`
            : profile.land_area?.value
            ? `${profile.land_area.value} ${profile.land_area.unit}`
            : '',
          land_size: profile.land_area?.value_acres || profile.land_area?.value || 0,
          land_unit: profile.land_area?.unit || 'acre',
          Crops: (profile.crops || []).join(', '),
          crops: (profile.crops || []).join(', '),
          Irrigation: profile.irrigation?.source || '',
          irrigation: profile.irrigation?.source || '',
          Ownership: profile.ownership || 'owned',
          ownership: profile.ownership || 'owned',
          'Assistance requirements': (profile.assistance_needs || []).join(', '),
          assistance_requirements: (profile.assistance_needs || []).join(', '),
          assistance_needs: (profile.assistance_needs || []).join(', '),
          // Geographic coordinates for real-time weather & mandi price integration
          Latitude: profile.additional_details?.lat || 12.9716,
          latitude: profile.additional_details?.lat || 12.9716,
          Longitude: profile.additional_details?.lon || 77.5946,
          longitude: profile.additional_details?.lon || 77.5946
        };

        const sessionId = customSessionId || `farmer_${Date.now()}`;

        // Initialize Official Browser Audio Interface directly from Sarvam SDK
        // Preserves the agent's original configured voice and audio stream delivered through SDK
        const audioInterface = new BrowserAudioInterface();
        audioInterfaceRef.current = audioInterface;

        // Sarvam Telephony/CALL interaction streams 8000 Hz 16-bit linear PCM audio chunks (1600 bytes = 100ms)
        // dynamically track the exact sample rate reported by Sarvam to ensure 1.0x speed and natural pitch
        let activeServerSampleRate = 8000;

        const nativeAudioOutput = audioInterface.output.bind(audioInterface);
        audioInterface.output = async (audio: Uint8Array, rate?: number) => {
          // Detect sample rate: if audio chunk is exactly 1600 bytes (800 samples = 100ms at 8kHz) or server reported 8k, use 8000
          const effectiveRate = activeServerSampleRate || (audio.length === 1600 ? 8000 : rate) || 8000;
          return nativeAudioOutput(audio, effectiveRate);
        };

        // Initialize Official Sarvam ConversationAgent with backend proxy
        const agent = new ConversationAgent({
          apiKey: '', // Empty in frontend; injected by backend reverse proxy
          baseUrl: '/api/sarvam/', // Reverse proxy route to https://apps.sarvam.ai/api/app-runtime/
          platform: 'browser',
          audioInterface,
          audioCallback: async (msg: any) => {
            if (msg?.sample_rate) {
              activeServerSampleRate = msg.sample_rate;
            }
          },
          config: {
            org_id: '01a18b2b-1150-71e3-8126-8aa3c8bf858e',
            workspace_id: '01a18b2b-115a-71c3-b2eb-eee0b3e8b254',
            app_id: 'Krishi-Mitr-e47b0654-55e7',
            user_identifier_type: 'custom',
            user_identifier: sessionId,
            interaction_type: InteractionType.CALL,
            input_sample_rate: 16000,
            output_sample_rate: 16000,
            initial_language_name: language === 'kn' ? ('Kannada' as any) : ('English' as any),
            agent_variables: farmerVariables
          },

          // Agent State Callback (IDLE, CONNECTING, CONNECTED, LISTENING, SPEAKING, ERROR)
          stateCallback: (newState: AgentState) => {
            console.log('[Sarvam Agent State]:', newState);
            setAgentState(newState);
            if (newState === AgentState.SPEAKING) {
              setIsProcessing(false);
            }
          },

          // Real-time audio level callback for waveform visualizer
          audioLevelCallback: (level: AudioLevel) => {
            setAudioLevel(level.rms || level.peak || 0);
          },

          // Streaming Text Callback (AI Responses)
          textCallback: async (msg: ServerTextChunkMsg | ServerTextMsgType) => {
            if (msg.text) {
              assistantBufferRef.current += msg.text;
              const fullText = assistantBufferRef.current;
              setCurrentAssistantText(fullText);
              if (options.onTranscriptUpdate) {
                options.onTranscriptUpdate(fullText);
              }
            }
          },

          // Live User & Agent Transcription Callback
          transcriptCallback: async (msg: ServerTranscriptMsg) => {
            if (msg.content) {
              if (msg.role === 'user') {
                setCurrentUserText(msg.content);
                setConversationHistory((prev) => [
                  ...prev,
                  {
                    id: `user_${Date.now()}`,
                    role: 'user',
                    text: msg.content,
                    timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                  }
                ]);
              } else if (msg.role === 'bot') {
                setCurrentAssistantText(msg.content);
                setConversationHistory((prev) => [
                  ...prev,
                  {
                    id: `bot_${Date.now()}`,
                    role: 'assistant',
                    text: msg.content,
                    timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                  }
                ]);
              }
            }
          },

          // Server Events Callback (VAD start/stop, interrupts, tool calls, interaction end)
          eventCallback: async (event: ServerEventBase) => {
            switch (event.type) {
              case 'server.event.user_speech_start':
                setIsProcessing(false);
                // When farmer speaks, commit previous assistant turn if pending
                if (assistantBufferRef.current) {
                  const botText = assistantBufferRef.current;
                  setConversationHistory((prev) => {
                    const last = prev[prev.length - 1];
                    if (!last || last.role !== 'assistant' || last.text !== botText) {
                      return [
                        ...prev,
                        {
                          id: `bot_${Date.now()}`,
                          role: 'assistant',
                          text: botText,
                          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                        }
                      ];
                    }
                    return prev;
                  });
                  assistantBufferRef.current = '';
                }
                break;
              case 'server.event.user_speech_end':
                setIsProcessing(true);
                break;
              case 'server.event.user_interrupt':
                setIsProcessing(false);
                assistantBufferRef.current = '';
                break;
              case 'server.action.interaction_end':
                setIsProcessing(false);
                setAgentState(AgentState.IDLE);
                if (options.onSessionEnded) options.onSessionEnded();
                break;
              default:
                break;
            }
          },

          startCallback: async () => {
            console.log('[Sarvam Conv AI] Connected successfully.');
            setAgentState(AgentState.CONNECTED);
          },

          endCallback: async () => {
            console.log('[Sarvam Conv AI] Session ended.');
            setAgentState(AgentState.IDLE);
            setIsProcessing(false);
            if (options.onSessionEnded) options.onSessionEnded();
          }
        });

        agentRef.current = agent;

        // Start session and await WebSocket connection
        await agent.start();
        const connected = await agent.waitForConnect(15);

        if (!connected) {
          throw new Error(
            'Connection timed out. Please check if your Sarvam API Key is active in backend .env.'
          );
        }
      } catch (err: any) {
        console.error('[Sarvam Error]:', err);
        const rawMsg = String(err?.message || '');
        let errMessage = rawMsg || 'Connection error';

        if (
          rawMsg.includes('402') ||
          rawMsg.toLowerCase().includes('insufficient balance') ||
          rawMsg.toLowerCase().includes('insufficient credits')
        ) {
          errMessage =
            language === 'kn'
              ? 'ಸರ್ವಂ ಖಾತೆಯಲ್ಲಿ ಕ್ರೆಡಿಟ್ ಕೊರತೆಯಿದೆ (402 Insufficient Balance). ದಯವಿಟ್ಟು sarvam.ai ಡ್ಯಾಶ್‌ಬೋರ್ಡ್‌ನಲ್ಲಿ ಬ್ಯಾಲೆನ್ಸ್ ಟಾಪ್-ಅಪ್ ಮಾಡಿ.'
              : 'Sarvam AI Account Notice (402): Insufficient balance/credits. Please top up your account at apps.sarvam.ai to enable live calls.';
        } else if (
          rawMsg.includes('401') ||
          rawMsg.toLowerCase().includes('unauthorized') ||
          rawMsg.toLowerCase().includes('invalid api key')
        ) {
          errMessage =
            language === 'kn'
              ? 'ಸರ್ವಂ ಎಪಿಐ ಕೀ ದೃಢೀಕರಣ ವಿಫಲವಾಗಿದೆ (401 Unauthorized). ದಯವಿಟ್ಟು backend/.env ನಲ್ಲಿ SARVAM_API_KEY ಪರಿಶೀಲಿಸಿ.'
              : 'Sarvam AI Authentication Failed (401): Please verify your SARVAM_API_KEY in backend/.env.';
        } else if (
          rawMsg.toLowerCase().includes('permission') ||
          rawMsg.toLowerCase().includes('microphone') ||
          rawMsg.toLowerCase().includes('notallowederror')
        ) {
          errMessage =
            language === 'kn'
              ? 'ಮೈಕ್ರೊಫೋನ್ ಅನುಮತಿ ನಿರಾಕರಿಸಲಾಗಿದೆ. ದಯವಿಟ್ಟು ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಮೈಕ್ ಅನುಮತಿ ನೀಡಿ.'
              : 'Microphone permission was denied. Please allow microphone access in your browser.';
        }

        setError(errMessage);
        setAgentState(AgentState.ERROR);
        if (agentRef.current) {
          await agentRef.current.stop().catch(() => {});
          agentRef.current = null;
        }
      }
    },
    [options]
  );

  const stopConversation = useCallback(async () => {
    try {
      if (agentRef.current) {
        await agentRef.current.stop();
        agentRef.current = null;
      }
      if (audioInterfaceRef.current) {
        audioInterfaceRef.current = null;
      }
      setAgentState(AgentState.IDLE);
      setIsProcessing(false);
      setIsMuted(false);
    } catch (err) {
      console.warn('[Sarvam Stop Notice]:', err);
    }
  }, []);

  const toggleMute = useCallback(() => {
    if (!agentRef.current) return;
    try {
      if (isMuted) {
        (agentRef.current as any).agent?.unmute();
        setIsMuted(false);
      } else {
        (agentRef.current as any).agent?.mute();
        setIsMuted(true);
      }
    } catch (e) {
      console.warn('[Sarvam Mute Toggle Warning]:', e);
    }
  }, [isMuted]);

  return {
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
    isConnected: agentState !== AgentState.IDLE && agentState !== AgentState.ERROR
  };
}

