"""
predict.py

Loads the trained Bounteous Motors AI pipeline and predicts
vehicle prices using the trained machine learning pipeline.
"""

import joblib
import pandas as pd

from ML.src.config import PIPELINE
from ML.src.model_loader import MODEL_PIPELINE
from ML.src.feature_engineering import engineer_features
from ML.src.schemas import VehicleInput


def load_pipeline():
    """
    Load the trained machine learning pipeline.

    Returns:
        sklearn.pipeline.Pipeline: Trained prediction pipeline.
    """
    return joblib.load(PIPELINE)


# Load the pipeline once when this module is imported
MODEL_PIPELINE = load_pipeline()


def predict_price(vehicle: VehicleInput) -> float:
    """
    Predict the selling price of a vehicle.

    Args:
        vehicle (VehicleInput):
            Validated vehicle information.

    Returns:
        float:
            Predicted vehicle price.
    """

    # Convert the Pydantic model to a dictionary
    vehicle_data = vehicle.model_dump()

    # Convert dictionary into a DataFrame
    df = pd.DataFrame([vehicle_data])

    # Apply the same feature engineering used during training
    df = engineer_features(df)

    # Drop Year if it was removed during training
    if "Year" in df.columns and "Car_Age" in df.columns:
        df = df.drop(columns=["Year"])

    # Predict
    prediction = MODEL_PIPELINE.predict(df)

    return float(prediction[0])


if __name__ == "__main__":

    sample_vehicle = VehicleInput(
        Name="Toyota Corolla GLI",
        Location="Nairobi",
        Year=2018,
        Kilometers_Driven=65000,
        Fuel_Type="Petrol",
        Transmission="Manual",
        Owner_Type="First",
        Mileage=18.4,
        Engine=1800,
        Power=138,
        Seats=5,
    )

    predicted_price = predict_price(sample_vehicle)

    print(f"Predicted Price: {predicted_price:,.2f}")