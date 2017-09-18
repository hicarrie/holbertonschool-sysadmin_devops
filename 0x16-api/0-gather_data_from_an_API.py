#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress
"""

import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    employee = requests.get(url + "users/" + employee_id)
    employee_json = employee.json()

    tasks = requests.get(url + "todos?userId=" + employee_id)
    tasks_json = tasks.json()

    tasks_done_list = []
    for item in tasks_json:
        if item.get('completed') is True:
            tasks_done_list.append(item)

    tasks_done = len(tasks_done_list)
    tasks_total = len(tasks_json)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_json.get('name'), tasks_done, tasks_total))
    for item in tasks_done_list:
        print("\t{}".format(item.get('title')))
