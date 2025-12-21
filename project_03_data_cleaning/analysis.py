import pandas as pd

df = pd.read_csv("data/customer_raw.csv")

print(df.head())
print(df.info())

df["signup_date"] = pd.to_datetime(df["signup_date"])
print(df.info())