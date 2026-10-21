
import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("retail_sales.csv")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Calculate revenue by product
sales = df.groupby("Product")["Revenue"].sum()
sales = sales.sort_values(ascending=False)

# Create bar chart
sales.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("revenue_by_product.png")
plt.show()
