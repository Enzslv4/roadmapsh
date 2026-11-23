# General class of the task tracker

from enum import Enum

class Status(Enum):
    NOT_DONE = "not done"
    IN_PROGRESS = "in progress"
    DONE = "done"

STATUS_CHOICES = {
    1: Status.NOT_DONE,
    2: Status.IN_PROGRESS,
    3: Status.DONE
}

class TaskTracker ():

    def __init__(self):
        self.taskList = {}

    def addTask(self, taskName):
        if taskName in self.taskList:
            return False
        self.taskList[taskName] = Status.NOT_DONE
        return True

    def deleteTask(self, taskName):
        return self.taskList.pop(taskName, None) is not None

    def updateTask(self, taskName, statusNumber):
        if taskName not in self.taskList or statusNumber not in STATUS_CHOICES:
            return False
        self.taskList[taskName] = STATUS_CHOICES[statusNumber]
        return True

    def taskByStatus(self, status):
        return list(task for task, s in self.taskList.items() if s == status)