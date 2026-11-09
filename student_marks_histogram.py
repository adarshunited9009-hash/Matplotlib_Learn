import matplotlib.pyplot as plt

marks = [22, 35, 45, 48, 52, 55, 58, 60, 62, 65,
         67, 70, 72, 75, 78, 80, 85, 88, 92, 95]

plt.hist(marks, bins=5, color="pink", edgecolor="black")
plt.xlabel("Student marks")
plt.ylabel("Frequency")
plt.title("Student Marks Distribution")
plt.grid()
plt.show()
