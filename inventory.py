import pandas as pd
import matplotlib.pyplot as plt

# Raw input data (10 products)
raw_data = {
    "Product": ["Cola", "Chips", "Milk", "Juice", "Biscuits", "Cheese", "Water", "Nuts", "Yogurt", "Soda"],
    "Category": ["beverages ", "SNACKS", " Dairy", "beverages", "Snacks", "Dairy ", "BEVERAGES", "SNACKS ", "dairy", "beverages"],
    "Price": ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 180", "Rs. 650", "Rs. 50", "Rs. 300", "Rs. 200", "Rs. 100"],
    "Stock": [40, 120, 60, 80, 150, 30, 200, 90, 50, 110]
}

df = pd.DataFrame(raw_data)

# (a) Clean Category text
df["Category"] = df["Category"].str.strip().str.title()

# (b) Convert Price to numeric by removing "Rs. " and commas
df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False).str.replace(",", "").astype(float)

# (c) Add Category_Code using label encoding
df["Category_Code"] = df["Category"].astype("category").cat.codes

print("Cleaned Inventory DataFrame:")
print(df)

# (d) Draw bar plot of avg price and pie chart of total stock side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 1: Average Price per Category
avg_price = df.groupby("Category")["Price"].mean()
axes[0].bar(avg_price.index, avg_price.values, color=["#4C78A8", "#F58518", "#54A24B"])
axes[0].set_title("Average Price per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")

# Subplot 2: Stock Share by Category
total_stock = df.groupby("Category")["Stock"].sum()
axes[1].pie(total_stock.values, labels=total_stock.index, autopct="%1.1f%%", startangle=90, colors=["#4C78A8", "#F58518", "#54A24B"])
axes[1].set_title("Stock Share by Category")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()