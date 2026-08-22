import random
import sys
from pathlib import Path
from datetime import datetime

# Add project directory to Python path
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_DIR))

import pandas as pd
from faker import Faker

from utils.drivers_data import (
    NATIONALITIES,
    LICENSE_TYPES,
    EMPLOYMENT_TYPES,
    REGIONS,
    VEHICLE_TYPES,
)

# ==========================================
# Configuration
# ==========================================

fake = Faker()

random.seed(42)
Faker.seed(42)

NUMBER_OF_DRIVERS = 1000

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "dim_drivers.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

drivers = []

# ==========================================
# Generate Drivers
# ==========================================

for i in range(1, NUMBER_OF_DRIVERS + 1):

    driver = {

        "driver_key": i,

        "driver_code": f"DRV{i:05}",

        "driver_name": fake.name(),

        "nationality": random.choice(NATIONALITIES),

        "hire_date": fake.date_between(
            start_date="-15y",
            end_date="-30d"
        ),

        "license_type": random.choice(LICENSE_TYPES),

        "years_of_experience": random.randint(1, 30),
        
                "employment_type": random.choice(EMPLOYMENT_TYPES),

        "assigned_region": random.choice(REGIONS),

        "assigned_vehicle_type": random.choice(VEHICLE_TYPES),

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

    drivers.append(driver)
# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(drivers)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "driver_key",
        "driver_code",
        "driver_name",
        "nationality",
        "hire_date",
        "license_type",
        "years_of_experience",
        "employment_type",
        "assigned_region",
        "assigned_vehicle_type",
        "active_status",
        "created_at",
        "updated_at",
        "source_system",
    ]
]

# ==========================================
# Data Validation
# ==========================================

assert df["driver_key"].is_unique
assert df["driver_code"].is_unique
assert df["driver_key"].isnull().sum() == 0
assert df["driver_code"].isnull().sum() == 0

print("=" * 60)
print("Driver Dimension Validation Passed")
print("=" * 60)

print(df.head())
print()

print(f"Total Records : {len(df):,}")
print(f"Columns       : {len(df.columns)}")

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
print("Driver Dimension Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nNationality Distribution")
print(df["nationality"].value_counts())

print("\nLicense Type Distribution")
print(df["license_type"].value_counts())

print("\nEmployment Type Distribution")
print(df["employment_type"].value_counts())

print("\nAssigned Region Distribution")
print(df["assigned_region"].value_counts())

print("\nActive Status")
print(df["active_status"].value_counts())

print("=" * 60)