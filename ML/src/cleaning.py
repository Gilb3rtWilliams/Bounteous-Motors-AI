"""
cleaning.py

Contains reusable functions for cleaning the Bounteous Motors AI vehicle dataset.
"""

import numpy as np
import pandas as pd

from ML.src.config import (
    CLEAN_DATASET,
    CURRENT_YEAR,
    SOURCE_CURRENCY,
    TARGET_CURRENCY,
    LAKH_TO_INR,
    INR_TO_KES,
    LOCATION_MAPPING,
)

# =============================================================================
# Column Cleaning
# =============================================================================

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""

    before = len(df)
    df = df.drop_duplicates()

    print(f"✓ Removed {before - len(df)} duplicate rows.")

    return df


def drop_unused_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Drop columns that are not useful for training."""

    columns_to_drop = ["S.No.", "New_Price"]

    existing_columns = [
        col for col in columns_to_drop
        if col in df.columns
    ]

    df = df.drop(columns=existing_columns)

    print(f"✓ Dropped columns: {existing_columns}")

    return df


def remove_missing_targets(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows where the target variable is missing."""

    before = len(df)

    df = df.dropna(subset=["Price"])

    print(f"✓ Removed {before - len(df)} rows with missing Price.")

    return df


# =============================================================================
# Numeric Cleaning
# =============================================================================

def clean_mileage(df: pd.DataFrame) -> pd.DataFrame:
    """Convert Mileage into numeric."""

    df["Mileage"] = (
        df["Mileage"]
        .astype(str)
        .str.extract(r"([\d.]+)")[0]
        .astype(float)
    )

    print("✓ Cleaned Mileage.")

    return df


def clean_engine(df: pd.DataFrame) -> pd.DataFrame:
    """Convert Engine into numeric."""

    df["Engine"] = (
        df["Engine"]
        .astype(str)
        .str.extract(r"([\d.]+)")[0]
        .astype(float)
    )

    print("✓ Cleaned Engine.")

    return df


def clean_power(df: pd.DataFrame) -> pd.DataFrame:
    """Convert Power into numeric."""

    df["Power"] = (
        df["Power"]
        .astype(str)
        .str.extract(r"([\d.]+)")[0]
        .astype(float)
    )

    print("✓ Cleaned Power.")

    return df


# =============================================================================
# Currency Conversion
# =============================================================================

def convert_currency(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert vehicle prices from Lakh Indian Rupees
    to Kenyan Shillings.
    """

    print(
        f"\nConverting prices from {SOURCE_CURRENCY} to {TARGET_CURRENCY}..."
    )

    df["Price"] = (
        df["Price"]
        * LAKH_TO_INR
        * INR_TO_KES
    )

    print("✓ Currency conversion complete.")

    return df


# =============================================================================
# Missing Values
# =============================================================================

def fix_invalid_seats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace invalid seat counts with NaN.
    """

    invalid = (df["Seats"] == 0).sum()

    if invalid > 0:

        df.loc[df["Seats"] == 0, "Seats"] = np.nan

        print(
            f"✓ Corrected {invalid} row(s) with invalid seat counts."
        )

    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values.

    Numerical columns -> Median
    Categorical columns -> Mode
    """

    numeric_columns = df.select_dtypes(include=np.number).columns

    categorical_columns = df.select_dtypes(include=["object", "string"]).columns

    for column in numeric_columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(df[column].median())

            print(f"✓ Filled '{column}' using median.")

    for column in categorical_columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(df[column].mode()[0])

            print(f"✓ Filled '{column}' using mode.")

    return df


# =============================================================================
# Standardization
# =============================================================================

def standardize_categories(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize categorical text."""

    categorical_columns = df.select_dtypes(include=["object", "string"]).columns

    for column in categorical_columns:

        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
            .str.title()
        )

    print("✓ Standardized categorical values.")

    return df


# =============================================================================
# Location Mapping
# =============================================================================

def map_locations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace Indian cities with Kenyan cities so that the
    model represents the Kenyan vehicle market.
    """

    df["Location"] = (
        df["Location"]
        .replace(LOCATION_MAPPING)
    )

    print("✓ Converted Indian locations to Kenyan locations.")

    return df


# =============================================================================
# Validation
# =============================================================================

def validate_dataset(df: pd.DataFrame) -> None:
    """Validate the cleaned dataset."""

    if df.empty:
        raise ValueError("Dataset is empty.")

    if (df["Price"] <= 0).any():
        raise ValueError("Invalid prices detected.")

    if (df["Year"] > CURRENT_YEAR).any():
        raise ValueError("Future vehicle years detected.")

    if (df["Year"] < 1980).any():
        print("⚠ Warning: Vehicles older than 1980 detected.")

    if (df["Seats"] <= 0).any():
        raise ValueError("Invalid seat counts detected.")

    print("✓ Dataset validation passed.")


# =============================================================================
# Save Dataset
# =============================================================================

def save_clean_dataset(df: pd.DataFrame) -> None:
    """Save the cleaned dataset."""

    df.to_csv(CLEAN_DATASET, index=False)

    print(f"✓ Clean dataset saved to:\n{CLEAN_DATASET}")


# =============================================================================
# Master Cleaning Pipeline
# =============================================================================

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Execute the full cleaning pipeline.
    """

    print("=" * 60)
    print("Starting dataset cleaning...")
    print("=" * 60)

    df = remove_duplicates(df)

    df = drop_unused_columns(df)

    df = remove_missing_targets(df)

    df = clean_mileage(df)

    df = clean_engine(df)

    df = clean_power(df)

    df = convert_currency(df)

    df = fix_invalid_seats(df)

    df = handle_missing_values(df)

    df = standardize_categories(df)

    df = map_locations(df)

    validate_dataset(df)

    save_clean_dataset(df)

    print("=" * 60)
    print("Dataset cleaning complete.")
    print("=" * 60)

    return df

# =============================================================================
# Script Entry Point
# =============================================================================

from ML.src.data_loader import load_dataset


if __name__ == "__main__":
    dataset = load_dataset()
    cleaned_dataset = clean_dataset(dataset)

    print("\nFirst five rows of the cleaned dataset:")
    print(cleaned_dataset.head())