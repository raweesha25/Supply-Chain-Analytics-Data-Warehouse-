CREATE TABLE dim_date (
    date_key SERIAL PRIMARY KEY,
    full_date DATE UNIQUE,
    month INTEGER,
    year INTEGER
);

CREATE TABLE dim_country (
    country_key SERIAL PRIMARY KEY,
    country_name VARCHAR(100),
    region VARCHAR(100)
);

CREATE TABLE dim_commodity (
    commodity_key SERIAL PRIMARY KEY,
    commodity VARCHAR(100),
    category VARCHAR(100),
    unit VARCHAR(50),
    currency VARCHAR(20)
);

CREATE TABLE dim_industry (
    industry_key SERIAL PRIMARY KEY,
    industry VARCHAR(100)
);

CREATE TABLE dim_port (
    port_key SERIAL PRIMARY KEY,
    port_name VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100)
);

-- FACT TABLE: COMMODITY PRICES

CREATE TABLE fact_commodity_prices (
    fact_id SERIAL PRIMARY KEY,
    commodity_key INTEGER,
    date_key INTEGER,

    price NUMERIC(18,4)
);

-- FACT TABLE: SHIPPING RATES

CREATE TABLE fact_shipping_rates (
    fact_id SERIAL PRIMARY KEY,
    date_key INTEGER,

    baltic_dry_index NUMERIC(18,4),
    container_rate_usd_40ft NUMERIC(18,4),
    air_cargo_rate_usd_kg NUMERIC(18,4),
    supply_chain_pressure_index NUMERIC(18,4),
    on_time_delivery_pct NUMERIC(18,4)
);

-- FACT TABLE: PORT CONGESTION

CREATE TABLE fact_port_congestion (
    fact_id SERIAL PRIMARY KEY,

    port_key INTEGER,
    date_key INTEGER,

    throughput_teu_mn NUMERIC(18,4),
    vessels_at_anchor INTEGER,
    avg_wait_days NUMERIC(18,4),
    congestion_index NUMERIC(18,4),
    port_utilization_pct NUMERIC(18,4),
    berth_delay_hrs NUMERIC(18,4)
);

-- FACT TABLE: TRADE FLOWS

CREATE TABLE fact_trade_flows (
    fact_id SERIAL PRIMARY KEY,

    date_key INTEGER,

    trade_value_bn_usd NUMERIC(18,4),
    yoy_growth_pct NUMERIC(18,4),
    effective_tariff_rate_pct NUMERIC(18,4),
    concentration_risk NUMERIC(18,4)
);

-- FACT TABLE: DISRUPTIONS

CREATE TABLE fact_disruptions (
    fact_id SERIAL PRIMARY KEY,

    date_key INTEGER,

    duration_days INTEGER,
    bdi_shock_pct NUMERIC(18,4),
    freight_rate_shock_pct NUMERIC(18,4),
    gdp_impact_pct NUMERIC(18,4),
    trade_volume_impact_pct NUMERIC(18,4),
    recovery_months INTEGER
);

CREATE TABLE fact_commodity_prices (
    fact_id SERIAL PRIMARY KEY,
    date DATE,
    year INT,
    month INT,
    commodity VARCHAR(100),
    category VARCHAR(100),
    unit VARCHAR(50),
    currency VARCHAR(20),
    price NUMERIC
);

CREATE TABLE fact_shipping_rates (

    fact_id SERIAL PRIMARY KEY,

    date DATE,

    year INT,
    month INT,

    baltic_dry_index NUMERIC,

    container_rate_usd_40ft NUMERIC,

    air_cargo_rate_usd_kg NUMERIC,

    bdi_mom_change_pct NUMERIC,

    container_yoy_pct NUMERIC,

    tanker_rate_aframax_usd_day NUMERIC,

    bulk_carrier_handysize_usd_day NUMERIC,

    supply_chain_pressure_index NUMERIC,

    on_time_delivery_pct NUMERIC
);


CREATE TABLE fact_port_congestion (

    fact_id SERIAL PRIMARY KEY,

    week_start DATE,

    year INT,

    port VARCHAR(100),

    country VARCHAR(100),

    region VARCHAR(100),

    throughput_teu_mn NUMERIC,

    vessels_at_anchor NUMERIC,

    avg_wait_days NUMERIC,

    congestion_index NUMERIC,

    port_utilization_pct NUMERIC,

    berth_delay_hrs NUMERIC
);

CREATE TABLE fact_trade_flows (

    fact_id SERIAL PRIMARY KEY,

    year INT,

    exporter VARCHAR(100),

    importer VARCHAR(100),

    trade_category VARCHAR(100),

    key_goods VARCHAR(255),

    trade_value_bn_usd NUMERIC,

    yoy_growth_pct NUMERIC,

    effective_tariff_rate_pct NUMERIC,

    trade_active BOOLEAN,

    supply_chain_integrated BOOLEAN,

    concentration_risk NUMERIC
);