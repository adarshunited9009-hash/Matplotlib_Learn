import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "Java", "DBMS", "English"]
study_hours = [10, 5, 3, 4, 2]

plt.pie(
    study_hours,
    labels=subjects,
    autopct="%1.1f%%",
    colors=["pink", "yellow", "brown", "black", "red"],
    explode=[0.1, 0, 0, 0, 0],
    startangle=90
)
plt.title("Weekly Study Time Distribution")
plt.show()
