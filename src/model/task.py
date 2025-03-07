import itertools
import os
import json
from datetime import datetime


class Task:
    
    id_iter = itertools.count()
    
    def __init__(self):
        self.id_iter = itertools.count(start=self._get_max_id() + 1)
        pass

    def _get_max_id(self):
        tasks = self.get_task_from_json("json/tasks.json")
        if tasks:
            return max(task['id'] for task in tasks)
        return 0

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
    
    @staticmethod
    def get_task_from_json(file):
        try:
            with open(file, 'r') as file:
                content = file.read()
                if not content:
                    return []
                return json.loads(content)
        except (FileNotFoundError):
            print(f"The file {file} does not exist")
            return []

    @staticmethod
    def save_in_json(file, tasks_list):
        if os.path.exists(file):
            with open(file,'w') as file:
                json.dump(tasks_list, file, indent=4)


    @staticmethod
    def update_task(tasks, task_id ,description):
        for task in tasks:
            if task['id'] == task_id:
                task['description'] = description
                task['updatedAt'] = datetime.now().isoformat()
        return tasks
    

    @staticmethod
    def delete_task(tasks, task_id):
        for task in tasks:
            if task['id'] == task_id:
                tasks.remove(task)
                return tasks
        return tasks
    
    @staticmethod
    def change_status(tasks ,task_id, status_code):
        for task in tasks:
            if task['id'] == task_id:
                if status_code == 1:
                    task['status'] = "in progress"
                    print("Status changed succesfuly")
                    return tasks
                elif status_code == 2:
                    task['status'] = "done"
                    print("Status changed succesfuly")
                    return tasks
                else:
                    print("task does not exist")
        return tasks

    @staticmethod
    def list_tasks(tasks, code):
        finished = []
        for task in tasks:
            if code == 1:
                if task['status'] == "done":
                    task_descr = task['description']
                    finished.append(task_descr)
            if code == 2:
                if task['status'] == "todo":
                    task_descr = task['description']
                    finished.append(task_descr)
            if code == 3:
                if task['status'] == "in progress":
                    task_descr = task['description']
                    finished.append(task_descr)
        return finished
        

            
    
       
       