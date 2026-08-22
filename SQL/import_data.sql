////////////////////////////////////////////////////////////
//
// Global Logistics Business Intelligence Data Warehouse
//
// File: import_data.sql
// Version: 4.0
//
////////////////////////////////////////////////////////////

-- =====================================================
-- DIMENSIONS
-- =====================================================

COPY dim_date
FROM 'D:/Global-Logistics-BI-Project/Python/output/dim_date.csv'
WITH (FORMAT csv, HEADER true);

COPY dim_customers
FROM 'D:/Global-Logistics-BI-Project/Python/output/dim_customers.csv'
WITH (FORMAT csv, HEADER true);

COPY dim_products
FROM 'D:/Global-Logistics-BI-Project/Python/output/dim_products.csv'
WITH (FORMAT csv, HEADER true);

COPY dim_routes
FROM 'D:/Global-Logistics-BI-Project/Python/output/dim_routes.csv'
WITH (FORMAT csv, HEADER true);

COPY dim_carriers
FROM 'D:/Global-Logistics-BI-Project/Python/output/dim_carriers.csv'
WITH (FORMAT csv, HEADER true);

COPY dim_drivers
FROM 'D:/Global-Logistics-BI-Project/Python/output/dim_drivers.csv'
WITH (FORMAT csv, HEADER true);

COPY dim_vehicles
FROM 'D:/Global-Logistics-BI-Project/Python/output/dim_vehicles.csv'
WITH (FORMAT csv, HEADER true);

COPY dim_warehouses
FROM 'D:/Global-Logistics-BI-Project/Python/output/dim_warehouses.csv'
WITH (FORMAT csv, HEADER true);

COPY dim_weather
FROM 'D:/Global-Logistics-BI-Project/Python/output/dim_weather.csv'
WITH (FORMAT csv, HEADER true);

-- =====================================================
-- FACT TABLES
-- =====================================================

COPY fact_shipments
FROM 'D:/Global-Logistics-BI-Project/Python/output/fact_shipments.csv'
WITH (FORMAT csv, HEADER true);

COPY fact_shipment_events
FROM 'D:/Global-Logistics-BI-Project/Python/output/fact_shipment_events.csv'
WITH (FORMAT csv, HEADER true);

COPY fact_financials
FROM 'D:/Global-Logistics-BI-Project/Python/output/fact_financials.csv'
WITH (FORMAT csv, HEADER true);

-- =====================================================
-- Finished
-- =====================================================

SELECT 'All CSV files imported successfully.' AS status;
