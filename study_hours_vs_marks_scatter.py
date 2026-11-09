import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 65, 70, 80, 90]

plt.scatter(study_hours, marks, color="blue", marker="o")
plt.xlabel("Student study hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Exam Marks")
plt.grid()
plt.show()
