#!/usr/bin/python3
"""
Export data in the JSON format.
"""
import json
import requests
from sys import argv


def export_all_to_json():
    """
    Export all tasks to JSON format.
    """
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = []

        for todo in todos:
            if todo.get("userId") == user_id:
                task_data = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
                user_tasks.append(task_data)

        all_data[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)


if __name__ == "__main__":
    export_all_to_json()
