"""
prediction_service.py

Service layer for vehicle price prediction.
This module bridges the FastAPI backend and the ML prediction pipeline.
"""

from datetime import datetime

from backend.app.database import predictions_collection
from backend.app.schemas import (
    PredictionResponse,
    VehiclePredictionRequest,
)
from ML.src.predict import predict_price


MODEL_VERSION = "1.0.0"
CURRENCY = "KES"


def predict_vehicle_price(
    request: VehiclePredictionRequest,
) -> PredictionResponse:
    """
    Generate a vehicle price prediction and
    save it to MongoDB.
    """

    # Convert request to dictionary
    vehicle_data = request.model_dump()

    # Predict price
    predicted_price = round(
        predict_price(vehicle_data),
        2,
    )

    # Create MongoDB document
    prediction_document = {
        **vehicle_data,
        "predicted_price": predicted_price,
        "currency": CURRENCY,
        "model_version": MODEL_VERSION,
        "created_at": datetime.utcnow(),
    }

    # Save prediction
    result = predictions_collection.insert_one(
        prediction_document
    )

    print(
        f"✓ Prediction saved: {result.inserted_id}"
    )

    # Return API response
    return PredictionResponse(
        predicted_price=predicted_price,
        currency=CURRENCY,
        model_version=MODEL_VERSION,
        status="success",
    )