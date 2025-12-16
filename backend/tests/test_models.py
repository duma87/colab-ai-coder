"""Test models endpoints."""

from fastapi.testclient import TestClient


def test_list_available_models(test_client: TestClient):
    """Test listing available models."""
    response = test_client.get("/api/v1/models/available")
    assert response.status_code == 200
    data = response.json()
    assert "models" in data
    assert len(data["models"]) > 0


def test_get_current_model(test_client: TestClient):
    """Test getting current model info."""
    response = test_client.get("/api/v1/models/current")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "loaded" in data
    assert "status" in data
