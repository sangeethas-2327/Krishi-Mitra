import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_weather_endpoint_default_location():
    response = client.get("/api/weather")
    assert response.status_code == 200
    data = response.json()
    assert "location_name" in data
    assert "current_temp" in data
    assert "humidity" in data
    assert "wind_speed" in data
    assert "hourly_forecast" in data
    assert len(data["hourly_forecast"]) > 0
    assert "daily_forecast" in data
    assert len(data["daily_forecast"]) >= 5
    assert "agronomic_insight" in data
    assert data["agronomic_insight"]["alert_level"] in ["optimal", "advisory", "warning"]

def test_weather_endpoint_with_district():
    response = client.get("/api/weather?district=Mandya&crops=sugarcane,paddy")
    assert response.status_code == 200
    data = response.json()
    assert "Mandya" in data["location_name"]
    assert data["precision_level"] == "district"
    assert data["latitude"] > 0
    assert data["longitude"] > 0
    assert "agronomic_insight" in data

