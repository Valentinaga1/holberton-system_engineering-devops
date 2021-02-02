#!/usr/bin/python3
"""Python Script that gather data from an API"""
import requests
import sys

if __name__ == "__main__":
    employee_id = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    employe_id_response = requests.get(employee_id)
    employe__id_response_dict = employe_id_response.json()
    # print(employe_id_response) /<Response [200]>
    # print(employe__id_response_list)/ dic with info of id 2
    # print(type(employe__id_response_list)) / dict
    employe_name = employe__id_response_dict.get("name")

    todos = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    todos_response = requests.get(todos)
    tasks_list = todos_response.json()
    # print(todos_response) / <Response [200]>
    # print(tasks_list) / list of dict with info
    # print(type(tasks_list)) /list

    total_number_of_tasks = len(tasks_list)
    number_of_done_tasks = 0
    task_titles = []
    for task in tasks_list:
        if task.get("completed") is True:
            number_of_done_tasks += 1
            task_titles.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
           employe_name, number_of_done_tasks, total_number_of_tasks))
    for title in task_titles:
        print("\t {}".format(title))
