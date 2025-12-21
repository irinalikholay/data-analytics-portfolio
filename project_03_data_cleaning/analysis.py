import pandas as pd

df = pd.read_csv("data/customer_raw.csv")

print(df.head())
print(df.info())