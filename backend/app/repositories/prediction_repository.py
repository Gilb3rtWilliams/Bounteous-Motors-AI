from bson import ObjectId

from backend.app.database import predictions_collection


def get_all_predictions():

    predictions = []

    cursor = predictions_collection.find().sort(
        "created_at",
        -1,
    )

    for item in cursor:

        item["id"] = str(item.pop("_id"))

        predictions.append(item)

    return predictions


def get_prediction(prediction_id: str):

    prediction = predictions_collection.find_one(
        {"_id": ObjectId(prediction_id)}
    )

    if prediction is None:
        return None

    prediction["id"] = str(prediction.pop("_id"))

    return prediction


def delete_prediction(prediction_id: str):

    result = predictions_collection.delete_one(
        {"_id": ObjectId(prediction_id)}
    )

    return result.deleted_count > 0


def delete_all_predictions():

    result = predictions_collection.delete_many({})

    return result.deleted_count