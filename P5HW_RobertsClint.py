# Menu Driven Program
# 5/4/2023
# CTI-110 P5HW - Math Quiz
# Clint Roberts
#

import random

# Generate two random numbers between 1 and 10
def generate_numbers():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

# Prompt the user to add the two random numbers
def add_numbers():
    num1, num2 = generate_numbers()
    result = num1 + num2
    print("   ", num1)
    print(" + ", num2)
    
    num_guesses = 0
    while True:
        num_guesses += 1
        guess = int(input("\nTry again: " if num_guesses > 1 else "\nEnter answer.\n"))
        if guess == result:
            print("\nCongratulations!!!! Your answer is correct.")
            print("Number of guesses: ", num_guesses)
            break
        elif guess < result:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

            
# Prompt the user to subtract the two random numbers
def subtract_numbers():
    num1, num2 = generate_numbers()
    result = num1 - num2
    print("   ", num1)
    print(" - ", num2)
    
    num_guesses = 0
    while True:
        num_guesses += 1
        guess = int(input("\nTry again: " if num_guesses > 1 else "\nEnter answer.\n"))
        if guess == result:
            print("\nCongratulations!!!! Your answer is correct.")
            print("Number of guesses: ", num_guesses)
            break
        elif guess < result:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

# Display the main menu
def menu():
    print("Welcome to the Math Quiz\n\n")
    print("MAIN MENU")
    print("-" * 33)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")

# Start the program and loop until the user chooses to exit
def main():
    while True:
        # Display the main menu and prompt the user for their choice
        menu()
        choice = input("Please choose one of the menu options: ")

        # Call the appropriate function based on the user's choice
        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            # Exit the program
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            # Invalid input
            print("Invalid input. Please try again.")

# Call the main function to start the program
if __name__ == "__main__":
    main()

