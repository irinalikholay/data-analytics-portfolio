# Project 05 — Advanced Sales Analysis (Python)

## Business Context
This project simulates a real-world sales analysis task for an e-commerce business.
The goal is to understand revenue drivers, customer behavior, and sales trends
using Python and pandas, without SQL.

## Business Questions
The analysis answers the following questions:
- Which countries generate the most revenue?
- How does revenue change over time?
- Who are the top customers by total spend?

## Dataset Overview
The dataset contains transactional sales data with the following key fields:
- order_id
- customer_id
- order_date
- country
- product_category
- price
- quantity
- revenue (engineered feature)

## Analysis Summary
The analysis included:
- Data loading and validation
- Data type correction for dates
- Feature engineering (revenue calculation)
- Aggregation by country, month, and customer
- Sorting and ranking of results

## Visual Findings
Three visualizations were created:
1. Revenue by country
2. Revenue over time (monthly)
3. Top customers by total revenue

All plots are saved in the "plots" directory.

## Key Insights
- Revenue is unevenly distributed across countries
- Clear trends can be observed over time
- A small number of customers contribute a large share of revenue

##  Next Steps
Possible next steps for further analysis:
- Customer segmentation
- Product category performance
- Migration of analysis logic to SQL

## Tools Used
- Python
- pandas
- matplotlib
- VS Code
- Git & GitHub