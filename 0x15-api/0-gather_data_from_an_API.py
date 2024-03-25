#!/usr/bin/python3
"""Retrieve information about an employee's TODO list progress
using the JSONPlaceholder REST API."""

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
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                 .format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    total_tasks = 0
    completed = 0

    for task in todos_response.json():
        if task.get('userId') == int(employee_id):
            total_tasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, completed, total_tasks))

    for task in todos_response.json():
        if task.get('userId') == int(employee_id) and task.get('completed'):
            print('\t {}'.format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_progress(employee_id)
