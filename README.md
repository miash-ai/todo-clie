# todo-clie
# ✅ To-Do CLI (Python)

A simple command-line To-Do app. Add tasks, list them, mark done, and clear completed. Data is stored in `tasks.json`.

## ✨ Features
- `add` — add a task
- `list` — show tasks (use `--all` to include completed)
- `done` — mark a task as completed
- `clear` — remove all completed tasks

## 🚀 Run locally
Requires Python 3.10+.

```bash
# clone the repo
git clone https://github.com/<your-username>/todo-cli.git
cd todo-cli

# add a task
python todo.py add "Buy milk"

# list tasks
python todo.py list

# mark task #1 as done
python todo.py done 1

# show all (including completed)
python todo.py list --all

# clear completed tasks
python todo.py clear
