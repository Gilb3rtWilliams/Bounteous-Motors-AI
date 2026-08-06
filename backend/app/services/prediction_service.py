"""
prediction_service.py

Service layer for vehicle price prediction.
This module bridges the FastAPI backend and the ML prediction pipeline.
"""

from ML.src.predict import predict_price
from backend.app.schemas import VehiclePredictionRequest, PredictionResponse


MODEL_VERSION = "1.0.0"
CURRENCY = "KES"


def predict_vehicle_price(
    request: VehiclePredictionRequest,
) -> PredictionResponse:
    """
    Generate a vehicle price prediction.

    Args:
        request: Incoming API request.

    Returns:
        PredictionResponse
    """

    # Convert the Pydantic model into a dictionary
    vehicle_data = request.model_dump()

    # Call the ML prediction pipeline
    predicted_price = predict_price(vehicle_data)

    # Build the API response
    return PredictionResponse(
        predicted_price=round(predicted_price, 2),
        currency=CURRENCY,
        model_version=MODEL_VERSION,
        status="success",
    )