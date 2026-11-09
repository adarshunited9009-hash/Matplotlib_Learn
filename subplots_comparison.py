import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "Java", "DBMS"]
hours = [10, 5, 3, 4]
marks = [90, 75, 65, 80]

# First chart: study hours by subject
plt.subplot(1, 3, 1)
plt.plot(subjects, hours, color="red", marker="o")
plt.xlabel("Subjects")
plt.ylabel("Study hours")
plt.title("Subject-wise Study Hours")

# Second chart: marks by subject
plt.subplot(1, 3, 2)
plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks by Subject")

# Third chart: share of study hours
plt.subplot(1, 3, 3)
plt.pie(hours, labels=subjects, autopct="%1.1f%%")
plt.title("Study Time Distribution")

plt.tight_layout()
plt.show()
