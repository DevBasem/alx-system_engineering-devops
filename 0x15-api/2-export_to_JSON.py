#!/usr/bin/python3
"""Retrieve information about an employee's TODO list progress
using the JSONPlaceholder REST API and export it to a JSON file."""

import json
import requests
import sys


def get_todo_progress(employee_id):
    """
    Retrieve and display information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    user_data = user_response.json()
    employee_name = user_data.get('username')

    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_data = todos_response.json()

    employee_tasks = []
    for task in todo_data:
        if task.get('userId') == int(employee_id):
            employee_tasks.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_name
            })

    filename = "{}.json".format(employee_id)
    with open(filename, mode='w') as json_file:
        json.dump({employee_id: employee_tasks}, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_progress(employee_id)
