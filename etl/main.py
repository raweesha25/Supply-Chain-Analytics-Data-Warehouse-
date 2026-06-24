from extract import extract_data
from transform import transform_data

from load import (
    load_dimensions,
    load_fact_commodity_prices,
    load_fact_shipping_rates,
    load_fact_port_congestion,
    load_fact_trade_flows,
    load_fact_tariff_timeline,
    load_fact_disruption_events,
    load_fact_industry_exposure
)

print("=" * 80)
print("SUPPLY CHAIN ETL PIPELINE")
print("=" * 80)

# Extract
datasets = extract_data()

# Transform
transformed = transform_data(datasets)

print("\nTRANSFORMATION RESULTS")

for name, df in transformed.items():
    print(f"{name}: {df.shape}")

print("\nTRADE FLOWS")
print(datasets["trade_flows"].dtypes)

print("\nTARIFF TIMELINE")
print(datasets["tariff_timeline"].dtypes)

print("\nDISRUPTION EVENTS")
print(datasets["disruption_events"].dtypes)

print("\nINDUSTRY EXPOSURE")
print(datasets["industry_exposure"].dtypes)

# Load Dimensions
load_dimensions(transformed)

# Load Fact Tables
load_fact_commodity_prices(datasets)

load_fact_shipping_rates(datasets)

load_fact_port_congestion(datasets)

load_fact_trade_flows(datasets)

load_fact_tariff_timeline(datasets)

load_fact_disruption_events(datasets)

load_fact_industry_exposure(datasets)