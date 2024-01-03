# todo_list.py
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"name": task, "status": "Pending"})

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["status"] = "Completed"
                break

    def clear_todo_list(self):
        self.tasks = []
