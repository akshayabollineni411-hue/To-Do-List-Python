tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, item in enumerate(tasks, start=1):
                status = "Completed" if item["completed"] else "Pending"
                print(f"{i}. {item['task']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")
            
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            number = int(input("Enter task number to mark as completed: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
