"""Configuration management for Colab AI Coder."""

from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # FastAPI
    FASTAPI_HOST: str = "0.0.0.0"
    FASTAPI_PORT: int = 8000
    FASTAPI_ENV: str = "development"
    DEBUG: bool = True

    # Model Configuration
    MODEL_NAME: str = "qwen2.5-coder:7b-q4_k_m"
    MODEL_PATH: str = "/models"
    NUM_CTX: int = 4096
    NUM_GPU_LAYERS: int = 40
    TEMPERATURE: float = 0.2
    TOP_P: float = 0.9
    TOP_K: int = 40
    REPEAT_PENALTY: float = 1.05
    MAX_TOKENS: int = 256

    # Device Configuration
    DEVICE_MAP: str = "auto"
    OFFLOAD_FOLDER: str = "/tmp/offload"
    USE_FLASH_ATTENTION_2: bool = True
    LOAD_IN_4BIT: bool = True

    # Cache Configuration
    CACHE_ENABLED: bool = True
    CACHE_BACKEND: str = "redis"
    REDIS_URL: str = "redis://localhost:6379/0"
    CACHE_TTL: int = 3600

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    # Security
    API_KEY: str = "your-secret-api-key-here"
    ALLOWED_ORIGINS: list = ["http://localhost:3000", "http://localhost:5173"]

    # Storage
    HISTORY_DIR: str = "/tmp/colab-ai-coder/history"
    PROMPT_TEMPLATES_DIR: str = "/tmp/colab-ai-coder/templates"

    # Sentry
    SENTRY_DSN: Optional[str] = None
    SENTRY_ENVIRONMENT: str = "development"

    class Config:
        """Pydantic config."""

        env_file = ".env"
        case_sensitive = True


def get_settings() -> Settings:
    """Get settings instance."""
    return Settings()
