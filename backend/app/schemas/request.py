"""
request.py

Request schemas for the Bounteous Motors AI API.
"""

from pydantic import BaseModel, Field


class VehiclePredictionRequest(BaseModel):
    """
    Schema for a vehicle price prediction request.
    """

    Name: str = Field(..., example="Toyota Corolla GLI")
    Location: str = Field(..., example="Nairobi")
    Year: int = Field(..., ge=1900, le=2100, example=2018)
    Kilometers_Driven: float = Field(..., ge=0, example=65000)
    Fuel_Type: str = Field(..., example="Petrol")
    Transmission: str = Field(..., example="Manual")
    Owner_Type: str = Field(..., example="First")
    Mileage: float = Field(..., ge=0, example=18.4)
    Engine: float = Field(..., ge=0, example=1800)
    Power: float = Field(..., ge=0, example=138)
    Seats: int = Field(..., ge=1, le=20, example=5)

    class Config:
        json_schema_extra = {
            "example": {
                "Name": "Toyota Corolla GLI",
                "Location": "Nairobi",
                "Year": 2018,
                "Kilometers_Driven": 65000,
                "Fuel_Type": "Petrol",
                "Transmission": "Manual",
                "Owner_Type": "First",
                "Mileage": 18.4,
                "Engine": 1800,
                "Power": 138,
                "Seats": 5
            }
        }