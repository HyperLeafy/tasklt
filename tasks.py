import os
import time
import json
from tabulate import tabulate

def get_tasks_file_path():
    config_dir = os.path.join(os.path.expanduser("~"), ".config", "tasklt")
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "tasks.json")

TASK_FILE = get_tasks_file_path()


class Task:
    def __init__(self, title, completed=False, created_at=None, completed_at=None) -> None:
        self.title = title
        self.completed = completed
        self.created_at = created_at if created_at else time.time()
        self.completed_at = completed_at
    
    def toggle(self):
        self.completed = not self.completed
        if self.completed:
            self.completed_at = time.time()
    
    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            completed=data["completed"],
            created_at=data["created_at"],
            completed_at=data["completed_at"],
        )

    def __str__(self) -> str:
        completed_str = "✅" if self.completed else "❌"
        completed_at_str = time.ctime(self.completed_at) if self.completed_at else ""
        return f"{self.title} | {completed_str} | {time.ctime(self.created_at)} | {completed_at_str}"


class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    # returns a list of the task in the file
    def load_tasks(self):
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as task_list_file:
                tasks_data = json.load(task_list_file)
                return [Task.from_dict(task) for task in tasks_data]
        return []

    # save/dumps the specified task into the file
    def save_task(self):
        with open(TASK_FILE, 'w') as task_list_file:
            json.dump([Task.to_dict(task) for task in self.tasks], task_list_file, indent=4)

    # append a new task object to the task list
    def add_task(self, title):
        task = Task(title=title)
        self.tasks.append(task)
        self.save_task()
        print(f"Task added: {title}")
    

    # prints out the task list in presentable formate
    def list_tasks(self):
        headers = ["#", "Title", "Completed", "Created At", "Completed At"]
        table = []
        for ids, task in enumerate(self.tasks):
            completed = "✅" if task.completed else "❌"
            created_at = time.ctime(task.created_at)
            completed_at = time.ctime(task.completed_at) if task.completed_at else ""
            table.append([ids, task.title, completed, created_at, completed_at])
        print(tabulate(table, headers, tablefmt="grid"))



    def toggle_task(self, index):
        if index < 0 or index >= len(self.tasks):
            print(f"Error: Invalid task index {index}")
            return
        task = self.tasks[index]
        task.toggle()
        self.save_task()
        print(f"Task '{task.title}' marked as {'completed' if task.completed else 'incomplete'}")
    
    
    def edit_task(self, index, new_title):
        if index < 0 or index >= len(self.tasks):
            print(f"Error: Invalid task index {index}")
            return
        self.tasks[index].title = new_title
        self.save_tasks()
        print(f"Task {index} edited to '{new_title}'.")

   
    def delete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            print(f"Error: Invalid task index {index}")
            return
        deleted_task = self.tasks.pop(index)
        self.save_tasks()
        print(f"Task '{deleted_task.title}' deleted.")