"""
feature_engineering.py

Creates new features from the cleaned vehicle dataset.
"""

import pandas as pd

from ML.src.config import (
    CURRENT_YEAR,
    CLEAN_DATASET,
    ENGINEERED_DATASET,
)

from ML.src.cleaning import clean_dataset
from ML.src.data_loader import load_dataset

LUXURY_BRANDS = {
    "Audi",
    "BMW",
    "Jaguar",
    "Lexus",
    "Mercedes-Benz",
    "Volvo",
    "Porsche",
    "Land"
}


def extract_brand(df: pd.DataFrame) -> pd.DataFrame:
    df["Brand"] = df["Name"].str.split().str[0]
    print("✓ Brand extracted.")
    return df


def extract_model(df: pd.DataFrame) -> pd.DataFrame:
    df["Model"] = df["Name"].str.split().str[1:].str.join(" ")
    print("✓ Model extracted.")
    return df


def create_car_age(df: pd.DataFrame) -> pd.DataFrame:
    df["Car_Age"] = CURRENT_YEAR - df["Year"]
    print("✓ Car_Age created.")
    return df


def create_luxury_brand(df: pd.DataFrame) -> pd.DataFrame:
    df["Luxury_Brand"] = (
        df["Brand"]
        .isin(LUXURY_BRANDS)
        .astype(int)
    )
    print("✓ Luxury_Brand created.")
    return df


def create_kilometers_per_year(df: pd.DataFrame) -> pd.DataFrame:
    df["Kilometers_Per_Year"] = (
        df["Kilometers_Driven"] /
        df["Car_Age"].clip(lower=1)
    )
    print("✓ Kilometers_Per_Year created.")
    return df


def create_power_per_cc(df: pd.DataFrame) -> pd.DataFrame:
    df["Power_Per_CC"] = (
        df["Power"] /
        df["Engine"]
    )
    print("✓ Power_Per_CC created.")
    return df


def drop_unused_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=["Name"])
    print("✓ Name column dropped.")
    return df

def save_engineered_dataset(df: pd.DataFrame) -> None:
    """
    Save the engineered dataset.
    """

    df.to_csv(ENGINEERED_DATASET, index=False)

    print(f"✓ Engineered dataset saved to:\n{ENGINEERED_DATASET}")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 60)
    print("Starting feature engineering...")
    print("=" * 60)

    df = extract_brand(df)
    df = extract_model(df)
    df = create_car_age(df)
    df = create_luxury_brand(df)
    df = create_kilometers_per_year(df)
    df = create_power_per_cc(df)
    df = drop_unused_columns(df)

    save_engineered_dataset(df)

    print("=" * 60)
    print("Feature engineering complete.")
    print("=" * 60)

    return df

    # =============================================================================
# Script Entry Point
# =============================================================================

if __name__ == "__main__":

    # Load the raw dataset
    dataset = load_dataset()

    # Clean it first
    cleaned_dataset = clean_dataset(dataset)

    # Engineer features
    engineered_dataset = engineer_features(cleaned_dataset)

    print("\nFirst five rows of engineered dataset:\n")
    print(engineered_dataset.head())