import os
TASKS_FILE = "tasks.txt"
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter the new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")
        elif choice == "3":
            view_tasks(tasks)
            index = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index] += " [Completed]"
                save_tasks(tasks)
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        elif choice == "4":
            view_tasks(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()