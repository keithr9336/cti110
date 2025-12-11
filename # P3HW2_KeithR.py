# P3HW2_KeithR
# 12/10/2025
# P3HW2_RyneKeith.py
# This program calculates an employee's gross pay including overtime pay.
# It asks for the employee's name, hours worked, and pay rate, then computes
# regular pay, overtime pay (if any), and displays all relevant information in a table.

"""
Pseudocode:

1. Start
2. Ask user to enter employee name and store in 'employee_name'
3. Ask user to enter hours worked and store in 'hours_worked'
4. Ask user to enter pay rate and store in 'pay_rate'
5. Initialize 'overtime_hours' and 'overtime_pay' to 0
6. If hours_worked > 40:
       a. overtime_hours = hours_worked - 40
       b. overtime_pay = overtime_hours * pay_rate * 1.5
       c. regular_pay = 40 * pay_rate
   Else:
       a. regular_pay = hours_worked * pay_rate
       b. overtime_hours and overtime_pay remain 0
7. Calculate gross_pay = regular_pay + overtime_pay
8. Display all information in a table:
       - Employee name
       - Hours worked
       - Pay rate
       - Overtime hours
       - Overtime pay
       - Regular pay
       - Gross pay
9. End
"""

# Input from user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Initialize overtime
overtime_hours = 0
overtime_pay = 0

# Calculate overtime and regular pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = 40 * pay_rate
else:
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results in table format
print("\n---------------------------------------------")
print(f"Employee name: {employee_name}\n")
print(f"{'Hours Worked':<13}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print("-" * 75)
print(f"{hours_worked:<13.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}")
