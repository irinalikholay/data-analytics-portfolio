# Project 03 - Data Cleaning with Python 

## Business goal
Clean and prepare customer data for analysis.

## Dataset
Raw customer dataset with missing values and inconsistencies.

## Tools
- Python 
- pandas

## Status
In progress

## Data quality issues identified 

- Missing values were found in the following columns:   "age", "gender", "country" and "spend".
- One record contained a negative value in the "spend" column.
- The "signup_date" column was initially stored as text instead of a date format.

## Data cleaning decisions

- Missing values is "age" were filled with the median value to preserve the distribution.
- Records with negative "spend" values were removed as they are not valid in this context.
- The "signup_date" column was converted to datetime format.
- Missing country values filled with "Unknown".
- Unrealistic age values (e.g. age > 100 ) were treated as missing and replaced with the median age.
