import pandas as pd

df = pd.read_csv("employees.csv")
print("raw data loaded")
print(df.head())
print(df.info())
print(df.isnull().sum())
df = df.drop_duplicates()
df['Price'] = df['Price'].fillna(0)
df['Product'] = df['Product'].fillna("Unknown")
df['Total_Sales'] = df['Quantity'] * df['Price']
df['Date'] = pd.to_datetime(df['Date'])

# 4️⃣ Check results after cleaning
print("\n✅ Cleaned Data Preview:")
print(df.head())

df.to_parquet("clean_sales.parquet", index=False)
print("cleaned data saved as clean_sales.parquet")

df2 = pd.read_parquet("clean_sales.parquet")
print(df2.head())




