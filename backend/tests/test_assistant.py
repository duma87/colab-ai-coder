"""Test assistant endpoints."""

from fastapi.testclient import TestClient


def test_generate_endpoint(test_client: TestClient):
    """Test code generation endpoint."""
    payload = {
        "prompt": "def hello",
        "task": "generate",
        "language": "python",
        "max_tokens": 100,
    }
    response = test_client.post("/api/v1/assistant/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert data["task"] == "generate"
    assert "model" in data


def test_refactor_endpoint(test_client: TestClient):
    """Test refactor endpoint."""
    payload = {
        "prompt": "for i in range(len(list)): print(i)",
        "task": "refactor",
    }
    response = test_client.post("/api/v1/assistant/refactor", json=payload)
    assert response.status_code == 200
    assert response.json()["task"] == "refactor"


def test_debug_endpoint(test_client: TestClient):
    """Test debug endpoint."""
    payload = {
        "prompt": "buggy_code_here",
        "task": "debug",
    }
    response = test_client.post("/api/v1/assistant/debug", json=payload)
    assert response.status_code == 200
    assert response.json()["task"] == "debug"


def test_audit_endpoint(test_client: TestClient):
    """Test security audit endpoint."""
    payload = {
        "prompt": "import os; os.system('rm -rf /')",
        "task": "audit",
    }
    response = test_client.post("/api/v1/assistant/audit", json=payload)
    assert response.status_code == 200
    assert response.json()["task"] == "audit"


def test_get_templates(test_client: TestClient):
    """Test getting prompt templates."""
    response = test_client.get("/api/v1/assistant/templates")
    assert response.status_code == 200
    data = response.json()
    assert "templates" in data
    assert "refactor" in data["templates"]
