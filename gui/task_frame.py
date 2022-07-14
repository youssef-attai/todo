import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QCheckBox, QPushButton

from components.todo_task import ToDoTask
from gui.reminder_dialog import ReminderDialog
from gui.rename_dialog import RenameDialog


class TaskFrame(QFrame):
    def __init__(self, task: ToDoTask, parent, window) -> None:
        super().__init__(parent)
        self.window = window
        self.task = task
        self.setLayout(QHBoxLayout(self))

        self.task_title = QLabel(self)
        self.task_title.setText(self.task.get_title())

        self.buttons_frame = QFrame(self)
        self.buttons_frame.setLayout(QHBoxLayout(self.buttons_frame))
        self.buttons_frame.layout().setAlignment(Qt.AlignRight)

        self.done_checkbox = QCheckBox(self)
        self.done_checkbox.setFixedWidth(25)
        self.done_checkbox.setChecked(self.task.is_done())

        self.reminder_text = QLabel(self.buttons_frame)
        self.reminder_text.setFont(QFont("", 8))
        self.reminder_text.hide()
        if self.task.has_reminder():
            self.reminder_text.setText(
                "Reminder set at " +
                datetime.datetime.fromtimestamp(self.task.get_reminder()).strftime("%m/%d/%Y %-I:%M %p")
            )
            self.reminder_text.show()
        self.toggle_reminder = QPushButton("reminder", self.buttons_frame)
        self.rename_button = QPushButton("rename", self.buttons_frame)
        self.delete_button = QPushButton("delete", self.buttons_frame)

        self.layout().addWidget(self.done_checkbox)
        self.layout().addWidget(self.task_title)
        self.layout().addWidget(self.buttons_frame)

        self.buttons_frame.layout().addWidget(self.reminder_text)
        self.buttons_frame.layout().addWidget(self.toggle_reminder)
        self.buttons_frame.layout().addWidget(self.rename_button)
        self.buttons_frame.layout().addWidget(self.delete_button)

        self.toggle_reminder.pressed.connect(
            self.reminder_dialog
        )

        self.delete_button.pressed.connect(
            lambda: self.window.delete_task(self.task.get_task_id())
        )

        self.done_checkbox.toggled.connect(
            lambda: self.window.toggle_task(self.task.get_task_id())
        )

        self.rename_button.pressed.connect(
            self.rename_dialog
        )

    def rename_dialog(self):
        dialog = RenameDialog(self.task.get_title(), self)
        if dialog.exec():
            self.window.rename_task(self.task.get_task_id(), dialog.rename_line_edit.text())

    def reminder_dialog(self):
        dialog = ReminderDialog(self.task.get_reminder(), self)
        res = dialog.exec()
        if res == 1:
            self.window.set_task_reminder(
                self.task.get_task_id(),
                dialog.reminder_datetime.dateTime().toPyDateTime().timestamp()
            )
            pass
        elif res == 2:
            self.window.set_task_reminder(self.task.get_task_id(), None)
            pass
