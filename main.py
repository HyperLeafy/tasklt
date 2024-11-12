import argparse
  # Import TaskManager from the package
from tasks import TaskManager

def main():
    # Initialize the task manager
    manager = TaskManager()

    # Set up the argument parser
    parser = argparse.ArgumentParser(description="A simple Todo CLI tool.")
    parser.add_argument("command", choices=["add", "list", "edit", "delete", "toggle"], help="Command to execute.")
    parser.add_argument("args", nargs="*", help="Arguments for the command.")

    # Parse arguments
    args = parser.parse_args()

    if args.command == "add":
        if args.args:
            title = " ".join(args.args)
            manager.add_task(title)
        else:
            print("Please provide a title for the task.")

    elif args.command == "list":
        manager.list_tasks()

    elif args.command == "edit":
        if len(args.args) >= 2:
            try:
                index = int(args.args[0])
                new_title = " ".join(args.args[1:])
                manager.edit_task(index, new_title)
            except ValueError:
                print("Invalid task index.")
        else:
            print("Please provide the task index and new title.")

    elif args.command == "delete":
        if args.args:
            try:
                index = int(args.args[0])
                manager.delete_task(index)
            except ValueError:
                print("Invalid task index.")
        else:
            print("Please provide the task index to delete.")

    elif args.command == "toggle":
        if args.args:
            try:
                index = int(args.args[0])
                manager.toggle_task(index)
            except ValueError:
                print("Invalid task index.")
        else:
            print("Please provide the task index to toggle.")

if __name__ == "__main__":
    main()
