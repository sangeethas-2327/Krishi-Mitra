# Technology Stack — Krishi Mitra

## 1. Complete Technology Matrix

| Layer | Technology | Version | Purpose & Rationale |
| :--- | :--- | :--- | :--- |
| **Frontend Framework** | React | 18.3.1 | Component-based, responsive SPA architecture. |
| **Language & Typings** | TypeScript | 5.7.2 | Strict end-to-end type safety preventing runtime null/undefined errors. |
| **Build Tool & Bundler** | Vite | 6.1.0 / 6.4.5 | Lightning-fast HMR and optimized production code splitting. |
| **Styling & Design System** | Tailwind CSS | 3.4.17 | Custom agricultural palette (`forest-*`, `emerald-*`, `earth-*`). |
| **Iconography** | Lucide React | 0.475.0 | Accessible, modern, consistent vector iconography. |
| **Backend Framework** | FastAPI | 0.110.0+ | High-performance Python async framework with native OpenAPI/Swagger docs. |
| **ASGI Server** | Uvicorn / Gunicorn | 0.28.0+ / 21.2.0 | Production-grade async server and multi-worker process manager. |
| **Schema Validation** | Pydantic & Pydantic-Settings | 2.6.0+ / 2.2.0 | Strict data validation, environment variable parsing, and JSON schemas. |
| **HTTP Client** | HTTPX | 0.27.0+ | Async HTTP client for low-latency calls to Gemini and Sarvam AI APIs. |
| **Generative AI** | Google Gemini 2.5 Flash | 1.0.0+ (`google-genai`) | Official Google Gen AI SDK for structured entity extraction and response generation. |
| **Speech-to-Text (STT)** | Sarvam AI Saaras | `saaras:v2` | State-of-the-art Kannada speech recognition supporting regional accents and code-mixing. |
| **Text-to-Speech (TTS)** | Sarvam AI Bulbul | `bulbul:v1` (`meera`) | Highly natural, expressive Kannada speech synthesis. |
| **Testing Harness** | Pytest & Pytest-Asyncio | 9.2.0 / 1.4.1 | Asynchronous backend test runner with 53 comprehensive unit and integration tests. |
| **Frontend Hosting** | Vercel | Production | Global CDN, automatic edge routing, and instant HTTPS. |
| **Backend Hosting** | Render / Container | Docker / Linux | Managed Python container service with automated health checking and zero downtime. |

---

## 2. Key Package Dependencies

### Backend (`requirements.txt`)
```txt
fastapi>=0.110.0
uvicorn[standard]>=0.28.0
gunicorn>=21.2.0
pydantic>=2.6.0
pydantic-settings>=2.2.0
python-multipart>=0.0.9
httpx>=0.27.0
google-genai>=1.0.0
pytest>=8.0.0
pytest-asyncio>=0.23.0
```

### Frontend (`package.json`)
```json
{
  "dependencies": {
    "clsx": "^2.1.1",
    "lucide-react": "^0.475.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "tailwind-merge": "^2.6.0"
  },
  "devDependencies": {
    "@types/react": "^18.3.18",
    "@types/react-dom": "^18.3.5",
    "@vitejs/plugin-react": "^4.3.4",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.5.1",
    "tailwindcss": "^3.4.17",
    "typescript": "~5.7.2",
    "vite": "^6.1.0"
  }
}
```

---

## 3. Design Tokens & Visual Hierarchy

* **Primary Palette:** `forest-900` (`#1B4332`), `forest-800` (`#2D6A4F`), `forest-700` (`#40916C`), `forest-500` (`#74C69D`).
* **Accent & Feedback:** `emerald-500` (Eligible/Success), `amber-500` (Info Needed), `purple-600` (Needs Official Verification), `red-600` (Not Suitable).
* **Typography:** Kannada-optimized font stack (`Noto Sans Kannada`, `system-ui`, sans-serif) with generous line heights ($1.5 - 1.7$) for maximum legibility of complex conjunct characters (*ottuakshara*).

