import datetime

from task_model import TaskModel
from views.task_view import TaskView


class TaskController:
    def __init__(self, model: TaskModel, view: TaskView):
        self.model = model
        self.view = view

        # Set the current view to the task list view
        self.view.layout().setCurrentIndex(0)

        self.view.task_list_view.new_task_button.clicked.connect(self.new_task_button_clicked_handler)

        self.load_all_tasks()

    def load_all_tasks(self):
        tasks = self.model.get_all_tasks()
        for task in tasks:
            self.create_task_widget(task)

    def new_task_button_clicked_handler(self):
        # Set the current view to the edit task view
        self.view.layout().setCurrentIndex(1)

        self.view.edit_task_view.title_lineedit.setText('')
        self.view.edit_task_view.due_datetimeedit.setDateTime(datetime.datetime.now())

        # Connect the OK button with the method that adds the new task using user input in edit task view
        self.view.edit_task_view.ok_button.clicked.connect(self.new_task)

        # Connect the Cancel button with the method that sets the current page to the task list page
        self.view.edit_task_view.cancel_button.clicked.connect(lambda: self.view.layout().setCurrentIndex(0))

    def new_task(self):
        # Disconnect the new task method from the OK button to avoid duplicate calls
        self.view.edit_task_view.ok_button.clicked.disconnect()

        # Get user input from the edit task view
        title = self.view.edit_task_view.title_lineedit.text()
        due = self.view.edit_task_view.due_datetimeedit.dateTime().toPython()
        reminders = []
        for child in self.view.edit_task_view.reminders_widget.layout().children():
            if isinstance(child, self.view.edit_task_view.ReminderWidget):
                reminders.append(child.due_datetimeedit.dateTime().toPython())

        # Create the task
        task = self.model.new_task(title, due, reminders)

        # Create the task widget and add it to the task list
        self.create_task_widget(task)

        # Set the current view to the task list view
        self.view.layout().setCurrentIndex(0)

    def create_task_widget(self, task):
        task_widget = self.view.task_list_view.TaskWidget(self.view.task_list_view)
        task_widget.title_label.setText(task.title)
        task_widget.due_label.setText(task.due)
        task_widget.done_checkbox.setChecked(task.done)
        task_widget.done_checkbox.stateChanged.connect(lambda state: self.model.toggle_task_done(task.tid))
        # task_widget.done_checkbox.stateChanged.connect(lambda x: print(x))
        self.view.task_list_view.tasks_widget.layout().addWidget(task_widget)
