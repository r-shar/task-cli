# Task CLI

A simple command-line task management tool built in Python that allows you to manage your tasks with persistent file storage.

## Features

- ✅ **Add tasks** - Create new tasks with descriptions
- 📝 **Update tasks** - Modify existing task descriptions
- 🗑️ **Delete tasks** - Remove tasks from your list
- 📊 **Track status** - Mark tasks as TODO, IN_PROGRESS, or DONE
- 📋 **List tasks** - View all tasks or filter by status
- 💾 **Persistent storage** - Tasks are saved to a JSON file

## Installation

1. Clone the repository:
```bash
git clone git@github.com:r-shar/task-cli.git
cd task-cli
```

2. Ensure you have Python 3.11+ installed (the project uses Python 3.11 features like match statements)

3. Navigate to the task-cli directory:
```bash
cd task-cli
```

## Usage

### Basic Commands

#### Add a new task
```bash
python main.py add "Your task description"
```

#### List all tasks
```bash
python main.py list
```

#### List tasks by status
```bash
python main.py list todo          # Show only TODO tasks
python main.py list in-progress   # Show only IN_PROGRESS tasks
python main.py list done          # Show only DONE tasks
```

#### Update a task
```bash
python main.py update <task_id> "Updated task description"
```

#### Delete a task
```bash
python main.py delete <task_id>
```

#### Mark task status
```bash
python main.py mark-in-progress <task_id>
python main.py mark-done <task_id>
```

### Examples

```bash
# Add some tasks
python main.py add "Buy groceries"
python main.py add "Write documentation"
python main.py add "Review pull requests"

# List all tasks to see their IDs
python main.py list

# Mark a task as in progress
python main.py mark-in-progress 95c01206-7a29-4e35-8c18-8af7bccd8248

# Update a task description
python main.py update 95c01206-7a29-4e35-8c18-8af7bccd8248 "Buy groceries and cook dinner"

# Mark a task as done
python main.py mark-done 95c01206-7a29-4e35-8c18-8af7bccd8248

# List only completed tasks
python main.py list done

# Delete a task
python main.py delete 95c01206-7a29-4e35-8c18-8af7bccd8248
```

## Project Structure

```
task-cli/
├── main.py           # Entry point and CLI argument parsing
├── task.py           # Task class definition
├── task_list.py      # TaskList class for managing tasks
├── status.py         # Status enum (TODO, IN_PROGRESS, DONE)
├── cli_command.py    # CLI command enum definitions
├── tasks.json        # Persistent storage file (created automatically)
```

## Task Properties

Each task has the following properties:
- **ID**: Unique UUID generated automatically
- **Description**: User-provided task description
- **Status**: One of TODO (0), IN_PROGRESS (1), or DONE (2)
- **Created At**: Timestamp when the task was created
- **Updated At**: Timestamp when the task was last modified

## Data Storage

Tasks are stored in a `tasks.json` file in the project directory. The file is created automatically when you first run the application. Each task is stored with its UUID as the key and contains all task properties.

### Task Status Values

```python
TODO = 0
IN_PROGRESS = 1
DONE = 2
```

## Error Handling

The application includes comprehensive error handling for:
- Invalid task IDs
- Missing tasks
- File I/O errors
- JSON parsing errors

## Help

For help with any command, use:
```bash
python main.py --help
python main.py <command> --help
```
