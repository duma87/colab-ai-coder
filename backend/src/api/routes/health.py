"""Health check endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "colab-ai-coder-api"}


@router.get("/health/ready")
async def readiness_check():
    """Readiness check endpoint."""
    return {"status": "ready"}


@router.get("/health/live")
async def liveness_check():
    """Liveness check endpoint."""
    return {"status": "alive"}
