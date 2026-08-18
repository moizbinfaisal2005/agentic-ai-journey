
### Exercise: Codebasics Student Performance Tracker

# You're tracking quiz scores for students in a Python cohort. Each student has taken 3 quizzes, and you want to figure out who's passing, who's topping, and the class average.

# ```
# students = {
#     "Aarav":   [85, 90, 78],
#     "Priya":   [72, 68, 75],
#     "Rohan":   [45, 52, 48],
#     "Sneha":   [95, 92, 98],
#     "Manish":  [60, 65, 70],
# }
# ```

# Each key is a student name, and each value is a list of 3 quiz scores (out of 100).

# Write code using for loops to do the following:

# 1. Calculate each student's average score and print it in this format:```Aarav: 84.33```
# 2. Classify each student based on their average:
#     80 and above → "Topper"
#     60 to 79 → "Pass"
#     Below 60 → "Needs improvement"
# 3. Find the topper of the class (highest average) and print their name and score.
# 4. Calculate the class average across all students.

# Expected output (roughly)

# ```
# === Student Averages ===
# Aarav: 84.33 - Topper
# Priya: 71.67 - Pass
# Rohan: 48.33 - Needs improvement
# Sneha: 95.00 - Topper
# Manish: 65.00 - Pass

# === Class Topper ===
# Sneha with average 95.00

# === Class Average ===
# 72.87
# ```


print("\n=== STUDENTS AVERAGE ===")

students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}

high_stud = None
high_avg = 0


for name, marks in students.items():
    avg = sum(marks) / len(marks)
    if  avg >= 80:
        status = "Topper"
    elif avg >= 60:
        status = "Pass"
    else:
        status = "Need Improvement"

    print(f"'{name}' Average:{avg: .2f} → {status}")




    if avg > high_avg:
      high_avg = avg
      high_stud = name

print("\n=== Class Topper ===")

print(f"{high_stud} with Highest Average: {high_avg: .2f}")

all_marks = []

for marks in students.values():
    all_marks.extend(marks)
    
print("\n=== CLASS AVERAGE ===")

class_avg = sum(all_marks)/ len(all_marks)

print(f"Class Average is:{class_avg: .2F}")











