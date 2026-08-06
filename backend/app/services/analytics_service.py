"""
analytics_service.py

Provides analytics for saved vehicle price predictions.
"""

from backend.app.database import predictions_collection


def get_prediction_statistics():
    """
    Return overall statistics about saved predictions.
    """

    total_predictions = predictions_collection.count_documents({})

    if total_predictions == 0:
        return {
            "total_predictions": 0,
            "average_price": 0,
            "minimum_price": 0,
            "maximum_price": 0,
        }

    pipeline = [
        {
            "$group": {
                "_id": None,
                "average_price": {
                    "$avg": "$predicted_price",
                },
                "minimum_price": {
                    "$min": "$predicted_price",
                },
                "maximum_price": {
                    "$max": "$predicted_price",
                },
            }
        }
    ]

    result = list(predictions_collection.aggregate(pipeline))[0]

    return {
        "total_predictions": total_predictions,
        "average_price": round(result["average_price"], 2),
        "minimum_price": round(result["minimum_price"], 2),
        "maximum_price": round(result["maximum_price"], 2),
    }