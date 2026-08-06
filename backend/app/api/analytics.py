"""
analytics.py

Analytics endpoints.
"""

from fastapi import APIRouter

from backend.app.services.analytics_service import (
    get_prediction_statistics,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/summary")
async def prediction_summary():
    """
    Return prediction analytics.
    """

    return get_prediction_statistics()