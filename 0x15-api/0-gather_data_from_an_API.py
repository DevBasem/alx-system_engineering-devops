#!/usr/bin/python3

import requests
import sys


def get_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = '{}/{}'.format(base_url, employee_id)
    user_url = '{}/todos'.format(todo_url)

    # Fetch user data
    user_response = requests.get(todo_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch todo list data
    todo_response = requests.get(user_url)
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    # Display progress
    print("Employee {} is done with tasks ({}"
          "/{}):".format(employee_name, done_tasks, total_tasks))
    for task in todo_data:
        if task['completed']:
            print("\t{}".format(task['title']))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_progress(employee_id)
