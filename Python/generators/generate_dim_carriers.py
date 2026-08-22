import random
import sys
from pathlib import Path
from datetime import datetime

# ==========================================
# Add Project Path
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_DIR))

import pandas as pd

from utils.carrier_data import (
    CARRIERS,
    SERVICE_LEVELS,
    HEADQUARTERS,
)

# ==========================================
# Configuration
# ==========================================

random.seed(42)

NUMBER_OF_RECORDS = 200

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "dim_carriers.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ==========================================
# Generate Records
# ==========================================

carriers = []

for i in range(1, NUMBER_OF_RECORDS + 1):

    carrier_name = random.choice(CARRIERS)
    carrier = {

        "carrier_key": i,

        "carrier_code": f"CAR{i:05}",

        "carrier_name": carrier_name,

        "service_level": random.choice(SERVICE_LEVELS),

        "headquarters_country": HEADQUARTERS[carrier_name],

        "active_status": random.choice([
            True,
            True,
            True,
            True,
            False
        ]),

        "effective_from": datetime.strptime(
            str(datetime.now().date().replace(year=2020)),
            "%Y-%m-%d"
        ).date(),

        "effective_to": None,

        "is_current": True,

        "created_at": CREATED_AT,

        "updated_at": CREATED_AT,

        "source_system": SOURCE_SYSTEM

    }

    carriers.append(carrier)
# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(carriers)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "carrier_key",
        "carrier_code",
        "carrier_name",
        "service_level",
        "headquarters_country",
        "active_status",
        "effective_from",
        "effective_to",
        "is_current",
        "created_at",
        "updated_at",
        "source_system",
    ]
]

# ==========================================
# Data Validation
# ==========================================

assert df["carrier_key"].is_unique
assert df["carrier_code"].is_unique
assert df["carrier_key"].isnull().sum() == 0
assert df["carrier_code"].isnull().sum() == 0

print("=" * 60)
print("Carrier Dimension Validation Passed")
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
print("Carrier Dimension Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nCarrier Distribution")
print(df["carrier_name"].value_counts())

print("\nService Level Distribution")
print(df["service_level"].value_counts())

print("\nHeadquarters Distribution")
print(df["headquarters_country"].value_counts())

print("\nActive Status")
print(df["active_status"].value_counts())

print("=" * 60)
