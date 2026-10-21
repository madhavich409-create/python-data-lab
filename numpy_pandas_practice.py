
import numpy as np
import pandas as pd

# NumPy practice
marks = np.array([85, 90, 78, 92, 88])

print("Student Marks:", marks)
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# Pandas practice
data = {
    "Name": ["Anu", "Ravi", "Sita", "Kiran", "Maya"],
    "Marks": marks
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)

print("\nStudents scoring above 85:")
print(df[df["Marks"] > 85])
