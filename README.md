# Global Logistics Business Intelligence & Analytics

**End-to-End Logistics BI Project | Python • PostgreSQL • SQL • Tableau**

## Project Overview

Global Logistics Business Intelligence & Analytics is an end-to-end Business Intelligence project designed to transform logistics data into actionable business insights.

The project covers shipment operations, financial performance, customers, drivers, vehicles, warehouses, weather conditions, and transportation routes through a centralized PostgreSQL data warehouse and interactive Tableau dashboards.

The solution demonstrates the complete BI workflow, from data preparation and warehouse design to SQL analysis, data validation, and dashboard development.

---

## Business Objectives

The project aims to:

- Monitor shipment and delivery performance.
- Analyze operational delays and transit efficiency.
- Evaluate logistics costs and financial performance.
- Understand customer revenue and segmentation.
- Analyze driver and vehicle-related logistics data.
- Measure the impact of weather and road conditions on shipments.
- Identify high-volume and high-delay routes.
- Monitor shipment events and operational anomalies.
- Support data-driven logistics decision-making.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data preparation, cleaning, transformation, and generation |
| Pandas | Data manipulation and processing |
| PostgreSQL | Data warehouse and relational database |
| SQL | Data modeling, analysis, indexing, and validation |
| Tableau | Interactive dashboards and business intelligence |
| DBML | Data warehouse modeling and ERD design |

---

## Data Architecture

The project uses an **Enterprise Star Schema** designed for scalable analytics and reporting.

### Dimension Tables

- `dim_date`
- `dim_customers`
- `dim_products`
- `dim_routes`
- `dim_carriers`
- `dim_drivers`
- `dim_vehicles`
- `dim_warehouses`
- `dim_weather`

### Fact Tables

- `fact_shipments`
- `fact_shipment_events`
- `fact_financials`

### Slowly Changing Dimensions

The following dimensions implement **SCD Type 2**:

- `dim_customers`
- `dim_carriers`

This allows historical changes to customer and carrier attributes to be preserved.

---

## Data Pipeline

```text
Source Data
     ↓
Python / Pandas
     ↓
Data Cleaning & Transformation
     ↓
PostgreSQL Data Warehouse
     ↓
Enterprise Star Schema
     ↓
SQL Analysis & Validation
     ↓
Tableau
     ↓
Interactive BI Dashboards


Author

Mohamed Alneel

Business Intelligence / Data Analyst

Skills demonstrated:

Python • Pandas • SQL • PostgreSQL • Tableau • Data Warehousing • ETL • Data Analysis • Data Visualization
