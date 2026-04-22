from utils import load_data, save_data

def expense_tracker():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Back")

        choice = input("Enter choice: ")
        data = load_data()

        if choice == "1":
            amt = float(input("Enter amount: "))
            data["expenses"].append(amt)
            save_data(data)

        elif choice == "2":
            for e in data["expenses"]:
                print(e)

        elif choice == "3":
            print("Total:", sum(data["expenses"]))

        elif choice == "4":
            break