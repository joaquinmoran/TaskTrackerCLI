import itertools
import os
import json
from datetime import datetime


class Task:
    
    id_iter = itertools.count()
    
    def __init__(self):
        pass

    def add_task(self, description):
        self.id = next(self.id_iter)
        self.description = description
        self.status = 'todo'
        self.createdAt = datetime.now()
        self.updatedAt = self.createdAt
        return self
    
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat()
        }

    def __str__(self):
        return (f"Task ID: {self.id}\n"
            f"Description: {self.description}\n"
            f"Status: {self.status}\n"
            f"Created At: {self.createdAt}\n"
            f"Updated At: {self.updatedAt}\n")
    
    def get_task_from_json(file):
        try:
            with open(file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError):
            print(f"The file {file} does not exist")
            return []


    def save_in_json(file, tasks_list):
        if os.path.exists(file):
            with open(file,'w') as file:
                json.dump(tasks_list, file, indent=4)


    def update_task(self, tasks, task_id ,description):
        for task in tasks:
            if task['id'] == task_id:
                task['description'] = description
                task['updateAt'] = datetime.now()
        return tasks
       