"""
health.py

Health check endpoints for the Bounteous Motors AI API.
"""

from datetime import datetime

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health_check():
    """
    Check the health status of the API.
    """

    return {
        "status": "healthy",
        "application": "Bounteous Motors AI",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }