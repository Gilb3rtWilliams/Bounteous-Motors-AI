"""
response.py

Response schemas for the Bounteous Motors AI API.
"""

from pydantic import BaseModel


class PredictionResponse(BaseModel):
    """
    Schema returned after a successful prediction.
    """

    predicted_price: float
    currency: str
    model_version: str
    status: str