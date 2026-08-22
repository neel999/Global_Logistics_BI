////////////////////////////////////////////////////////////
//
// Global Logistics Business Intelligence Data Warehouse
//
// File         : logistics_erd_v4.sql
// Version      : 4.0
// Architecture : Enterprise Star Schema
// Database     : PostgreSQL
//
// Author       : Mohamed Alneel
//
// Source of Truth:
// create_tables_v4.sql
//
////////////////////////////////////////////////////////////


-- =====================================================
-- ENUM TYPES
-- =====================================================

CREATE TYPE "shipment_status_enum" AS ENUM (
    'Delivered',
    'In Transit',
    'Delayed',
    'Cancelled',
    'Returned'
);

CREATE TYPE "priority_level_enum" AS ENUM (
    'Low',
    'Medium',
    'High',
    'Critical'
);

CREATE TYPE "delivery_type_enum" AS ENUM (
    'Standard',
    'Express',
    'Same Day'
);


-- =====================================================
-- DIM_DATE
-- =====================================================

CREATE TABLE "dim_date" (

    "date_key" INT PRIMARY KEY,

    "full_date" date NOT NULL,

    "day_number" int,

    "day_name" varchar(20),

    "day_of_week" int,

    "week_number" int,

    "month_number" int,

    "month_name" varchar(20),

    "quarter_number" int,

    "year_number" int,

    "fiscal_month" int,

    "fiscal_quarter" int,

    "fiscal_year" int,

    "is_weekend" boolean,

    "is_month_start" boolean,

    "is_month_end" boolean,

    "created_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- DIM_CUSTOMERS
-- SCD TYPE 2
-- =====================================================

CREATE TABLE "dim_customers" (

    "customer_key" INT PRIMARY KEY,

    "customer_code" varchar(20) UNIQUE NOT NULL,

    "customer_name" varchar(100),

    "customer_type" varchar(50),

    "customer_segment" varchar(50),

    "industry" varchar(100),

    "country" varchar(50),

    "city" varchar(50),

    "registration_date" date,

    "account_manager" varchar(100),

    "credit_limit_usd" decimal(14,2),

    "active_status" boolean,

    "effective_from" date,

    "effective_to" date,

    "is_current" boolean,

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- DIM_PRODUCTS
-- =====================================================

CREATE TABLE "dim_products" (

    "product_key" INT PRIMARY KEY,

    "product_code" varchar(20) UNIQUE NOT NULL,

    "product_name" varchar(100),

    "product_category" varchar(50),

    "product_subcategory" varchar(50),

    "unit_weight_kg" decimal(12,2),

    "unit_volume_m3" decimal(12,2),

    "hazardous_flag" boolean,

    "temperature_controlled" boolean,

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- DIM_ROUTES
-- =====================================================

CREATE TABLE "dim_routes" (

    "route_key" INT PRIMARY KEY,

    "route_code" varchar(20) UNIQUE NOT NULL,

    "origin_city" varchar(50),

    "destination_city" varchar(50),

    "origin_country" varchar(50),

    "destination_country" varchar(50),

    "transport_mode" varchar(30),

    "planned_distance_km" decimal(12,2),

    "estimated_transit_hours" decimal(10,2),

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- DIM_CARRIERS
-- SCD TYPE 2
-- =====================================================

CREATE TABLE "dim_carriers" (

    "carrier_key" INT PRIMARY KEY,

    "carrier_code" varchar(20) UNIQUE NOT NULL,

    "carrier_name" varchar(100),

    "service_level" varchar(50),

    "headquarters_country" varchar(50),

    "active_status" boolean,

    "effective_from" date,

    "effective_to" date,

    "is_current" boolean,

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- DIM_DRIVERS
-- =====================================================

CREATE TABLE "dim_drivers" (

    "driver_key" INT PRIMARY KEY,

    "driver_code" varchar(20) UNIQUE NOT NULL,

    "driver_name" varchar(100),

    "nationality" varchar(50),

    "hire_date" date,

    "license_type" varchar(30),

    "years_of_experience" int,

    "employment_type" varchar(30),

    "assigned_region" varchar(50),

    "assigned_vehicle_type" varchar(50),

    "active_status" boolean,

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- DIM_VEHICLES
-- =====================================================

CREATE TABLE "dim_vehicles" (

    "vehicle_key" INT PRIMARY KEY,

    "vehicle_code" varchar(20) UNIQUE NOT NULL,

    "license_plate" varchar(20) UNIQUE NOT NULL,

    "vehicle_type" varchar(50),

    "manufacturer" varchar(50),

    "model" varchar(50),

    "model_year" int,

    "fuel_type" varchar(30),

    "cargo_capacity_kg" decimal(14,2),

    "cargo_volume_m3" decimal(14,2),

    "average_fuel_consumption" decimal(10,2),

    "maintenance_status" varchar(30),

    "purchase_date" date,

    "active_status" boolean,

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- DIM_WAREHOUSES
-- =====================================================

CREATE TABLE "dim_warehouses" (

    "warehouse_key" INT PRIMARY KEY,

    "warehouse_code" varchar(20) UNIQUE NOT NULL,

    "warehouse_name" varchar(100),

    "warehouse_type" varchar(50),

    "city" varchar(50),

    "country" varchar(50),

    "operating_region" varchar(50),

    "storage_capacity_tons" decimal(14,2),

    "temperature_controlled" boolean,

    "active_status" boolean,

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- DIM_WEATHER
-- =====================================================

CREATE TABLE "dim_weather" (

    "weather_key" INT PRIMARY KEY,

    "weather_code" varchar(20) UNIQUE NOT NULL,

    "weather_condition" varchar(50),

    "severity_level" varchar(30),

    "visibility_level" varchar(30),

    "road_condition" varchar(30),

    "transportation_impact" varchar(50),

    "active_status" boolean,

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- FACT_SHIPMENTS
-- =====================================================

CREATE TABLE "fact_shipments" (

    "shipment_key" INT PRIMARY KEY,

    "shipment_id" varchar(20) UNIQUE NOT NULL,

    "date_key" int NOT NULL,

    "customer_key" int NOT NULL,

    "product_key" int NOT NULL,

    "carrier_key" int NOT NULL,

    "route_key" int NOT NULL,

    "driver_key" int NOT NULL,

    "vehicle_key" int NOT NULL,

    "warehouse_key" int NOT NULL,

    "weather_key" int NOT NULL,

    "shipment_status" shipment_status_enum,

    "weight_kg" decimal(14,2),

    "volume_m3" decimal(14,2),

    "shipment_value_usd" decimal(14,2),

    "freight_cost_usd" decimal(14,2),

    "insurance_cost_usd" decimal(14,2),

    "transit_hours" decimal(10,2),

    "delay_hours" decimal(10,2),

    "distance_km" decimal(14,2),

    "risk_score" decimal(6,2),

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- FACT_SHIPMENT_EVENTS
-- =====================================================

CREATE TABLE "fact_shipment_events" (

    "event_key" INT PRIMARY KEY,

    "shipment_key" int NOT NULL,

    "date_key" int NOT NULL,

    "route_key" int NOT NULL,

    "warehouse_key" int NOT NULL,

    "weather_key" int NOT NULL,

    "event_timestamp" timestamp NOT NULL,

    "event_type" varchar(50),

    "event_status" varchar(30),

    "location_name" varchar(100),

    "gps_latitude" decimal(10,6),

    "gps_longitude" decimal(10,6),

    "temperature_c" decimal(6,2),

    "humidity_pct" decimal(5,2),

    "event_delay_minutes" int,

    "event_duration_minutes" int,

    "fuel_consumed_liters" decimal(10,2),

    "co2_emissions_kg" decimal(10,2),

    "anomaly_flag" boolean,

    "alert_sent" boolean,

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- FACT_FINANCIALS
-- =====================================================

CREATE TABLE "fact_financials" (

    "financial_key" INT PRIMARY KEY,

    "shipment_key" int NOT NULL,

    "date_key" int NOT NULL,

    "customer_key" int NOT NULL,

    "carrier_key" int NOT NULL,

    "revenue_usd" decimal(14,2),

    "freight_cost_usd" decimal(14,2),

    "fuel_cost_usd" decimal(14,2),

    "warehouse_cost_usd" decimal(14,2),

    "insurance_cost_usd" decimal(14,2),

    "customs_cost_usd" decimal(14,2),

    "handling_cost_usd" decimal(14,2),

    "other_cost_usd" decimal(14,2),

    "total_cost_usd" decimal(14,2),

    "gross_profit_usd" decimal(14,2),

    "profit_margin_pct" decimal(6,2),

    "currency" varchar(10),

    "created_at" timestamp,

    "updated_at" timestamp,

    "source_system" varchar(100)
);


-- =====================================================
-- TABLE COMMENTS
-- =====================================================

COMMENT ON TABLE "dim_date" IS
'Date Dimension

Grain:
One Row = One Calendar Date';


COMMENT ON TABLE "dim_customers" IS
'Customer Dimension

SCD Type 2

Grain:
One Row = One Customer Version';


COMMENT ON TABLE "dim_products" IS
'Product Dimension

Grain:
One Row = One Product';


COMMENT ON TABLE "dim_routes" IS
'Route Dimension

Grain:
One Row = One Route';


COMMENT ON TABLE "dim_carriers" IS
'Carrier Dimension

SCD Type 2

Grain:
One Row = One Carrier Version';


COMMENT ON TABLE "dim_drivers" IS
'Driver Dimension

Grain:
One Row = One Driver';


COMMENT ON TABLE "dim_vehicles" IS
'Vehicle Dimension

Grain:
One Row = One Vehicle';


COMMENT ON TABLE "dim_warehouses" IS
'Warehouse Dimension

Grain:
One Row = One Warehouse';


COMMENT ON TABLE "dim_weather" IS
'Weather Dimension

Grain:
One Row = One Weather Condition';


COMMENT ON TABLE "fact_shipments" IS
'Shipment Fact Table

Grain:
One Row = One Shipment

Contains operational shipment metrics.

Financial metrics are stored separately
in fact_financials.';


COMMENT ON TABLE "fact_shipment_events" IS
'Shipment Events Fact Table

Grain:
One Row = One Shipment Event

Stores operational tracking events,
GPS locations,
IoT sensor readings,
shipment milestones,
alerts,
and transportation monitoring data.';


COMMENT ON TABLE "fact_financials" IS
'Financial Fact Table

Grain:
One Row = One Shipment Financial Record

Stores shipment revenue,
costs,
profit,
and financial KPIs.';


-- =====================================================
-- FOREIGN KEY RELATIONSHIPS
-- =====================================================

-- FACT_SHIPMENTS → DIMENSIONS

ALTER TABLE "fact_shipments"
ADD FOREIGN KEY ("date_key")
REFERENCES "dim_date" ("date_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipments"
ADD FOREIGN KEY ("customer_key")
REFERENCES "dim_customers" ("customer_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipments"
ADD FOREIGN KEY ("product_key")
REFERENCES "dim_products" ("product_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipments"
ADD FOREIGN KEY ("carrier_key")
REFERENCES "dim_carriers" ("carrier_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipments"
ADD FOREIGN KEY ("route_key")
REFERENCES "dim_routes" ("route_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipments"
ADD FOREIGN KEY ("driver_key")
REFERENCES "dim_drivers" ("driver_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipments"
ADD FOREIGN KEY ("vehicle_key")
REFERENCES "dim_vehicles" ("vehicle_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipments"
ADD FOREIGN KEY ("warehouse_key")
REFERENCES "dim_warehouses" ("warehouse_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipments"
ADD FOREIGN KEY ("weather_key")
REFERENCES "dim_weather" ("weather_key")
DEFERRABLE INITIALLY IMMEDIATE;


-- FACT_SHIPMENT_EVENTS → FACT_SHIPMENTS

ALTER TABLE "fact_shipment_events"
ADD FOREIGN KEY ("shipment_key")
REFERENCES "fact_shipments" ("shipment_key")
DEFERRABLE INITIALLY IMMEDIATE;


-- FACT_SHIPMENT_EVENTS → DIMENSIONS

ALTER TABLE "fact_shipment_events"
ADD FOREIGN KEY ("date_key")
REFERENCES "dim_date" ("date_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipment_events"
ADD FOREIGN KEY ("route_key")
REFERENCES "dim_routes" ("route_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipment_events"
ADD FOREIGN KEY ("warehouse_key")
REFERENCES "dim_warehouses" ("warehouse_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_shipment_events"
ADD FOREIGN KEY ("weather_key")
REFERENCES "dim_weather" ("weather_key")
DEFERRABLE INITIALLY IMMEDIATE;


-- FACT_FINANCIALS → FACT_SHIPMENTS

ALTER TABLE "fact_financials"
ADD FOREIGN KEY ("shipment_key")
REFERENCES "fact_shipments" ("shipment_key")
DEFERRABLE INITIALLY IMMEDIATE;


-- FACT_FINANCIALS → DIMENSIONS

ALTER TABLE "fact_financials"
ADD FOREIGN KEY ("date_key")
REFERENCES "dim_date" ("date_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_financials"
ADD FOREIGN KEY ("customer_key")
REFERENCES "dim_customers" ("customer_key")
DEFERRABLE INITIALLY IMMEDIATE;


ALTER TABLE "fact_financials"
ADD FOREIGN KEY ("carrier_key")
REFERENCES "dim_carriers" ("carrier_key")
DEFERRABLE INITIALLY IMMEDIATE;
