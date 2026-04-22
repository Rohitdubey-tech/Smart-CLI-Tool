from utils import load_data, save_data
def todo_menu():
    while True:
        print("\n --- TO-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")
        choice = input("Enter Choice: ")
        data = load_data()

        if choice == "1":
            task = input ("Enter task: ")
            data["tasks"].append(task)
            save_data(data)
            print("Task added successfully")

        elif choice == "2":
            for i, t in enumerate(data["tasks"], 1):
                print(f"{i}. {t}")
        elif choice == "3":
            for i, t in enumerate(data["tasks"], 1):
                print(f"{i}. {t}")
            idx = int(input("Enter task number: "))-1
            if 0<= idx < len(data["tasks"]):
                data["tasks"].pop(idx)
                save_data(data)
        elif choice == "4":
            break 