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

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "fact_financials.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

financials = []

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
# Financial Configuration
# ==========================================

CURRENCIES = [

    "USD"

]

MIN_FUEL_COST = 25
MAX_FUEL_COST = 5000

MIN_WAREHOUSE_COST = 20
MAX_WAREHOUSE_COST = 3000

MIN_CUSTOMS_COST = 0
MAX_CUSTOMS_COST = 8000

MIN_HANDLING_COST = 10
MAX_HANDLING_COST = 1000

MIN_OTHER_COST = 0
MAX_OTHER_COST = 500

print("Financial Configuration Loaded Successfully")
print("=" * 60)

# ==========================================
# Generate Financial Facts
# ==========================================

financial_key = 1

for _, shipment in fact_shipments_df.iterrows():

    revenue = round(
        shipment["shipment_value_usd"],
        2
    )

    freight_cost = round(
        shipment["freight_cost_usd"],
        2
    )

    insurance_cost = round(
        shipment["insurance_cost_usd"],
        2
    )

    # ==========================================
# Generate Realistic Costs
# ==========================================

    fuel_cost = round(
        revenue * random.uniform(0.03, 0.08),
    2
)

    warehouse_cost = round(
        revenue * random.uniform(0.01, 0.04),
    2
)

    customs_cost = round(
        revenue * random.uniform(0.00, 0.05),
    2
)

    handling_cost = round(
        revenue * random.uniform(0.005, 0.02),
    2
)

    other_cost = round(
        revenue * random.uniform(0.00, 0.01),
    2
)

    total_cost = round(

        freight_cost +

        fuel_cost +

        warehouse_cost +

        insurance_cost +

        customs_cost +

        handling_cost +

        other_cost,

        2

    )

    gross_profit = round(

        revenue - total_cost,

        2

    )

    if revenue > 0:

        profit_margin = round(

            (gross_profit / revenue) * 100,

            2

        )
        profit_margin = max(
            -100,
            min(
                profit_margin,
                100
            )
        )

    else:

        profit_margin = 0

    financial_record = {

        "financial_key": financial_key,

        "shipment_key": shipment["shipment_key"],

        "date_key": shipment["date_key"],

        "customer_key": shipment["customer_key"],

        "carrier_key": shipment["carrier_key"],

        "revenue_usd": revenue,

        "freight_cost_usd": freight_cost,

        "fuel_cost_usd": fuel_cost,

        "warehouse_cost_usd": warehouse_cost,

        "insurance_cost_usd": insurance_cost,

        "customs_cost_usd": customs_cost,

        "handling_cost_usd": handling_cost,

        "other_cost_usd": other_cost,

        "total_cost_usd": total_cost,

        "gross_profit_usd": gross_profit,

        "profit_margin_pct": profit_margin,

        "currency": random.choice(CURRENCIES),

        "created_at": CREATED_AT,

        "updated_at": CREATED_AT,

        "source_system": SOURCE_SYSTEM

    }

    financials.append(financial_record)

    financial_key += 1

print("=" * 60)
print("Financial Records Generated Successfully")
print("=" * 60)

print(f"Total Financial Records : {len(financials):,}")

print("=" * 60)

# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(financials)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "financial_key",
        "shipment_key",
        "date_key",
        "customer_key",
        "carrier_key",
        "revenue_usd",
        "freight_cost_usd",
        "fuel_cost_usd",
        "warehouse_cost_usd",
        "insurance_cost_usd",
        "customs_cost_usd",
        "handling_cost_usd",
        "other_cost_usd",
        "total_cost_usd",
        "gross_profit_usd",
        "profit_margin_pct",
        "currency",
        "created_at",
        "updated_at",
        "source_system"
    ]
]

# ==========================================
# Data Quality Checks
# ==========================================

assert df["financial_key"].is_unique, \
    "Duplicate financial_key found."

assert df["shipment_key"].is_unique, \
    "Duplicate shipment_key found."

assert df["financial_key"].isnull().sum() == 0

assert df["shipment_key"].isnull().sum() == 0

assert len(df) == len(fact_shipments_df)

print("=" * 60)
print("Financial Fact Validation Passed")
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
print("Fact Financials Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nAverage Revenue")
print(round(df["revenue_usd"].mean(), 2))

print("\nAverage Total Cost")
print(round(df["total_cost_usd"].mean(), 2))

print("\nAverage Gross Profit")
print(round(df["gross_profit_usd"].mean(), 2))

print("\nAverage Profit Margin (%)")
print(round(df["profit_margin_pct"].mean(), 2))

print("\nCurrency Distribution")
print(df["currency"].value_counts())

print("=" * 60)