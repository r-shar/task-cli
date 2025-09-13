from collections import defaultdict
from typing import List
from task import Task
import os, sys
import json

from status import Status   

class TaskList:

  def __init__(self, filename: str="tasks.json"):
    self.filename=filename
    self._check_file_exists()

  def _check_file_exists(self) -> None:
    if not os.path.exists(self.filename):
      with open(self.filename, 'w') as f:
        json.dump({}, f)

  def _load_tasks(self):
    try: 
      with open(self.filename, 'r') as f:
        data = json.load(f)
        return {task_id: Task.from_dict(task_id, task_data) for task_id, task_data in data.items()}
    except (json.JSONDecodeError, FileNotFoundError):
      return {}
    
  def _write_tasks(self, tasks: List[Task]):
    data = {str(k): v.to_dict() for k,v in tasks.items()}
    
    with open(self.filename, 'w') as f:
      json.dump(data, f)

  def add_task(self, task: Task) -> None:
    if not task.get_task_id() or task.get_task_id == None:
      print(f'task: {task.get_description()} does not have a valid id')
      return

    tasks = self._load_tasks()
    # add task
    tasks[task.get_task_id()] = task 
    self._write_tasks(tasks)  

    print(f'Task added successfully (ID: {task.get_task_id()})')
    
    
  def update_task(self, task_id: str, updated_task_desc: str) -> None:
    if task_id == None:
      print(f'Please enter valid task_id')
      return 
    tasks = self._load_tasks()
    if task_id not in tasks:
      print(f'Task id: {task_id} is not present in task list. Unable to update.')
      return
    tasks[task_id].set_description(updated_task_desc)
    try:
      self._write_tasks(tasks)
    except Exception as e:
      print(f'Failed to save task: {e}')
      return
    
    print(f'Successfully updated task with task id: {task_id}.')


  def delete_task(self, task_id: str) -> None:
    if task_id == None:
      print(f'Please enter valid task_id')
      return 
    tasks = self._load_tasks()
    if task_id not in tasks:
      print(f'Task id: {task_id} is not present in task list. Unable to delete.')
      return
    task = tasks[task_id]
    del tasks[task_id]
    self._write_tasks(tasks)
    
    print(f'Successfully deleted task with task id: {task_id} and description: {task.get_description()}')

  def mark_task(self, task_id: str, status_str: str) -> None:
    if task_id == None:
      print(f'Please enter valid task_id')
      return 
    tasks = self._load_tasks()
    if task_id not in tasks:
      print(f'Task id: {task_id} is not present in task list. Unable to update status.')
      return
    match status_str:
      case "mark-in-progress":
        tasks[task_id].set_status(Status.IN_PROGRESS)
      case "mark-done":
        tasks[task_id].set_status(Status.DONE)
      case _:
        print(f'Invalid status state passed: {status_str}')


    self._write_tasks(tasks)
    print(f'Successfully marked task with task id: {task_id} as: {tasks[task_id].get_status()}')
    

  def get_all_tasks(self) -> None:
    tasks = self._load_tasks()
    return tasks

  def get_done_tasks(self) -> None:
    tasks = self._load_tasks()
    done_tasks = {k:v for k,v in tasks.items() if v.get_status() == Status.DONE}
    return done_tasks 

  def get_incomplete_tasks(self) -> None:
    tasks = self._load_tasks()
    incomplete_tasks = {k:v for k,v in tasks.items() if v.get_status() == Status.TODO}
    return incomplete_tasks

  def get_in_progress_tasks(self) -> None:
    tasks = self._load_tasks()
    in_progress_tasks = {k:v for k,v in tasks.items() if v.get_status() == Status.IN_PROGRESS}
    return in_progress_tasks


