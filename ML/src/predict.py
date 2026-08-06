"""
predict.py

Loads the trained Bounteous Motors AI pipeline and predicts
vehicle prices using the trained machine learning pipeline.
"""

from typing import Union

import pandas as pd

from ML.src.feature_engineering import engineer_features
from ML.src.model_loader import MODEL_PIPELINE
from ML.src.schemas import VehicleInput


def predict_price(vehicle: Union[VehicleInput, dict]) -> float:
    """
    Predict the selling price of a vehicle.

    Args:
        vehicle:
            Either a VehicleInput object or a dictionary
            containing vehicle details.

    Returns:
        float:
            Predicted vehicle price.
    """

    # Convert the input into a dictionary
    if isinstance(vehicle, VehicleInput):
        vehicle_data = vehicle.model_dump()

    elif isinstance(vehicle, dict):
        vehicle_data = vehicle

    else:
        raise TypeError(
            "vehicle must be either a VehicleInput instance or a dictionary."
        )

    # Convert dictionary into a DataFrame
    df = pd.DataFrame([vehicle_data])

    # Apply feature engineering
    df = engineer_features(df)

    # Drop Year if it was removed during training
    if "Year" in df.columns and "Car_Age" in df.columns:
        df = df.drop(columns=["Year"])

    # Generate prediction
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

    print(f"Predicted Price: KES {predicted_price:,.2f}")