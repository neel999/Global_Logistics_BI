////////////////////////////////////////////////////////////
//
// Global Logistics Business Intelligence Data Warehouse
//
// File: validation_queries.sql
// Version: 4.0
//
////////////////////////////////////////////////////////////

-- =====================================================
-- DATABASE INFORMATION
-- =====================================================

SELECT current_database() AS database_name;

SELECT version() AS postgresql_version;

-- =====================================================
-- TABLE RECORD COUNTS
-- =====================================================

SELECT 'dim_date' AS table_name, COUNT(*) AS total_records
FROM dim_date

UNION ALL

SELECT 'dim_customers', COUNT(*)
FROM dim_customers

UNION ALL

SELECT 'dim_products', COUNT(*)
FROM dim_products

UNION ALL

SELECT 'dim_routes', COUNT(*)
FROM dim_routes

UNION ALL

SELECT 'dim_carriers', COUNT(*)
FROM dim_carriers

UNION ALL

SELECT 'dim_drivers', COUNT(*)
FROM dim_drivers

UNION ALL

SELECT 'dim_vehicles', COUNT(*)
FROM dim_vehicles

UNION ALL

SELECT 'dim_warehouses', COUNT(*)
FROM dim_warehouses

UNION ALL

SELECT 'dim_weather', COUNT(*)
FROM dim_weather

UNION ALL

SELECT 'fact_shipments', COUNT(*)
FROM fact_shipments

UNION ALL

SELECT 'fact_shipment_events', COUNT(*)
FROM fact_shipment_events

UNION ALL

SELECT 'fact_financials', COUNT(*)
FROM fact_financials

ORDER BY table_name;

-- =====================================================
-- CHECK FOR EMPTY TABLES
-- =====================================================

SELECT
    table_name,
    total_records,
    CASE
        WHEN total_records = 0
            THEN 'FAILED'
        ELSE 'PASSED'
    END AS validation_status
FROM
(
    SELECT 'dim_date' table_name, COUNT(*) total_records FROM dim_date
    UNION ALL
    SELECT 'dim_customers', COUNT(*) FROM dim_customers
    UNION ALL
    SELECT 'dim_products', COUNT(*) FROM dim_products
    UNION ALL
    SELECT 'dim_routes', COUNT(*) FROM dim_routes
    UNION ALL
    SELECT 'dim_carriers', COUNT(*) FROM dim_carriers
    UNION ALL
    SELECT 'dim_drivers', COUNT(*) FROM dim_drivers
    UNION ALL
    SELECT 'dim_vehicles', COUNT(*) FROM dim_vehicles
    UNION ALL
    SELECT 'dim_warehouses', COUNT(*) FROM dim_warehouses
    UNION ALL
    SELECT 'dim_weather', COUNT(*) FROM dim_weather
    UNION ALL
    SELECT 'fact_shipments', COUNT(*) FROM fact_shipments
    UNION ALL
    SELECT 'fact_shipment_events', COUNT(*) FROM fact_shipment_events
    UNION ALL
    SELECT 'fact_financials', COUNT(*) FROM fact_financials
) t;

-- =====================================================
-- PRIMARY KEY VALIDATION
-- =====================================================

SELECT
'fact_shipments' AS table_name,
COUNT(*) total_records,
COUNT(DISTINCT shipment_key) unique_keys,
COUNT(*)-COUNT(DISTINCT shipment_key) duplicate_keys
FROM fact_shipments

UNION ALL

SELECT
'fact_shipment_events',
COUNT(*),
COUNT(DISTINCT event_key),
COUNT(*)-COUNT(DISTINCT event_key)
FROM fact_shipment_events

UNION ALL

SELECT
'fact_financials',
COUNT(*),
COUNT(DISTINCT financial_key),
COUNT(*)-COUNT(DISTINCT financial_key)
FROM fact_financials;

--------------------------------------------------------
-- NULL PRIMARY KEYS
--------------------------------------------------------

SELECT
'fact_shipments' table_name,
COUNT(*) null_keys
FROM fact_shipments
WHERE shipment_key IS NULL

UNION ALL

SELECT
'fact_shipment_events',
COUNT(*)
FROM fact_shipment_events
WHERE event_key IS NULL

UNION ALL

SELECT
'fact_financials',
COUNT(*)
FROM fact_financials
WHERE financial_key IS NULL;

--------------------------------------------------------
-- NULL FOREIGN KEYS
--------------------------------------------------------

SELECT
'fact_shipments.date_key',
COUNT(*)
FROM fact_shipments
WHERE date_key IS NULL

UNION ALL

SELECT
'fact_shipments.customer_key',
COUNT(*)
FROM fact_shipments
WHERE customer_key IS NULL

UNION ALL

SELECT
'fact_shipments.product_key',
COUNT(*)
FROM fact_shipments
WHERE product_key IS NULL

UNION ALL

