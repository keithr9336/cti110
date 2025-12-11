# Ryne Keith
# 2025-12-10
# P4HW2
# This program calculates gross pay, regular pay, and overtime pay for multiple employees,
# and displays totals for all employees when the user finishes entering data, formatted in a table.

# -------------------------------
# Pseudocode:
# 1. Initialize totals for regular pay, overtime pay, and gross pay to 0.
# 2. Initialize employee count to 0.
# 3. Loop indefinitely:
#    a. Ask user to enter employee name.
#       - If name is "Done", break the loop.
#    b. Ask user to enter hours worked and hourly pay rate.
#    c. Validate that hours and pay rate are positive numbers.
#    d. Calculate regular pay (up to 40 hours) and overtime pay (hours above 40 * 1.5 rate).
#    e. Calculate gross pay = regular pay + overtime pay.
#    f. Display the employee's payroll in a formatted table.
#    g. Add employee's regular pay, overtime pay, and gross pay to totals.
#    h. Increment employee count.
# 4. After loop ends, display:
#    - Total number of employees entered
#    - Total regular pay
#    - Total overtime pay
#    - Total gross pay
# -------------------------------

# Step 1: Initialize totals
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

# Step 3: Main loop for employee data entry
while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.strip().lower() == "done":
        break

    # Validate hours worked
    while True:
        try:
            hours_worked = float(input(f"How many hours did {employee_name} work? "))
            if hours_worked >= 0:
                break
            else:
                print("Hours worked must be zero or positive.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for hours worked.")

    # Validate pay rate
    while True:
        try:
            pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
            if pay_rate >= 0:
                break
            else:
                print("Pay rate must be zero or positive.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for pay rate.")

    # Calculate regular and overtime pay
    overtime_hours = max(0, hours_worked - 40)
    regular_hours = min(40, hours_worked)
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    # Display employee payroll table
    print(f"\nEmployee name:  {employee_name}\n")
    print(f"{'Hours Worked':>12} {'Pay Rate':>10} {'OverTime':>10} {'OverTime Pay':>14} {'RegHour Pay':>14} {'Gross Pay':>12}")
    print("-" * 72)
    print(f"{hours_worked:12.1f} {pay_rate:10.2f} {overtime_hours:10.1f} {overtime_pay:14.2f} ${regular_pay:13.2f} ${gross_pay:10.2f}\n")

    # Update totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

# Display totals summary
print("\nTotal number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
