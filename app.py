from model import TaskModel
from typing import Dict


class Controller:
    def __init__(self):
        self.last_used_id = -1
        self.task_db: Dict[int, TaskModel] = {}

    def create_task(self, task: TaskModel):
        self.last_used_id += 1
        self.task_db[self.last_used_id] = task
        return self.task_db[self.last_used_id]

    def update_task(self, task_id, task: TaskModel):
        if task_id not in self.task_db:
            return None
        self.task_db[task_id] = task
        return self.task_db[task_id]

    def read_task(self, task_id):
        if task_id not in self.task_db:
            return None
        return self.task_db[task_id]

    def delete_task(self, task_id):
        if task_id not in self.task_db:
            return None
        return self.task_db.pop(task_id)

    def read_all_tasks(self):
        return self.task_db


controller = Controller()
