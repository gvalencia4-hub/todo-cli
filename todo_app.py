"""
To-Do List CLI App
- Add tasks
- View tasks
- Delete tasks
- Quit
Tasks stored in a Python list.
Includes input validation and try/except/else/finally error handling.
"""

def show_welcome() -> None:
    """Print welcome message."""
    print("\n==============================")
    print("   Welcome to the To-Do App   ")
    print("==============================\n")


def run_app(tasks: list) -> None:
    """Main menu loop for the To-Do CLI app."""
    while True:
        try:
            print("\nMain Menu")
            print("1) Add task")
            print("2) View tasks")
            print("3) Delete task")
            print("4) Quit")

            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                delete_task(tasks)
            elif choice == "4":
                print("\n👋 Goodbye! Thanks for using the To-Do App.\n")
                break
            else:
                raise ValueError("Invalid menu option. Please choose 1-4.")

        except ValueError as e:
            print(f"⚠️ {e}")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
        else:
            # runs only if no exception happened
            pass
        finally:
            # runs every loop no matter what
            pass


def delete_task(tasks: list) -> None:
    """Delete a task by its number."""
    try:
        if len(tasks) == 0:
            raise ValueError("No tasks available to delete.")

        view_tasks(tasks)
        choice = input("\nEnter the task number to delete: ").strip()

        # Validate it is an integer
        task_num = int(choice)

        # Validate range
        if task_num < 1 or task_num > len(tasks):
            raise IndexError("That task number does not exist.")

    except ValueError:
        print("⚠️ Invalid input. Please enter a valid number.")
    except IndexError as e:
        print(f"⚠️ {e}")
    else:
        removed = tasks.pop(task_num - 1)
        print(f"🗑️ Deleted: {removed}")
    finally:
        # Demonstrates finally block always runs
        pass


def get_menu_choice() -> str:
    """
    Ask the user for a menu choice.
    Uses try/except/else/finally to validate selection.
    """
    try:
        choice = input("\nChoose an option (1-4): ").strip()
        if choice not in {"1", "2", "3", "4"}:
            raise ValueError("Menu option does not exist.")
    except ValueError as e:
        print(f"⚠️ {e} Please choose 1, 2, 3, or 4.")
        return ""
    else:
        return choice
    finally:
        # Always runs; included to satisfy requirement
        pass


def main() -> None:
    """Main program loop."""
    tasks = []  # Storage method: Python list
    show_welcome()

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "":
            continue

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\n👋 Goodbye! Thanks for using the To-Do App.\n")
            break

    


def main():
    tasks = []
    show_welcome()
    run_app(tasks)

if __name__ == "__main__":
    main()
