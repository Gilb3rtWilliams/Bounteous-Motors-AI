"""
main.py

Entry point for the Bounteous Motors AI FastAPI application.
"""

from fastapi import FastAPI

from backend.app.api.health import router as health_router
from backend.app.api.prediction import router as prediction_router
from backend.app.api.prediction_history import (
    router as prediction_history_router,
)
from backend.app.api.analytics import (
    router as analytics_router,
)

app = FastAPI(
    title="Bounteous Motors AI",
    description="AI-powered vehicle price prediction API",
    version="1.0.0",
    contact={
        "name": "Gilbert Nyange",
        "email": "gilbert.nyange23@students.dkut.ac.ke",
    },
    license_info={
        "name": "MIT License",
    },
)


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint.
    """

    return {
        "application": "Bounteous Motors AI",
        "status": "Running",
        "version": "1.0.0",
        "message": "Welcome to the Bounteous Motors AI API",
    }


# =============================================================================
# Register API Routers
# =============================================================================

app.include_router(health_router)
app.include_router(prediction_router)
app.include_router(prediction_history_router)
app.include_router(analytics_router)