from calculator import calculator
from password import generate_password
from todo import todo_menu
from expense import expense_tracker

def main():
    while True:
        print("\n===== SMART TOOL =====")
        print("1. Calculator")
        print("2. Password Generator")
        print("3. To-Do List")
        print("4. Expense Tracker")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            generate_password()
        elif choice == "3":
            todo_menu()
        elif choice == "4":
            expense_tracker()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()