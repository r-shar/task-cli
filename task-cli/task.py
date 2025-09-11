from status import Status
from datetime import datetime 
from uuid import uuid4

class Task:
  def __init__(self, 
               description: str, 
               updated_at: datetime = None,
               created_at: datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
               status: Status = Status.TODO,
              ):
    self.description = description
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.id = uuid4()

  def __dir__(self):
    return ['description', 'status', 'created_at', 'updated_at', 'id']
  
  def _set_updated_at(self):
    curr_datetime = datetime.now()
    self.updated_at = curr_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")  # Convert to string
    return self.updated_at

  def get_description(self) -> str:
    return self.description
  
  def set_description(self, new_desc) -> None:
    self.description = new_desc
    self._set_updated_at()

  def get_status(self) -> Status:
    return self.status 
  
  def set_status(self, new_status: Status) -> None:
    self.status = new_status
  
  def get_created_at(self) -> datetime:
    return self.created_at
  
  def get_updated_at(self) -> datetime | None:
    return self.updated_at

  
  def get_task_id(self):
    return self.id
  
  def to_dict(self):
    return {
        'id': str(self.id),
        'description': self.description,
        'status': self.status.value if hasattr(self.status, 'value') else str(self.status),
        'created_at': self.created_at,
        'updated_at': self.updated_at
    }
  
  @classmethod
  def from_dict(cls, task_id: str, task_data: dict):
    instance = cls.__new__(cls)

    instance.description = task_data.get('description')
    instance.status = Status(task_data.get('status')) if isinstance(task_data.get('status'), int) else task_data.get('status')
    instance.created_at = task_data.get('created_at')
    instance.updated_at = task_data.get('updated_at')
    instance.id = task_id
    
    return instance
