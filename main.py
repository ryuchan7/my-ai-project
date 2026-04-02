# UniMAP Data Science Project - Main Entry Point
import calculator  # This imports your other file

def display_welcome():
    print("======================================")
    print("   WELCOME TO THE AI PROJECT TOOLS   ")
    print("======================================")
    print("1. Run Calculator")
    print("2. Exit")

def start_program():
    display_welcome()
    choice = input("\nSelect an option (1-2): ")

    if choice == '1':
        print("\nStarting Calculator...\n")
        # Since calculator.py has code that runs immediately, 
        # importing it will trigger its logic!
    elif choice == '2':
        print("Goodbye!")
    else:
        print("Invalid selection. Try again.")

if __name__ == "__main__":
    start_program()