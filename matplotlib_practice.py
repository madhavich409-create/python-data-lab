
import matplotlib.pyplot as plt

students = ["Anu", "Ravi", "Sita", "Kiran", "Maya"]
marks = [85, 90, 78, 92, 88]

plt.bar(students, marks)

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)

plt.show()
