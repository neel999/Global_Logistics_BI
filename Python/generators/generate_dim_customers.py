import random
import sys
from pathlib import Path

# Add the Python project folder to the module search path
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_DIR))
from pathlib import Path
from datetime import datetime

import pandas as pd
from faker import Faker

from utils.customer_data import (
    COUNTRIES,
    CITIES,
    CUSTOMER_TYPES,
    CUSTOMER_SEGMENTS,
    COMPANIES,
)

# ==========================================
# Configuration
# ==========================================

fake = Faker()

random.seed(42)
Faker.seed(42)

NUMBER_OF_CUSTOMERS = 10000

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "dim_customers.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ==========================================
# Generate Customer Records
# ==========================================

customers = []

for i in range(1, NUMBER_OF_CUSTOMERS + 1):

    country = random.choice(COUNTRIES)

    city = random.choice(CITIES[country])

    company = random.choice(list(COMPANIES.keys()))

    industry = COMPANIES[company]

    customer = {

    "customer_key": i,

    "customer_code": f"CUST{i:06}",

    "customer_name": company,

    "customer_type": random.choice(CUSTOMER_TYPES),

    "customer_segment": random.choice(CUSTOMER_SEGMENTS),

    "industry": industry,

    "country": country,

    "city": city,

        "registration_date": fake.date_between(
            start_date="-8y",
            end_date="today"
        ),

        "account_manager": fake.name(),

        "credit_limit_usd": random.choice([
            10000,
            25000,
            50000,
            100000,
            250000,
            500000
        ]),

        "active_status": random.choice([
            True,
            True,
            True,
            True,
            False
        ]),

        "effective_from": fake.date_between(
            start_date="-8y",
            end_date="today"
        ),

        "effective_to": None,

        "is_current": True,

        "created_at": CREATED_AT,

        "updated_at": CREATED_AT,

        "source_system": SOURCE_SYSTEM

    }

    customers.append(customer)
# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(customers)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "customer_key",
        "customer_code",
        "customer_name",
        "customer_type",
        "customer_segment",
        "industry",
        "country",
        "city",
        "registration_date",
        "account_manager",
        "credit_limit_usd",
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
# Data Quality Checks
# ==========================================

assert df["customer_key"].is_unique, "Duplicate customer_key found."

assert df["customer_code"].is_unique, "Duplicate customer_code found."

assert df.isnull().sum()["customer_key"] == 0

assert df.isnull().sum()["customer_code"] == 0

print("=" * 50)
print("Customer Dimension Validation Passed")
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
print("Customer Dimension Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nCustomer Type Distribution")
print(df["customer_type"].value_counts())

print("\nCustomer Segment Distribution")
print(df["customer_segment"].value_counts())

print("\nTop 10 Countries")
print(df["country"].value_counts().head(10))

print("\nActive Customers")
print(df["active_status"].value_counts())

print("=" * 60)