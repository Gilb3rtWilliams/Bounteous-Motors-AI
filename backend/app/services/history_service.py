from bson import ObjectId
from bson.errors import InvalidId

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

    try:

        object_id = ObjectId(prediction_id)

    except InvalidId:

        return None

    prediction = predictions_collection.find_one(
        {"_id": object_id}
    )

    if prediction is None:
        return None

    prediction["id"] = str(prediction.pop("_id"))

    return prediction