import requests

#todo.py
def get_tasks():
    return requests.get(_url('/tasks/'))

def describe_task(task_id):
    pass

def add_task(summary, description=""):
    pass

def task_done(task_id):
    pass

def update_task(task_id, summary, description):
    pass

def _url(path):
    return 'https://jsonplaceholder.typicode.com/todos' + path
