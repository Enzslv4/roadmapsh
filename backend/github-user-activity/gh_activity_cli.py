from gh_activity import GHActivity, QueryFileError
import sys

USAGE = """\
Usage:
  github-activity <username>
"""

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
        user_activity = GHActivity()
    except QueryFileError as e:
        return error(e)

    try:
        user_activityies = user_activity.query_user(command)
        print(user_activity.treat_data())

    except OSError as e:
        return error(f"could not save tasks ({e})")

if __name__ == "__main__":
    sys.exit(main())