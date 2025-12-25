import pandas as pd

#Load dataset
df = pd.read_csv("data/customers.csv")

print("Dataset loaded successfully")
print(df.head())
print(df.info())


#Convert signup_date to datetime
df["signup_date"] = pd.to_datetime(df["signup_date"])
print("After converting signup_date:")
print(df.info())


#Create age groups
def age_group(age):
    if age < 30:
        return "Young"
    elif age < 50:
        return "Middle"
    else:
        return "Senior"
    
df["age_group"] = df["age"].apply(age_group)

print("Age groups created:")
print(df[["age", "age_group"]].head())