SELECT
'fact_shipments.route_key',
COUNT(*)
FROM fact_shipments
WHERE route_key IS NULL

UNION ALL

SELECT
'fact_shipments.carrier_key',
COUNT(*)
FROM fact_shipments
WHERE carrier_key IS NULL

UNION ALL

SELECT
'fact_shipments.driver_key',
COUNT(*)
FROM fact_shipments
WHERE driver_key IS NULL

UNION ALL

SELECT
'fact_shipments.vehicle_key',
COUNT(*)
FROM fact_shipments
WHERE vehicle_key IS NULL

UNION ALL

SELECT
'fact_shipments.warehouse_key',
COUNT(*)
FROM fact_shipments
WHERE warehouse_key IS NULL

UNION ALL

SELECT
'fact_shipments.weather_key',
COUNT(*)
FROM fact_shipments
WHERE weather_key IS NULL;

--------------------------------------------------------
-- FACT SHIPMENT EVENTS NULL KEYS
--------------------------------------------------------

SELECT
'events.shipment_key',
COUNT(*)
FROM fact_shipment_events
WHERE shipment_key IS NULL

UNION ALL

SELECT
'events.date_key',
COUNT(*)
FROM fact_shipment_events
WHERE date_key IS NULL

UNION ALL

SELECT
'events.route_key',
COUNT(*)
FROM fact_shipment_events
WHERE route_key IS NULL

UNION ALL

SELECT
'events.warehouse_key',
COUNT(*)
FROM fact_shipment_events
WHERE warehouse_key IS NULL

UNION ALL

SELECT
'events.weather_key',
COUNT(*)
FROM fact_shipment_events
WHERE weather_key IS NULL;

--------------------------------------------------------
-- FACT FINANCIALS NULL KEYS
--------------------------------------------------------

SELECT
'financials.shipment_key',
COUNT(*)
FROM fact_financials
WHERE shipment_key IS NULL

UNION ALL

SELECT
'financials.date_key',
COUNT(*)
FROM fact_financials
WHERE date_key IS NULL

UNION ALL

SELECT
'financials.customer_key',
COUNT(*)
FROM fact_financials
WHERE customer_key IS NULL

UNION ALL

SELECT
'financials.carrier_key',
COUNT(*)
FROM fact_financials
WHERE carrier_key IS NULL;

-- =====================================================
-- FOREIGN KEY INTEGRITY VALIDATION
-- =====================================================

--------------------------------------------------------
-- FACT SHIPMENTS
--------------------------------------------------------

SELECT
'fact_shipments -> dim_date' AS relationship,
COUNT(*) AS orphan_records
FROM fact_shipments fs
LEFT JOIN dim_date d
ON fs.date_key = d.date_key
WHERE d.date_key IS NULL

UNION ALL

SELECT
'fact_shipments -> dim_customers',
COUNT(*)
FROM fact_shipments fs
LEFT JOIN dim_customers c
ON fs.customer_key = c.customer_key
WHERE c.customer_key IS NULL

UNION ALL

SELECT
'fact_shipments -> dim_products',
COUNT(*)
FROM fact_shipments fs
LEFT JOIN dim_products p
ON fs.product_key = p.product_key
WHERE p.product_key IS NULL

UNION ALL

SELECT
'fact_shipments -> dim_routes',
COUNT(*)
FROM fact_shipments fs
LEFT JOIN dim_routes r
ON fs.route_key = r.route_key
WHERE r.route_key IS NULL

UNION ALL

SELECT
'fact_shipments -> dim_carriers',
COUNT(*)
FROM fact_shipments fs
LEFT JOIN dim_carriers c
ON fs.carrier_key = c.carrier_key
WHERE c.carrier_key IS NULL

UNION ALL

SELECT
'fact_shipments -> dim_drivers',
COUNT(*)
FROM fact_shipments fs
LEFT JOIN dim_drivers d
ON fs.driver_key = d.driver_key
WHERE d.driver_key IS NULL

UNION ALL

SELECT
'fact_shipments -> dim_vehicles',
COUNT(*)
FROM fact_shipments fs
LEFT JOIN dim_vehicles v
ON fs.vehicle_key = v.vehicle_key
WHERE v.vehicle_key IS NULL

UNION ALL

SELECT
'fact_shipments -> dim_warehouses',
COUNT(*)
FROM fact_shipments fs
LEFT JOIN dim_warehouses w
ON fs.warehouse_key = w.warehouse_key
WHERE w.warehouse_key IS NULL

UNION ALL

SELECT
'fact_shipments -> dim_weather',
COUNT(*)
FROM fact_shipments fs
LEFT JOIN dim_weather w
ON fs.weather_key = w.weather_key
WHERE w.weather_key IS NULL;

--------------------------------------------------------
-- FACT SHIPMENT EVENTS
--------------------------------------------------------

SELECT
'events -> fact_shipments' AS relationship,
COUNT(*) AS orphan_records
FROM fact_shipment_events e
LEFT JOIN fact_shipments s
ON e.shipment_key = s.shipment_key
WHERE s.shipment_key IS NULL

