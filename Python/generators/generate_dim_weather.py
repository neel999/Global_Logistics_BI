import random
import sys
from pathlib import Path
from datetime import datetime

# ==========================================
# Add Project Directory
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_DIR))

import pandas as pd

from utils.weather_data import (
    WEATHER_CONDITIONS,
    SEVERITY_LEVELS,
    VISIBILITY_LEVELS,
    ROAD_CONDITIONS,
    TRANSPORTATION_IMPACTS,
)

# ==========================================
# Configuration
# ==========================================

random.seed(42)

NUMBER_OF_WEATHER_PROFILES = 100

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "dim_weather.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

weather_profiles = []
# ==========================================
# Generate Weather Records
# ==========================================

for i in range(1, NUMBER_OF_WEATHER_PROFILES + 1):

    weather = {

        "weather_key": i,

        "weather_code": f"WTH{i:05}",

        "weather_condition": random.choice(
            WEATHER_CONDITIONS
        ),

        "severity_level": random.choice(
            SEVERITY_LEVELS
        ),

        "visibility_level": random.choice(
            VISIBILITY_LEVELS
        ),

        "road_condition": random.choice(
            ROAD_CONDITIONS
        ),

        "transportation_impact": random.choice(
            TRANSPORTATION_IMPACTS
        ),

        "active_status": random.choice([
            True,
            True,
            True,
            True,
            False
        ]),

        "created_at": CREATED_AT,

        "updated_at": CREATED_AT,

        "source_system": SOURCE_SYSTEM

    }

    weather_profiles.append(weather)
# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(weather_profiles)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "weather_key",
        "weather_code",
        "weather_condition",
        "severity_level",
        "visibility_level",
        "road_condition",
        "transportation_impact",
        "active_status",
        "created_at",
        "updated_at",
        "source_system",
    ]
]

# ==========================================
# Data Quality Checks
# ==========================================

assert df["weather_key"].is_unique, "Duplicate weather_key found."

assert df["weather_code"].is_unique, "Duplicate weather_code found."

assert df["weather_key"].isnull().sum() == 0

assert df["weather_code"].isnull().sum() == 0

print("=" * 50)
print("Weather Dimension Validation Passed")
print("=" * 50)

print(f"Total Records : {len(df):,}")
print(f"Columns       : {len(df.columns)}")

print(df.head())

# ==========================================
# Export CSV
# ==========================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================
# Summary
# ==========================================

print("\n" + "=" * 60)
print("Weather Dimension Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nWeather Conditions")
print(df["weather_condition"].value_counts())

print("\nSeverity Levels")
print(df["severity_level"].value_counts())

print("\nVisibility Levels")
print(df["visibility_level"].value_counts())

print("\nRoad Conditions")
print(df["road_condition"].value_counts())

print("\nTransportation Impact")
print(df["transportation_impact"].value_counts())

print("\nActive Status")
print(df["active_status"].value_counts())

print("=" * 60)