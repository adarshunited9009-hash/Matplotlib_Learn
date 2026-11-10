import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
daily_revenue = [4200, 5100, 4800, 6200, 5900, 7800, 7300]

ad_spend = [500, 650, 600, 800, 750, 1000, 950]

categories = ["Electronics", "Clothing", "Grocery", "Books", "Beauty"]
category_revenue = [18000, 12500, 9500, 6200, 10800]

order_values = [199, 249, 299, 349, 399, 450, 499, 550,
                599, 649, 699, 799, 899, 999, 1299]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Line chart
axes[0, 0].plot(days, daily_revenue, marker="o", color="red", linestyle="--")
axes[0, 0].set_title("Daily Revenue")
axes[0, 0].set_xlabel("Day")
axes[0, 0].set_ylabel("Revenue")

# Bar chart
axes[0, 1].bar(categories, category_revenue)
axes[0, 1].set_title("Revenue by Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Revenue")

# Scatter plot
axes[1, 0].scatter(ad_spend, daily_revenue)
axes[1, 0].set_title("Advertising Spend vs Revenue")
axes[1, 0].set_xlabel("Advertising Spend")
axes[1, 0].set_ylabel("Daily Revenue")

# Histogram
axes[1, 1].hist(order_values, bins=5, edgecolor="black")
axes[1, 1].set_title("Order Value Distribution")
axes[1, 1].set_xlabel("Order Value")
axes[1, 1].set_ylabel("Number of Orders")

fig.suptitle("Sales Performance Dashboard", fontsize=16)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
