import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder if it does not exist
os.makedirs("charts", exist_ok=True)

# Load datasets
sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")
marketing = pd.read_csv("marketing.csv")
expenses = pd.read_csv("monthly_expenses.csv")
competitors = pd.read_csv("competitors.csv")

# Clean column names
sales.columns = sales.columns.str.strip()
customers.columns = customers.columns.str.strip()
marketing.columns = marketing.columns.str.strip()
expenses.columns = expenses.columns.str.strip()
competitors.columns = competitors.columns.str.strip()

# Make revenue column if not already made
sales["Revenue"] = sales["Quantity"] * sales["Price"]

# Convert date
sales["Date"] = pd.to_datetime(sales["Date"])

# -----------------------------
# BASIC KPI ANALYSIS
# -----------------------------

total_revenue = sales["Revenue"].sum()
total_orders = sales["Order_ID"].nunique()
avg_order_value = total_revenue / total_orders
total_customers = customers["Customer_Type"].nunique()

print("===== GOPHLE MOMO BUSINESS ANALYSIS =====")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ${avg_order_value:.2f}")
print(f"Total Customers: {total_customers}")

# -----------------------------
# PRODUCT ANALYSIS
# -----------------------------

best_selling = sales.groupby("Item")["Quantity"].sum().sort_values(ascending=False)

revenue_by_product = sales.groupby("Item")["Revenue"].sum().sort_values(ascending=False)

print("\n===== BEST SELLING PRODUCTS =====")
print(best_selling)

print("\n===== REVENUE BY PRODUCT =====")
print(revenue_by_product)

# Chart: Best Selling Products
best_selling.plot(kind="bar")
plt.title("Best Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/best_selling_products.png")
plt.close()

# Chart: Revenue by Product
revenue_by_product.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/revenue_by_product.png")
plt.close()

# -----------------------------
# SALES TREND
# -----------------------------

daily_sales = sales.groupby("Date")["Revenue"].sum()

daily_sales.plot(kind="line", marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/daily_sales_trend.png")
plt.close()

# -----------------------------
# CUSTOMER ANALYSIS
# -----------------------------

#merged = sales.merge(customers, on="Customer_ID", how="left")

#revenue_by_age = merged.groupby("Age_Group")["Revenue"].sum().sort_values(ascending=False)

#print("\n===== REVENUE BY AGE GROUP =====")
#print(revenue_by_age)

#revenue_by_age.plot(kind="bar")
#plt.title("Revenue by Age Group")
#plt.xlabel("Age Group")
#plt.ylabel("Revenue")
#plt.tight_layout()
#plt.savefig("charts/revenue_by_age_group.png")
#plt.close()

customer_type_revenue = sales.groupby("Customer_Type")["Revenue"].sum()

print("\n===== REVENUE BY CUSTOMER TYPE =====")
print(customer_type_revenue)

# -----------------------------
# MARKETING ANALYSIS
# -----------------------------

if "Customers_Gained" in marketing.columns and "Cost" in marketing.columns:
    marketing["CAC"] = marketing["Cost"] / marketing["Customers_Gained"]

    print("\n===== MARKETING PERFORMANCE =====")
    print(marketing)

    marketing.plot(x="Campaign", y="CAC", kind="bar")
    plt.title("Customer Acquisition Cost by Campaign")
    plt.xlabel("Campaign")
    plt.ylabel("CAC")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("charts/marketing_cac.png")
    plt.close()

# -----------------------------
# EXPENSE + PROFIT ANALYSIS
# -----------------------------

total_expenses = expenses["High_Cost"].sum()
profit = total_revenue - total_expenses
profit_margin = (profit / total_revenue) * 100

print("\n===== FINANCIAL SUMMARY =====")
print(f"Total Expenses: ${total_expenses:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")

print("\nCharts saved successfully in the charts folder.")

# -----------------------------
# CREATE SQLITE DATABASE
# -----------------------------

import sqlite3

conn = sqlite3.connect("gophle.db")

sales.to_sql("sales", conn, if_exists="replace", index=False)
customers.to_sql("customers", conn, if_exists="replace", index=False)
marketing.to_sql("marketing", conn, if_exists="replace", index=False)
expenses.to_sql("monthly_expenses", conn, if_exists="replace", index=False)
competitors.to_sql("competitors", conn, if_exists="replace", index=False)

conn.close()

print("SQLite database created successfully: gophle.db")