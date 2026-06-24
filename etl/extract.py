import pandas as pd
from pathlib import Path

DATA_PATH = Path("data")


def extract_data():
    datasets = {}

    csv_files = [
        "commodity_prices_supply_chain.csv",
        "disruption_events.csv",
        "industry_exposure.csv",
        "port_congestion.csv",
        "shipping_rates.csv",
        "tariff_timeline.csv",
        "trade_flows.csv"
    ]

    for file in csv_files:
        file_path = DATA_PATH / file

        print(f"Loading {file}...")

        df = pd.read_csv(file_path)

        datasets[file.replace(".csv", "")] = df

        print(f"Loaded {len(df)} rows")

    return datasets