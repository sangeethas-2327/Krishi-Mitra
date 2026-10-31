import sys
import httpx

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=== 1. BACKEND DIRECT HEALTH CHECK ===")
with httpx.Client(timeout=10.0) as client:
    health_res = client.get("http://127.0.0.1:8000/api/health")
    print(f"Backend HTTP Status: {health_res.status_code}")
    print("Health JSON:", health_res.json())

    print("\n=== 2. FRONTEND HTML LOAD ===")
    fe_res = client.get("http://localhost:5173/")
    print(f"Frontend HTTP Status: {fe_res.status_code}")
    print(f"Frontend HTML length: {len(fe_res.text)} bytes")

    print("\n=== 3. FRONTEND PROXY HEALTH CHECK ===")
    proxy_res = client.get("http://localhost:5173/api/health")
    print(f"Proxy Health HTTP Status: {proxy_res.status_code}")
    print("Proxy Health JSON:", proxy_res.json())

    print("\n=== 4. SCHEME COMPARISON API ===")
    comp_res = client.get("http://localhost:5173/api/schemes/compare?ids=pm-kisan,pmfby,demo-micro-irrigation")
    comp_data = comp_res.json()
    print(f"Comparison HTTP Status: {comp_res.status_code}")
    print(f"Compared Schemes Count: {len(comp_data['schemes'])}")
    for s in comp_data['schemes']:
        print(f"  - Scheme: {s['name']} [{s['scheme_type']}] | Category: {s['category']}")
    print("Comparison Matrix Dimensions:", list(comp_data['comparison_matrix'].keys()))

    print("\n=== 5. APPLICATION READINESS CHECKLIST API ===")
    chk_res = client.get("http://localhost:5173/api/schemes/pm-kisan/checklist")
    chk_data = chk_res.json()
    print(f"Checklist HTTP Status: {chk_res.status_code}")
    print(f"Checklist Scheme: {chk_data['scheme_name']}")
    print(f"Items Count: {len(chk_data['items'])}")
    for it in chk_data['items']:
        print(f"  * [{it['category']}] {it['title']} (Mandatory: {it['is_mandatory']})")
    print(f"Disclaimer: {chk_data['disclaimer'][:80]}...")

    print("\n=== 6. MULTI-CROP & TALUK CHAT REQUEST VIA PROXY ===")
    chat_payload = {
        'session_id': 'live-audit-phase2',
        'message': 'ನನ್ನ ಬಳಿ ತೀರ್ಥಹಳ್ಳಿ ತಾಲೂಕಿನಲ್ಲಿ 4 ಎಕರೆ ಸ್ವಂತ ಜಮೀನಿದೆ. ನಾನು ಅಡಿಕೆ, ಭತ್ತ ಮತ್ತು ರಾಗಿ ಬೆಳೆಯುತ್ತೇನೆ, ಹನಿ ನೀರಾವರಿಗೆ ಸಹಾಯಧನ ಬೇಕು.',
        'language': 'kn'
    }
    chat_res = client.post("http://localhost:5173/api/chat", json=chat_payload)
    chat_data = chat_res.json()
    p = chat_data['updated_profile']
    print(f"Chat HTTP Status: {chat_res.status_code}")
    print("Session ID:", chat_data['session_id'])
    print("Extracted Crops:", p['crops'])
    print("Extracted Taluk:", p['location']['taluk'])
    print("Extracted District:", p['location']['district'])
    print("Extracted Land Acres:", p['land_area']['value_acres'])
    print("Extracted Ownership:", p['ownership'])
    print("Next Question:", chat_data.get('next_question'))
    print(f"Recommendations Count: {len(chat_data['recommendations'])}")
    for rec in chat_data['recommendations']:
        print(f"  -> Scheme: {rec['scheme']['name']} ({rec['scheme']['scheme_type']}) => Status: {rec['evaluation_status']} (Score: {rec['score']})")

