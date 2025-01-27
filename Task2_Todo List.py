import argparse
import json
import os

# File to store the to-do list
TODO_FILE = "todo_list.json"

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(args):
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "task": args.task, "status": "Pending"})
    save_tasks(tasks)
    print(f"Task added: {args.task}")

# Function to view tasks
def view_tasks(args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['task']} - {task['status']}")

# Function to update a task
def update_task(args):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == args.id:
            task["task"] = args.task
            save_tasks(tasks)
            print(f"Task updated to: {args.task}")
            return
    print("Task not found.")

# Function to delete a task
def delete_task(args):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != args.id]
    save_tasks(tasks)
    print(f"Task with ID {args.id} deleted.")

# Function to mark a task as done
def mark_done(args):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == args.id:
            task["status"] = "Done"
            save_tasks(tasks)
            print(f"Task marked as done: {task['task']}")
            return
    print("Task not found.")

# Main function to set up the CLI
def main():
    parser = argparse.ArgumentParser(description="To-Do List Manager")
    subparsers = parser.add_subparsers(help="Commands")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="The task description")
    add_parser.set_defaults(func=add_task)

    # View tasks command
    view_parser = subparsers.add_parser("view", help="View all tasks")
    view_parser.set_defaults(func=view_tasks)

    # Update task command
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="The ID of the task to update")
    update_parser.add_argument("task", type=str, help="The new task description")
    update_parser.set_defaults(func=update_task)

    # Delete task command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="The ID of the task to delete")
    delete_parser.set_defaults(func=delete_task)

    # Mark task as done command
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="The ID of the task to mark as done")
    done_parser.set_defaults(func=mark_done)

    # Parse arguments and execute the corresponding function
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
