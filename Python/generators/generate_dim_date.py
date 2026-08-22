from pathlib import Path
import pandas as pd
from datetime import datetime

# =====================================
# Configuration
# =====================================

START_DATE = "2020-01-01"
END_DATE = "2030-12-31"

# =====================================
# Generate Date Range
# =====================================

dates = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="D"
)

df = pd.DataFrame()

df["full_date"] = dates

# =====================================
# Date Key
# =====================================

df["date_key"] = df["full_date"].dt.strftime("%Y%m%d").astype(int)

# =====================================
# Calendar Attributes
# =====================================

df["day_number"] = df["full_date"].dt.day

df["day_name"] = df["full_date"].dt.day_name()

df["day_of_week"] = df["full_date"].dt.weekday + 1

df["week_number"] = df["full_date"].dt.isocalendar().week.astype(int)

df["month_number"] = df["full_date"].dt.month

df["month_name"] = df["full_date"].dt.month_name()

df["quarter_number"] = df["full_date"].dt.quarter

df["year_number"] = df["full_date"].dt.year

# =====================================
# Fiscal Calendar
# (Fiscal Year = Calendar Year)
# =====================================

df["fiscal_month"] = df["month_number"]

df["fiscal_quarter"] = df["quarter_number"]

df["fiscal_year"] = df["year_number"]

# =====================================
# Flags
# =====================================

df["is_weekend"] = df["day_of_week"].isin([6, 7])

df["is_month_start"] = df["full_date"].dt.is_month_start

df["is_month_end"] = df["full_date"].dt.is_month_end

# =====================================
# Metadata
# =====================================

created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df["created_at"] = created_at

df["source_system"] = "Global Logistics Generator"

# =====================================
# Column Order
# =====================================

df = df[
    [
        "date_key",
        "full_date",
        "day_number",
        "day_name",
        "day_of_week",
        "week_number",
        "month_number",
        "month_name",
        "quarter_number",
        "year_number",
        "fiscal_month",
        "fiscal_quarter",
        "fiscal_year",
        "is_weekend",
        "is_month_start",
        "is_month_end",
        "created_at",
        "source_system",
    ]
]
# =====================================
# Output Directory
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

output_path = OUTPUT_DIR / "dim_date.csv"
# =====================================
# Export
# =====================================


df.to_csv(
    output_path,
    index=False
)

print("=" * 40)
print("Date Dimension Generated Successfully")
print(df.head())
print("=" * 40)
print(df.shape)