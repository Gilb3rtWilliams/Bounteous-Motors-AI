"""
prediction_history.py

API endpoints for retrieving prediction history.
"""

from fastapi import APIRouter, HTTPException

from backend.app.repositories.prediction_repository import (
    get_all_predictions,
    get_prediction,
    delete_prediction,
    delete_all_predictions,
)

from backend.app.schemas import PredictionHistory


router = APIRouter(
    prefix="/predictions",
    tags=["Prediction History"],
)


@router.get(
    "/",
    response_model=list[PredictionHistory],
)
async def prediction_history():
    """
    Retrieve every saved prediction.
    """

    return [
        PredictionHistory(**prediction)
        for prediction in get_all_predictions()
    ]


@router.get(
    "/{prediction_id}",
    response_model=PredictionHistory,
)
async def prediction_by_id(
    prediction_id: str,
):
    """
    Retrieve a prediction by its ID.
    """

    prediction = get_prediction(
        prediction_id
    )

    if prediction is None:

        raise HTTPException(
            status_code=404,
            detail="Prediction not found.",
        )

    return PredictionHistory(**prediction)

@router.delete("/{prediction_id}")
async def remove_prediction(
    prediction_id: str,
):
    """
    Delete a saved prediction.
    """

    deleted = delete_prediction(prediction_id)

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Prediction not found.",
        )

    return {
        "status": "success",
        "message": "Prediction deleted successfully.",
    }

@router.delete("/")
async def clear_prediction_history():
    """
    Delete every saved prediction.
    """

    deleted = delete_all_predictions()

    return {
        "status": "success",
        "deleted_records": deleted,
        "message": "Prediction history cleared.",
    }