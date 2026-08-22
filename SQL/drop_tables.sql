////////////////////////////////////////////////////////////
//
// Global Logistics Business Intelligence Data Warehouse
//
// File: drop_tables.sql
// Version: 4.0
// Database: PostgreSQL
//
////////////////////////////////////////////////////////////

-- ==========================================
-- Drop Fact Tables
-- ==========================================

DROP TABLE IF EXISTS fact_financials CASCADE;

DROP TABLE IF EXISTS fact_shipment_events CASCADE;

DROP TABLE IF EXISTS fact_shipments CASCADE;

-- ==========================================
-- Drop Dimension Tables
-- ==========================================

DROP TABLE IF EXISTS dim_weather CASCADE;

DROP TABLE IF EXISTS dim_warehouses CASCADE;

DROP TABLE IF EXISTS dim_vehicles CASCADE;

DROP TABLE IF EXISTS dim_drivers CASCADE;

DROP TABLE IF EXISTS dim_carriers CASCADE;

DROP TABLE IF EXISTS dim_routes CASCADE;

DROP TABLE IF EXISTS dim_products CASCADE;

DROP TABLE IF EXISTS dim_customers CASCADE;

DROP TABLE IF EXISTS dim_date CASCADE;

-- ==========================================
-- Drop ENUM Types
-- ==========================================

DROP TYPE IF EXISTS shipment_status_enum CASCADE;

DROP TYPE IF EXISTS priority_level_enum CASCADE;

DROP TYPE IF EXISTS delivery_type_enum CASCADE;

-- ==========================================
-- Verification
-- ==========================================

SELECT
    table_name
FROM
    information_schema.tables
WHERE
    table_schema = 'public'
ORDER BY
    table_name;
