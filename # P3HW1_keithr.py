# P3HW1_keithr.py
# Final corrected version ready for submission

# Initialize list to store grades
grades = []

# Ask user for grades for each module
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Calculate average grade
average = sum(grades) / len(grades)

# Display results
print("\nGrades entered:", grades)
print("Average grade:", average)

# Display grades above and below average
above_avg = [g for g in grades if g > average]
below_avg = [g for g in grades if g < average]

print("Grades above average:", above_avg)
print("Grades below average:", below_avg)
