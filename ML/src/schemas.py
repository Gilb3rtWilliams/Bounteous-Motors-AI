from pydantic import BaseModel

class VehicleInput(BaseModel):
    Name: str
    Location: str
    Year: int
    Kilometers_Driven: float
    Fuel_Type: str
    Transmission: str
    Owner_Type: str
    Mileage: float
    Engine: float
    Power: float
    Seats: int