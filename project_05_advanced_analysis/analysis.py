import pandas as pd
import matplotlib.pyplot as plt

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

# 7.1 revenue by country (bar chart)

plt.figure(figsize=(8, 5))
plt.bar(revenue_by_country.index, revenue_by_country.values)

plt.title("Revenue by Country")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.tight_layout()
plt.savefig("plots/revenue_by_country.png")
plt.close()

# 7.2 Revenue over time (line chart )

plt.figure(figsize=(10,5))

plt.plot(
    monthly_revenue["order_month"].astype(str),
    monthly_revenue["revenue"]
)

plt.title("Revenue Over Time (Monthly)")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("plots/revenue_over_time.png")
plt.close()

# Top customers by revenue 

top_customers = (
    df
    .groupby("customer_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop customers by revenue:")
print(top_customers)

# 7.3 Top customers (bar chart)

plt.figure(figsize=(8, 5))
plt.bar(top_customers.index.astype(str), top_customers.values)

plt.title("Top 10 Customer by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue")

plt.tight_layout()
plt.savefig("plots/top_customer.png")
plt.close()