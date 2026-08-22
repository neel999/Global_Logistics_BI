import random
import sys
from pathlib import Path
from datetime import datetime

# Add project directory to Python path
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_DIR))

import pandas as pd

from utils.routes_data import (
    ORIGIN_CITIES,
    DESTINATION_CITIES,
    CITY_COUNTRY,
    TRANSPORT_MODES,
)

# ==========================================
# Configuration
# ==========================================

random.seed(42)

NUMBER_OF_ROUTES = 500

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "dim_routes.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

routes = []

# ==========================================
# Generate Routes
# ==========================================

for i in range(1, NUMBER_OF_ROUTES + 1):

    origin = random.choice(ORIGIN_CITIES)

    destination = random.choice(DESTINATION_CITIES)

    while destination == origin:
        destination = random.choice(DESTINATION_CITIES)

    transport_mode = random.choice(TRANSPORT_MODES)

    planned_distance = round(random.uniform(50, 2500), 2)

    estimated_transit = round(planned_distance / random.uniform(40, 80), 2)
    
    route = {

        "route_key": i,

        "route_code": f"RTE{i:05}",

        "origin_city": origin,

        "destination_city": destination,

        "origin_country": CITY_COUNTRY[origin],

        "destination_country": CITY_COUNTRY[destination],

        "transport_mode": transport_mode,

        "planned_distance_km": planned_distance,

        "estimated_transit_hours": estimated_transit,

        "created_at": CREATED_AT,

        "updated_at": CREATED_AT,

        "source_system": SOURCE_SYSTEM

    }

    routes.append(route)

# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(routes)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "route_key",
        "route_code",
        "origin_city",
        "destination_city",
        "origin_country",
        "destination_country",
        "transport_mode",
        "planned_distance_km",
        "estimated_transit_hours",
        "created_at",
        "updated_at",
        "source_system",
    ]
]

# ==========================================
# Data Validation
# ==========================================

assert df["route_key"].is_unique
assert df["route_code"].is_unique
assert df["route_key"].isnull().sum() == 0
assert df["route_code"].isnull().sum() == 0

print("=" * 60)
print("Route Dimension Validation Passed")
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
print("Route Dimension Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nTransport Mode Distribution")
print(df["transport_mode"].value_counts())

print("\nTop Origin Cities")
print(df["origin_city"].value_counts().head(10))

print("\nTop Destination Cities")
print(df["destination_city"].value_counts().head(10))

print("=" * 60)