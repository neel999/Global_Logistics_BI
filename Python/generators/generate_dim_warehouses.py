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
from faker import Faker

from utils.warehouses_data import (
    WAREHOUSE_TYPES,
    COUNTRIES,
    CITIES,
    REGIONS,
    WAREHOUSE_NAMES,
)

# ==========================================
# Configuration
# ==========================================

fake = Faker()

random.seed(42)
Faker.seed(42)

NUMBER_OF_WAREHOUSES = 300

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "dim_warehouses.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

warehouses = []
# ==========================================
# Generate Warehouse Records
# ==========================================

for i in range(1, NUMBER_OF_WAREHOUSES + 1):

    country = random.choice(COUNTRIES)

    city = random.choice(CITIES[country])

    warehouse = {

        "warehouse_key": i,

        "warehouse_code": f"WH{i:05}",

        "warehouse_name": random.choice(WAREHOUSE_NAMES),

        "warehouse_type": random.choice(WAREHOUSE_TYPES),

        "city": city,

        "country": country,

        "operating_region": random.choice(REGIONS),

        "storage_capacity_tons": round(
            random.uniform(500, 50000),
            2
        ),

        "temperature_controlled": random.choice([
            True,
            True,
            False
        ]),

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

    warehouses.append(warehouse)
# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(warehouses)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "warehouse_key",
        "warehouse_code",
        "warehouse_name",
        "warehouse_type",
        "city",
        "country",
        "operating_region",
        "storage_capacity_tons",
        "temperature_controlled",
        "active_status",
        "created_at",
        "updated_at",
        "source_system",
    ]
]

# ==========================================
# Data Quality Checks
# ==========================================

assert df["warehouse_key"].is_unique, "Duplicate warehouse_key found."

assert df["warehouse_code"].is_unique, "Duplicate warehouse_code found."

assert df["warehouse_key"].isnull().sum() == 0

assert df["warehouse_code"].isnull().sum() == 0

print("=" * 50)
print("Warehouse Dimension Validation Passed")
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
print("Warehouse Dimension Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nWarehouse Type Distribution")
print(df["warehouse_type"].value_counts())

print("\nCountries")
print(df["country"].value_counts())

print("\nTemperature Controlled")
print(df["temperature_controlled"].value_counts())

print("\nActive Warehouses")
print(df["active_status"].value_counts())

print("=" * 60)