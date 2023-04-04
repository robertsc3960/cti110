# A brief description of the project
# Date: 04/04/2023
# CTI-110 P1HW1 - Travel Expense
# Name: Clint Roberts
#

print("This program calculates and displays travel expenses")

# Ask user to enter their budget
budget = float(input("\nEnter Budget: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas_expense = float(input("How much do you think you will spend on gas? "))

# Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Approximately, how much will you need for accomodation/hotel? "))

# Ask user for amount they will spend on food
food_expense = float(input("Last, how much do you need for food? "))

# Add expenses
total_expense = gas_expense + accommodation_expense + food_expense

# Subtract expenses from budget
remaining_budget = budget - total_expense

# Display results
print("\n------------Travel Expenses------------")
print("Location: " + destination)
print("Intial Budget: $" + str(budget))

print("\nFuel: $" + str(gas_expense))
print("Accomodation: $" + str(accommodation_expense))
print("Food: $" + str(food_expense))

print("Remaining Balance: $" + str(remaining_budget))

