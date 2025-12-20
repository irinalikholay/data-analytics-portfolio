
import matplotlib.pyplot as plt
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

#Revenue by country
revenue_by_country = (
    df
    .groupby("country") ["revenue"]
    .sum()
    .sort_values(ascending=False)

)

print("\nTotal revenue by country:")
print(revenue_by_country)


revenue_by_country.plot(kind="bar")
plt.title("Total revenue by country")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()