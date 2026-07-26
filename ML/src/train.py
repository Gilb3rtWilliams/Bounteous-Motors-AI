"""
train.py

Main training script for the Bounteous Motors AI price prediction model.
"""

import json
import joblib

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from config import (
    TARGET_COLUMN,
    TEST_SIZE,
    RANDOM_STATE,
    PIPELINE,
    METADATA,
)

from data_loader import load_dataset
from cleaning import clean_dataset
from feature_engineering import engineer_features
from preprocessing import create_preprocessor
from tuning import (
    get_models,
    tune_model,
)
from evaluation import evaluate_model


def train():

    print("=" * 70)
    print("BOUNTEOUS MOTORS AI MODEL TRAINING")
    print("=" * 70)

    # ----------------------------------------------------
    # Load Dataset
    # ----------------------------------------------------

    df = load_dataset()

    # ----------------------------------------------------
    # Clean Dataset
    # ----------------------------------------------------

    df = clean_dataset(df)

    # ----------------------------------------------------
    # Feature Engineering
    # ----------------------------------------------------

    df = engineer_features(df)

    # ----------------------------------------------------
    # Split Features / Target
    # ----------------------------------------------------

    X = df.drop(columns=[TARGET_COLUMN])

    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    # ----------------------------------------------------
    # Preprocessing
    # ----------------------------------------------------

    preprocessor = create_preprocessor()

    # ----------------------------------------------------
    # Train Models
    # ----------------------------------------------------

    best_score = float("-inf")
    best_pipeline = None
    best_name = None
    best_metrics = None

    for name, model in get_models().items():

        print(f"\nTraining {name}...")

        tuned_model = tune_model(
            name,
            model,
            X_train,
            y_train,
            preprocessor,
        )

        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", tuned_model),
            ]
        )

        pipeline.fit(X_train, y_train)

        metrics = evaluate_model(
            pipeline,
            X_test,
            y_test,
            X_train,
            y_train,
        )

        if metrics["R²"] > best_score:

            best_score = metrics["R²"]

            best_pipeline = pipeline

            best_name = name

            best_metrics = metrics

    # ----------------------------------------------------
    # Save Pipeline
    # ----------------------------------------------------

    joblib.dump(best_pipeline, PIPELINE)

    metadata = {

        "best_model": best_name,

        "metrics": best_metrics,

    }

    with open(METADATA, "w") as f:

        json.dump(metadata, f, indent=4)

    print("\nTraining Complete!")

    print(f"Best Model : {best_name}")

    print(f"R² : {best_metrics['R²']:.4f}")


if __name__ == "__main__":
    train()