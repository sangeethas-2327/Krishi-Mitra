# 5-Minute Hackathon Judges' Demonstration Script

**Project Title:** Krishi Mitra (ಕೃಷಿ ಮಿತ್ರ) — Voice-First Conversational AI for Indian Agricultural Schemes  
**Presentation Time:** 5 Minutes (300 Seconds)  
**Presenter:** Antigravity Engineering Team  

---

## Demonstration Timeline & Step-by-Step Flow

```
0:00 - 0:45 │ Hook & Problem Statement
0:45 - 1:30 │ Live Spoken Kannada Interaction & Transcript Review
1:30 - 2:30 │ Automatic Profile Extraction & Conversational Correction
2:30 - 3:30 │ Deterministic Eligibility Matching & Explainability
3:30 - 4:15 │ Scheme Comparison & Application Readiness Checklist
4:15 - 5:00 │ Architecture Highlight & Technical Q&A
```

---

### Step 1: Hook & The Human Problem (0:00 – 0:45)
* **Presenter Dialogue:**
  > *"Respected judges, over 70% of farmers in Karnataka are smallholders, but less than 35% receive the government welfare and subsidies they are entitled to. Why? Because official portals are in bureaucratic English, require complex keyboard navigation, and generic AI chatbots hallucinate policies. Today, we introduce **Krishi Mitra (ಕೃಷಿ ಮಿತ್ರ)**: a voice-first Kannada conversational AI that listens to farmers in their mother tongue and pairs with an uncompromising, deterministic eligibility engine."*
* **Visual Action:** Show the clean Krishi Mitra landing page (`http://localhost:5173` or deployed Vercel URL) with its green agricultural identity and the **Quick Start Guide**.

---

### Step 2: Live Spoken Kannada Interaction (0:45 – 1:30)
* **Presenter Action:** Click the large circular microphone button.
* **Spoken Kannada Utterance:**
  > *"ನನಗೆ ಕೃಷಿಗೆ ಸಹಾಯಧನ ಬೇಕು. ನಾನು 3 ಎಕರೆ ಅಡಿಕೆ ಮತ್ತು ತೆಂಗು ಬೆಳೆಯುತ್ತಿದ್ದೇನೆ."*  
  > *(English: "I need agricultural assistance. I grow 3 acres of arecanut and coconut.")*
* **What Judges See:**
  * Animated pulsing soundwave and real-time recording timer.
  * Stop recording $\rightarrow$ Sarvam Saaras transcribes the Kannada audio into the **Transcript Review Modal**.
  * Point out: *"Notice that the farmer can review or edit their words before submitting, ensuring 100% agency."*
  * Click **"ಪ್ರಶ್ನೆ ಸಲ್ಲಿಸಿ (Submit Voice)"**.

---

### Step 3: Transparent Profile Extraction & Self-Correction (1:30 – 2:30)
* **What Judges See:**
  * The **Farmer Profile Panel** instantly updates:
    * Crops: `['arecanut', 'coconut']`
    * Land Area: `3.0 Acres` (with confidence meter)
  * The Assistant replies in natural spoken Kannada via Sarvam Bulbul TTS and asks an adaptive follow-up question regarding location and ownership.
* **Demonstrate Conversational Correction:**
  * Presenter speaks or types:
    > *"ಕ್ಷಮಿಸಿ, 3 ಎಕರೆ ಅಲ್ಲ 2 ಎಕರೆ, ಜಮೀನು ಶಿವಮೊಗ್ಗದಲ್ಲಿದೆ, ಸ್ವಂತ ಭೂಮಿ."*  
    > *(English: "Sorry, not 3 acres, 2 acres; the land is in Shivamogga, self-owned.")*
  * Highlight to Judges: *"Krishi Mitra recognizes the negation pattern 'X ಅಲ್ಲ Y'. It corrects the land to 2.0 acres and logs the previous 3.0 value in conflict history without getting confused."*

---

### Step 4: Deterministic Eligibility Engine & Explainability (2:30 – 3:30)
* **What Judges See:**
  * The **Scheme Recommendations** section updates dynamically below.
  * **PM-KISAN:** Marked `POTENTIALLY_SUITABLE` (since ownership is owned and land is $\le 2$ ha).
  * **Karnataka Micro-Irrigation (KMF-DRIP):** Shows `INSUFFICIENT_INFORMATION` because irrigation source is still unknown, with a one-click button to answer.
  * Explain Engine Decoupling:
    > *"Judges, please note our core architectural innovation: The LLM does NOT decide eligibility. Our independent Python rule engine evaluated these criteria mathematically. An LLM can never hallucinate a farmer into receiving a subsidy they are legally barred from."*

---

### Step 5: Scheme Comparison & Readiness Checklist (3:30 – 4:15)
* **Presenter Action:**
  1. Click on **PM-KISAN** card $\rightarrow$ Opens **Scheme Modal**.
  2. Point out official portal link (`https://pmkisan.gov.in/`).
  3. Show the **Application Readiness Checklist**:
     * Visual progress bar (e.g. 75% Ready).
     * Documents needed: Pahani/RTC, Aadhaar seeded to bank account.
  4. Click **"ಯೋಜನೆಗಳನ್ನು ಹೋಲಿಕೆ ಮಾಡಿ (Compare Schemes)"** $\rightarrow$ Shows side-by-side comparison matrix with PMFBY and state horticulture grants.

---

### Step 6: Spoken Audio Response & Wrap-Up (4:15 – 5:00)
* **Presenter Action:**
  * Click the Speaker icon on the assistant message.
  * Krishi Mitra speaks out the explanation in natural, fluent Kannada (*"ನಿಮ್ಮ ವಿವರಗಳ ಪ್ರಕಾರ, ನೀವು ಪ್ರಧಾನ ಮಂತ್ರಿ ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ನಿಧಿ ಯೋಜನೆಗೆ ಪ್ರಾಥಮಿಕವಾಗಿ ಅರ್ಹರಾಗಿದ್ದೀರಿ..."*).
* **Closing Statement:**
  > *"Krishi Mitra proves that generative AI is most powerful not when it replaces legal rules, but when it serves as a compassionate, vernacular voice interface to transparent public governance. Thank you!"*

---

## Backup Offline Demonstration Plan

If WiFi or cloud connectivity is disrupted during the live demonstration:
1. Krishi Mitra operates seamlessly in **Offline Demo Mode**.
2. All 53 backend tests verify that regex heuristics, the local Kannada vocabulary corpus, and synthetic audio chime generation operate with **zero external network calls**.
3. Point out the badge in the Navbar: `"ಡೆಮೋ ಮೋಡ್ (ನಿಯಮ ಎಂಜಿನ್)"` and explain how rural edge devices can run this engine even in low-bandwidth taluks.

