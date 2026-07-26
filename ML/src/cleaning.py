"""
cleaning.py

Contains reusable functions for cleaning the Bounteous Motors AI vehicle dataset.
"""

import pandas as pd
import numpy as np

from config import (
    CLEAN_DATASET,
    CURRENT_YEAR,
    SOURCE_CURRENCY,
    TARGET_CURRENCY,
    USD_TO_KES,
)

# =============================================================================
# Column Cleaning
# =============================================================================

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""

    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)

    print(f"✓ Removed {removed} duplicate rows.")

    return df


def drop_unused_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Drop columns that are not useful for training."""

    columns_to_drop = ["S.No.", "New_Price"]

    existing_columns = [col for col in columns_to_drop if col in df.columns]

    df = df.drop(columns=existing_columns)

    print(f"✓ Dropped columns: {existing_columns}")

    return df


def remove_missing_targets(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows where the target variable is missing."""

    before = len(df)

    df = df.dropna(subset=["Price"])

    removed = before - len(df)

    print(f"✓ Removed {removed} rows with missing Price.")

    return df


# =============================================================================
# Numeric Cleaning
# =============================================================================

def clean_mileage(df: pd.DataFrame) -> pd.DataFrame:
    """Convert Mileage column into numeric."""

    df["Mileage"] = (
        df["Mileage"]
        .astype(str)
        .str.extract(r"([\d.]+)")[0]
        .astype(float)
    )

    print("✓ Cleaned Mileage.")

    return df


def clean_engine(df: pd.DataFrame) -> pd.DataFrame:
    """Convert Engine column into numeric."""

    df["Engine"] = (
        df["Engine"]
        .astype(str)
        .str.extract(r"([\d.]+)")[0]
        .astype(float)
    )

    print("✓ Cleaned Engine.")

    return df


def clean_power(df: pd.DataFrame) -> pd.DataFrame:
    """Convert Power column into numeric."""

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

def convert_currency(
    df: pd.DataFrame,
    column: str,
    rate: float,
) -> pd.DataFrame:
    """
    Convert a currency column using the supplied exchange rate.
    """

    df[column] = df[column] * rate

    print(
        f"✓ Converted {column} "
        f"from {SOURCE_CURRENCY} to {TARGET_CURRENCY}."
    )

    return df


# =============================================================================
# Missing Values
# =============================================================================

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values.

    Numerical columns -> Median
    Categorical columns -> Mode
    """

    numeric_columns = df.select_dtypes(include=np.number).columns

    categorical_columns = df.select_dtypes(include="object").columns

    for column in numeric_columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(df[column].median())

            print(f"✓ Filled missing values in '{column}' using median.")

    for column in categorical_columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(df[column].mode()[0])

            print(f"✓ Filled missing values in '{column}' using mode.")

    return df


# =============================================================================
# Standardization
# =============================================================================

def standardize_categories(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize categorical values."""

    categorical_columns = df.select_dtypes(include="object").columns

    for column in categorical_columns:

        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
            .str.title()
        )

    print("✓ Standardized categorical columns.")

    return df


# =============================================================================
# Validation
# =============================================================================

def validate_dataset(df: pd.DataFrame) -> None:
    """
    Perform sanity checks on the cleaned dataset.
    """

    if df.empty:
        raise ValueError("Dataset is empty.")

    if (df["Price"] <= 0).any():
        raise ValueError("Negative or zero prices detected.")

    if (df["Year"] > CURRENT_YEAR).any():
        raise ValueError("Future vehicle years detected.")

    if (df["Year"] < 1980).any():
        print("⚠ Warning: Vehicles older than 1980 detected.")

    if (df["Seats"] <= 0).any():
        raise ValueError("Invalid seat counts detected.")

    print("✓ Dataset validation passed.")


# =============================================================================
# Save Clean Dataset
# =============================================================================

def save_clean_dataset(df: pd.DataFrame) -> None:
    """Save the cleaned dataset."""

    df.to_csv(CLEAN_DATASET, index=False)

    print(f"✓ Clean dataset saved to:\n{CLEAN_DATASET}")


# =============================================================================
# Master Cleaning Function
# =============================================================================

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Execute the complete data-cleaning pipeline.
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

    df = convert_currency(df, "Price", USD_TO_KES)

    df = handle_missing_values(df)

    df = standardize_categories(df)

    validate_dataset(df)

    save_clean_dataset(df)

    print("=" * 60)
    print("Dataset cleaning complete.")
    print("=" * 60)

    return df