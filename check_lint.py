"""
Simple To-Do List Program.

This program allows users to manage a to-do list by adding,
viewing, and removing tasks through a simple menu interface.
"""

TASKS = []


def show_menu():
    """Display the menu options."""
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


def view_tasks():
    """Display all tasks in the to-do list."""
    if not TASKS:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(TASKS, start=1):
            print(f"{index}. {task}")


def add_task():
    """Add a new task to the to-do list."""
    task = input("\nEnter the task you want to add: ").strip()
    if task:
        TASKS.append(task)
        print(f"'{task}' has been added to your to-do list.")
    else:
        print("Task cannot be empty. Please try again.")


def remove_task():
    """Remove a task from the to-do list."""
    view_tasks()
    if TASKS:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(TASKS):
                removed_task = TASKS.pop(task_num - 1)
                print(f"'{removed_task}' has been removed from your to-do list.")
            else:
                print("Invalid task number! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    """Main program loop to manage the to-do list."""
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
