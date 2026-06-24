import pandas as pd


def transform_data(datasets):

    transformed = {}

    # ==========================
    # DIM DATE
    # ==========================

    date_frames = []

    for table in [
        "commodity_prices_supply_chain",
        "shipping_rates",
        "disruption_events"
    ]:

        if "date" in datasets[table].columns:
            temp = datasets[table][["date"]].copy()
            date_frames.append(temp)

    dim_date = pd.concat(date_frames)

    dim_date["date"] = pd.to_datetime(
        dim_date["date"],
        format="mixed",
        errors="coerce"
    )

    dim_date = dim_date.dropna(subset=["date"])

    dim_date = dim_date.drop_duplicates()

    dim_date["month"] = dim_date["date"].dt.month
    dim_date["year"] = dim_date["date"].dt.year

    transformed["dim_date"] = dim_date

    # ==========================
    # DIM COMMODITY
    # ==========================

    dim_commodity = datasets[
        "commodity_prices_supply_chain"
    ][
        ["commodity", "category", "unit", "currency"]
    ].drop_duplicates()

    transformed["dim_commodity"] = dim_commodity

    # ==========================
    # DIM INDUSTRY
    # ==========================

    dim_industry = datasets[
        "industry_exposure"
    ][
        ["industry"]
    ].drop_duplicates()

    transformed["dim_industry"] = dim_industry

    # ==========================
    # DIM PORT
    # ==========================

    dim_port = datasets[
        "port_congestion"
    ][
        ["port", "country", "region"]
    ].drop_duplicates()

    transformed["dim_port"] = dim_port

    return transformed