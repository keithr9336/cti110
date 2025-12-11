# P4LAB2_KeithRyne.py

run_again = "yes"  # Control variable for the while loop

while run_again.lower() == "yes":
    try:
        number = int(input("Enter an integer: "))

        if number >= 0:
            print(f"\nMultiplication table for {number}:\n")
            for i in range(1, 13):
                # Format numbers to align in columns
                print(f"{number:>3} x {i:>2} = {number*i:>4}")
        else:
            print("Cannot accept negative values.")

        # Ask user if they want to run the program again
        run_again = input("\nDo you want to run the program again? (yes/no): ")
        print()  # Blank line for readability

    except ValueError:
        print("Invalid input. Please enter an integer.\n")
