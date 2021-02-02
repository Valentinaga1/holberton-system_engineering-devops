#!/usr/bin/python3
"""Using and API and work in Json
"""
import json
from requests import get


if __name__ == "__main__":
    info = "https://jsonplaceholder.typicode.com/users/"
    users = get(info).json()
    totalU = [user for user in users]
    d = {}
    for userId in range(1, len(totalU) + 1):
        name = get("https://jsonplaceholder.typicode.com/users/{}"
                   .format(userId)).json()
        tasksuser = get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(userId)).json()
        dict_ = []
        for task in tasksuser:
            dict_.append({"task": task.get("title"),
                         "completed": task.get("completed"),
                          "username": name.get("username")})
        d[userId] = dict_
    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(d, indent=4))
