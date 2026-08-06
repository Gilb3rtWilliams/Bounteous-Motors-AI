"""
train.py

Main training script for the Bounteous Motors AI
vehicle price prediction model.
"""

import json
import joblib

from ML.src.config import (
    PIPELINE,
    METADATA,
)

from ML.src.data_loader import load_dataset
from ML.src.cleaning import clean_dataset
from ML.src.feature_engineering import engineer_features
from ML.src.preprocessing import prepare_data
from ML.src.tuning import (
    get_models,
    tune_model,
)
from ML.src.evaluation import evaluate_model


def train():
    """
    Execute the complete machine learning training pipeline.
    """

    print("=" * 70)
    print("BOUNTEOUS MOTORS AI MODEL TRAINING")
    print("=" * 70)

    # ============================================================
    # Load Dataset
    # ============================================================

    dataset = load_dataset()

    # ============================================================
    # Clean Dataset
    # ============================================================

    cleaned_dataset = clean_dataset(dataset)

    # ============================================================
    # Feature Engineering
    # ============================================================

    engineered_dataset = engineer_features(cleaned_dataset)

    # ============================================================
    # Prepare Data
    # ============================================================

    print("\nPreparing data...")

    (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor,
    ) = prepare_data(engineered_dataset)

    # ============================================================
    # Train Candidate Models
    # ============================================================

    best_score = float("-inf")
    best_pipeline = None
    best_name = None
    best_metrics = None

    models = get_models()

    print(f"\nTraining {len(models)} candidate models...\n")

    for name, model in models.items():

        print("=" * 60)
        print(f"Training: {name}")
        print("=" * 60)

        pipeline = tune_model(
            model_name=name,
            model=model,
            X_train=X_train,
            y_train=y_train,
            preprocessor=preprocessor,
        )

        metrics = evaluate_model(
            pipeline=pipeline,
            X_test=X_test,
            y_test=y_test,
            X_train=X_train,
            y_train=y_train,
        )

        print(
            f"R²={metrics['R²']:.4f} | "
            f"MAE={metrics['MAE']:.2f} | "
            f"RMSE={metrics['RMSE']:.2f}"
        )

        if metrics["R²"] > best_score:

            best_score = metrics["R²"]
            best_pipeline = pipeline
            best_name = name
            best_metrics = metrics

    # ============================================================
    # Save Best Pipeline
    # ============================================================

    joblib.dump(best_pipeline, PIPELINE)

    print(f"\n✓ Pipeline saved to:\n{PIPELINE}")

    # ============================================================
    # Save Metadata
    # ============================================================

    metadata = {
        "best_model": best_name,
        "metrics": best_metrics,
    }

    with open(METADATA, "w") as file:
        json.dump(metadata, file, indent=4)

    print(f"✓ Metadata saved to:\n{METADATA}")

    # ============================================================
    # Training Summary
    # ============================================================

    print("\n" + "=" * 70)
    print("TRAINING COMPLETE")
    print("=" * 70)

    print(f"Best Model : {best_name}")
    print(f"R²         : {best_metrics['R²']:.4f}")
    print(f"MAE        : {best_metrics['MAE']:.2f}")
    print(f"RMSE       : {best_metrics['RMSE']:.2f}")

    return best_pipeline


if __name__ == "__main__":
    train()