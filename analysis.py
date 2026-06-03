import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("../charts", exist_ok=True)

sales = pd.read_csv("../data/sales.csv")
competitors = pd.read_csv("../data/competitors.csv")
marketing = pd.read_csv("../data/marketing.csv")

sales["Revenue"] = sales["Quantity"] * sales["Price"]
sales["Profit"] = sales["Quantity"] * (sales["Price"] - sales["Cost"])
sales["Profit_Margin"] = (sales["Profit"] / sales["Revenue"]) * 100

print("Total Revenue:", round(sales["Revenue"].sum(), 2))
print("Total Profit:", round(sales["Profit"].sum(), 2))
print("Average Profit Margin:", round(sales["Profit_Margin"].mean(), 2))

# Revenue by item
revenue_by_item = sales.groupby("Item")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
revenue_by_item.plot(kind="bar")
plt.title("Revenue by Menu Item")
plt.xlabel("Menu Item")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../charts/revenue_by_item.png")
plt.show()

# Profit by item
profit_by_item = sales.groupby("Item")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
profit_by_item.plot(kind="bar")
plt.title("Profit by Menu Item")
plt.xlabel("Menu Item")
plt.ylabel("Profit")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../charts/profit_by_item.png")
plt.show()

# Marketing ROI
marketing["Conversion_Rate"] = (marketing["Orders_Generated"] / marketing["Views"]) * 100
marketing["Cost_Per_Order"] = marketing["Ad_Cost"] / marketing["Orders_Generated"]

print("\nMarketing Performance:")
print(marketing)

# Competitor comparison
print("\nCompetitor Comparison:")
print(competitors.sort_values(by="Rating", ascending=False))