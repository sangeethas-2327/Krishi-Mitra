# Eligibility Engine — Krishi Mitra Deterministic Rule Engine

## 1. Engine Philosophy: Absolute Decoupling

In Krishi Mitra, **no LLM or generative model makes eligibility decisions**. The eligibility engine is a deterministic, rule-based expert system implemented in Python (`app/services/eligibility_engine.py` and `app/services/scheme_recommender.py`).

### Why Determinism is Essential in Agritech:
1. **Auditability:** Every qualification decision can be traced to a specific mathematical comparison.
2. **Statutory Integrity:** Legal rules (e.g. land ownership ceilings or exclusion lists) cannot be bypassed by clever conversational prompt injection.
3. **Transparent Explanations:** The engine provides exact rule descriptions in Kannada explaining *why* a farmer qualified or what missing document needs to be resolved.

---

## 2. The Four-State Classification Model

Rather than a simplistic binary "Eligible / Ineligible", the engine outputs one of four actionable states:

| Status | Mathematical Definition | User Action & Explanation |
| :--- | :--- | :--- |
| `POTENTIALLY_SUITABLE` | $\forall r \in \text{MandatoryRules}, \text{eval}(r) = \text{True}$ | The farmer meets all known criteria. Show application checklist. |
| `INSUFFICIENT_INFORMATION` | $\exists r \in \text{MandatoryRules}, \text{eval}(r) = \text{UNKNOWN}$ and no rule evaluated to False. | The farmer has not provided required parameters (e.g. land size, district). Triggers adaptive question. |
| `REQUIRES_OFFICIAL_VERIFICATION` | All rules are True/Unknown, but at least one rule requires offline inspection. | The farmer needs physical verification (e.g. RTC survey number, soil testing, Aadhaar bank seeding). |
| `NOT_SUITABLE_BASED_ON_KNOWN_RULES` | $\exists r \in \text{MandatoryRules}, \text{eval}(r) = \text{False}$ | The farmer violates a mandatory exclusion. Displays exact failing rule in Kannada. |

---

## 3. Supported Rule Operators

The engine supports rich relational and set-theoretic operators:

```python
OPERATORS = {
    "==": lambda val, target: val == target,
    "!=": lambda val, target: val != target,
    "<=": lambda val, target: val <= target,
    ">=": lambda val, target: val >= target,
    "<":  lambda val, target: val < target,
    ">":  lambda val, target: val > target,
    "in": lambda val, target: val in target,
    "contains": lambda val, target: target in val if isinstance(val, (list, str)) else False,
    "any_in": lambda val, target: bool(set(val).intersection(set(target))) if isinstance(val, list) else False,
    "between": lambda val, target: target[0] <= val <= target[1] if isinstance(target, (list, tuple)) else False
}
```

---

## 4. Compound Rules & Fallbacks

* **Compound `OR` Rules:** Supports sub-rules where fulfilling any single condition satisfies the clause (e.g., qualifying by being a small farmer OR an SC/ST farmer).
* **Optional Rules:** Non-mandatory criteria (e.g., preferred crops or optional subsidies) do not block base qualification if unsatisfied.
* **Confirmed Field Protection:** Fields confirmed by the farmer cannot be overridden by ambiguous or low-confidence conversational inferences.

---

## 5. Reference Scheme Dataset

Krishi Mitra includes five structured scheme profiles in `backend/app/data/schemes.json`:

1. **PM-KISAN (Real):** Pradhan Mantri Kisan Samman Nidhi.
   * *Mandatory Criteria:* Registered land owner (`ownership == 'owned'`), cultivable land in India.
   * *Exclusions:* Institutional landholders, tenant-only farmers.
2. **PMFBY (Real):** Pradhan Mantri Fasal Bima Yojana.
   * *Mandatory Criteria:* Growing notified crop (paddy, arecanut, ragi, etc.) in notified season/area; **open to both owner and tenant farmers**.
   * *Verification:* Enrollment before state cut-off date.
3. **KMF-DRIP (Demonstration):** Karnataka Micro-Irrigation Scheme.
   * *Mandatory Criteria:* Cultivable land $\le 5.0$ acres; source of water available (borewell, open well, canal).
   * *Benefit:* Up to 90% subsidy for micro-drip setups.
4. **K-HORTI (Demonstration):** Karnataka Horticulture Expansion Incentive.
   * *Mandatory Criteria:* Minimum 1.0 acre of perennial plantation crop (arecanut, coconut, coffee, banana).
5. **K-SEED (Demonstration):** Certified Drought Seed Subsidy Scheme.
   * *Mandatory Criteria:* Rainfed cultivation, dryland crops (ragi, pulses, groundnut).

> **Transparency Standard:** Real schemes are clearly flagged with verified URLs to official portals (e.g., `https://pmkisan.gov.in/` and `https://pmfby.gov.in/`). Synthetic demonstration schemes carry an explicit disclaimer.

