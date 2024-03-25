#!/usr/bin/python3
"""Retrieve information about an employee's TODO list progress
using the JSONPlaceholder REST API and export data in CSV format."""

import csv
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
    # Fetch user data
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todo list data
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_data = todos_response.json()

    # Collect tasks owned by the employee
    employee_tasks = []
    for task in todo_data:
        if task.get('userId') == int(employee_id):
            task_row = [
                "{}".format(employee_id),
                "{}".format(employee_name),
                "{}".format(str(task.get('completed'))),
                "{}".format(task.get('title'))
            ]
            employee_tasks.append(task_row)

    # Export data to CSV file
    filename = '{}.csv'.format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(employee_tasks)

    print("Data exported to", filename)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_progress(employee_id)
