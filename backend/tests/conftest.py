"""Test configuration."""

import pytest
from typing import Generator


@pytest.fixture
def test_client():
    """Create test client for FastAPI."""
    from fastapi.testclient import TestClient
    from src.main import app

    return TestClient(app)
