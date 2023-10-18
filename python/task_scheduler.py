#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Task Scheduler"""
# version: 0.3.2
# license: MIT
# author: Anthony Pagan
# email: get-tony@outlook.com

import sys
import json
import os
import datetime
from typing import List, Dict


# Define system encoding
ENCODING: str = sys.getfilesystemencoding() or sys.getdefaultencoding()

# Define the data file to store tasks
TASKS_FILE: str = "tasks.json"

# Load tasks from the data file (if it exists)
tasks: List[Dict[str, str]] = []
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r", encoding=ENCODING) as task_file:
        tasks = json.load(task_file)


def save_tasks() -> None:
    """Save tasks to the data file."""
    with open(TASKS_FILE, "w", encoding=ENCODING) as save_file:
        json.dump(tasks, save_file)


def add_task() -> None:
    """Add a task to the list."""
    task_name: str = input("Enter the task name: ")
    due_date: str = input("Enter the due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks.append({"name": task_name, "due_date": due_date})
    save_tasks()
    print(f"Task '{task_name}' added successfully!")


def view_tasks() -> None:
    """View the list of tasks."""
    print("Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['name']} (Due: {task['due_date']})")


def delete_task() -> None:
    """Delete a task from the list."""
    view_tasks()
    task_index: str = input("Enter the task number to delete: ")

    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            deleted_task: Dict[str, str] = tasks.pop(task_index - 1)
            save_tasks()
            print(f"Task '{deleted_task['name']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


SCHEDULER_MENU: str = """
Task Scheduler Menu:
1. Add Task
2. View Tasks
3. Delete Task
4. Quit
"""

while True:
    print("\n" + SCHEDULER_MENU)

    choice: str = input("Enter your choice: ")

    match choice:
        case "1":
            add_task()
        case "2":
            view_tasks()
        case "3":
            delete_task()
        case "4":
            break
        case _:
            print("Invalid choice. Please choose a valid option.")

print("Goodbye!")
