
import pandas as pd

# Load the dataset
df = pd.read_csv("retail_sales.csv")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("===== RETAIL SALES SUMMARY =====")

print("\nTotal Records:", len(df))
print("Total Quantity Sold:", df["Quantity"].sum())
print("Total Revenue: Rs.", df["Revenue"].sum())
print("Average Revenue per Sale: Rs.", round(df["Revenue"].mean(), 2))

print("\nRevenue by Category:")
print(df.groupby("Category")["Revenue"].sum())

print("\nTop Product by Revenue:")
print(df.groupby("Product")["Revenue"].sum().idxmax())
