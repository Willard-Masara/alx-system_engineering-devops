#!/usr/bin/python3
"""
Using employee id to track their wok progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmployee = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmployee)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmployee)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    updateUser[idEmployee] = totalTasks

    file_Json = idEmployee + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
