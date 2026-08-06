"""
preprocessing.py

Creates the preprocessing pipeline for the Bounteous Motors AI
machine learning workflow.
"""

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from ML.src.config import (
    ENGINEERED_DATASET,
    NUMERICAL_FEATURES,
    CATEGORICAL_FEATURES,
    TARGET_COLUMN,
    TEST_SIZE,
    RANDOM_STATE,
)


# =============================================================================
# Load Engineered Dataset
# =============================================================================

def load_engineered_dataset() -> pd.DataFrame:
    """
    Load the engineered dataset.
    """

    df = pd.read_csv(ENGINEERED_DATASET)

    print(
        f"✓ Engineered dataset loaded: "
        f"{df.shape[0]:,} rows × {df.shape[1]} columns"
    )

    return df


# =============================================================================
# Create Preprocessing Pipeline
# =============================================================================

def create_preprocessor() -> ColumnTransformer:
    """
    Create the preprocessing pipeline.
    """

    numeric_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "scaler",
                StandardScaler(),
            ),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent"),
            ),
            (
                "encoder",
                OneHotEncoder(handle_unknown="ignore"),
            ),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                numeric_pipeline,
                NUMERICAL_FEATURES,
            ),
            (
                "categorical",
                categorical_pipeline,
                CATEGORICAL_FEATURES,
            ),
        ]
    )

    print("✓ Preprocessing pipeline created.")

    return preprocessor


# =============================================================================
# Prepare Data
# =============================================================================

def prepare_data(df: pd.DataFrame | None = None):
    """
    Prepare the dataset for model training.

    Parameters
    ----------
    df : pd.DataFrame, optional
        Engineered dataset already in memory.
        If None, the dataset is loaded from disk.

    Returns
    -------
    tuple
        (
            X_train,
            X_test,
            y_train,
            y_test,
            preprocessor,
        )
    """

    if df is None:

        df = load_engineered_dataset()

    else:

        print(
            f"✓ Using engineered dataset already in memory "
            f"({df.shape[0]:,} rows × {df.shape[1]} columns)"
        )

    # ============================================================
    # Features / Target
    # ============================================================

    X = df.drop(columns=[TARGET_COLUMN])

    y = df[TARGET_COLUMN]

    # ============================================================
    # Train/Test Split
    # ============================================================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    print(f"✓ Training samples: {len(X_train):,}")
    print(f"✓ Testing samples : {len(X_test):,}")

    # ============================================================
    # Create Preprocessor
    # ============================================================

    preprocessor = create_preprocessor()

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor,
    )


# =============================================================================
# Script Entry Point
# =============================================================================

if __name__ == "__main__":

    (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor,
    ) = prepare_data()

    print("\nPreprocessing complete.")

    print(f"Training samples : {X_train.shape}")
    print(f"Testing samples  : {X_test.shape}")