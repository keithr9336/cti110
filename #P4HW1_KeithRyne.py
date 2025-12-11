# Ryne Keith
# 2025-12-10
# P4HW1
# This program collects user-entered scores, validates them, drops the lowest score,
# calculates the average of the remaining scores, and determines the letter grade.

# -------------------------------
# Pseudocode:
# 1. Ask the user for the number of scores they want to enter.
# 2. Initialize an empty list to store valid scores.
# 3. For the number of scores:
#    a. Prompt the user to enter a score.
#    b. While the entered score is not valid (not between 0 and 100), keep asking.
#    c. Add the valid score to the list of scores.
# 4. Identify the lowest score in the list.
# 5. Remove the lowest score from the list.
# 6. Display the lowest score and the modified list.
# 7. Calculate the average of the modified list.
# 8. Determine the letter grade based on the average:
#    - 90-100: A
#    - 80-89: B
#    - 70-79: C
#    - 60-69: D
#    - Below 60: F
# 9. Display the average and the letter grade to the user.
# -------------------------------

# Step 1: Ask for number of scores
while True:
    try:
        num_scores = int(input("Enter the number of scores you would like to input: "))
        if num_scores > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Step 2: Initialize list
score_list = []

# Step 3: Collect scores using a loop
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1} (0-100): "))
            if 0 <= score <= 100:
                score_list.append(score)
                break
            else:
                print("Invalid score. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Step 4: Identify and remove lowest score
lowest_score = min(score_list)
score_list.remove(lowest_score)

# Step 5: Display results
print(f"\nLowest score entered: {lowest_score}")
print(f"Score list after dropping lowest score: {score_list}")

# Step 6: Calculate average
average_score = sum(score_list) / len(score_list)
print(f"Average score (after dropping lowest): {average_score:.2f}")

# Step 7: Determine letter grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Letter grade for the average: {grade}")
