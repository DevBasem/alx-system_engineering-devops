#!/usr/bin/python3
"""Retrieve information about an employee's TODO list progress
using the JSONPlaceholder REST API and export it to a CSV file."""

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
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    user_data = user_response.json()
    employee_name = user_data.get('username')

    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_data = todos_response.json()

    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator='\n'
        )
        for task in todo_data:
            if task.get('userId') == int(employee_id):
                writer.writerow([
                    str(employee_id),
                    employee_name,
                    str(task.get('completed')),
                    task.get('title')
                ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_progress(employee_id)
