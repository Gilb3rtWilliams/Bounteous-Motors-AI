from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PredictionHistory(BaseModel):
    id: str

    Name: str
    Location: str
    Year: int

    Kilometers_Driven: int

    Fuel_Type: str
    Transmission: str
    Owner_Type: str

    Mileage: float
    Engine: float
    Power: float
    Seats: int

    predicted_price: float

    currency: str
    model_version: str

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )