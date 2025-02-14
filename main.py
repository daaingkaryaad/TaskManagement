import sys
import json
import os
from datetime import datetime, date
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLineEdit, QTextEdit, QMessageBox, QDateEdit
)

class TaskBase:
    #our base class for tasks, description, sorting by deadline

    def __init__(self, title, description, deadline=None, timestamp=None):
        self.title = title
        self.description = description
        self.timestamp = timestamp if timestamp else datetime.now().isoformat()
        self.deadline = deadline if deadline else None  #to store as string (YYYY-MM-DD)

    def update(self, new_title=None, new_description=None, new_deadline=None):

        #update task details and refreshes timestamp

        if new_title:
            self.title = new_title
        if new_description:
            self.description = new_description
        if new_deadline:
            self.deadline = new_deadline
        self.timestamp = datetime.now().isoformat()  #to refresh timestamp


    def to_dict(self):

        #to convert task to dictionary for saving to json

        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data):

        #to create a Task object from dictionary data

        return Task(
            data["title"],
            data["description"],
            data.get("deadline"),  #to get deadline
            data.get("timestamp", datetime.now().isoformat())
        )

    def __str__(self):

        #format task display in list

        formatted_time = datetime.fromisoformat(self.timestamp).strftime("%Y-%m-%d %H:%M:%S")
        deadline_display = f" | Deadline: {self.deadline}" if self.deadline else ""
        return f"{self.title} - {self.description}{deadline_display} (Last Modified: {formatted_time})"


class Task(TaskBase):

    #standard task that inherits from TaskBase

    pass  #just inherits everything


class TaskManager:

    #to manage tasks and to file storage

    FILE_PATH = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description, deadline):

        #adds a new task with a deadline

        task = Task(title, description, deadline)
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, index, new_title, new_description, new_deadline):

        #to update an existing task and refresh timestamp

        if 0 <= index < len(self.tasks):
            self.tasks[index].update(new_title, new_description, new_deadline)
            self.save_tasks()

    def delete_task(self, index):

        #to delete a task

        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def get_task_list(self):

        #to return the task list as strings

        return [str(task) for task in self.tasks]

    def search_tasks(self, keyword):

        #search tasks that match the word (keyword)

        keyword = keyword.lower()
        return [str(task) for task in self.tasks if keyword in task.title.lower() or keyword in task.description.lower()]

    def save_tasks(self):

        #Saves tasks to a json file

        with open(self.FILE_PATH, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):

        #to load tasks from existing json file

        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as file:
                try:
                    tasks_data = json.load(file)
                    self.tasks = [TaskBase.from_dict(task) for task in tasks_data]
                except json.JSONDecodeError:
                    self.tasks = []  #reset tasks in case of corruption

    def sort_tasks_by_deadline(self):

        #to sort tasks based on their deadline (earliest/overdue first)

        self.tasks.sort(
            key=lambda task: datetime.strptime(task.deadline, "%Y-%m-%d") if task.deadline else datetime.max
        )


class TaskManagerGUI(QWidget):

    #main GUI for Task Manager, we used PyQt5

    def __init__(self):
        super().__init__()

        self.task_manager = TaskManager()

        #window setup
        self.setWindowTitle("Task Manager")
        self.setGeometry(100, 100, 600, 500)

        #layout
        layout = QVBoxLayout()

        #search bar
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search tasks...")
        self.search_input.textChanged.connect(self.search_tasks)
        layout.addWidget(self.search_input)

        #task list
        self.task_list = QListWidget()
        self.load_tasks_into_list()
        layout.addWidget(self.task_list)

        #input fields
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter task title")
        layout.addWidget(self.title_input)

        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Enter task description")
        layout.addWidget(self.description_input)

        #deadline setup
        self.deadline_input = QDateEdit()
        self.deadline_input.setCalendarPopup(True)
        layout.addWidget(self.deadline_input)

        #buttons layout
        button_layout = QHBoxLayout()

        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        button_layout.addWidget(add_button)

        update_button = QPushButton("Update Task")
        update_button.clicked.connect(self.update_task)
        button_layout.addWidget(update_button)

        delete_button = QPushButton("Delete Task")
        delete_button.clicked.connect(self.delete_task)
        button_layout.addWidget(delete_button)

        sort_deadline_button = QPushButton("Sort by Deadline")
        sort_deadline_button.clicked.connect(self.sort_by_deadline)
        button_layout.addWidget(sort_deadline_button)

        layout.addLayout(button_layout)

        #set layout
        self.setLayout(layout)

    def load_tasks_into_list(self, filtered_tasks=None):

        # to load tasks into the list widget

        self.task_list.clear()
        tasks_to_display = filtered_tasks if filtered_tasks is not None else self.task_manager.get_task_list()
        for task in tasks_to_display:
            self.task_list.addItem(task)

    def search_tasks(self):

        #to search and filter tasks based on user input

        keyword = self.search_input.text().strip()
        if keyword:
            filtered_tasks = self.task_manager.search_tasks(keyword)
            self.load_tasks_into_list(filtered_tasks)
        else:
            self.load_tasks_into_list()

    def add_task(self):

        #to add a new task with a deadline

        title = self.title_input.text().strip()
        description = self.description_input.toPlainText().strip()
        deadline = self.deadline_input.date().toString("yyyy-MM-dd")

        if title and description:
            self.task_manager.add_task(title, description, deadline)
            self.load_tasks_into_list()
            self.title_input.clear()
            self.description_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Both title and description are required.")

    def update_task(self):

        #to update the selected task

        selected_index = self.task_list.currentRow()
        if selected_index != -1:
            new_title = self.title_input.text().strip()
            new_description = self.description_input.toPlainText().strip()
            new_deadline = self.deadline_input.date().toString("yyyy-MM-dd")

            self.task_manager.update_task(selected_index, new_title, new_description, new_deadline)
            self.load_tasks_into_list()
        else:
            QMessageBox.warning(self, "Selection Error", "Select a task to update.")

    def delete_task(self):

        #to delete the selected task

        selected_index = self.task_list.currentRow()
        if selected_index != -1:
            self.task_manager.delete_task(selected_index)
            self.load_tasks_into_list()
        else:
            QMessageBox.warning(self, "Selection Error", "Select a task to delete.")

    def sort_by_deadline(self):

        #sort tasks by deadline

        self.task_manager.sort_tasks_by_deadline()
        self.load_tasks_into_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = TaskManagerGUI()
    gui.show()
    sys.exit(app.exec_())