UNION ALL

SELECT
'events -> dim_date',
COUNT(*)
FROM fact_shipment_events e
LEFT JOIN dim_date d
ON e.date_key = d.date_key
WHERE d.date_key IS NULL

UNION ALL

SELECT
'events -> dim_routes',
COUNT(*)
FROM fact_shipment_events e
LEFT JOIN dim_routes r
ON e.route_key = r.route_key
WHERE r.route_key IS NULL

UNION ALL

SELECT
'events -> dim_warehouses',
COUNT(*)
FROM fact_shipment_events e
LEFT JOIN dim_warehouses w
ON e.warehouse_key = w.warehouse_key
WHERE w.warehouse_key IS NULL

UNION ALL

SELECT
'events -> dim_weather',
COUNT(*)
FROM fact_shipment_events e
LEFT JOIN dim_weather w
ON e.weather_key = w.weather_key
WHERE w.weather_key IS NULL;

--------------------------------------------------------
-- FACT FINANCIALS
--------------------------------------------------------

SELECT
'financials -> fact_shipments' AS relationship,
COUNT(*) AS orphan_records
FROM fact_financials f
LEFT JOIN fact_shipments s
ON f.shipment_key = s.shipment_key
WHERE s.shipment_key IS NULL

UNION ALL

SELECT
'financials -> dim_date',
COUNT(*)
FROM fact_financials f
LEFT JOIN dim_date d
ON f.date_key = d.date_key
WHERE d.date_key IS NULL

UNION ALL

SELECT
'financials -> dim_customers',
COUNT(*)
FROM fact_financials f
LEFT JOIN dim_customers c
ON f.customer_key = c.customer_key
WHERE c.customer_key IS NULL

UNION ALL

SELECT
'financials -> dim_carriers',
COUNT(*)
FROM fact_financials f
LEFT JOIN dim_carriers c
ON f.carrier_key = c.carrier_key
WHERE c.carrier_key IS NULL;

-- =====================================================
-- BUSINESS RULES VALIDATION
-- =====================================================

--------------------------------------------------------
-- Shipment Metrics
--------------------------------------------------------

SELECT
'Negative Weight' AS validation,
COUNT(*) AS invalid_records
FROM fact_shipments
WHERE weight_kg < 0

UNION ALL

SELECT
'Negative Volume',
COUNT(*)
FROM fact_shipments
WHERE volume_m3 < 0

UNION ALL

SELECT
'Negative Distance',
COUNT(*)
FROM fact_shipments
WHERE distance_km < 0

UNION ALL

SELECT
'Negative Transit Hours',
COUNT(*)
FROM fact_shipments
WHERE transit_hours < 0

UNION ALL

SELECT
'Negative Delay',
COUNT(*)
FROM fact_shipments
WHERE delay_hours < 0;

///
Shipment Status Distribution
///

SELECT
    shipment_status,
    COUNT(*) AS total_shipments
FROM fact_shipments
GROUP BY shipment_status
ORDER BY total_shipments DESC;

///
Financial Summary
///

SELECT
    ROUND(SUM(revenue_usd),2) AS total_revenue,
    ROUND(SUM(total_cost_usd),2) AS total_cost,
    ROUND(SUM(gross_profit_usd),2) AS total_profit,
    ROUND(AVG(profit_margin_pct),2) AS avg_profit_margin
FROM fact_financials;

///
Top 10 Customers by Revenue
///

SELECT
    c.customer_name,
    ROUND(SUM(f.revenue_usd),2) AS revenue
FROM fact_financials f
JOIN dim_customers c
ON f.customer_key = c.customer_key
GROUP BY c.customer_name
ORDER BY revenue DESC
LIMIT 10;

///
Top Routes
///

SELECT
    r.origin_city,
    r.destination_city,
    COUNT(*) AS shipments
FROM fact_shipments s
JOIN dim_routes r
ON s.route_key = r.route_key
GROUP BY
    r.origin_city,
    r.destination_city
ORDER BY shipments DESC
LIMIT 10;

///
Carrier Performance
///

SELECT
    c.carrier_name,
    COUNT(*) AS shipments,
    ROUND(AVG(f.profit_margin_pct),2) AS avg_margin
FROM fact_financials f
JOIN dim_carriers c
ON f.carrier_key = c.carrier_key
GROUP BY c.carrier_name
ORDER BY shipments DESC
LIMIT 10;

///
Shipment Event Distribution
///

SELECT
    event_type,
    COUNT(*) AS total_events
FROM fact_shipment_events
GROUP BY event_type
ORDER BY total_events DESC;

///
Delay Analysis
///

SELECT
    shipment_status,
    ROUND(AVG(delay_hours),2) AS avg_delay_hours
FROM fact_shipments
GROUP BY shipment_status
ORDER BY avg_delay_hours DESC;