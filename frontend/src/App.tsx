import React, { useState, useEffect, useCallback } from 'react';
import { Navbar, NavTab } from './components/layout/Navbar';
import { DiscoverView } from './components/views/DiscoverView';
import { VoiceStudioView } from './components/views/VoiceStudioView';
import { MyFarmView } from './components/views/MyFarmView';
import { SchemeIntelligenceView } from './components/views/SchemeIntelligenceView';
import { ApplicationJourneyView } from './components/views/ApplicationJourneyView';
import { TrustBanner } from './components/common/TrustBanner';
import { useAudioPlayer } from './hooks/useAudioPlayer';
import { api } from './services/api';
import { FarmerProfile, ChatMessage, SchemeMatchResult } from './types';
import { translations } from './utils/translations';
import { WifiOff } from 'lucide-react';

const createInitialProfile = (): FarmerProfile => ({
  location: { state: 'Karnataka', district: null, taluk: null, village: null },
  land_area: { value: null, unit: 'acre', value_acres: null },
  crops: [],
  ownership: null,
  season: 'kharif',
  irrigation: { has_irrigation: null, source: null, type: null },
  assistance_needs: [],
  additional_details: {},
  field_confidence: {},
  confirmed_fields: [],
  unknown_fields: [
    'location.district',
    'land_area.value_acres',
    'crops',
    'ownership',
    'assistance_needs'
  ],
  conflict_fields: {},
  fields_metadata: {}
});

