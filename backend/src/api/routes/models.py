"""Model management endpoints."""

from typing import Any, Dict

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/available")
async def list_available_models() -> Dict[str, Any]:
    """List available models."""
    return {
        "models": [
            {
                "name": "qwen2.5-coder:7b-q4_k_m",
                "size": "5.2GB",
                "context": 4096,
                "description": "Qwen 2.5 Coder 7B quantized to Q4_K_M",
                "recommended": True,
            },
            {
                "name": "qwen2.5-coder:1.5b",
                "size": "2.5GB",
                "context": 2048,
                "description": "Qwen 2.5 Coder 1.5B - Fast fallback",
                "recommended": False,
            },
        ]
    }


@router.get("/current")
async def get_current_model() -> Dict[str, Any]:
    """Get currently loaded model info."""
    return {
        "name": "qwen2.5-coder:7b-q4_k_m",
        "size": "5.2GB",
        "loaded": True,
        "vram_usage": "5.2GB",
        "status": "ready",
    }


@router.post("/load/{model_name}")
async def load_model(model_name: str) -> Dict[str, Any]:
    """Load a specific model."""
    # TODO: Implement model loading logic
    return {"status": "loading", "model": model_name}


@router.post("/unload")
async def unload_model() -> Dict[str, Any]:
    """Unload current model."""
    # TODO: Implement model unloading logic
    return {"status": "unloaded"}
