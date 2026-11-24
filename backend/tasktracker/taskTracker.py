# Core logic of the task tracker: tasks are stored in a JSON file

import json
import os
from datetime import datetime
from enum import Enum

DATA_DIR = "data"
FILE = os.path.join(DATA_DIR, "list.json")

class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

class TaskFileError(Exception):
    """Raised when the JSON file exists but can't be used."""

def timestamp():
    return datetime.now().isoformat(timespec="seconds")

class TaskTracker:

    def __init__(self):
        self.tasks = self.load()

    # ---------- Persistence ----------

    def load(self):
        # No file yet: start with an empty list (the file is created on the first save)
        if not os.path.exists(FILE):
            return []

        try:
            with open(FILE, encoding="utf-8") as f:
                content = f.read().strip()
        except OSError as e:
            raise TaskFileError(f"could not read {FILE} ({e})") from e

        # Empty file counts as an empty list
        if not content:
            return []

        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            raise TaskFileError(f"{FILE} is not valid JSON") from e

        if not isinstance(data, list):
            raise TaskFileError(f"{FILE} must contain a list of tasks")

        return data

    def save(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    # ---------- Queries (read only) ----------

    def findTask(self, taskId):
        for task in self.tasks:
            if task["id"] == taskId:
                return task
        return None

    def listTasks(self, status=None):
        if status is None:
            return list(self.tasks)
        return [task for task in self.tasks if task["status"] == status.value]

    # ---------- Changes (always save) ----------

    def addTask(self, description):
        now = timestamp()
        newId = max((task["id"] for task in self.tasks), default=0) + 1
        self.tasks.append({
            "id": newId,
            "description": description,
            "status": Status.TODO.value,
            "createdAt": now,
            "updatedAt": now,
        })
        self.save()
        return newId

    def updateTask(self, taskId, description):
        task = self.findTask(taskId)
        if task is None:
            return False
        task["description"] = description
        task["updatedAt"] = timestamp()
        self.save()
        return True

    def deleteTask(self, taskId):
        task = self.findTask(taskId)
        if task is None:
            return False
        self.tasks.remove(task)
        self.save()
        return True

    def markTask(self, taskId, status):
        task = self.findTask(taskId)
        if task is None:
            return False
        task["status"] = status.value
        task["updatedAt"] = timestamp()
        self.save()
        return True