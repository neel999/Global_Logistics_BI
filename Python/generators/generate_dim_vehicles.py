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

from utils.vehicles_data import (
    VEHICLE_TYPES,
    MANUFACTURERS,
    MODELS,
    FUEL_TYPES,
    MAINTENANCE_STATUS,
)

# ==========================================
# Configuration
# ==========================================

fake = Faker()

random.seed(42)
Faker.seed(42)

NUMBER_OF_VEHICLES = 500

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "dim_vehicles.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

vehicles = []

# ==========================================
# Generate Vehicle Records
# ==========================================

for i in range(1, NUMBER_OF_VEHICLES + 1):

    vehicle_type = random.choice(VEHICLE_TYPES)

    manufacturer = random.choice(MANUFACTURERS)

    model = random.choice(MODELS)

    fuel_type = random.choice(FUEL_TYPES)

    maintenance_status = random.choice(MAINTENANCE_STATUS)

    vehicle = {

        "vehicle_key": i,

        "vehicle_code": f"VEH{i:05}",

        "license_plate": fake.license_plate(),

        "vehicle_type": vehicle_type,

        "manufacturer": manufacturer,

        "model": model,

        "model_year": random.randint(2018, 2026),

        "fuel_type": fuel_type,

        "cargo_capacity_kg": round(random.uniform(500, 30000), 2),

        "cargo_volume_m3": round(random.uniform(5, 120), 2),

        "average_fuel_consumption": round(random.uniform(6, 45), 2),

        "maintenance_status": maintenance_status,

        "purchase_date": fake.date_between(
            start_date="-8y",
            end_date="today"
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

    vehicles.append(vehicle)

# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(vehicles)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "vehicle_key",
        "vehicle_code",
        "license_plate",
        "vehicle_type",
        "manufacturer",
        "model",
        "model_year",
        "fuel_type",
        "cargo_capacity_kg",
        "cargo_volume_m3",
        "average_fuel_consumption",
        "maintenance_status",
        "purchase_date",
        "active_status",
        "created_at",
        "updated_at",
        "source_system",
    ]
]

# ==========================================
# Data Quality Checks
# ==========================================

assert df["vehicle_key"].is_unique, "Duplicate vehicle_key found."

assert df["vehicle_code"].is_unique, "Duplicate vehicle_code found."

assert df["vehicle_key"].isnull().sum() == 0

assert df["vehicle_code"].isnull().sum() == 0

print("=" * 50)
print("Vehicle Dimension Validation Passed")
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
print("Vehicle Dimension Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nVehicle Type Distribution")
print(df["vehicle_type"].value_counts())

print("\nFuel Type Distribution")
print(df["fuel_type"].value_counts())

print("\nMaintenance Status")
print(df["maintenance_status"].value_counts())

print("\nActive Vehicles")
print(df["active_status"].value_counts())

print("=" * 60)