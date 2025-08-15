import json, os, argparse

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(text):
    tasks = load_tasks()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"✅ Added: {text}")

def list_tasks(show_all=False):
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "•"
        if show_all or not t["done"]:
            print(f"{i}. [{status}] {t['text']}")

def mark_done(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    tasks[index - 1]["done"] = True
    save_tasks(tasks)
    print(f"🎉 Done: {tasks[index - 1]['text']}")

def clear_done():
    tasks = load_tasks()
    tasks = [t for t in tasks if not t["done"]]
    save_tasks(tasks)
    print("🧹 Cleared completed tasks.")

def parse_args():
    p = argparse.ArgumentParser(description="Simple To-Do CLI")
    sub = p.add_subparsers(dest="cmd")

    a = sub.add_parser("add", help="Add a task")
    a.add_argument("text", nargs="+", help="Task description")

    l = sub.add_parser("list", help="List tasks")
    l.add_argument("--all", action="store_true", help="Show completed too")

    d = sub.add_parser("done", help="Mark task as done")
    d.add_argument("number", type=int, help="Task number (from list)")

    sub.add_parser("clear", help="Clear completed tasks")
    return p.parse_args()

def main():
    args = parse_args()
    if args.cmd == "add":
        add_task(" ".join(args.text))
    elif args.cmd == "list":
        list_tasks(show_all=args.all)
    elif args.cmd == "done":
        mark_done(args.number)
    elif args.cmd == "clear":
        clear_done()
    else:
        print('Use: add | list [--all] | done <number> | clear\nExample: python todo.py add "Buy milk"')

if __name__ == "__main__":
    main()
