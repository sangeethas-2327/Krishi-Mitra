#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Krishi Mitra Phase 3A Live End-to-End Verification Script
Tests real HTTP endpoints against the running FastAPI backend and Vite frontend.
"""

import sys
import json
import httpx

BACKEND_URL = "http://127.0.0.1:8000"
FRONTEND_URL = "http://localhost:5173"

def main():
    print("=" * 70)
    print("KRISHI MITRA PHASE 3A LIVE VERIFICATION")
    print("=" * 70)

    client = httpx.Client(timeout=10.0)
    passed_tests = 0
    total_tests = 0

    # 1. Frontend Vite Server Check
    total_tests += 1
    try:
        r_fe = client.get(FRONTEND_URL)
        if r_fe.status_code == 200 and "<html" in r_fe.text.lower():
            print(f"[PASS] 1. Frontend Vite Server is running at {FRONTEND_URL} (Status 200)")
            passed_tests += 1
        else:
            print(f"[FAIL] 1. Frontend returned status {r_fe.status_code}")
    except Exception as e:
        print(f"[FAIL] 1. Could not connect to Frontend: {e}")

    # 2. Backend Health Check
    total_tests += 1
    try:
        r_health = client.get(f"{BACKEND_URL}/api/health")
        if r_health.status_code == 200:
            h_data = r_health.json()
            assert h_data.get("status") == "healthy"
            assert "llm_provider" in h_data
            assert "gemini_model" in h_data
            print(f"[PASS] 2. Backend Health Check: status='{h_data['status']}', model='{h_data['gemini_model']}', provider='{h_data['llm_provider']}', demo_mode={h_data['demo_mode']}")
            passed_tests += 1
        else:
            print(f"[FAIL] 2. Backend Health returned status {r_health.status_code}")
    except Exception as e:
        print(f"[FAIL] 2. Health check exception: {e}")

    # 3. Chat Turn 1: Multi-Crop & Land Area Extraction
    total_tests += 1
    session_id = "live_verify_phase3a_session"
    try:
        t1_payload = {
            "session_id": session_id,
            "message": "ನನಗೆ ಕೃಷಿಗೆ ಸಹಾಯಧನ ಬೇಕು. ನಾನು 3 ಎಕರೆ ಅಡಿಕೆ ಮತ್ತು ತೆಂಗು ಬೆಳೆಯುತ್ತೇನೆ.",
            "language": "kn"
        }
        r_t1 = client.post(f"{BACKEND_URL}/api/chat", json=t1_payload)
        if r_t1.status_code == 200:
            d1 = r_t1.json()
            prof = d1.get("updated_profile", {})
            crops = prof.get("crops", [])
            land = prof.get("land_area", {}).get("value_acres")
            assert land == 3.0, f"Expected land 3.0, got {land}"
            assert "arecanut" in crops, f"Expected arecanut in crops, got {crops}"
            assert "coconut" in crops, f"Expected coconut in crops, got {crops}"
            assert d1.get("llm_provider") in ["gemini-live", "demo-deterministic"]
            print(f"[PASS] 3. Chat Turn 1: Successfully extracted land={land} acres and crops={crops}")
            print(f"       Follow-up Question: {d1.get('next_question_kn')}")
            passed_tests += 1
        else:
            print(f"[FAIL] 3. Chat Turn 1 failed with status {r_t1.status_code}")
    except Exception as e:
        print(f"[FAIL] 3. Chat Turn 1 exception: {e}")

    # 4. Chat Turn 2: Location & Ownership
    total_tests += 1
    try:
        t2_payload = {
            "session_id": session_id,
            "message": "ನನ್ನ ಜಮೀನು ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯಲ್ಲಿದೆ ಮತ್ತು ಇದು ನನ್ನ ಸ್ವಂತ ಜಮೀನು.",
            "language": "kn"
        }
        r_t2 = client.post(f"{BACKEND_URL}/api/chat", json=t2_payload)
        if r_t2.status_code == 200:
            d2 = r_t2.json()
            prof = d2.get("updated_profile", {})
            dist = prof.get("location", {}).get("district")
            own = prof.get("ownership")
            recs = d2.get("recommendations", [])
            assert dist == "Shivamogga", f"Expected district Shivamogga, got {dist}"
            assert own == "owned", f"Expected owned, got {own}"
            assert len(recs) >= 2, f"Expected recommendations, got {len(recs)}"
            print(f"[PASS] 4. Chat Turn 2: Location={dist}, Ownership={own}. Evaluated schemes={len(recs)}")
            for r in recs[:2]:
                print(f"       - Scheme: {r['scheme']['name']} ({r['scheme']['scheme_type']}) -> Status: {r['evaluation_status']}")
            passed_tests += 1
        else:
            print(f"[FAIL] 4. Chat Turn 2 failed with status {r_t2.status_code}")
    except Exception as e:
        print(f"[FAIL] 4. Chat Turn 2 exception: {e}")

    # 5. Chat Turn 3: Conversational Correction & Confirmed Field Protection
    total_tests += 1
    try:
        t3_payload = {
            "session_id": session_id,
            "message": "ತಪ್ಪು ಹೇಳಿದೆ, ನನ್ನ ಬಳಿ 3 ಎಕರೆ ಅಲ್ಲ 2 ಎಕರೆ ಜಮೀನಿದೆ.",
            "language": "kn"
        }
        r_t3 = client.post(f"{BACKEND_URL}/api/chat", json=t3_payload)
        if r_t3.status_code == 200:
            d3 = r_t3.json()
            prof = d3.get("updated_profile", {})
            land = prof.get("land_area", {}).get("value_acres")
            dist = prof.get("location", {}).get("district")
            conflicts = prof.get("conflict_fields", {})
            assert land == 2.0, f"Expected corrected land 2.0, got {land}"
            assert dist == "Shivamogga", f"Expected confirmed district Shivamogga preserved, got {dist}"
            assert "land_area.value_acres" in conflicts, f"Expected conflict logged for land_area, got {conflicts}"
            print(f"[PASS] 5. Chat Turn 3: Corrected land to {land} acres, preserved confirmed district={dist}, conflict logged.")
            passed_tests += 1
        else:
            print(f"[FAIL] 5. Chat Turn 3 failed with status {r_t3.status_code}")
    except Exception as e:
        print(f"[FAIL] 5. Chat Turn 3 exception: {e}")

    # 6. Scheme Comparison Endpoint Check
    total_tests += 1
    try:
        r_comp = client.post(f"{BACKEND_URL}/api/schemes/compare", json=["pm-kisan", "pmfby"])
        if r_comp.status_code == 200:
            comp_data = r_comp.json()
            assert len(comp_data.get("schemes", [])) == 2
            print(f"[PASS] 6. Scheme Comparison Endpoint: Successfully compared 2 schemes")
            passed_tests += 1
        else:
            print(f"[FAIL] 6. Scheme Comparison failed with status {r_comp.status_code}")
    except Exception as e:
        print(f"[FAIL] 6. Scheme Comparison exception: {e}")

    # 7. Application Readiness Checklist Endpoint Check
    total_tests += 1
    try:
        r_chk = client.get(f"{BACKEND_URL}/api/schemes/pm-kisan/checklist?session_id={session_id}")
        if r_chk.status_code == 200:
            chk_data = r_chk.json()
            assert chk_data.get("scheme_id") == "pm-kisan"
            assert "items" in chk_data
            print(f"[PASS] 7. Readiness Checklist Endpoint: {chk_data['scheme_name']} ({chk_data['completion_percentage']}% ready)")
            passed_tests += 1
        else:
            print(f"[FAIL] 7. Checklist failed with status {r_chk.status_code}")
    except Exception as e:
        print(f"[FAIL] 7. Checklist exception: {e}")

    # 8. Reset Session Endpoint Check
    total_tests += 1
    try:
        r_rst = client.post(f"{BACKEND_URL}/api/session/reset", json={"session_id": session_id})
        if r_rst.status_code == 200:
            print(f"[PASS] 8. Session Reset Endpoint: Successfully reset session")
            passed_tests += 1
        else:
            print(f"[FAIL] 8. Reset session failed with status {r_rst.status_code}")
    except Exception as e:
        print(f"[FAIL] 8. Reset session exception: {e}")

    print("=" * 70)
    print(f"VERIFICATION SUMMARY: {passed_tests}/{total_tests} tests passed.")
    print("=" * 70)

    if passed_tests == total_tests:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
