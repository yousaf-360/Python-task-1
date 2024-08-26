import json
from typing import List, Optional
from task import Task

class TaskManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task(description=ele['description'], completed=ele['completed'], id=ele['id']) for ele in data]
        except Exception as e:
            print(f'An error occurred while loading tasks: {e}')
            return []

    def save_tasks(self):
        try:
            tasks_dict = [{
                "description": task.description,
                "completed": task.completed,
                "id": task.id
            } for task in self.tasks]
            
            with open(self.filename, 'w') as file:
                json.dump(tasks_dict, file, indent=4)
        except Exception as e:
            print(f'An error occurred while saving tasks: {e}')

    def add_task(self, description: str):
        try:
            new_task = Task(description=description)
            self.tasks.append(new_task)
            print('Task Added')
        except Exception as e:
            print(f'Error adding task: {e}')

    def delete_task(self, task_id: str):
        try:
            self.tasks = [task for task in self.tasks if task.id != task_id]
            print(f'Task with ID {task_id} deleted')
        except Exception as e:
            print(f'Error deleting task: {e}')

    def update_status(self, task_id: str):
        task = self.find_task_by_id(task_id)
        if task:
            task.mark_completed()
            print(f'Task with ID {task_id} marked as completed')
        else:
            print(f"Task with ID {task_id} does not exist.")

    def find_task_by_id(self, task_id: str) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def print_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)