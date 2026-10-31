# Problem Statement — The Agritech Access Gap for Kannada Farmers

## 1. Context: Public Welfare in Indian Agriculture

Agriculture sustains over 55% of Karnataka's population, with small and marginal farmers (< 2 hectares of land) representing approximately 78% of all operational land holdings.

Both the Union Ministry of Agriculture & Farmers Welfare and Karnataka's Department of Agriculture run extensive assistance programs:
* Direct income support (e.g., PM-KISAN, giving ₹6,000 annually).
* Crop insurance coverage against drought, pests, and unseasonal rainfall (e.g., PMFBY).
* Drip and sprinkler irrigation subsidies up to 90% for SC/ST and small farmers.
* Subsidized seeds, farm mechanization, and soil health management.

Yet, hundreds of thousands of farming households never receive these benefits.

---

## 2. Core Failure Modes of Current Portals & Apps

### A. Linguistic Inaccessibility & Administrative Jargon
Official portals (such as Seva Sindhu, Samrakshane, and PM-KISAN Portal) primarily present information in bureaucratic language. Terms like *Pahani*, *RTC*, *Survey Number*, *Aadhaar seeding*, *e-KYC*, and *Notified Unit Area* are rarely explained in conversational Kannada. Farmers who speak regional vernaculars (e.g., North Karnataka *Uttara Karnataka* dialect, Malenadu phrases) struggle to decode eligibility rules.

### B. The Text-and-Form Paradigm
Most government portals are designed around lengthy digital forms featuring multi-level dropdowns, captcha codes, and mandatory English inputs. For farmers with limited formal education or touch-screen keyboard experience, completing these forms without paying informal intermediaries ("middlemen" or cyber café agents) is virtually impossible.

### C. The Danger of Generic Generative AI Chatbots
While modern Large Language Models (LLMs) can generate fluent text, **pure LLM chatbots are hazardous in public policy and agricultural welfare**:
1. **Hallucination of Criteria:** An LLM might tell a tenant farmer that they qualify for PM-KISAN, even though statutory guidelines strictly require registered land ownership.
2. **Fabrication of Deadlines & Amounts:** LLMs frequently produce outdated subsidy limits or invent application windows.
3. **Lack of Negative Explanations:** When a farmer is not eligible, LLMs often say "You are not eligible" without identifying the exact failing criterion or what remedial steps could make them eligible.

---

## 3. Specific Difficulties in Kannada Agricultural Processing

* **Crop Homonyms & Ambiguity:** The word `"ಜೋಳ"` (*Jola*) can refer either to *Great Millet / Jowar* (sorghum, drought-resilient) or *Maize / Corn* (heavy irrigation). Automatic systems that guess incorrectly distort subsidy advice.
* **Non-Standard Land Measurements:** Farmers express land in *Guntas*, *Anas*, *Cents*, or *Hectares* rather than standard acres.
* **Code-Mixing in Everyday Speech:** Farmers regularly interleave Kannada verbs with English agricultural nouns (e.g., *"Borewell ide, pump set subsidy bekithu"*).
* **Conversational Corrections:** Farmers often correct themselves mid-sentence (*"3 acre alla, 2 acre"*). Naive models extract the first number they hear and fail to update.

---

## 4. The Krishi Mitra Mandate

Krishi Mitra was built to bridge this systemic divide. By marrying **accessible Kannada voice interaction** with an **uncompromising, deterministic rule engine**, Krishi Mitra ensures that no farmer is left behind due to literacy, language, or bureaucratic complexity.

