# Task Manager

A simple Task Manager application built in Python, utilizing data classes and a command-line interface to manage tasks. This project includes features such as adding, deleting, updating, and listing tasks, with persistent storage using JSON.

## Features

- **Add Tasks**: Add new tasks with descriptions.
- **Delete Tasks**: Remove tasks by their unique ID.
- **Update Status**: Mark tasks as completed.
- **List Tasks**: View all tasks with their current status.
- **Persistent Storage**: Save and load tasks from a JSON file.

## Project Structure

- `task.py`: Contains the `Task` data class definition.
- `task_manager.py`: Manages tasks, including adding, deleting, updating, and saving tasks.
- `utils.py`: Provides utility functions for displaying the menu and handling user input.
- `main.py`: Entry point for the application that initializes and runs the Task Manager.

## Setup

### Prerequisites

- Python 3.6 or higher

## Usage

After running the application, you will be presented with a menu in the terminal:

1. **Add Task**: Enter a description to add a new task.
2. **Delete Task**: Provide the ID of the task to delete it.
3. **Mark Task as Completed**: Provide the ID of the task to mark it as completed.
4. **List Tasks**: View all current tasks with their descriptions and statuses.
5. **Exit**: Save changes and exit the application.

## Contributing

Feel free to fork the repository and submit pull requests with improvements or bug fixes. Make sure to follow standard coding conventions and provide clear commit messages.
