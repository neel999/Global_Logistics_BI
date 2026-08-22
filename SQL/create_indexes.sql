////////////////////////////////////////////////////////////
//
// Global Logistics Business Intelligence Data Warehouse
//
// File: create_indexes.sql
// Version: 4.0
//
////////////////////////////////////////////////////////////

-- =====================================================
-- FACT_SHIPMENTS
-- =====================================================

CREATE INDEX idx_fact_shipments_date
ON fact_shipments(date_key);

CREATE INDEX idx_fact_shipments_customer
ON fact_shipments(customer_key);

CREATE INDEX idx_fact_shipments_product
ON fact_shipments(product_key);

CREATE INDEX idx_fact_shipments_carrier
ON fact_shipments(carrier_key);

CREATE INDEX idx_fact_shipments_route
ON fact_shipments(route_key);

CREATE INDEX idx_fact_shipments_driver
ON fact_shipments(driver_key);

CREATE INDEX idx_fact_shipments_vehicle
ON fact_shipments(vehicle_key);

CREATE INDEX idx_fact_shipments_warehouse
ON fact_shipments(warehouse_key);

CREATE INDEX idx_fact_shipments_weather
ON fact_shipments(weather_key);

CREATE INDEX idx_fact_shipments_status
ON fact_shipments(shipment_status);

CREATE INDEX idx_fact_shipments_date_status
ON fact_shipments(date_key, shipment_status);

-- =====================================================
-- FACT_SHIPMENT_EVENTS
-- =====================================================

CREATE INDEX idx_events_shipment
ON fact_shipment_events(shipment_key);

CREATE INDEX idx_events_date
ON fact_shipment_events(date_key);

CREATE INDEX idx_events_route
ON fact_shipment_events(route_key);

CREATE INDEX idx_events_warehouse
ON fact_shipment_events(warehouse_key);

CREATE INDEX idx_events_weather
ON fact_shipment_events(weather_key);

CREATE INDEX idx_events_timestamp
ON fact_shipment_events(event_timestamp);

CREATE INDEX idx_events_type
ON fact_shipment_events(event_type);

CREATE INDEX idx_events_status
ON fact_shipment_events(event_status);

CREATE INDEX idx_events_anomaly
ON fact_shipment_events(anomaly_flag);

-- =====================================================
-- FACT_FINANCIALS
-- =====================================================

CREATE INDEX idx_financials_shipment
ON fact_financials(shipment_key);

CREATE INDEX idx_financials_date
ON fact_financials(date_key);

CREATE INDEX idx_financials_customer
ON fact_financials(customer_key);

CREATE INDEX idx_financials_carrier
ON fact_financials(carrier_key);

CREATE INDEX idx_financials_profit
ON fact_financials(gross_profit_usd);

CREATE INDEX idx_financials_margin
ON fact_financials(profit_margin_pct);

-- =====================================================
-- DIMENSIONS
-- =====================================================

CREATE INDEX idx_customer_code
ON dim_customers(customer_code);

CREATE INDEX idx_product_code
ON dim_products(product_code);

CREATE INDEX idx_route_code
ON dim_routes(route_code);

CREATE INDEX idx_carrier_code
ON dim_carriers(carrier_code);

CREATE INDEX idx_driver_code
ON dim_drivers(driver_code);

CREATE INDEX idx_vehicle_code
ON dim_vehicles(vehicle_code);

CREATE INDEX idx_vehicle_plate
ON dim_vehicles(license_plate);

CREATE INDEX idx_warehouse_code
ON dim_warehouses(warehouse_code);

CREATE INDEX idx_weather_code
ON dim_weather(weather_code);

-- =====================================================
-- End
-- =====================================================
