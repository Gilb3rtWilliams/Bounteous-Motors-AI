"""
evaluation.py

Utilities for evaluating machine learning pipelines.
"""

import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from ML.src.config import (
    METRICS_FILE,
    FIGURES_DIR,
)


def evaluate_model(
    pipeline,
    X_test,
    y_test,
    X_train=None,
    y_train=None,
):
    """
    Evaluate a trained pipeline.
    """

    predictions = pipeline.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions,
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions,
        )
    )

    r2 = r2_score(
        y_test,
        predictions,
    )

    metrics = {
        "MAE": float(mae),
        "RMSE": float(rmse),
        "R²": float(r2),
    }

    if X_train is not None:

        metrics["Train R²"] = float(
            pipeline.score(
                X_train,
                y_train,
            )
        )

    print_metrics(metrics)

    save_metrics(metrics)

    plot_actual_vs_predicted(
        y_test,
        predictions,
    )

    plot_residuals(
        y_test,
        predictions,
    )

    plot_feature_importance(pipeline)

    return metrics


def print_metrics(metrics):

    print("=" * 60)

    print("pipeline EVALUATION")

    print("=" * 60)

    for key, value in metrics.items():

        print(f"{key:<12}: {value:.4f}")

    print("=" * 60)


def save_metrics(metrics):

    with open(
        METRICS_FILE,
        "w",
    ) as f:

        json.dump(
            metrics,
            f,
            indent=4,
        )


def plot_actual_vs_predicted(
    y_true,
    predictions,
):

    Path(FIGURES_DIR).mkdir(
        exist_ok=True
    )

    plt.figure(figsize=(8, 8))

    plt.scatter(
        y_true,
        predictions,
        alpha=0.5,
    )

    plt.plot(

        [
            y_true.min(),
            y_true.max(),
        ],

        [
            y_true.min(),
            y_true.max(),
        ],

        linewidth=2,

    )

    plt.xlabel("Actual Price")

    plt.ylabel("Predicted Price")

    plt.title(
        "Actual vs Predicted"
    )

    plt.tight_layout()

    plt.savefig(
        Path(FIGURES_DIR)
        / "actual_vs_predicted.png"
    )

    plt.close()


def plot_residuals(
    y_true,
    predictions,
):

    residuals = y_true - predictions

    plt.figure(figsize=(8,6))

    plt.scatter(
        predictions,
        residuals,
        alpha=0.5,
    )

    plt.axhline(
        y=0,
        linestyle="--",
    )

    plt.xlabel("Predicted")

    plt.ylabel("Residual")

    plt.title("Residual Plot")

    plt.tight_layout()

    plt.savefig(
        Path(FIGURES_DIR)
        / "residual_plot.png"
    )

    plt.close()

def plot_feature_importance(pipeline):

    estimator = pipeline.named_steps["model"]

    if hasattr(estimator, "feature_importances_"):

        importance = estimator.feature_importances_

    elif hasattr(estimator, "coef_"):

        importance = np.abs(estimator.coef_)

    else:

        print("Feature importance not available for this model.")

        return

    plt.figure(figsize=(12, 6))

    plt.bar(range(len(importance)), importance)

    plt.title("Feature Importance")

    plt.tight_layout()

    plt.savefig(
        Path(FIGURES_DIR) / "feature_importance.png"
    )

    plt.close()