export const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<NavTab>('discover');
  const [language, setLanguage] = useState<'kn' | 'en'>('kn');
  const [sessionId, setSessionId] = useState<string>(() => `session_${Date.now()}`);
  const [isDemoMode, setIsDemoMode] = useState<boolean>(true);
  const [llmProvider, setLlmProvider] = useState<string>('demo-deterministic');
  const [geminiModel, setGeminiModel] = useState<string>('gemini-2.5-flash');
  const [voiceProvider, setVoiceProvider] = useState<string>('demo-synthetic');
  const [backendStatus, setBackendStatus] = useState<'checking' | 'connected' | 'disconnected'>('checking');
  const [profile, setProfile] = useState<FarmerProfile>(createInitialProfile);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [recommendations, setRecommendations] = useState<SchemeMatchResult[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [selectedJourneyScheme, setSelectedJourneyScheme] = useState<SchemeMatchResult | null>(null);

  const { isPlaying, playText, stop } = useAudioPlayer();
  const t = translations[language];

  // Check backend health & initial scheme list
  const initializeApp = useCallback(async () => {
    try {
      const health = await api.getHealth();
      setBackendStatus('connected');
      setIsDemoMode(Boolean(health.demo_mode));
      if (health.llm_provider) setLlmProvider(health.llm_provider);
      if (health.gemini_model) setGeminiModel(health.gemini_model);
      if (health.voice_provider) setVoiceProvider(health.voice_provider);

      // Fetch initial scheme recommendations based on profile
      const matched = await api.matchSchemes(profile);
      setRecommendations(matched);
    } catch (err) {
      console.warn('Backend connection notice:', err);
      setBackendStatus('disconnected');
    }
  }, [profile]);

  useEffect(() => {
    initializeApp();
  }, []);

  // Initial welcome message
  useEffect(() => {
    if (messages.length === 0) {
      const welcomeKn = 'ನಮಸ್ಕಾರ! ನಾನು ಕೃಷಿ ಮಿತ್ರ. ನಿಮಗೆ ಸೂಕ್ತವಾದ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಲು ನಿಮ್ಮ ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ, ಬೆಳೆ ಮತ್ತು ಅಗತ್ಯವಿರುವ ನೆರವಿನ ಬಗ್ಗೆ ತಿಳಿಸಿ.';
      const welcomeEn = 'Welcome! I am Krishi Mitra. Tell me about your land size, crops, and assistance needs so I can match you with government agricultural schemes.';

      setMessages([
        {
          id: 'welcome-1',
          role: 'assistant',
          content: language === 'kn' ? welcomeKn : welcomeEn,
          content_kn: welcomeKn,
          content_en: welcomeEn,
          created_at: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }
      ]);
    }
  }, [language, messages.length]);

  const handleToggleLanguage = () => {
    setLanguage((prev) => (prev === 'kn' ? 'en' : 'kn'));
  };

  const handleResetSession = async () => {
    stop();
    try {
      await api.resetSession(sessionId);
    } catch (e) {
      console.warn('Reset session notice:', e);
    }
    const newSessionId = `session_${Date.now()}`;
    setSessionId(newSessionId);
    const newProfile = createInitialProfile();
    setProfile(newProfile);
    setMessages([]);

    try {
      const matched = await api.matchSchemes(newProfile);
      setRecommendations(matched);
    } catch (e) {
      console.warn('Could not refresh schemes on reset:', e);
    }
  };

  const handleSendMessage = async (text: string) => {
    if (!text.trim() || isLoading) return;

    const userMessage: ChatMessage = {
      id: `user_${Date.now()}`,
      role: 'user',
      content: text,
      created_at: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const res = await api.sendMessage(sessionId, text, language);

      if (res.updated_profile) {
        setProfile(res.updated_profile);
      }

      if (res.recommendations && res.recommendations.length > 0) {
        setRecommendations(res.recommendations);
      }

      if (res.llm_provider) {
        setLlmProvider(res.llm_provider);
      }

      const botReply: ChatMessage = {
        id: `bot_${Date.now()}`,
        role: 'assistant',
        content: language === 'kn' ? (res.response_text_kn || res.response_text) : (res.response_text_en || res.response_text),
        content_kn: res.response_text_kn || res.response_text,
        content_en: res.response_text_en,
        audio_url: res.audio_url,
        audio_base64: res.audio_base64,
        voice_provider: res.voice_provider,
        created_at: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        llm_provider: res.llm_provider
      };

      setMessages((prev) => [...prev, botReply]);

      // Immediate voice response playback for natural dialogue loop
      const speechText = language === 'kn' ? (res.response_text_kn || res.response_text) : (res.response_text_en || res.response_text);
      if (speechText) {
        playText(speechText, language, res.audio_base64);
      }
    } catch (err: any) {
      console.error('Error sending message:', err);
      const errorReply: ChatMessage = {
        id: `bot_err_${Date.now()}`,
        role: 'assistant',
        content: language === 'kn'
          ? 'ಕ್ಷಮಿಸಿ, ಸಂದೇಶ ಸಂಸ್ಕರಣೆಯಲ್ಲಿ ದೋಷ ಕಂಡುಬಂದಿದೆ. ದಯವಿಟ್ಟು ಮತ್ತೊಮ್ಮೆ ಪ್ರಯತ್ನಿಸಿ.'
          : 'Sorry, an error occurred while processing your message. Please try again.',
        created_at: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        isError: true,
        retryText: text
      };
      setMessages((prev) => [...prev, errorReply]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleUpdateProfile = async (updates: Partial<FarmerProfile>) => {
    try {
      const updated = await api.updateFarmerProfile(sessionId, updates);
      setProfile(updated);
      const matched = await api.matchSchemes(updated);
      setRecommendations(matched);
    } catch (err) {
      console.error('Failed to update profile:', err);
    }
  };

  const suitableCount = recommendations.filter(r => r.evaluation_status === 'POTENTIALLY_SUITABLE').length;

  return (
    <div className="min-h-screen bg-[#F5F1E8] text-[#282C27] flex flex-col font-sans selection:bg-[#D7A85B]/30 selection:text-[#183B2B]">
      
      {/* Editorial Navigation Header */}
      <Navbar
        language={language}
        onToggleLanguage={handleToggleLanguage}
        onResetSession={handleResetSession}
        isDemoMode={isDemoMode}
        llmProvider={llmProvider}
        geminiModel={geminiModel}
        activeTab={activeTab}
        onTabChange={(tab) => {
          stop();
          setActiveTab(tab);
        }}
        cropsCount={profile.crops.length}
        landAcres={profile.land_area.value_acres}
        suitableSchemesCount={suitableCount}
        isVoiceActive={isLoading || isPlaying}
      />

      {/* Backend Disconnection Banner */}
      {backendStatus === 'disconnected' && (
        <div className="bg-terracotta text-white px-4 py-2.5 text-center text-xs flex items-center justify-center space-x-2 font-medium shadow-sm">
          <WifiOff className="w-4 h-4" />
          <span>
            {language === 'kn'
              ? 'ಸರ್ವರ್ ಸಂಪರ್ಕ ಹೊಂದಿಲ್ಲ (Backend offline on port 8000). ದಯವಿಟ್ಟು ಸರ್ವರ್ ಚಾಲನೆಯಲ್ಲಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.'
              : 'Backend server is not reachable at http://127.0.0.1:8000. Ensure the FastAPI server is running.'}
          </span>
          <button
            onClick={initializeApp}
            className="underline ml-2 bg-black/20 px-2 py-0.5 rounded text-[11px] hover:bg-black/30"
          >
            Retry
          </button>
        </div>
      )}

      {/* Main Workspace with 5 Distinct Experiences */}
      <main className="flex-1 max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8">
        
        {/* A. DISCOVER EXPERIENCE */}
        {activeTab === 'discover' && (
          <DiscoverView
            language={language}
            onNavigate={(tab) => setActiveTab(tab)}
            onQuickPrompt={(text) => handleSendMessage(text)}
            isDemoMode={isDemoMode}
            suitableSchemesCount={suitableCount}
            profile={profile}
          />
        )}

        {/* B. VOICE STUDIO EXPERIENCE */}
        {activeTab === 'voice' && (
          <VoiceStudioView
            language={language}
            onSendMessage={handleSendMessage}
            isLoading={isLoading}
            voiceProvider={voiceProvider}
            llmProvider={llmProvider}
            profile={profile}
            messages={messages}
            recommendations={recommendations}
            onPlayAudio={(text, audioBase64) => playText(text, language, audioBase64)}
            onStopAudio={stop}
            isPlayingAudio={isPlaying}
            onNavigateToSchemes={() => setActiveTab('schemes')}
            onNavigateToFarm={() => setActiveTab('myfarm')}
          />
        )}

        {/* C. MY FARM EXPERIENCE */}
        {activeTab === 'myfarm' && (
          <MyFarmView
            profile={profile}
            language={language}
            onUpdateProfile={handleUpdateProfile}
            onNavigateToVoice={() => setActiveTab('voice')}
            onNavigateToSchemes={() => setActiveTab('schemes')}
          />
        )}

        {/* D. SCHEME INTELLIGENCE EXPERIENCE */}
        {activeTab === 'schemes' && (
          <SchemeIntelligenceView
            recommendations={recommendations}
            language={language}
            onPlayAudio={(text) => playText(text, language)}
            onStopAudio={stop}
            isPlayingAudio={isPlaying}
            sessionId={sessionId}
            onNavigateToJourney={(scheme) => {
              setSelectedJourneyScheme(scheme);
              setActiveTab('journey');
            }}
          />
        )}

        {/* E. APPLICATION JOURNEY EXPERIENCE */}
        {activeTab === 'journey' && (
          <ApplicationJourneyView
            recommendations={recommendations}
            language={language}
            sessionId={sessionId}
            selectedSchemeTarget={selectedJourneyScheme}
            onNavigateToVoice={() => setActiveTab('voice')}
            onNavigateToSchemes={() => setActiveTab('schemes')}
          />
        )}

        {/* Trust & Provenance Footer */}
        <TrustBanner language={language} />

      </main>

    </div>
  );
};

export default App;
