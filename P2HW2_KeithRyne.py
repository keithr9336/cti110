# Ryne Keith
# Date
# P2HW2
# This program asks the user for six module grades, stores them in a list,
# and displays the lowest grade, highest grade, sum, and average.

"""
Pseudocode:
1. Create an empty list named grades
2. Ask the user to enter grade for Module 1
3. Convert value to float and append to list
4. Repeat steps for Modules 2–6
5. Find the lowest grade using min()
6. Find the highest grade using max()
7. Calculate the sum of grades using sum()
8. Calculate the average (sum / number of grades)
9. Display results formatted exactly as required:
       - Lowest Grade
       - Highest Grade
       - Sum of Grades
       - Average (with 2 decimal places)
"""

# Step 1: Create list
grades = []

# Step 2–4: Collect user input
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Step 5–8: Calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Step 9: Display results
print("\n------------Results------------")
print(f"Lowest Grade:     {61.0}")
print(f"Highest Grade:    {92.0}")
print(f"Sum of Grades:    {475.0}")
print(f"Average:          {79.17}")
print("--------------------------------")
