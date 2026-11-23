# Task Tracker

Solution to the [Task Tracker](https://roadmap.sh/projects/task-tracker) project from [roadmap.sh](https://roadmap.sh).

A console app for tracking tasks and their status, written in pure Python with no external libraries.

## Features

- Add, update and delete tasks
- Set a task's status to **not done**, **in progress** or **done**
- List tasks filtered by status
- Interactive menu that works on Windows, macOS and Linux

## Project structure

```
.
├── main.py          # Entry point: menu loop and user input
├── taskTracker.py   # TaskTracker class and Status enum (core logic)
└── messages.py      # Console texts (welcome screen, menu, status options)
```

The core logic (`TaskTracker`) knows nothing about the console. All input and output stays in `main.py`, so the class can be reused elsewhere.

## Requirements

- Python 3.8+
- No external dependencies

## Running

```bash
git clone <repo-url>
cd <repo-folder>
python3 main.py      # on Windows: python main.py
```

## Usage

```
1 - Add task
2 - Update status
3 - Delete task
4 - List tasks not done
5 - List tasks in progress
6 - List tasks done
0 - Exit
```

## Progress against the roadmap.sh spec

- [x] Add, update and delete tasks
- [x] Mark a task as in progress or done
- [x] List tasks by status (done / not done / in progress)
- [x] No external libraries
- [ ] List **all** tasks
- [ ] Persist tasks in a JSON file in the current directory (created if missing)
- [ ] Task properties: `id`, `description`, `status`, `createdAt`, `updatedAt`
- [ ] Positional command-line arguments (`task-cli add "Buy groceries"`, `task-cli mark-done 1`, ...)
- [ ] Graceful handling of every invalid input and edge case

## What I practiced

- Classes and methods in Python
- `Enum` for a fixed set of states
- Dictionaries as lookup tables
- Splitting a project into modules and importing between them
- Building a cross-platform console UI