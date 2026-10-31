# Future Scope & Product Roadmap — Krishi Mitra

While Krishi Mitra has proven its core value proposition across Phases 1 through 5, several high-impact expansion pathways are planned for scale across India.

---

## 1. Direct Integration with State Government Land Registries (Bhoomi & FRUITS)

* **Bhoomi API Integration:** In Karnataka, the **Bhoomi** portal digitizes millions of land ownership records (RTC / *Pahani*). Future iterations can support authorized farmer authentication (via OTP or biometric thumbprint) to auto-fetch official survey numbers, land acreage, and crop history directly, eliminating manual data entry.
* **FRUITS Database (Farmer Registration and Unified Beneficiary Information System):** Automated linking with Karnataka's FRUITS ID (FID) to pre-populate farmer profile cards and check previous direct benefit transfers (DBT).

---

## 2. Expansion to Multilingual Pan-Indian Vernaculars

* **Indian Language Extension:** While currently optimized for Kannada (ಕನ್ನಡ), the architecture is decoupled from language. Using Sarvam AI's multi-lingual models, Krishi Mitra can easily extend to:
  * Telugu (తెలుగు) — Andhra Pradesh & Telangana
  * Tamil (தமிழ்) — Tamil Nadu
  * Marathi (मराठी) — Maharashtra
  * Hindi (हिन्दी) — Northern agricultural belt
* **Hyperlocal Dialect Adaptation:** Expanding dialect coverage for *Uttara Karnataka*, *Kalyana Karnataka*, *Malenadu*, and *Tulu-mixed* agricultural idioms.

---

## 3. WhatsApp & Telegram Voice Bot Interfaces

* **Headless Conversational Access:** Deploying Krishi Mitra as an interactive WhatsApp audio bot using the Meta WhatsApp Cloud API.
* **Farmer Experience:** A farmer sends an 8-second Kannada voice note on WhatsApp; Krishi Mitra responds with an audio message and a PDF summary card containing their scheme checklist.

---

## 4. Computer Vision for Crop Disease & Soil Health Advisory

* **Multimodal Image Diagnosis:** Integrating Gemini 2.5 Flash's multimodal vision capabilities to allow farmers to upload photos of diseased leaves, pest infestations, or nutrient deficiencies alongside their voice queries.
* **Integrated Subsidy Suggestions:** If an arecanut yellow leaf disease (*Kole Roga*) or fall armyworm infection is detected, the engine can immediately suggest pest-control compensation or certified replacement sapling schemes.

---

## 5. Offline Edge Deployment for Gram Panchayats

* **Low-Cost Hardware Pods:** Packaging the FastAPI backend, deterministic rule engine, and lightweight quantized speech models (e.g. Whisper-small or offline ONNX runtimes) onto a Raspberry Pi or local village kiosk (Gram One center), operating completely offline without cellular connectivity.

