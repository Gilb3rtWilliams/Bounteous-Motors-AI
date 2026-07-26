"""
data_loader.py

Responsible for loading the raw dataset into a Pandas DataFrame.
"""

from pathlib import Path

import pandas as pd

from config import RAW_DATASET


def load_dataset():
    """
    Load the raw vehicle dataset.

    Returns:
        pd.DataFrame: The loaded dataset.

    Raises:
        FileNotFoundError: If the dataset file does not exist.
        ValueError: If the dataset is empty.
    """

    if not RAW_DATASET.exists():
        raise FileNotFoundError(
            f"Dataset not found: {RAW_DATASET}"
        )

    df = pd.read_csv(RAW_DATASET)

    if df.empty:
        raise ValueError("The dataset is empty.")

    print(
        f"Dataset loaded successfully: "
        f"{df.shape[0]:,} rows × {df.shape[1]} columns"
    )

    return df


if __name__ == "__main__":
    dataset = load_dataset()

    print(dataset.head())