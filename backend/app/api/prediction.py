"""
prediction.py

Prediction endpoints for the Bounteous Motors AI API.
"""

from fastapi import APIRouter, HTTPException

from backend.app.schemas import (
    PredictionResponse,
    VehiclePredictionRequest,
)
from backend.app.services import predict_vehicle_price

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
)


@router.post(
    "/",
    response_model=PredictionResponse,
    summary="Predict Vehicle Price",
    description="Predict the market value of a vehicle using the trained machine learning model.",
)
async def predict(request: VehiclePredictionRequest) -> PredictionResponse:
    """
    Predict the market value of a vehicle using the trained ML model.

    Args:
        request: Validated vehicle information.

    Returns:
        PredictionResponse: Predicted vehicle price and metadata.
    """
    try:
        return predict_vehicle_price(request)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}",
        )