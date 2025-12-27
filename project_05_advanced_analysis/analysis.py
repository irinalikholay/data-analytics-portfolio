import pandas as pd

# 1. Load data
df = pd.read_csv("data/sales_customers.csv")

#2. Basic checks 
print("\nDataset info:")
print(df.info())

print("Dataset shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())