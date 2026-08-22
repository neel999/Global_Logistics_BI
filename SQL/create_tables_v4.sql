////////////////////////////////////////////////////////////
//
// Global Logistics Business Intelligence Data Warehouse
//
// File         : create_tables_v4.sql
// Version      : 4.0
// Architecture : Enterprise Star Schema
// Database     : PostgreSQL
//
// Author       : Mohamed Alneel
//
////////////////////////////////////////////////////////////

-- =====================================================
-- ENUM TYPES
-- =====================================================

CREATE TYPE shipment_status_enum AS ENUM
(
    'Delivered',
    'In Transit',
    'Delayed',
    'Cancelled',
    'Returned'
);

CREATE TYPE priority_level_enum AS ENUM
(
    'Low',
    'Medium',
    'High',
    'Critical'
);

CREATE TYPE delivery_type_enum AS ENUM
(
    'Standard',
    'Express',
    'Same Day'
);

-- =====================================================
-- DIM_DATE
-- =====================================================

CREATE TABLE dim_date
(
    date_key                INTEGER PRIMARY KEY,

    full_date               DATE NOT NULL,

    day_number              INTEGER,

    day_name                VARCHAR(20),

    day_of_week             INTEGER,

    week_number             INTEGER,

    month_number            INTEGER,

    month_name              VARCHAR(20),

    quarter_number          INTEGER,

    year_number             INTEGER,

    fiscal_month            INTEGER,

    fiscal_quarter          INTEGER,

    fiscal_year             INTEGER,

    is_weekend              BOOLEAN,

    is_month_start          BOOLEAN,

    is_month_end            BOOLEAN,

    created_at              TIMESTAMP,

    source_system           VARCHAR(100)
);

COMMENT ON TABLE dim_date IS
'Date Dimension
Grain:
One Row = One Calendar Date';

-- =====================================================
-- DIM_CUSTOMERS (SCD TYPE 2)
-- =====================================================

CREATE TABLE dim_customers
(
    customer_key            INTEGER PRIMARY KEY,

    customer_code           VARCHAR(20) UNIQUE NOT NULL,

    customer_name           VARCHAR(100),

    customer_type           VARCHAR(50),

    customer_segment        VARCHAR(50),

    industry                VARCHAR(100),

    country                 VARCHAR(50),

    city                    VARCHAR(50),

    registration_date       DATE,

    account_manager         VARCHAR(100),

    credit_limit_usd        DECIMAL(14,2),

    active_status           BOOLEAN,

    effective_from          DATE,

    effective_to            DATE,

    is_current              BOOLEAN,

    created_at              TIMESTAMP,

    updated_at              TIMESTAMP,

    source_system           VARCHAR(100)
);

COMMENT ON TABLE dim_customers IS
'Customer Dimension

SCD Type 2

Grain:
One Row = One Customer Version';
-- =====================================================
-- DIM_PRODUCTS
-- =====================================================

CREATE TABLE dim_products
(
    product_key                 INTEGER PRIMARY KEY,

    product_code                VARCHAR(20) UNIQUE NOT NULL,

    product_name                VARCHAR(100),

    product_category            VARCHAR(50),

    product_subcategory         VARCHAR(50),

    unit_weight_kg              DECIMAL(12,2),

    unit_volume_m3              DECIMAL(12,2),

    hazardous_flag              BOOLEAN,

    temperature_controlled      BOOLEAN,

    created_at                  TIMESTAMP,

    updated_at                  TIMESTAMP,

    source_system               VARCHAR(100)
);

COMMENT ON TABLE dim_products IS
'Product Dimension

Grain:
One Row = One Product';

-- =====================================================
-- DIM_ROUTES
-- =====================================================

CREATE TABLE dim_routes
(
    route_key                   INTEGER PRIMARY KEY,

    route_code                  VARCHAR(20) UNIQUE NOT NULL,

    origin_city                 VARCHAR(50),

    destination_city            VARCHAR(50),

    origin_country              VARCHAR(50),

    destination_country         VARCHAR(50),

    transport_mode              VARCHAR(30),

    planned_distance_km         DECIMAL(12,2),

    estimated_transit_hours     DECIMAL(10,2),

    created_at                  TIMESTAMP,

    updated_at                  TIMESTAMP,

    source_system               VARCHAR(100)
);

COMMENT ON TABLE dim_routes IS
'Route Dimension

