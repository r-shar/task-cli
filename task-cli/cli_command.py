from enum import Enum

class CLICommand(str, Enum):
  ADD = "add"
  UPDATE = "update"
  DELETE = "delete"

  MARK_IN_PROGRESS = "mark-in-progress"
  MARK_DONE = "mark-done"

  LIST = "list"

