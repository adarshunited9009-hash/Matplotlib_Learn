import matplotlib.pyplot as plt

x = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
y = [2, 3, 4, 1, 6, 7, 8]

plt.plot(x, y, color="yellow", marker="o", linestyle="--")
plt.xlabel("Day of the week")
plt.ylabel("Study hours")
plt.title("Study Analysis")
plt.grid()
plt.show()
