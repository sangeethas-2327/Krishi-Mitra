# Security and Privacy Architecture — Krishi Mitra

## 1. Principles of Public Trust

Agricultural advisory systems handle sensitive socio-economic data: farmer identities, landholding sizes, bank account linkage statuses, and geographical coordinates. 

Krishi Mitra is designed under **Zero-Trust Public Welfare** principles:
1. **No Personally Identifiable Information (PII) Required to Explore:** Farmers can evaluate scheme eligibility completely anonymously without entering Aadhaar numbers, phone numbers, or bank account credentials.
2. **Backend-Exclusive Secret Management:** All third-party AI keys (`GEMINI_API_KEY`, `SARVAM_API_KEY`) reside exclusively in server-side environment variables and are never bundled into the client browser bundle.
3. **Session Ephemerality:** Profile data is stored in memory scoped to a dynamic `session_id`. Clicking "Clear Session" / `"ಹೊಸ ಅಧಿವೇಶನ"` purges the profile instantly from both client and server memory.

---

## 2. API Security Controls

### 2.1 Credential Secrecy
* `/api/health` and `/healthz` endpoints return operational status flags (`demo_mode: true`, `llm_provider: "gemini-live"`) without exposing raw key characters or environment paths.
* Secret validation scripts mask keys using `mask_key()` (`k[:4]...k[-4:]`).

### 2.2 Upload Restrictions & DoS Protection
* Audio file uploads to `/api/voice/transcribe` enforce a hard ceiling of **15 MB** (`MAX_AUDIO_UPLOAD_SIZE_MB`). Larger payloads are rejected immediately with `HTTP 400 / 413`.
* File headers are inspected for valid audio MIME types (`audio/wav`, `audio/webm`, `audio/ogg`, `audio/mpeg`, `audio/mp4`, `audio/flac`). Arbitrary executables or script uploads trigger an instant `HTTP 400 Unsupported audio format` exception.

### 2.3 CORS & Host Defense
* FastAPI `CORSMiddleware` is configured to whitelist authorized client domains:
  * Local: `http://localhost:5173`, `http://127.0.0.1:5173`, `http://localhost:3000`.
  * Production: Configurable via `CORS_ORIGINS` environment variable (e.g. `https://krishi-mitra.vercel.app`), preventing unauthorized cross-origin scraping.

---

## 3. Grounding & Anti-Hallucination Safeguards

* **No System Prompt Leakage:** Prompts do not leak internal system credentials or private instructions.
* **Deterministic Containment:** The prompt provided to Gemini contains the *already-computed* JSON eligibility verdict. Gemini is instructed via system prompt to translate and explain the facts, but is forbidden from altering the suitability status.

---

## 4. Production Hardening Checklist

- [x] HTTPS enforced on production deployment (Vercel & Render).
- [x] Docker container runs as non-root user (`appuser`).
- [x] All API dependencies pinned and audited.
- [x] CORS origins restricted to approved frontends.
- [x] No credentials checked into Git.

