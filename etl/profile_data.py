import pandas as pd
from pathlib import Path

DATA_FOLDER = Path("data")

print("=" * 80)
print("SUPPLY CHAIN DATA PROFILING")
print("=" * 80)

for file in DATA_FOLDER.glob("*.csv"):

    print("\n")
    print("=" * 80)
    print(f"FILE: {file.name}")
    print("=" * 80)

    try:
        df = pd.read_csv(file)

        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("\nCOLUMN NAMES")

        for column in df.columns:
            print(f" - {column}")

    except Exception as e:
        print(f"ERROR: {e}")