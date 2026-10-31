# AI & Machine Learning Implementation — Krishi Mitra

## 1. Dual-Engine Architecture

Krishi Mitra implements a hybrid architecture: Generative AI handles unstructured conversational language in Kannada, while a deterministic rule engine handles statutory welfare qualification.

```
[Unstructured Voice / Text] 
       │
       ▼
┌────────────────────────────────────────┐
│  AI Conversational Layer                │
│  - Sarvam Saaras (ASR / STT)           │
│  - Gemini 2.5 Flash (Entity Extraction)│
│  - Vocabulary Normalization            │
└──────────────────┬─────────────────────┘
                   │ Emits Structured JSON
                   ▼
┌────────────────────────────────────────┐
│  Deterministic Decision Layer          │
│  - Boolean & Relational Operators      │
│  - 4-State Qualification Engine        │
│  - Audit Logs & Provenance Tracking    │
└──────────────────┬─────────────────────┘
                   │ Emits Grounded Facts
                   ▼
┌────────────────────────────────────────┐
│  AI Explanation & Voice Synthesis      │
│  - Gemini 2.5 Flash (Grounded Summary) │
│  - Sarvam Bulbul (Kannada TTS)         │
└────────────────────────────────────────┘
```

---

## 2. Google Gemini 2.5 Flash Integration

### 2.1 Official Google Gen AI SDK
The system utilizes the latest `google-genai` SDK (`from google import genai`), configured via `GEMINI_API_KEY` and configurable `GEMINI_MODEL` (default: `gemini-2.5-flash`).

### 2.2 Structured JSON Entity Extraction
To prevent hallucinated structures, Gemini is invoked with **Structured Outputs** bound to a Pydantic schema (`ExtractedFarmerInfo`):

```python
config = types.GenerateContentConfig(
    temperature=0.1,  # Low temperature for strict factual extraction
    response_mime_type="application/json",
    response_schema=ExtractedFarmerInfo,
    system_instruction=(
        "You are an expert Kannada Agricultural Information Extractor for Krishi Mitra...\n"
        "Rules:\n"
        "1. Standardize districts to Karnataka official names.\n"
        "2. Convert land measurements to acres (1 acre = 40 guntas).\n"
        "3. Capture ALL crops in the message into the crops array.\n"
        "4. If farmer corrects previous facts (e.g. '3 acre alla 2 acre'), set is_correction: true.\n"
        "5. Never invent or hallucinate facts not stated."
    )
)
```

### 2.3 Grounded Explanation Generation
When generating responses, the prompt receives:
1. The **exact eligibility results** produced by the rule engine.
2. The **failing criteria** and **satisfied criteria**.
3. A strict rule: *"You MUST explain ONLY the schemes evaluated by the engine. Never tell a farmer they are eligible if the engine marked them NOT_SUITABLE."*

---

## 3. Sarvam AI Voice Integration

### 3.1 Speech-to-Text: Saaras (`saaras:v2`)
* Endpoint: `POST https://api.sarvam.ai/speech-to-text`
* Target Language: `kn-IN` (Kannada)
* Handles audio formats: `audio/wav`, `audio/webm`, `audio/ogg`, `audio/mpeg`.
* Robust against Indian rural background acoustics and mixed agricultural phrases.

### 3.2 Text-to-Speech: Bulbul (`bulbul:v1`)
* Endpoint: `POST https://api.sarvam.ai/text-to-speech`
* Speaker: `meera` (Kannada natural female voice)
* Sample Rate: 22,050 Hz, 16-bit PCM WAV.
* Delivers melodic, culturally appropriate Kannada pronunciation with natural cadence.

---

## 4. Linguistic Guardrails & Vocabulary Normalization

The system maintains a comprehensive Kannada agricultural ontology in `app/data/kannada_vocabulary.json`:
* **Crops:** `arecanut` (`ಅಡಿಕೆ`, `ಅಡಕೆ`), `paddy` (`ಭತ್ತ`, `ಬತ್ತ`), `ragi` (`ರಾಗಿ`), `sugarcane` (`ಕಬ್ಬು`), `coconut` (`ತೆಂಗು`), `maize` (`ಮೆಕ್ಕೆಜೋಳ`).
* **Ambiguous Terms:** Traps `"ಜೋಳ"` and generates an immediate clarification question between Sorghum and Maize.
* **Land Units:** Normalizes `ಗುಂಟೆ` (0.025 acres), `ಹೆಕ್ಟೇರ್` (2.471 acres), `ಸೆಂಟು` (0.01 acres).
* **Negation Regex Engine:** Prioritizes post-negation figures in phrases like `"X ಅಲ್ಲ Y"` (*not X, but Y*).

