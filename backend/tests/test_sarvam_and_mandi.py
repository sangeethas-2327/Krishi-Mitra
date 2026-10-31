import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_mandi_prices_all():
    resp = client.get("/api/mandi")
    assert resp.status_code == 200
    data = resp.json()
    assert "source" in data
    assert "prices" in data
    assert data["total_records"] > 0
    assert len(data["prices"]) > 0

def test_mandi_prices_filter_district():
    resp = client.get("/api/mandi?district=Mandya")
    assert resp.status_code == 200
    data = resp.json()
    assert data["filter_district"] == "Mandya"
    assert all(p["district"] == "Mandya" for p in data["prices"])

def test_mandi_commodities_list():
    resp = client.get("/api/mandi/commodities")
    assert resp.status_code == 200
    commodities = resp.json()
    assert isinstance(commodities, list)
    assert len(commodities) > 0
    assert any(c["name_en"] == "Ragi" for c in commodities)

def test_mandi_markets_list():
    resp = client.get("/api/mandi/markets")
    assert resp.status_code == 200
    markets = resp.json()
    assert isinstance(markets, list)
    assert len(markets) > 0
    assert any("Mandya" in m["market"] for m in markets)

def test_sarvam_proxy_healthy():
    # Calling the proxy endpoint for signed URL
    resp = client.get("/api/sarvam/orgs/01a18b2b-1150-71e3-8126-8aa3c8bf858e/workspaces/01a18b2b-115a-71c3-b2eb-eee0b3e8b254/apps/Krishi-Mitr-e47b0654-55e7/url?interaction_type=call")
    # In live mode with valid SARVAM_API_KEY, upstream Sarvam API returns 200 with signed url or 402 if credit top-up is needed
    assert resp.status_code in [200, 402]
    if resp.status_code == 200:
        data = resp.json()
        assert "url" in data
        assert "reference_id" in data
        assert data["url"].startswith("wss://")