Grain:
One Row = One Route';

-- =====================================================
-- DIM_CARRIERS (SCD TYPE 2)
-- =====================================================

CREATE TABLE dim_carriers
(
    carrier_key                 INTEGER PRIMARY KEY,

    carrier_code                VARCHAR(20) UNIQUE NOT NULL,

    carrier_name                VARCHAR(100),

    service_level               VARCHAR(50),

    headquarters_country        VARCHAR(50),

    active_status               BOOLEAN,

    effective_from              DATE,

    effective_to                DATE,

    is_current                  BOOLEAN,

    created_at                  TIMESTAMP,

    updated_at                  TIMESTAMP,

    source_system               VARCHAR(100)
);

COMMENT ON TABLE dim_carriers IS
'Carrier Dimension

SCD Type 2

Grain:
One Row = One Carrier Version';
-- =====================================================
-- DIM_DRIVERS
-- =====================================================

CREATE TABLE dim_drivers
(
    driver_key                  INTEGER PRIMARY KEY,

    driver_code                 VARCHAR(20) UNIQUE NOT NULL,

    driver_name                 VARCHAR(100),

    nationality                 VARCHAR(50),

    hire_date                   DATE,

    license_type                VARCHAR(30),

    years_of_experience         INTEGER,

    employment_type             VARCHAR(30),

    assigned_region             VARCHAR(50),

    assigned_vehicle_type       VARCHAR(50),

    active_status               BOOLEAN,

    created_at                  TIMESTAMP,

    updated_at                  TIMESTAMP,

    source_system               VARCHAR(100)
);

COMMENT ON TABLE dim_drivers IS
'Driver Dimension

Grain:
One Row = One Driver';

-- =====================================================
-- DIM_VEHICLES
-- =====================================================

CREATE TABLE dim_vehicles
(
    vehicle_key                 INTEGER PRIMARY KEY,

    vehicle_code                VARCHAR(20) UNIQUE NOT NULL,

    license_plate               VARCHAR(20) UNIQUE NOT NULL,

    vehicle_type                VARCHAR(50),

    manufacturer                VARCHAR(50),

    model                       VARCHAR(50),

    model_year                  INTEGER,

    fuel_type                   VARCHAR(30),

    cargo_capacity_kg           DECIMAL(14,2),

    cargo_volume_m3             DECIMAL(14,2),

    average_fuel_consumption    DECIMAL(10,2),

    maintenance_status          VARCHAR(30),

    purchase_date               DATE,

    active_status               BOOLEAN,

    created_at                  TIMESTAMP,

    updated_at                  TIMESTAMP,

    source_system               VARCHAR(100)
);

COMMENT ON TABLE dim_vehicles IS
'Vehicle Dimension

Grain:
One Row = One Vehicle';

-- =====================================================
-- DIM_WAREHOUSES
-- =====================================================

CREATE TABLE dim_warehouses
(
    warehouse_key               INTEGER PRIMARY KEY,

    warehouse_code              VARCHAR(20) UNIQUE NOT NULL,

    warehouse_name              VARCHAR(100),

    warehouse_type              VARCHAR(50),

    city                        VARCHAR(50),

    country                     VARCHAR(50),

    operating_region            VARCHAR(50),

    storage_capacity_tons       DECIMAL(14,2),

    temperature_controlled      BOOLEAN,

    active_status               BOOLEAN,

    created_at                  TIMESTAMP,

    updated_at                  TIMESTAMP,

    source_system               VARCHAR(100)
);

COMMENT ON TABLE dim_warehouses IS
'Warehouse Dimension

Grain:
One Row = One Warehouse';

-- =====================================================
-- DIM_WEATHER
-- =====================================================

CREATE TABLE dim_weather
(
    weather_key                 INTEGER PRIMARY KEY,

    weather_code                VARCHAR(20) UNIQUE NOT NULL,

    weather_condition           VARCHAR(50),

    severity_level              VARCHAR(30),

    visibility_level            VARCHAR(30),

    road_condition              VARCHAR(30),

    transportation_impact       VARCHAR(50),

    active_status               BOOLEAN,

    created_at                  TIMESTAMP,

    updated_at                  TIMESTAMP,

    source_system               VARCHAR(100)
);

COMMENT ON TABLE dim_weather IS
'Weather Dimension

