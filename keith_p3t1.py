# CTI 110
# P3LAB - Correct Change
# keithr
# 10/9

# Get some amount of money, and break it into chang
# First, find out how many dollars.
amount_float = float(input("Enter a dollar amount with decimals: $"))
#print("You entered $", amount_float)
if (amount_float == 0):
    print("No change")
# Step1: convert to pennies
amount = int(amount_float * 100)

# Next, removeall the dollars
dollars = amount // 100 # // means integer division
amount  = amount % 100  # %  means just keep the remainder

# TODO: do the rest of the math (25, 10, 5, and 1)
quarters = 0
dimes = 0
nickels = 0
pennies = amount # fix this

# Last step: Print the answe
if dollars > 0:
    print(dollars, "Dollars")
if quarters > 0:
    print(quarters, "Quarters")
if dimes > 0:
    print(dimes, "Dimes")
if nickels > 0: 
    print(nickels, "Nickels")
if pennies > 0:
    print(pennies, "Pennies")
