"""Test health endpoints."""

import pytest
from fastapi.testclient import TestClient


def test_health_check(test_client: TestClient):
    """Test health check endpoint."""
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_readiness_check(test_client: TestClient):
    """Test readiness check endpoint."""
    response = test_client.get("/health/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_liveness_check(test_client: TestClient):
    """Test liveness check endpoint."""
    response = test_client.get("/health/live")
    assert response.status_code == 200
    assert response.json()["status"] == "alive"


def test_root_endpoint(test_client: TestClient):
    """Test root endpoint."""
    response = test_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Colab AI Coder API"
    assert "docs" in data
