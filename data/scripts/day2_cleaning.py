from pathlib import Path
import pandas as pd

base_path = Path(__file__).resolve().parent.parent
csv_path = base_path / "data" / "sales_data.csv"

df = pd.read_csv(csv_path)
print("✅ Raw data loaded")
print(df.head())
