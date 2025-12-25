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


#Total spend by age group
spend_by_age_group = df.groupby("age_group")["total_spend"].sum()

print("Total spend by age group:")
print(spend_by_age_group)


import matplotlib.pyplot as plt

#Plot total spend by age group 
spend_by_age_group.plot(kind="bar")

plt.title("Total Spend by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Spend")

plt.tight_layout()

plt.savefig("plots/avg_spend_by_age_group.png")
plt.close()
plt.show()