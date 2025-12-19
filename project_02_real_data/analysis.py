import os
print("CWD:", os.getcwd())
print("FILES:", os.listdir())

import os 
print("I AM RUNNING THIS FILE")
print(os.getcwd())


import pandas as pd

# Load dataset 
df = pd.read_csv("data/sales_data.csv")

print("Dataset loaded successfully")
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())


df["revenue"] = df["price"] * df["quantity"]

print("\nRevenue column added:")
print(df[["price", "quantity", "revenue"]].head())