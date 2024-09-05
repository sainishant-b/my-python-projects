### todo_list.py
def show_menu():
    print("\nTo-Do List Application")
    print("----------------------")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Quit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved.")

def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, 'r') as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        print("No saved tasks found.")
    return tasks

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            save_tasks(tasks)
            print("Quitting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
