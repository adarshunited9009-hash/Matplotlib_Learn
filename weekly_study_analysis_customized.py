import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [2, 3, 4, 2, 5, 7, 6]

plt.figure(figsize=(8, 5))
plt.plot(days, hours, color="blue", marker="o")
plt.xlabel("Day of the week")
plt.ylabel("Study hours")
plt.grid(linestyle="--")
plt.annotate("Highest", xy=("Sat", 7))
plt.title("Daily Study Analysis")
plt.show()
