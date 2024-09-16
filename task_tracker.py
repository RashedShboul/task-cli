
import json
import os
from datetime import datetime

FILE_PATH = 'tasks.json'

def save_tasks(tasks):
    #Save the list of tasks to the file
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    #Load tasks from the file, or return an empty list if the file doesn't exist
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        return json.load(file)

def add_task(desc):
    """Add a new task to the task list"""
    new_task = {
        "id": 1,
        "description": desc,
        "status": 'todo',
        "createdAt": str(datetime.now().replace(microsecond=0)),
        "updatedAt": str(datetime.now().replace(microsecond=0))
    }
    tasks = load_tasks()
    if not tasks:
        new_task['id'] = 1
    else:
        new_task['id'] = max(item['id'] for item in tasks) + 1

    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task "{desc}" added with ID {new_task["id"]}')
            
def list_tasks(option):
        tasks = load_tasks()
        if not tasks:
            print('No Tasks')
            return
        for task in tasks:
            if option == 'all' or task['status'] == option:
                print(str(task['id']) + ' ' + task['description'])


def update_description(id_to_update, new_desc):
    tasks = load_tasks()
    if not tasks: 
        print(f'Task with ID {id_to_update} not found')
        return
    id_to_update = int(id_to_update)
    updated = False
    for task in tasks: 
        if (task['id'] == id_to_update):
            task['description'] = new_desc
            task['updatedAt'] = str(datetime.now().replace(microsecond=0))
            print(f'Task with ID {id_to_update} Updated')
            save_tasks(tasks)
            return
    print(f'Task with {id_to_update} not found')
    
    
def change_status(id_to_update, new_status):
    tasks = load_tasks()
    if not tasks: 
        print(f'Task with ID {id_to_update} not found')
        return
    id_to_update = int(id_to_update)
    for task in tasks: 
        if (task['id'] == id_to_update):
            task['status'] = new_status
            task['updatedAt'] = str(datetime.now().replace(microsecond=0))
            save_tasks(tasks)
            print(f'Task with ID {id_to_update} status changed to {new_status}')
            return
    print(f'Task with ID {id_to_update} not found')
        
        
def delete_task(id_to_delete):
    tasks = load_tasks()
    if not tasks: 
        print(f'Task with ID {id_to_delete} not found')
        return
    id_to_delete = int(id_to_delete)
    for task in tasks: 
        if (task['id'] == id_to_delete):
            tasks.remove(task)
            print(f'Task with ID {id_to_delete} deleted')
            save_tasks(tasks)
            return
    print(f'Task with ID {id_to_delete} not found')
    
