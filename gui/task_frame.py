from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QCheckBox, QPushButton

from components.todo_task import ToDoTask
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
        self.done_checkbox.setChecked(self.task.is_done())

        self.rename_button = QPushButton("rename", self)
        self.delete_button = QPushButton("delete", self)

        self.layout().addWidget(self.task_title)
        self.layout().addWidget(self.buttons_frame)

        self.buttons_frame.layout().addWidget(self.done_checkbox)
        self.buttons_frame.layout().addWidget(self.rename_button)
        self.buttons_frame.layout().addWidget(self.delete_button)

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
        dialog = RenameDialog(self)
        if dialog.exec():
            self.window.rename_task(self.task.get_task_id(), dialog.rename_line_edit.text())
