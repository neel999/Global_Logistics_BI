import random
import sys
from pathlib import Path
from datetime import datetime

import pandas as pd
from faker import Faker

# ==========================================
# Add project path
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_DIR))

from utils.product_data import (
    PRODUCTS,
    HAZARDOUS_CATEGORIES,
    TEMPERATURE_CONTROLLED,
)

# ==========================================
# Configuration
# ==========================================

fake = Faker()

random.seed(42)
Faker.seed(42)

NUMBER_OF_PRODUCTS = 1000

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "dim_products.csv"

SOURCE_SYSTEM = "Global Logistics Generator"

CREATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ==========================================
# Generate Product Records
# ==========================================

products = []

for i in range(1, NUMBER_OF_PRODUCTS + 1):

    category = random.choice(list(PRODUCTS.keys()))

    product_name = random.choice(PRODUCTS[category])

    subcategory = category

    hazardous_flag = category in HAZARDOUS_CATEGORIES

    temperature_controlled = category in TEMPERATURE_CONTROLLED

    product = {

        "product_key": i,

        "product_code": f"PROD{i:06}",

        "product_name": product_name,

        "product_category": category,

        "product_subcategory": subcategory,

        "unit_weight_kg": round(random.uniform(0.5, 150.0), 2),

        "unit_volume_m3": round(random.uniform(0.01, 5.00), 2),

        "hazardous_flag": hazardous_flag,

        "temperature_controlled": temperature_controlled,

        "created_at": CREATED_AT,

        "updated_at": CREATED_AT,

        "source_system": SOURCE_SYSTEM

    }

    products.append(product)
# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(products)

# ==========================================
# Column Order
# ==========================================

df = df[
    [
        "product_key",
        "product_code",
        "product_name",
        "product_category",
        "product_subcategory",
        "unit_weight_kg",
        "unit_volume_m3",
        "hazardous_flag",
        "temperature_controlled",
        "created_at",
        "updated_at",
        "source_system",
    ]
]

# ==========================================
# Data Quality Validation
# ==========================================

assert df["product_key"].is_unique, "Duplicate product_key found."

assert df["product_code"].is_unique, "Duplicate product_code found."

assert df["product_key"].isnull().sum() == 0

assert df["product_code"].isnull().sum() == 0

assert (df["unit_weight_kg"] > 0).all()

assert (df["unit_volume_m3"] > 0).all()

print("=" * 60)
print("Product Dimension Validation Passed")
print("=" * 60)

print(f"Total Records : {len(df):,}")
print(f"Columns       : {len(df.columns)}")

print("\nCategory Distribution")
print(df["product_category"].value_counts())

print("\nHazardous Products")
print(df["hazardous_flag"].value_counts())

print("\nTemperature Controlled")
print(df["temperature_controlled"].value_counts())

print("\nSample Records")
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
print("Product Dimension Generated Successfully")
print("=" * 60)

print(f"Records Generated : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nProduct Category Distribution")
print(df["product_category"].value_counts())

print("\nHazardous Products")
print(df["hazardous_flag"].value_counts())

print("\nTemperature Controlled Products")
print(df["temperature_controlled"].value_counts())

print("\nAverage Product Weight (kg)")
print(round(df["unit_weight_kg"].mean(), 2))

print("\nAverage Product Volume (m³)")
print(round(df["unit_volume_m3"].mean(), 2))

print("\nSample Records")
print(df.head())

print("\n" + "=" * 60)
print("Product Dimension Generation Completed Successfully")
print("=" * 60)