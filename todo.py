tasks = []
try:
    with open("tasks.txt","r") as file:
        for line in file:
            task=line.strip()
            if task:
                tasks.append({"task":task,"completed":False})
except:
    pass
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task": task, "completed": False})
        with open("tasks.txt","a") as file:
            file.write(task+"\n")
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")

            for i, item in enumerate(tasks, 1):
                if item["completed"]:
                    print(i, item["task"], "- Completed")
                else:
                    print(i, item["task"], "- Pending")

    # Delete Task
    elif choice == "3":
        try:
            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")

        except:
            print("Please enter a number!")

    # Mark Completed
    elif choice == "4":
        try:
            task_number = int(input("Enter task number to complete: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                with open("tasks.txt","w") as file:
                    for item in tasks:
                        file.write(item["task"]+"\n")
                print("Task marked as completed!")
            else:
                print("Invalid task number!")
        except:
            print("Please enter a number!")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice!")
