
# Python Fundamentals Practice

# Variables and lists
name = "Madhavi"
marks = [85, 90, 78, 92, 88]

print("Name:", name)
print("Marks:", marks)

# Basic calculations
total = sum(marks)
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)

# Conditional statements
if average >= 80:
    print("Result: Good performance")
else:
    print("Result: Keep practicing")

# Loop through marks
print("Individual Marks:")
for mark in marks:
    print(mark)
