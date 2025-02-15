# TaskManagement

Welcome to the Task Manager! This program allows you to organize and manage your tasks with ease. It lets you add, update, delete, and sort tasks, while also giving you the ability to set and track deadlines. Built using Python and PyQt5, it provides a simple graphical interface for a smooth user experience.

Whether you're managing personal tasks, work deadlines, or school assignments, this tool can help you stay on top of things. The application stores your tasks in a JSON file, so you can load and save them between sessions.

# Features
- Add Tasks: Add new tasks with titles, descriptions, and deadlines.

- Update Tasks: Edit existing tasks by updating the title, description, or deadline.

- Delete Tasks: Remove tasks that are no longer needed.

- Sort Tasks: Sort tasks by deadline to prioritize important tasks.

- Search Tasks: Search for tasks by title or description.

- Persistent Storage: Your tasks are saved in a tasks.json file and loaded when you open the application.

# Installation
Requirements
To run this application, you need:

- Python 3.x (recommended Python 3.7 or later)
- PyQt5: The GUI library used for building the interface.

# Steps to Install

- Clone the repository:
git clone https://github.com/daaingkaryaad/TaskManagement.git
 and 
cd TaskManagement

- Create a virtual environment (optional but recommended): "python -m venv .venv"

- Activate the virtual environment:

For Windows: ".\.venv\Scripts\activate"

macOS/Linux: "source .venv/bin/activate"

- Install dependencies:

"pip install -r requirements.txt"
(If you don't have a requirements.txt, you can manually install PyQt5 with: pip install PyQt5)

- Run the Application: "python main.py"


# Usage
1. Main Interface: 
when you launch the application, you will see a graphical interface with the following components:

- Search Bar: Search for tasks by keyword.
- Task List: Displays all tasks. You can select a task to update or delete.
- Task Input Fields: Enter the title, description, and deadline for a new task.

2. Buttons:
- Add Task: Adds a new task to the list.
- Update Task: Updates the selected task with new details.
- Delete Task: Deletes the selected task.
- Sort by Deadline: Sorts tasks by deadline, showing tasks that are due sooner first.

3. Adding a Task
- Enter the task title.
- Enter the description of the task.
- Select the deadline using the date picker.
- Click the Add Task button to add the task to the list.

4. Updating a Task
- Select a task from the list.
- Modify the title, description, or deadline.
- Click the Update Task button to save the changes.

5. Deleting a Task
- Select the task you want to delete.
- Click the Delete Task button to remove it from the list.

6. Sorting Tasks by Deadline
- Click the Sort by Deadline button to reorder tasks by their deadline. Tasks with upcoming deadlines will be shown first.

7. Searching for Tasks
Type a keyword into the Search Bar to filter tasks by their title or description.

8. File Storage
All tasks are saved in a tasks.json file in the same directory as the application. This file is automatically loaded when you start the program, allowing you to continue where you left off.

# Contributing
Feel free to contribute to this project! If you have suggestions for improvements, or encounter bugs, please open an issue or submit a pull request.

Fork the repository to your GitHub account.
Clone your fork to your local machine.
Make your changes and commit them.
Push your changes to your fork and submit a pull request.