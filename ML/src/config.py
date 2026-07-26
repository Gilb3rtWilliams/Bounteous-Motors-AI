from pathlib import Path
from datetime import datetime

# ==========================
# Project Paths
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "dataset"
MODELS_DIR = BASE_DIR / "models"
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# ==========================
# Dataset Files
# ==========================
RAW_DATASET = DATASET_DIR / "used_cars_data.csv"
CLEAN_DATASET = DATASET_DIR / "cleaned_used_cars_data.csv"

# ==========================
# Model Files
# ==========================
BEST_MODEL = MODELS_DIR / "price_predictor.pkl"
PIPELINE = MODELS_DIR / "pipeline.pkl"
METADATA = MODELS_DIR / "model_metadata.json"

# ==========================
# Training Configuration
# ==========================
CURRENT_YEAR = datetime.now().year
RANDOM_STATE = 42
TEST_SIZE = 0.20
CV_FOLDS = 5

# ==========================
# Evaluation Metrics
# ==========================
METRICS = [
    "MAE",
    "RMSE",
    "R2",
    "MAPE"
]

# ==========================
# Create Required Directories
# ==========================
MODELS_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# =============================================================================
# Currency
# =============================================================================

SOURCE_CURRENCY = "USD"
TARGET_CURRENCY = "KES"

# Exchange rate used for converting the dataset prices.
# Update this value if required before training.
USD_TO_KES = 130.0

TARGET_COLUMN = "Price"

NUMERICAL_FEATURES = [
    "Kilometers_Driven",
    "Mileage",
    "Engine",
    "Power",
    "Seats",
    "Car_Age",
    "Kilometers_Per_Year",
    "Power_Per_CC"
]

CATEGORICAL_FEATURES = [
    "Brand",
    "Model",
    "Location",
    "Fuel_Type",
    "Transmission",
    "Owner_Type"
]