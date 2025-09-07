from status import Status
from datetime import datetime 
from uuid import uuid4

class Task:
  def __init__(self, 
               description: str, 
               created_at: datetime,
               updated_at: datetime | None,
               status: Status = Status.TODO,
              ):
    self.description = description
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.id = uuid4()
  
  def get_description(self) -> str:
    return self.description
  
  def get_status(self) -> Status:
    return self.status 
  
  def get_created_at(self) -> datetime:
    return self.created_at
  
  def get_updated_at(self) -> datetime | None:
    return self.updated_at
  
  def __set_updated_at(self):
    curr_datetime = datetime.now()
    self.updated_at = curr_datetime
    return self.updated_at
  
  def get_task_id(self):
    return self.id

  
     