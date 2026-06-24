from sqlalchemy import create_engine
import pandas as pd


def get_engine():
    engine = create_engine(
        "postgresql+psycopg://postgres:postgres123@localhost:5432/warehouse"
    )
    return engine


def load_dimensions(transformed):

    engine = get_engine()

    transformed["dim_date"].to_sql(
        "dim_date",
        engine,
        if_exists="replace",
        index=False
    )

    transformed["dim_commodity"].to_sql(
        "dim_commodity",
        engine,
        if_exists="replace",
        index=False
    )

    transformed["dim_industry"].to_sql(
        "dim_industry",
        engine,
        if_exists="replace",
        index=False
    )

    transformed["dim_port"].to_sql(
        "dim_port",
        engine,
        if_exists="replace",
        index=False
    )

    print("\nDimensions Loaded Successfully!")

def load_fact_commodity_prices(datasets):

    engine = get_engine()

    fact_df = datasets["commodity_prices_supply_chain"].copy()

    fact_df["date"] = pd.to_datetime(fact_df["date"])

    fact_df.to_sql(
        "fact_commodity_prices",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"\nLoaded {len(fact_df)} rows into fact_commodity_prices"
    )

def load_fact_shipping_rates(datasets):

    engine = get_engine()

    fact_df = datasets["shipping_rates"].copy()

    fact_df["date"] = pd.to_datetime(
        fact_df["date"]
    )

    fact_df.to_sql(
        "fact_shipping_rates",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"Loaded {len(fact_df)} rows into fact_shipping_rates."
    )


def load_fact_port_congestion(datasets):

    engine = get_engine()

    fact_df = datasets["port_congestion"].copy()

    fact_df["week_start"] = pd.to_datetime(
        fact_df["week_start"]
    )

    fact_df.to_sql(
        "fact_port_congestion",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"Loaded {len(fact_df)} rows into fact_port_congestion."
    )

def load_fact_trade_flows(datasets):

    engine = get_engine()

    fact_df = datasets["trade_flows"].copy()

    # Convert integer flags to booleans
    fact_df["trade_active"] = (
        fact_df["trade_active"]
        .astype(int)
        .astype(bool)
    )

    fact_df["supply_chain_integrated"] = (
        fact_df["supply_chain_integrated"]
        .astype(int)
        .astype(bool)
    )

    fact_df.to_sql(
        "fact_trade_flows",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"Loaded {len(fact_df)} rows into fact_trade_flows."
    )

def load_fact_tariff_timeline(datasets):

    engine = get_engine()

    fact_df = datasets["tariff_timeline"].copy()

    fact_df["date"] = pd.to_datetime(
        fact_df["date"]
    )

    bool_columns = [
        "is_trump_1_0",
        "is_biden",
        "is_trump_2_0",
        "is_retaliation",
        "is_section_232",
        "is_section_301",
        "is_ieepa"
    ]

    for col in bool_columns:
        fact_df[col] = fact_df[col].astype(bool)

    fact_df.to_sql(
        "fact_tariff_timeline",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"Loaded {len(fact_df)} rows into fact_tariff_timeline."
    )

def load_fact_disruption_events(datasets):

    engine = get_engine()

    fact_df = datasets["disruption_events"].copy()

    fact_df["date"] = pd.to_datetime(
        fact_df["date"]
    )

    bool_columns = [
        "is_pandemic",
        "is_geopolitical",
        "is_natural",
        "is_financial",
        "straits_affected",
        "port_closure"
    ]

    for col in bool_columns:
        fact_df[col] = fact_df[col].astype(bool)

    fact_df.to_sql(
        "fact_disruption_events",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"Loaded {len(fact_df)} rows into fact_disruption_events."
    )

def load_fact_industry_exposure(datasets):

    engine = get_engine()

    fact_df = datasets["industry_exposure"].copy()

    fact_df.to_sql(
        "fact_industry_exposure",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"Loaded {len(fact_df)} rows into fact_industry_exposure."
    )