import matplotlib.pyplot as plt

products = ["laptop", "mobile", "tablet", "headphones", "keyboard"]
sales = [50, 80, 30, 65, 40]

plt.bar(products, sales, width=0.5, color="pink")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales Analysis")
plt.grid()
plt.show()
