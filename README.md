# Simple Task Manager

A command-line task management tool built with Python.
Learning project from https://roadmap.sh/projects/task-tracker

## Features

- Add tasks
- List tasks (all, todo, in-progress, done)
- Mark tasks as in-progress or done
- Update task descriptions
- Delete tasks

## Usage

```
python task-cli.py <command> [arguments]
```

Commands:
- `add <description>`: Add a new task
- `list [all|todo|in-progress|done]`: List tasks
- `mark-in-progress <task_id>`: Mark a task as in-progress
- `mark-done <task_id>`: Mark a task as done
- `update <task_id> <new_description>`: Update task description
- `delete <task_id>`: Delete a task
- `help`: Show usage information

## Examples

```
python task-cli.py add "Buy groceries"
python task-cli.py list all
python task-cli.py mark-done 1
python task-cli.py delete 2
```

## File Structure

- `task_tracker.py`: Core functionality
- `task-cli.py`: Command-line interface
- `tasks.json`: Task storage (created automatically)

## Requirements

- Python 3.6+
