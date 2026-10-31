# Production Deployment Guide — Krishi Mitra

This guide provides step-by-step instructions for deploying Krishi Mitra to production using **Render** for the FastAPI backend and **Vercel** for the React + Vite frontend.

---

## 1. Architecture & Deployment Prerequisites

* A **GitHub** repository containing the Krishi Mitra source code.
* A **Render** account (for Python/FastAPI web service).
* A **Vercel** account (for React/TypeScript static frontend).
* Optional AI Credentials:
  * Google Gemini API Key: [Google AI Studio](https://aistudio.google.com/)
  * Sarvam AI API Key: [Sarvam AI Platform](https://dashboard.sarvam.ai/)

---

## 2. Backend Deployment on Render

### Step 2.1: Create Web Service
1. Log in to [Render Dashboard](https://dashboard.render.com/).
2. Click **New +** $\rightarrow$ **Web Service**.
3. Connect your GitHub repository.
4. Configure the service settings:
   * **Name:** `krishi-mitra-backend`
   * **Root Directory:** `backend`
   * **Runtime:** `Python`
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   * **Plan:** Free

### Step 2.2: Configure Environment Variables
In the Render Service Dashboard, navigate to **Environment** and add:

| Key | Recommended Production Value | Note |
| :--- | :--- | :--- |
| `ENVIRONMENT` | `production` | Enables production mode |
| `DEMO_MODE` | `true` | Keeps fallback heuristics active if cloud APIs fail |
| `GEMINI_API_KEY` | *(Your Gemini API Key)* | Optional (Enables live Gemini 2.5 Flash) |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Configurable model identifier |
| `SARVAM_API_KEY` | *(Your Sarvam AI Key)* | Optional (Enables live Saaras STT & Bulbul TTS) |
| `SARVAM_BASE_URL` | `https://api.sarvam.ai` | Official endpoint |
| `SARVAM_STT_MODEL` | `saaras:v2` | Primary Kannada ASR model |
| `SARVAM_TTS_MODEL` | `bulbul:v1` | Primary Kannada TTS model |
| `SARVAM_TTS_SPEAKER` | `meera` | Natural Kannada female voice |
| `CORS_ORIGINS` | `https://krishi-mitra.vercel.app,http://localhost:5173` | Comma-separated allowed frontend origins |
| `MAX_AUDIO_UPLOAD_SIZE_MB` | `15` | Audio upload ceiling |

### Step 2.3: Verify Backend Health
Once deployed, Render provides a public URL (e.g. `https://krishi-mitra-backend.onrender.com`).  
Verify deployment by visiting:
* `https://krishi-mitra-backend.onrender.com/healthz` $\rightarrow$ `{"status": "healthy"}`
* `https://krishi-mitra-backend.onrender.com/api/health` $\rightarrow$ `{"status": "ok", "app": "Krishi Mitra"}`

---

## 3. Frontend Deployment on Vercel

### Step 3.1: Import Project to Vercel
1. Log in to [Vercel Dashboard](https://vercel.com/).
2. Click **Add New...** $\rightarrow$ **Project**.
3. Import your GitHub repository.
4. In Project Settings:
   * **Framework Preset:** `Vite`
   * **Root Directory:** `frontend`
   * **Build Command:** `npm run build` (`tsc && vite build`)
   * **Output Directory:** `dist`

### Step 3.2: Configure Frontend Environment Variables
Add the backend URL to Vercel Environment Variables:

| Key | Value |
| :--- | :--- |
| `VITE_API_BASE_URL` | `https://krishi-mitra-backend.onrender.com` |

*(Note: Replace with your actual Render backend URL without trailing slash).*

### Step 3.3: Deploy & Verify
Click **Deploy**. Vercel will build and assign a domain (e.g., `https://krishi-mitra.vercel.app`).
1. Open the Vercel URL in your browser.
2. Confirm the green Navbar shows connected status.
3. Test a Kannada message or click a QuickStart prompt to confirm frontend-backend connectivity.

---

## 4. One-Click Blueprint Deployment (render.yaml)

Alternatively, Krishi Mitra includes a root `render.yaml` specification. In Render, select **New +** $\rightarrow$ **Blueprint** and point to the repository. Render will automatically configure the web service, build steps, and environment variables.

