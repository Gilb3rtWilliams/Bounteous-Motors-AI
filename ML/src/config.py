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
PREPROCESSOR = MODELS_DIR / "preprocessor.pkl"

# ==========================
# Dataset Files
# ==========================
RAW_DATASET = DATASET_DIR / "used_cars_data.csv"
CLEAN_DATASET = DATASET_DIR / "cleaned_used_cars_data.csv"
ENGINEERED_DATASET = DATASET_DIR / "engineered_used_cars_data.csv"

# ==========================
# Model Files
# ==========================
BEST_MODEL = MODELS_DIR / "price_predictor.pkl"
PIPELINE = MODELS_DIR / "pipeline.pkl"
METADATA = MODELS_DIR / "model_metadata.json"
METRICS_FILE = REPORTS_DIR / "metrics.json"

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

# Original dataset currency
SOURCE_CURRENCY = "Lakh INR"

# Target currency
TARGET_CURRENCY = "KES"

# Conversion constants
LAKH_TO_INR = 100_000

# Fixed exchange rate used throughout the project
# (Update this value if desired before retraining.)
INR_TO_KES = 1.48

TARGET_COLUMN = "Price"

# =============================================================================
# Location Mapping
# =============================================================================

# Maps the original Indian cities to Kenyan cities with
# similar commercial or logistical characteristics.

LOCATION_MAPPING = {
    "Mumbai": "Nairobi",
    "Delhi": "Nairobi",
    "Chennai": "Mombasa",
    "Kochi": "Mombasa",
    "Bangalore": "Nakuru",
    "Hyderabad": "Kisumu",
    "Pune": "Eldoret",
    "Ahmedabad": "Thika",
    "Jaipur": "Nyeri",
    "Coimbatore": "Naivasha",
    "Kolkata": "Kisumu",
}

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