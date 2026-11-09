import matplotlib.pyplot as plt

products = ["laptop", "mobile", "tablet", "headphones", "keyboard"]
sales = [50, 80, 30, 65, 40]

plt.barh(products, sales, color="pink")
plt.xlabel("Sales")
plt.ylabel("Products")
plt.title("Horizontal Product Sales Analysis")
plt.grid()
plt.show()
