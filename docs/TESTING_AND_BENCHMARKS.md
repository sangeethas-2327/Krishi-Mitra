# Testing & Benchmarks — Krishi Mitra

## 1. Testing Methodology

Krishi Mitra employs a comprehensive multi-layered test pyramid:
1. **Unit Tests (Pydantic Schemas, Rule Operators):** Mathematical verification of Boolean logic, normalization, and land unit conversions.
2. **Integration Tests (Service Mocking):** Verification of Gemini structured output parsing and Sarvam STT/TTS API contracts using `unittest.mock.AsyncMock`.
3. **End-to-End Live HTTP Tests (`qa_phase4_e2e_evaluation.py`):** Real HTTP roundtrips against live FastAPI server testing multi-turn context retention, conversational corrections, audio MIME handling, and CORS.
4. **Smoke Test Harness (`smoke_test_cloud_apis.py`):** Live credential detection and cloud API smoke tests distinguishing mock from live calls.

---

## 2. Pytest Test Suite Results

**Execution Command:** `pytest backend/tests/ -v`  
**Test Suite Status:** **53 / 53 passed (100%)**  
**Execution Time:** 3.36 seconds  

### Breakdown by Module:
* `backend/tests/test_api.py` (9 tests): Health endpoint, scheme listing, scheme details, comparison API, checklist generation, chat endpoint, STT/TTS endpoints, profile patch/reset.
* `backend/tests/test_conversation.py` (4 tests): Multi-turn conversation, land unit conversions, explicit conversational corrections, adaptive follow-ups.
* `backend/tests/test_eligibility.py` (5 tests): Relational operators, unknown field handling, PM-KISAN qualification, PM-KISAN tenant failure, synthetic scheme flagging.
* `backend/tests/test_phase2_eligibility_and_schemes.py` (7 tests): Compound OR rules, between operator, offline verification criteria, optional rule evaluation, scheme comparison service, readiness checklists, real vs. fictional scheme separation.
* `backend/tests/test_phase2_profile_and_vocab.py` (7 tests): Multiple crop extraction, Kannada spelling variations, Gunta-to-acre conversions, ambiguous crop (`ಜೋಳ`) detection, taluk/village parsing, irrigation source extraction, conflict tracking.
* `backend/tests/test_phase3a_gemini.py` (9 tests): Missing key handling, invalid key handling, structured output validation, malformed LLM response fallback, confirmed field protection, conversational correction persistence, multiple crop extraction, strict rule engine independence, metadata provenance.
* `backend/tests/test_phase3b_voice.py` (12 tests): Audio upload validation, empty audio rejection, non-audio format rejection, file size limit rejection, WAV transcription, WebM browser format support, mock Sarvam Saaras call, empty TTS rejection, synthetic WAV chime synthesis, mock Sarvam Bulbul call, Kannada agricultural corpus scenarios, multi-turn voice context preservation.

---

## 3. End-to-End HTTP Benchmarks

Measured via live wall-clock HTTP calls in `qa_phase4_e2e_evaluation.py`:

| Test / Endpoint | Target Budget | Measured Latency | Status |
| :--- | :--- | :--- | :--- |
| **`GET /api/health`** | $< 100 \text{ ms}$ | **4.8 ms** | Passed |
| **`POST /api/voice/transcribe` (WAV)** | $< 800 \text{ ms}$ | **1.3 ms** | Passed (Demo Mode) |
| **`POST /api/voice/transcribe` (WebM)** | $< 800 \text{ ms}$ | **1.3 ms** | Passed (Demo Mode) |
| **`POST /api/voice/synthesize` (Bulbul)** | $< 800 \text{ ms}$ | **9.7 ms** | Passed (Demo Mode) |
| **`POST /api/chat` (Turn 1: Extraction & Audio)** | $< 1500 \text{ ms}$ | **11.3 ms** | Passed |
| **`POST /api/chat` (Turn 2: Context Enrichment)** | $< 1500 \text{ ms}$ | **11.1 ms** | Passed |
| **`POST /api/chat` (Turn 3: Correction Pattern)** | $< 1500 \text{ ms}$ | **11.2 ms** | Passed |
| **`POST /api/schemes/compare`** | $< 100 \text{ ms}$ | **2.1 ms** | Passed |
| **`GET /api/schemes/{id}/checklist`** | $< 100 \text{ ms}$ | **1.9 ms** | Passed |

---

## 4. Frontend Production Build Performance

* **Bundler:** Vite v6.4.5 with TypeScript v5.7.2.
* **Build Command:** `tsc && vite build`
* **Build Time:** 2.46 seconds.
* **Output Artifacts:**
  * `dist/index.html`: 1.08 kB (gzip: 0.66 kB)
  * `dist/assets/index-C21rNQ6X.css`: 32.22 kB (gzip: 6.09 kB)
  * `dist/assets/index-8DmNyk3f.js`: 257.20 kB (gzip: 72.65 kB)
* **Optimization:** Zero build warnings, tree-shaken dependencies, CSS purged of unused classes.

