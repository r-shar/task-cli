from collections import defaultdict
from task import Task

class TaskList:

  def __init__(self):
    self.tasks = defaultdict(Task)
    # self.to_do_tasks = defaultdict(list)
    # self.in_progress_tasks = defaultdict(list)
    # self.done_tasks = defaultdict(list)

  # all method return types = None because we are doing file r/w operations

  def add_task(self, task: Task) -> None:
    pass 
    
  def update_task(self, task_id: int, updated_task: Task) -> None:
    pass

  def delete_task(self, task_id: int) -> None:
    pass

  def get_all_tasks(self) -> None:
    pass

  def get_done_tasks(self) -> None:
    pass 

  def get_incomplete_tasks(self) -> None:
    pass

  def get_in_progress_tasks(self) -> None:
    pass 


