# Krishi Mitra (ಕೃಷಿ ಮಿತ್ರ) — Project Overview

**Tagline:** Your Voice. Our Support. Government Schemes Made Simple.  
**Target Domain:** Agritech / Public Sector Digital Enablement / Voice-First Conversational AI  
**Primary Language:** Kannada (ಕನ್ನಡ), with bilingual English subtitles & explanations  
**Target Beneficiaries:** Small, marginal, tenant, and women farmers across Karnataka, India  

---

## 1. Executive Summary

**Krishi Mitra (ಕೃಷಿ ಮಿತ್ರ)** is an accessible, voice-first conversational AI and deterministic government scheme advisory platform purpose-built for Kannada-speaking farmers. 

While Indian state and central governments allocate tens of thousands of crores annually to agricultural subsidies, financial support, and crop insurance, **less than 35% of eligible smallholder farmers successfully access these schemes**. The root causes are well-documented:
1. **Linguistic and Digital Literacy Barriers:** Portals are published in complex bureaucratic English or formal Kannada with confusing jargon.
2. **Text-Heavy Web Interfaces:** Portals assume keyboard navigation, mouse interactions, and high digital fluency.
3. **Black-Box AI Hallucinations:** Generic generative AI chatbots frequently invent non-existent scheme rules, hallucinate qualification amounts, or fail to enforce statutory criteria.
4. **Opaque Eligibility Decisions:** Farmers are rarely told *why* they do not qualify or *what specific document* is needed to become eligible.

Krishi Mitra resolves this crisis through a **bimodal hybrid architecture**:
* A **conversational voice frontend** powered by **Sarvam AI (Saaras STT & Bulbul TTS)** and **Google Gemini 2.5 Flash** that listens to spoken Kannada, extracts multi-parameter farmer profiles (crops, land area, ownership, irrigation, district), and asks adaptive follow-up questions.
* An **independent, deterministic Python rule engine** that evaluates scheme eligibility using Boolean logic, mathematical operators, and official scheme criteria. LLMs never make eligibility decisions.

---

## 2. Key Capabilities at a Glance

* **Voice-First Kannada Dialogue:** Full speech-to-text recording, transcript review/correction modal, and synthesized voice audio playback.
* **Dialect & Code-Mixing Resilience:** Handles colloquial Kannada, North/Coastal Karnataka terms, and mixed phrases (e.g., *"3 acre land ide, sugarcane belithini"*).
* **Transparent Profile Extraction:** Shows extracted land size, normalized acre conversions (e.g., Gunta $\rightarrow$ Acre), crops, and ownership with field-level confidence and conflict tracking.
* **Deterministic Scheme Eligibility:** Categorizes schemes into:
  * `POTENTIALLY_SUITABLE`
  * `INSUFFICIENT_INFORMATION` (prompts adaptive questions)
  * `REQUIRES_OFFICIAL_VERIFICATION`
  * `NOT_SUITABLE_BASED_ON_KNOWN_RULES`
* **Real vs. Fictional Scheme Transparency:** Clearly distinguishes statutory schemes (PM-KISAN, PMFBY) from demonstration schemes with verified source links.
* **Side-by-Side Scheme Comparison Matrix:** Allows farmers to compare benefits, mandatory criteria, and required documents.
* **Document Readiness Checklist:** Dynamic progress bar showing what documents the farmer possesses versus what is missing before applying.
* **Offline Demo Resilience:** Fully operational offline fallback heuristics and audio chime generation when cloud API credentials are absent or disconnected.

---

## 3. Project Structure

```
krishi-mitra/
├── backend/
│   ├── app/
│   │   ├── api/             # FastAPI routers (health, chat, voice, schemes, farmer)
│   │   ├── core/            # Logging and security utilities
│   │   ├── data/            # schemes.json and kannada_vocabulary.json
│   │   ├── models/          # Pydantic schemas (farmer, scheme, conversation)
│   │   ├── services/        # Rule engine, Gemini client, Sarvam voice, recommender
│   │   └── config.py        # Environment settings & CORS validation
│   ├── tests/               # 53 pytest test cases (100% pass rate)
│   ├── Dockerfile           # Multi-stage production container
│   ├── Procfile             # PaaS startup definition
│   └── requirements.txt     # Python production dependencies
├── frontend/
│   ├── src/
│   │   ├── components/      # Chat, Voice, Farmer Profile, Schemes, Modals
│   │   ├── hooks/           # useVoiceRecorder, useAudioPlayer
│   │   ├── services/        # API client with VITE_API_BASE_URL
│   │   ├── types/           # Strict TypeScript interfaces
│   │   └── utils/           # Bilingual translations and vocabulary
│   ├── vercel.json          # SPA routing configuration
│   └── package.json         # React 18 + TypeScript + Vite + Tailwind
├── docs/                    # Complete hackathon & technical documentation
├── render.yaml              # Render blueprint infrastructure-as-code
└── smoke_test_cloud_apis.py # API smoke test & credential verification harness
```

