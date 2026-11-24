# Task Tracker CLI - roadmap.sh project
# Usage: python3 task_cli.py <command> [arguments]

import sys
from taskTracker import TaskTracker, Status, TaskFileError

USAGE = """\
Usage:
  task-cli add "<description>"
  task-cli update <id> "<description>"
  task-cli delete <id>
  task-cli mark-in-progress <id>
  task-cli mark-done <id>
  task-cli list [todo | in-progress | done]"""

LIST_FILTERS = {
    "todo": Status.TODO,
    "in-progress": Status.IN_PROGRESS,
    "done": Status.DONE,
}

MARK_COMMANDS = {
    "mark-in-progress": Status.IN_PROGRESS,
    "mark-done": Status.DONE,
}


def error(message):
    print(f"Error: {message}", file=sys.stderr)
    return 1


def parseId(value):
    value = value.strip()
    return int(value) if value.isdigit() else None


def printTasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']} ({task['status']}) "
            f"- updated {task['updatedAt']}")


def main():
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        return 1

    command, params = args[0], args[1:]

    try:
        tracker = TaskTracker()
    except TaskFileError as e:
        return error(e)

    try:
        if command == "add":
            if len(params) != 1 or not params[0].strip():
                return error('usage: task-cli add "<description>"')
            newId = tracker.addTask(params[0].strip())
            print(f"Task added successfully (ID: {newId})")

        elif command == "update":
            if len(params) != 2 or not params[1].strip():
                return error('usage: task-cli update <id> "<description>"')
            taskId = parseId(params[0])
            if taskId is None:
                return error(f"invalid id '{params[0]}'")
            if not tracker.updateTask(taskId, params[1].strip()):
                return error(f"task {taskId} not found")
            print(f"Task {taskId} updated successfully")

        elif command == "delete":
            if len(params) != 1:
                return error("usage: task-cli delete <id>")
            taskId = parseId(params[0])
            if taskId is None:
                return error(f"invalid id '{params[0]}'")
            if not tracker.deleteTask(taskId):
                return error(f"task {taskId} not found")
            print(f"Task {taskId} deleted successfully")

        elif command in MARK_COMMANDS:
            if len(params) != 1:
                return error(f"usage: task-cli {command} <id>")
            taskId = parseId(params[0])
            if taskId is None:
                return error(f"invalid id '{params[0]}'")
            status = MARK_COMMANDS[command]
            task = tracker.findTask(taskId)
            if task is None:
                return error(f"task {taskId} not found")
            if task["status"] == status.value:
                print(f"Task {taskId} is already {status.value}")
                return 0
            tracker.markTask(taskId, status)
            print(f"Task {taskId} marked as {status.value}")

        elif command == "list":
            if len(params) > 1:
                return error("usage: task-cli list [todo | in-progress | done]")
            if not params:
                printTasks(tracker.listTasks())
            elif params[0] in LIST_FILTERS:
                printTasks(tracker.listTasks(LIST_FILTERS[params[0]]))
            else:
                return error(f"unknown filter '{params[0]}' "
                             "(use todo, in-progress or done)")

        else:
            print(f"Unknown command '{command}'\n", file=sys.stderr)
            print(USAGE, file=sys.stderr)
            return 1

    except OSError as e:
        return error(f"could not save tasks ({e})")

    return 0


if __name__ == "__main__":
    sys.exit(main())