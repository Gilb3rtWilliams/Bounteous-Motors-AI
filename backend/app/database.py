"""
database.py

MongoDB configuration for Bounteous Motors AI.
"""

import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "bounteous_motors_ai")

if not MONGODB_URI:
    raise ValueError(
        "MONGODB_URI was not found in the .env file."
    )

# ============================================================
# Connect to MongoDB
# ============================================================

try:

    client = MongoClient(
        MONGODB_URI,
        serverSelectionTimeoutMS=5000,
    )

    # Force a connection attempt
    client.admin.command("ping")

    print("✓ Connected to MongoDB Atlas.")

except ConnectionFailure as error:

    raise RuntimeError(
        f"Could not connect to MongoDB Atlas.\n{error}"
    )

# ============================================================
# Database
# ============================================================

db = client[DATABASE_NAME]

# ============================================================
# Collections
# ============================================================

predictions_collection = db["predictions"]