# Task Tracker de console

from time import sleep
import os
from taskTracker import TaskTracker, Status
from messages import *

tracker = TaskTracker()

def clearConsole():
    os.system("cls" if os.name == "nt" else "clear")

def trackerLogic():
    running = True
    clearConsole()
    print(WELCOME)
    while running:
        choice = int(input(MENU))
        if choice == 1:
            taskName = input("Digite o nome da task:\n")
            if tracker.addTask(taskName=taskName):
                print("\nTask adicionada!" + "\n")
            else:
                print("\nEssa task já existe." + "\n")
        elif choice == 2:
            taskName = input("\nDigite o nome da task:\n")
            taskStatus = int(input("\n" + STATUS_OPTIONS))
            if tracker.updateTask(taskName, taskStatus):
                print("\nTask atualizada!" + "\n")
            else:
                print("\nTask ou status inválidos." + "\n")
        elif choice == 3:
            taskName = input("\nDigite o nome da task:\n")
            if tracker.deleteTask(taskName=taskName):
                print("\nTask deletada!" + "\n")
            else:
                print("\nEssa task não existe." + "\n")
        elif choice == 4:
            print(tracker.taskByStatus(Status.NOT_DONE))
        elif choice == 5:
            print(tracker.taskByStatus(Status.IN_PROGRESS))
        elif choice == 6:
            print(tracker.taskByStatus(Status.DONE))
        elif choice == 0:
            print("\nEncerrando.")
            running = False
        else:
            print("Opção Inválida." + "\n")

        sleep(1)


trackerLogic()