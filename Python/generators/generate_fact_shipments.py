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

# ==========================================
# Configuration
# ==========================================

fake = Faker()

random.seed(42)
Faker.seed(42)

NUMBER_OF_SHIPMENTS = 100000

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "fact_shipments.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

shipments = []
# ==========================================
# Load Dimension Tables
# ==========================================

date_df = pd.read_csv(
    OUTPUT_DIR / "dim_date.csv"
)

customer_df = pd.read_csv(
    OUTPUT_DIR / "dim_customers.csv"
)

product_df = pd.read_csv(
    OUTPUT_DIR / "dim_products.csv"
)

carrier_df = pd.read_csv(
    OUTPUT_DIR / "dim_carriers.csv"
)
# ==========================================
# Carrier Delay Factors
# ==========================================

carrier_delay_factor = {}

for _, row in carrier_df.iterrows():

    carrier_delay_factor[row["carrier_key"]] = random.uniform(0.6, 1.8)
    route_df = pd.read_csv(
    OUTPUT_DIR / "dim_routes.csv"
)

driver_df = pd.read_csv(
    OUTPUT_DIR / "dim_drivers.csv"
)

vehicle_df = pd.read_csv(
    OUTPUT_DIR / "dim_vehicles.csv"
)

warehouse_df = pd.read_csv(
    OUTPUT_DIR / "dim_warehouses.csv"
)

weather_df = pd.read_csv(
    OUTPUT_DIR / "dim_weather.csv"
)

# ==========================================
# Extract Dimension Keys
# ==========================================

date_keys = date_df["date_key"].tolist()

customer_keys = customer_df["customer_key"].tolist()

product_keys = product_df["product_key"].tolist()

carrier_keys = carrier_df["carrier_key"].tolist()

route_keys = route_df["route_key"].tolist()

driver_keys = driver_df["driver_key"].tolist()

vehicle_keys = vehicle_df["vehicle_key"].tolist()

warehouse_keys = warehouse_df["warehouse_key"].tolist()

weather_keys = weather_df["weather_key"].tolist()

print("=" * 60)
print("Dimension Tables Loaded Successfully")
print("=" * 60)

print(f"Dates       : {len(date_keys):,}")
print(f"Customers   : {len(customer_keys):,}")
print(f"Products    : {len(product_keys):,}")
print(f"Carriers    : {len(carrier_keys):,}")
print(f"Routes      : {len(route_keys):,}")
print(f"Drivers     : {len(driver_keys):,}")
print(f"Vehicles    : {len(vehicle_keys):,}")
print(f"Warehouses  : {len(warehouse_keys):,}")
print(f"Weather     : {len(weather_keys):,}")

print("=" * 60)
# ==========================================
# Generate Shipment Facts
# ==========================================

SHIPMENT_STATUSES = [
    "Delivered",
    "In Transit",
    "Delayed",
    "Cancelled",
    "Returned"
]

for i in range(1, NUMBER_OF_SHIPMENTS + 1):

    carrier_key = random.choice(carrier_keys)

    status = random.choices(
        SHIPMENT_STATUSES,
        weights=[60, 20, 10, 5, 5],
        k=1
    )[0]

    if status == "Delivered":
        base_delay = random.uniform(0, 12)

    elif status == "In Transit":
        base_delay = random.uniform(6, 24)

    elif status == "Delayed":
        base_delay = random.uniform(24, 72)

    elif status == "Cancelled":
        base_delay = random.uniform(0, 6)

    else:  # Returned
        base_delay = random.uniform(6, 36)

    delay = min(
        base_delay * carrier_delay_factor[carrier_key],
        72
    )

    shipment = {

        "shipment_key": i,

        "shipment_id": f"SHP{i:08}",

        "date_key": random.choice(date_keys),

        "customer_key": random.choice(customer_keys),

        "product_key": random.choice(product_keys),

        "carrier_key": carrier_key,

        "route_key": random.choice(route_keys),

        "driver_key": random.choice(driver_keys),

        "vehicle_key": random.choice(vehicle_keys),

        "warehouse_key": random.choice(warehouse_keys),

        "weather_key": random.choice(weather_keys),

        "shipment_status": status,

        "weight_kg": round(
            random.uniform(10, 30000), 2
        ),

        "volume_m3": round(
            random.uniform(0.5, 120), 2
        ),

        "shipment_value_usd": round(
            random.uniform(100, 500000), 2
        ),

        "freight_cost_usd": round(
            random.uniform(50, 30000), 2
        ),

        "insurance_cost_usd": round(
            random.uniform(10, 5000), 2
        ),

        "transit_hours": round(
            random.uniform(2, 240), 2
        ),

        "delay_hours": round(delay, 2),

        "distance_km": round(
            random.uniform(20, 12000), 2
        ),

        "risk_score": round(
            random.uniform(0, 100), 2
        ),

        "created_at": CREATED_AT,

        "updated_at": CREATED_AT,

        "source_system": SOURCE_SYSTEM

    }

    shipments.append(shipment)

# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(shipments)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "shipment_key",
        "shipment_id",
        "date_key",
        "customer_key",
        "product_key",
        "carrier_key",
        "route_key",
        "driver_key",
        "vehicle_key",
        "warehouse_key",
        "weather_key",
        "shipment_status",
        "weight_kg",
        "volume_m3",
        "shipment_value_usd",
        "freight_cost_usd",
        "insurance_cost_usd",
        "transit_hours",
        "delay_hours",
        "distance_km",
        "risk_score",
        "created_at",
        "updated_at",
        "source_system"
    ]
]

# ==========================================
# Data Quality Checks
# ==========================================

assert df["shipment_key"].is_unique, \
    "Duplicate shipment_key found."

assert df["shipment_id"].is_unique, \
    "Duplicate shipment_id found."

assert df["shipment_key"].isnull().sum() == 0

assert df["shipment_id"].isnull().sum() == 0

assert len(df) == NUMBER_OF_SHIPMENTS

print("=" * 60)
print("Shipment Fact Validation Passed")
print("=" * 60)

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
print("Fact Shipments Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nShipment Status Distribution")
print(df["shipment_status"].value_counts())

print("\nAverage Shipment Value")
print(round(df["shipment_value_usd"].mean(), 2))

print("\nAverage Freight Cost")
print(round(df["freight_cost_usd"].mean(), 2))

print("\nAverage Risk Score")
print(round(df["risk_score"].mean(), 2))

print("=" * 60)