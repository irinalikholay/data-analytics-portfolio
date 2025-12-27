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

# 3. Convert data types 
df["order_date"] = pd.to_datetime(df["order_date"])
print(df.dtypes)

# 4. Create revenue column
df["revenue"] = df["price"] * df["quantity"]

print("\nRevenue column created:")
print(df[["price", "quantity", "revenue"]].head())

# 5. Revenue by country
revenue_by_country = (
    df
    .groupby("country")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by country:")
print(revenue_by_country)

# 6. Revenue over time (by month)

#Extract month from order_date
df["order_month"] = df["order_date"].dt.to_period("M")

#Aggregate revenue by month 
monthly_revenue = (
    df
    .groupby("order_month")["revenue"]
    .sum()
    .reset_index()
)

print("\nMonthly revenue:")
print(monthly_revenue.head())