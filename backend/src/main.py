"""Main FastAPI application for Colab AI Coder."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZIPMiddleware

from src.config import get_settings
from src.api.routes import assistant, health, models

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    logger.info("🚀 Starting Colab AI Coder API")
    # Startup logic here
    yield
    logger.info("🛑 Shutting down Colab AI Coder API")
    # Cleanup logic here


# Initialize FastAPI app
settings = get_settings()
app = FastAPI(
    title="Colab AI Coder API",
    description="Assistant IA complet basé sur Qwen-2.5-Coder 7B Q4_K_M",
    version="0.1.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add GZIP middleware
app.add_middleware(GZIPMiddleware, minimum_size=1000)

# Include routers
app.include_router(health.router, tags=["Health"])
app.include_router(models.router, prefix="/api/v1/models", tags=["Models"])
app.include_router(assistant.router, prefix="/api/v1/assistant", tags=["Assistant"])


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "Colab AI Coder API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.FASTAPI_HOST,
        port=settings.FASTAPI_PORT,
        log_level=settings.LOG_LEVEL.lower(),
    )
