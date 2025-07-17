
import json
import os

FILE_NAME = "todo_list.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{idx}. [{status}] {task['task']}")
    print()

# Add a new task
def add_task(tasks):
    task_desc = input("Enter a new task: ").strip()
    if task_desc:
        tasks.append({"task": task_desc, "done": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

# Mark a task as complete
def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as complete: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: "))
        if 1 <= index <= len(tasks):
            deleted = tasks.pop(index - 1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
import json
import os

FILE_NAME = "todo_list.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{idx}. [{status}] {task['task']}")
    print()

# Add a new task
def add_task(tasks):
    task_desc = input("Enter a new task: ").strip()
    if task_desc:
        tasks.append({"task": task_desc, "done": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

# Mark a task as complete
def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as complete: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: "))
        if 1 <= index <= len(tasks):
            deleted = tasks.pop(index - 1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
import json
import os

FILE_NAME = "todo_list.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{idx}. [{status}] {task['task']}")
    print()

# Add a new task
def add_task(tasks):
    task_desc = input("Enter a new task: ").strip()
    if task_desc:
        tasks.append({"task": task_desc, "done": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

# Mark a task as complete
def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as complete: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: "))
        if 1 <= index <= len(tasks):
            deleted = tasks.pop(index - 1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
