# Project 01 - Exploratory Data Analysis
# Author: Irina
# Description: Initial setup for data analysis project

print("EDA project started")

import pandas as pd
import numpy as np

print("Libraries imported successfully")


# Create a simple dataset

data = {
    "customer_id": [1, 2, 3, 4, 5],
    "age": [23, 35, 45, 28, 52],
    "country": ["Germany", "France", "Germany", "Spain", "France"],
    "purchase_amount": [120, 340, 560, 80, 220]

    }

df = pd.DataFrame(data)

print(df)

print("\nDataset shape:")
print(df.shape)

print("\nFirst rows:")
print(df.head())

average_age = df["age"].mean()
print("\nAverage age of customers:")
print(average_age)

min_age = df["age"].min()
max_age = df["age"].max()

print("\nMinimum customer age:")
print(min_age)

print("\nMaximum customer age:")
print(max_age)


average_purchase_by_country = (
    df
    .groupby("country") ["purchase_amount"]
    .mean()
)

print("\nAverage purchase amount by country:")
print(average_purchase_by_country)