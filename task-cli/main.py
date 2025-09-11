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

  # define subparsers
  add_parser = subparsers.add_parser('add', help='Add a new task')
  add_parser.add_argument('description', type=str, help='Task description')
  delete_parser = subparsers.add_parser('delete', help='Delete an existing task')
  delete_parser.add_argument('task_id', type=str, help='Task ID')
  update_parser = subparsers.add_parser('update', help='Update an existing task')
  update_parser.add_argument('task_id', type=str, help='Task ID')
  update_parser.add_argument('updated_task', type=str, help='Updated Task')


  args = argparser.parse_args()

  task_list = TaskList()

  if args.command == 'add':
    task_list.add_task(Task(args.description))
  elif args.command == 'delete':
    task_list.delete_task(args.task_id)
  elif args.command == 'update':
    task_list.update_task(args.task_id, args.updated_task)
  else:
    argparser.print_help()




if __name__=='__main__':
  main()