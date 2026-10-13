import pandas as pd
import matplotlib.pyplot as plt

products = ["Cola", "Chips", "Milk", "Biscuits", "Juice", "Yogurt", "Water", "Cheese", "Popcorn", "Tea"]
categories = ["beverages ", "SNACKS", " Dairy", "Snacks", "beverages", "dairy ", "BEVERAGES", " Dairy", "snacks ", "Beverages"]
prices = ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 1,800", "Rs. 220", "Rs. 60", "Rs. 950", "Rs. 150", "Rs. 700"]
stock = [40, 120, 60, 85, 25, 45, 200, 30, 95, 70]

df = pd.DataFrame({"Product": products, "Category": categories, "Price": prices, "Stock": stock})

df["Category"] = df["Category"].str.strip().str.title()

df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False).str.replace(",", "", regex=False).astype(float)

df["Category_Code"] = df["Category"].astype("category").cat.codes

print(df)

avg_price = df.groupby("Category")["Price"].mean()
total_stock = df.groupby("Category")["Stock"].sum()

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

axes[0].bar(avg_price.index, avg_price.values, color=["#4C78A8", "#F58518", "#54A24B"])
axes[0].set_title("Average Price per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")

axes[1].pie(total_stock.values, labels=total_stock.index, autopct="%1.1f%%", startangle=90,
            colors=["#4C78A8", "#F58518", "#54A24B"])
axes[1].set_title("Share of Total Stock by Category")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()

print("Saved inventory_plots.png")