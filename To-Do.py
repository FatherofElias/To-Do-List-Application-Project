def display_menu():
    """Display the menu of options for the to-do list application."""
    print("\nWelcome to the To-Do List App!\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def main():
    """Run the to-do list application."""
    tasks = []
    while True:
        try:
            display_menu()
            choice = input("Please choose an option: ")
            if choice == "1":
                title = input("Enter the task title: ")
                tasks.append({"title": title, "status": "Incomplete"})
            elif choice == "2":
                if not tasks:
                    print("The task list is empty.")
                    continue
                else:
                    for i, task in enumerate(tasks):
                        print(f"{i+1}. {task['title']} - {task['status']}")
            elif choice == "3":
                if not tasks:
                    print("The task list is empty.")
                    continue
                else:
                    task_number = int(input("Enter the task number to mark as complete: "))
                    tasks[task_number-1]["status"] = "Complete"
            elif choice == "4":
                if not tasks:
                    print("The task list is empty.")
                    continue
                else:
                    task_number = int(input("Enter the task number to delete: "))
                    del tasks[task_number-1]
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
        except IndexError:
            print("Oops! That task number does not exist. Try again...")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        else:
            print("Your command was executed successfully!")
        finally:
            print("Thank you for using the To-Do List App!")

if __name__ == "__main__":
    main()