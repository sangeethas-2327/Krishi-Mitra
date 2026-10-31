import {
  ChatResponse,
  FarmerProfile,
  SchemeRecord,
  SchemeMatchResult,
  SchemeComparisonResponse,
  SchemeReadinessChecklist,
  FarmWeatherResponse,
  MandiPricesResponse
} from '../types';

const API_BASE = import.meta.env.VITE_API_BASE_URL || '';

export const api = {
  async getHealth() {
    const res = await fetch(`${API_BASE}/api/health`);
    if (!res.ok) throw new Error('Health check failed');
    return res.json();
  },

  async sendMessage(
    sessionId: string,
    message: string,
    language: string = 'kn',
    correctedFields?: Record<string, any>
  ): Promise<ChatResponse> {
    const res = await fetch(`${API_BASE}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        session_id: sessionId,
        message,
        language,
        corrected_fields: correctedFields
      })
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || 'Failed to send message');
    }
    return res.json();
  },

  async transcribeAudio(audioBlob: Blob): Promise<{ transcript: string; confidence: number; provider_metadata: any }> {
    const ext = audioBlob.type.includes('webm') ? 'webm' : audioBlob.type.includes('ogg') ? 'ogg' : 'wav';
    const filename = `speech_recording.${ext}`;
    const formData = new FormData();
    formData.append('file', audioBlob, filename);

    const res = await fetch(`${API_BASE}/api/voice/transcribe`, {
      method: 'POST',
      body: formData
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || 'Audio transcription failed');
    }
    return res.json();
  },

  async synthesizeSpeech(text: string, language: string = 'kn'): Promise<{ audio_base64?: string; provider: string }> {
    const res = await fetch(`${API_BASE}/api/voice/synthesize`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, language })
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || 'Speech synthesis failed');
    }
    return res.json();
  },

  async getSchemes(category?: string): Promise<SchemeRecord[]> {
    const url = category && category !== 'all'
      ? `${API_BASE}/api/schemes?category=${encodeURIComponent(category)}`
      : `${API_BASE}/api/schemes`;
    const res = await fetch(url);
    if (!res.ok) throw new Error('Failed to load schemes');
    return res.json();
  },

  async getSchemeDetail(schemeId: string): Promise<SchemeRecord> {
    const res = await fetch(`${API_BASE}/api/schemes/${encodeURIComponent(schemeId)}`);
    if (!res.ok) throw new Error(`Failed to load scheme details for ${schemeId}`);
    return res.json();
  },

  async matchSchemes(profile: FarmerProfile, category?: string): Promise<SchemeMatchResult[]> {
    const url = category && category !== 'all'
      ? `${API_BASE}/api/schemes/match?category=${encodeURIComponent(category)}`
      : `${API_BASE}/api/schemes/match`;
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(profile)
    });
    if (!res.ok) throw new Error('Failed to evaluate schemes');
    return res.json();
  },

  async compareSchemes(schemeIds: string[]): Promise<SchemeComparisonResponse> {
    const res = await fetch(`${API_BASE}/api/schemes/compare`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(schemeIds)
    });
    if (!res.ok) throw new Error('Failed to compare schemes');
    return res.json();
  },

  async getSchemeChecklist(schemeId: string, sessionId?: string): Promise<SchemeReadinessChecklist> {
    const url = sessionId
      ? `${API_BASE}/api/schemes/${encodeURIComponent(schemeId)}/checklist?session_id=${encodeURIComponent(sessionId)}`
      : `${API_BASE}/api/schemes/${encodeURIComponent(schemeId)}/checklist`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Failed to load readiness checklist for ${schemeId}`);
    return res.json();
  },

  async updateFarmerProfile(sessionId: string, updates: Partial<FarmerProfile>): Promise<FarmerProfile> {
    const res = await fetch(`${API_BASE}/api/farmer/profile?session_id=${encodeURIComponent(sessionId)}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(updates)
    });
    if (!res.ok) throw new Error('Failed to update profile');
    return res.json();
  },

  async getWeather(params?: {
    village?: string | null;
    taluk?: string | null;
    district?: string | null;
    state?: string | null;
    lat?: number | null;
    lon?: number | null;
    crops?: string[];
    refresh?: boolean;
  }): Promise<FarmWeatherResponse> {
    const q = new URLSearchParams();
    if (params?.village) q.set('village', params.village);
    if (params?.taluk) q.set('taluk', params.taluk);
    if (params?.district) q.set('district', params.district);
    if (params?.state) q.set('state', params.state);
    if (params?.lat) q.set('lat', params.lat.toString());
    if (params?.lon) q.set('lon', params.lon.toString());
    if (params?.crops && params.crops.length > 0) q.set('crops', params.crops.join(','));
    if (params?.refresh) q.set('refresh', 'true');

    const res = await fetch(`${API_BASE}/api/weather?${q.toString()}`);
    if (!res.ok) throw new Error('Failed to fetch farm weather');
    return res.json();
  },

  async resetSession(sessionId: string): Promise<void> {
    const res = await fetch(`${API_BASE}/api/session/reset`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_id: sessionId })
    });
    if (!res.ok) throw new Error('Failed to reset session');
  },

  async getMandiPrices(params?: {
    district?: string | null;
    commodity?: string | null;
    market?: string | null;
  }): Promise<MandiPricesResponse> {
    const q = new URLSearchParams();
    if (params?.district && params.district !== 'all') q.set('district', params.district);
    if (params?.commodity && params.commodity !== 'all') q.set('commodity', params.commodity);
    if (params?.market && params.market !== 'all') q.set('market', params.market);

    const res = await fetch(`${API_BASE}/api/mandi?${q.toString()}`);
    if (!res.ok) throw new Error('Failed to fetch APMC mandi prices');
    return res.json();
  },

  async getMandiCommodities(): Promise<Array<{ name_en: string; name_kn: string }>> {
    const res = await fetch(`${API_BASE}/api/mandi/commodities`);
    if (!res.ok) throw new Error('Failed to fetch mandi commodities');
    return res.json();
  },

  async getMandiMarkets(): Promise<Array<{ market: string; market_kn: string; district: string; district_kn: string }>> {
    const res = await fetch(`${API_BASE}/api/mandi/markets`);
    if (!res.ok) throw new Error('Failed to fetch mandi markets');
    return res.json();
  }
};
