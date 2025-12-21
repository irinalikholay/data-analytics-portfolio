import pandas as pd

df = pd.read_csv("data/customer_raw.csv")

print(df.head())
print(df.info())

df["signup_date"] = pd.to_datetime(df["signup_date"])
print(df.info())

#Fill missing age with median 
median_age = df["age"].median()
df["age"] = df["age"].fillna(median_age)

print("Missing value is age after filling")
print(df["age"].isnull().sum())

#Remove rows with negative spend

df = df[df["spend"] >= 0 ]
print("Rows after removing negative spend:")
print(len(df))