"""
model_loader.py

Loads the trained machine learning pipeline.
"""

from pathlib import Path

import joblib

from ML.src.config import PIPELINE


def load_pipeline():
    """
    Load the trained machine learning pipeline.

    Returns
    -------
    sklearn.pipeline.Pipeline
        The trained prediction pipeline.
    """

    if not Path(PIPELINE).exists():
        raise FileNotFoundError(
            f"Pipeline not found:\n{PIPELINE}\n"
            "Run train.py to generate the trained model."
        )

    print(f"✓ Loading trained pipeline...\n{PIPELINE}")

    pipeline = joblib.load(PIPELINE)

    print("✓ Pipeline loaded successfully.")

    return pipeline


# Load once when the module is imported
MODEL_PIPELINE = load_pipeline()