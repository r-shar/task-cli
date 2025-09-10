from task_list import TaskList
from task import Task 
from status import Status
from argparse import ArgumentParser 

def main():
  argparser = ArgumentParser(
    prog='task-cli',
    description='Manages Task List from CLI',
  )
  subparsers = argparser.add_subparsers(dest='command')

  add_parser = subparsers.add_parser('add', help='Add a new task')
  delete_parser = subparsers.add_parser('delete', help='Delete an existing task')
  add_parser.add_argument('description', type=str, help='Task description')
  delete_parser.add_argument('task_id', type=str, help='Task ID')

  args = argparser.parse_args()

  task_list = TaskList()

  if args.command == 'add':
    task_list.add_task(Task(args.description))
  elif args.command == 'delete':
    task_list.delete_task(str(args.task_id))
  else:
    argparser.print_help()




if __name__=='__main__':
  main()