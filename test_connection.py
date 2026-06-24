from sqlalchemy import create_engine

try:
    engine = create_engine(
        "postgresql+psycopg://postgres:postgres123@localhost:5432/warehouse"
    )

    with engine.connect() as conn:
        print("CONNECTED SUCCESSFULLY!")

except Exception as e:
    print("ERROR:")
    print(e)