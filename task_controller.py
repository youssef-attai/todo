import datetime

from PySide6.QtCore import QTimer

from task_model import TaskModel
from views.task_view import TaskView


class TaskController:
    def __init__(self, model: TaskModel, view: TaskView):
        self.model = model
        self.view = view
        self.timers = []

        # Set the current view to the task list view
        self.view.layout().setCurrentIndex(0)

        self.view.task_list_view.new_task_button.clicked.connect(
            self.new_task_button_clicked_handler)

        self.view.edit_task_view.add_due_button.clicked.connect(
            self.view.edit_task_view.add_due_button_clicked_handler)

        self.view.edit_task_view.remove_due_button.clicked.connect(
            self.view.edit_task_view.remove_due_button_clicked_handler)

        self.view.edit_task_view.new_reminder_button.clicked.connect(
            self.view.edit_task_view.new_reminder_button_clicked_handler)

        self.load_tasks()
        self.load_reminders()

    def fire_reminder(self, reminder):
        task = self.model.get_task(reminder.tid)
        # TODO Add:
        #  Reminder notification instead of print statement
        print(task.title, task.due)
        self.model.remove_reminder(reminder)

    def load_reminders(self):
        reminders = self.model.get_all_reminders()
        for reminder in reminders:
            self.new_timer(reminder)

    def load_tasks(self):
        tasks = self.model.get_all_tasks()
        for task in tasks:
            self.create_task_widget(task)

    def new_task_button_clicked_handler(self):
        # Set the current view to the edit task view
        self.view.layout().setCurrentIndex(1)

        self.view.edit_task_view.reset_view()

        # Connect the OK button with the method that adds the new task using user input in edit task view
        self.view.edit_task_view.ok_button.clicked.connect(self.new_task)

        # Connect the Cancel button with the method that sets the current page to the task list page
        self.view.edit_task_view.cancel_button.clicked.connect(lambda: self.view.layout().setCurrentIndex(0))

    def new_task(self):
        # Disconnect the new task method from the OK button to avoid duplicate calls
        self.view.edit_task_view.ok_button.clicked.disconnect()

        # Get user input from the edit task view
        title = self.view.edit_task_view.title_lineedit.text()
        if not title:
            self.view.display_error("Task title cannot be empty")
            self.view.edit_task_view.ok_button.clicked.connect(self.new_task)
            return

        due = None
        if not self.view.edit_task_view.add_due_button.isVisible():
            due = self.view.edit_task_view.due_datetimeedit.dateTime().toPython().replace(second=0, microsecond=0)

        reminders = set()  # Can't have more than one reminder for the same minute
        for child in self.view.edit_task_view.reminders_widget.findChildren(self.view.edit_task_view.ReminderWidget):
            reminders.add(child.due_datetimeedit.dateTime().toPython().replace(second=0, microsecond=0))

        # Create the task
        task = self.model.new_task(title, due, reminders)
        for reminder in map(lambda r: self.model.Reminder((task.tid, r.strftime("%Y-%m-%d %H:%M:%S"))), reminders):
            self.new_timer(reminder)

        # Create the task widget and add it to the task list
        self.create_task_widget(task)

        # Set the current view to the task list view
        self.view.layout().setCurrentIndex(0)

    def create_task_widget(self, task):
        task_widget = self.view.task_list_view.TaskWidget(self.view.task_list_view.tasks_widget)
        task_widget.title_label.setText(task.title)
        if task.due is not None:
            task_widget.due_datetimeedit.setDateTime(datetime.datetime.fromisoformat(task.due))
        else:
            task_widget.due_datetimeedit.hide()
        task_widget.done_checkbox.setChecked(task.done)
        task_widget.done_checkbox.stateChanged.connect(lambda state: self.model.toggle_task_done(task.tid))
        task_widget.remove_button.clicked.connect(lambda state: self.remove_task(task_widget, task.tid))
        self.view.task_list_view.tasks_widget.layout().addWidget(task_widget)

    def remove_task(self, task_widget, task_id):
        task_widget.setParent(None)
        self.model.remove_task(task_id)

    def new_timer(self, reminder):
        self.timers.append(QTimer())
        self.timers[-1].setSingleShot(True)
        self.timers[-1].timeout.connect(lambda r=reminder: self.fire_reminder(r))
        timer_time = ((lambda r=reminder: datetime.datetime.fromisoformat(
            r.due))() - datetime.datetime.now()).total_seconds() * 1000
        self.timers[-1].start(timer_time if timer_time > 0 else 0)
        # print(f"TIMER FOR {reminder.tid} AT {reminder.due}")
