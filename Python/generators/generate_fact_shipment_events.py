import random
import sys
from pathlib import Path
from datetime import datetime, timedelta

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

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "fact_shipment_events.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

events = []

# ==========================================
# Load Source Tables
# ==========================================

fact_shipments_df = pd.read_csv(
    OUTPUT_DIR / "fact_shipments.csv"
)

print("=" * 60)
print("Fact Shipment Table Loaded Successfully")
print("=" * 60)

print(f"Shipments : {len(fact_shipments_df):,}")

print("=" * 60)

# ==========================================
# Event Configuration
# ==========================================

EVENT_TYPES = [

    "Shipment Created",

    "Picked Up",

    "Warehouse Arrival",

    "Warehouse Departure",

    "Customs Clearance",

    "Port Arrival",

    "Port Departure",

    "In Transit",

    "Delay Reported",

    "Out for Delivery",

    "Delivered"

]

EVENT_STATUS = [

    "Completed",

    "In Progress",

    "Delayed"

]

MIN_EVENTS = 5

MAX_EVENTS = 12

# ==========================================
# Generate Shipment Events
# ==========================================

event_key = 1

for _, shipment in fact_shipments_df.iterrows():

    shipment_key = shipment["shipment_key"]

    date_key = shipment["date_key"]

    route_key = shipment["route_key"]

    warehouse_key = shipment["warehouse_key"]

    weather_key = shipment["weather_key"]

    shipment_status = shipment["shipment_status"]

    event_count = random.randint(
        MIN_EVENTS,
        MAX_EVENTS
    )

    shipment_start = fake.date_time_between(
        start_date="-2y",
        end_date="now"
    )

    current_time = shipment_start

    selected_events = EVENT_TYPES[:event_count]

    for event in selected_events:

        current_time += timedelta(

            hours=random.randint(2, 12),

            minutes=random.randint(5, 55)

        )

        delay = max(

            0,

            int(random.gauss(20, 25))

        )

        duration = random.randint(

            15,

            180

        )

        fuel = round(

            random.uniform(5, 120),

            2

        )

        co2 = round(

            fuel * 2.68,

            2

        )

        anomaly = random.random() < 0.03

        alert = anomaly

        if event == "Delivered":

            status = "Completed"

        elif shipment_status == "Delayed":

            status = "Delayed"

        else:

            status = random.choice(EVENT_STATUS)

        event_record = {

            "event_key": event_key,

            "shipment_key": shipment_key,

            "date_key": date_key,

            "route_key": route_key,

            "warehouse_key": warehouse_key,

            "weather_key": weather_key,

            "event_timestamp": current_time,

            "event_type": event,

            "event_status": status,

            "location_name": fake.city(),

            "gps_latitude": round(
                random.uniform(-60, 60), 6
            ),

            "gps_longitude": round(
                random.uniform(-180, 180), 6
            ),

            "temperature_c": round(
                random.uniform(-5, 45), 1
            ),

            "humidity_pct": round(
                random.uniform(20, 95), 1
            ),

            "event_delay_minutes": delay,

            "event_duration_minutes": duration,

            "fuel_consumed_liters": fuel,

            "co2_emissions_kg": co2,

            "anomaly_flag": anomaly,

            "alert_sent": alert,

            "created_at": CREATED_AT,

            "updated_at": CREATED_AT,

            "source_system": SOURCE_SYSTEM

        }

        events.append(event_record)

        event_key += 1

print("=" * 60)
print("Shipment Events Generated Successfully")
print("=" * 60)
print(f"Total Events : {len(events):,}")
print("=" * 60)

# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(events)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "event_key",
        "shipment_key",
        "date_key",
        "route_key",
        "warehouse_key",
        "weather_key",
        "event_timestamp",
        "event_type",
        "event_status",
        "location_name",
        "gps_latitude",
        "gps_longitude",
        "temperature_c",
        "humidity_pct",
        "event_delay_minutes",
        "event_duration_minutes",
        "fuel_consumed_liters",
        "co2_emissions_kg",
        "anomaly_flag",
        "alert_sent",
        "created_at",
        "updated_at",
        "source_system"
    ]
]

# ==========================================
# Sort Data
# ==========================================

df = df.sort_values(
    by=[
        "shipment_key",
        "event_timestamp"
    ]
).reset_index(drop=True)

# ==========================================
# Data Quality Checks
# ==========================================

assert df["event_key"].is_unique, \
    "Duplicate event_key found."

assert df["shipment_key"].isnull().sum() == 0

assert df["event_timestamp"].isnull().sum() == 0

assert len(df) >= (
    len(fact_shipments_df) * MIN_EVENTS
)

print("=" * 60)
print("Shipment Event Validation Passed")
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
print("Fact Shipment Events Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nEvent Type Distribution")
print(
    df["event_type"].value_counts()
)

print("\nEvent Status Distribution")
print(
    df["event_status"].value_counts()
)

print("\nAverage Delay (Minutes)")
print(
    round(
        df["event_delay_minutes"].mean(),
        2
    )
)

print("\nAverage Fuel Consumption")
print(
    round(
        df["fuel_consumed_liters"].mean(),
        2
    )
)

print("\nAverage CO2 Emissions")
print(
    round(
        df["co2_emissions_kg"].mean(),
        2
    )
)

print("=" * 60)