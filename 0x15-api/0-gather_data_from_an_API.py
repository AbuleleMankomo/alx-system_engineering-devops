#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    url_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])
    employee = requests.get(url_user).json()

    employeeName = employee.get('name')

    done_tasks = []
    # This loops the the tasks and check to
    all_tasks = requests.get(url_todo).json()
    for task in all_tasks:
        if task.get('completed') is True:
            done_tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        employeeName, len(done_tasks), len(all_tasks)))

    for task in done_tasks:
        print("\t {}".format(task))
