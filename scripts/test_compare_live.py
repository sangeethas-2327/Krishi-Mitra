import httpx

client = httpx.Client(timeout=10.0)
schemes = ['pm-kisan', 'pmfby', 'fruits-portal', 'karnataka-micro-irrigation', 'demo-micro-irrigation']
res = client.post('http://127.0.0.1:8000/api/schemes/compare', json=schemes)
print("Status Code:", res.status_code)
data = res.json()
print("Total schemes returned:", len(data["schemes"]))
for s in data["schemes"]:
    print(f"- ID: {s['scheme_id']}")
    print(f"  Name: {s['name']}")
    print(f"  Level: {s.get('government_level')}")
    print(f"  Official Portal: {s.get('official_url')}")
    print(f"  Application Steps: {len(s.get('application_steps', []))}")
    print(f"  Verification Status: {s.get('verification_status')}")

