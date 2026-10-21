
import pandas as pd

# Load the sales dataset
df = pd.read_csv("retail_sales.csv")

# Calculate revenue for each sale
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Display the dataset
print("RETAIL SALES DATA")
print(df)

# Calculate total revenue
print("\nTotal Revenue:", df["Revenue"].sum())

# Revenue by product
print("\nRevenue by Product:")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

# Revenue by category
print("\nRevenue by Category:")
print(df.groupby("Category")["Revenue"].sum())

# Best-selling products by quantity
print("\nQuantity Sold by Product:")
print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False))