Grain:
One Row = One Weather Condition';
-- =====================================================
-- FACT_SHIPMENTS
-- =====================================================

CREATE TABLE fact_shipments
(
    shipment_key               INTEGER PRIMARY KEY,

    shipment_id                VARCHAR(20) UNIQUE NOT NULL,

    date_key                   INTEGER NOT NULL,

    customer_key               INTEGER NOT NULL,

    product_key                INTEGER NOT NULL,

    carrier_key                INTEGER NOT NULL,

    route_key                  INTEGER NOT NULL,

    driver_key                 INTEGER NOT NULL,

    vehicle_key                INTEGER NOT NULL,

    warehouse_key              INTEGER NOT NULL,

    weather_key                INTEGER NOT NULL,

    shipment_status            shipment_status_enum,

    weight_kg                  DECIMAL(14,2),

    volume_m3                  DECIMAL(14,2),

    shipment_value_usd         DECIMAL(14,2),

    freight_cost_usd           DECIMAL(14,2),

    insurance_cost_usd         DECIMAL(14,2),

    transit_hours              DECIMAL(10,2),

    delay_hours                DECIMAL(10,2),

    distance_km                DECIMAL(14,2),

    risk_score                 DECIMAL(6,2),

    created_at                 TIMESTAMP,

    updated_at                 TIMESTAMP,

    source_system              VARCHAR(100)
);

COMMENT ON TABLE fact_shipments IS
'Shipment Fact Table

Grain:
One Row = One Shipment

Contains operational shipment metrics.

Financial metrics are stored separately
in fact_financials.';
-- =====================================================
-- FACT_SHIPMENT_EVENTS
-- =====================================================

CREATE TABLE fact_shipment_events
(
    event_key                  INTEGER PRIMARY KEY,

    shipment_key               INTEGER NOT NULL,

    date_key                   INTEGER NOT NULL,

    route_key                  INTEGER NOT NULL,

    warehouse_key              INTEGER NOT NULL,

    weather_key                INTEGER NOT NULL,

    event_timestamp            TIMESTAMP NOT NULL,

    event_type                 VARCHAR(50),

    event_status               VARCHAR(30),

    location_name              VARCHAR(100),

    gps_latitude               DECIMAL(10,6),

    gps_longitude              DECIMAL(10,6),

    temperature_c              DECIMAL(6,2),

    humidity_pct               DECIMAL(5,2),

    event_delay_minutes        INTEGER,

    event_duration_minutes     INTEGER,

    fuel_consumed_liters       DECIMAL(10,2),

    co2_emissions_kg           DECIMAL(10,2),

    anomaly_flag               BOOLEAN,

    alert_sent                 BOOLEAN,

    created_at                 TIMESTAMP,

    updated_at                 TIMESTAMP,

    source_system              VARCHAR(100)
);

COMMENT ON TABLE fact_shipment_events IS
'Shipment Events Fact Table

Grain:
One Row = One Shipment Event

Stores operational tracking events,
GPS locations,
IoT sensor readings,
shipment milestones,
alerts,
and transportation monitoring data.';
-- =====================================================
-- FACT_FINANCIALS
-- =====================================================

CREATE TABLE fact_financials
(
    financial_key              INTEGER PRIMARY KEY,

    shipment_key               INTEGER NOT NULL,

    date_key                   INTEGER NOT NULL,

    customer_key               INTEGER NOT NULL,

    carrier_key                INTEGER NOT NULL,

    revenue_usd                DECIMAL(14,2),

    freight_cost_usd           DECIMAL(14,2),

    fuel_cost_usd              DECIMAL(14,2),

    warehouse_cost_usd         DECIMAL(14,2),

    insurance_cost_usd         DECIMAL(14,2),

    customs_cost_usd           DECIMAL(14,2),

    handling_cost_usd          DECIMAL(14,2),

    other_cost_usd             DECIMAL(14,2),

    total_cost_usd             DECIMAL(14,2),

    gross_profit_usd           DECIMAL(14,2),

    profit_margin_pct          DECIMAL(6,2),

    currency                   VARCHAR(10),

    created_at                 TIMESTAMP,

    updated_at                 TIMESTAMP,

    source_system              VARCHAR(100)
);

COMMENT ON TABLE fact_financials IS
'Financial Fact Table

Grain:
One Row = One Shipment Financial Record

Stores shipment revenue,
costs,
profit,
and financial KPIs.';
