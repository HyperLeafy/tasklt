# tasklt is a command-line tool that helps you manage your to-do list with simple commands for adding, listing, editing, deleting, and toggling tasks.
# Installation

    Clone the Repository

git clone https://github.com/your-username/tasklt.git
cd tasklt

Set Up Virtual Environment (Optional but Recommended)

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

#Install Dependencies

Make sure you have dependencies installed, if any are specified in requirment.txt.

    pip install -r requirment.txt

# Usage
Commands

tasklt supports the following commands:

# Add a Task

    Add a new task to your to-do list.

python main.py add <task_title>

    Example: python main.py add "Buy groceries"

# List All Tasks

List all tasks with their current status (completed or not).

python main.py list

# Edit a Task

Edit an existing task's title. Provide the index of the task followed by the new title.

python main.py edit <task_index> <new_task_title>

    Example: python main.py edit 1 "Buy fresh groceries"

# Delete a Task

Delete a task by providing its index.

python main.py delete <task_index>

    Example: python main.py delete 1

# Toggle Task Completion Status

Toggle a task's status (mark as completed or incomplete) by providing its index.

    python main.py toggle <task_index>

        Example: python main.py toggle 1

# Examples

    Add a task: python main.py add "Read a book"
    List tasks: python main.py list
    Edit a task: python main.py edit 2 "Read a new book"
    Delete a task: python main.py delete 2
    Toggle a task's status: python main.py toggle 2

# Notes

    Task Index: The index refers to the task’s position in the list displayed by the list command.
    Error Handling: If you provide invalid input, such as an invalid task index, tasklt will display an error message.
