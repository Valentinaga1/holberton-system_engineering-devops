# 0x15. API

# Learning Objectives

* What Bash scripting should not be used for
* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python

### [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py)
Python script that, using this REST API:https://jsonplaceholder.typicode.com/ , for a given employee ID, returns information about his/her TODO list progress.

### [1-export_to_CSV.py](./1-export_to_CSV.py)
Python script to export data in the CSV format.  
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

### [2-export_to_JSON.py](./2-export_to_JSON.py)
Python script to export data in the JSON format.  
Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}

### [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py)
Python script to export data in the JSON format.  
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}