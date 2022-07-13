from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLineEdit

from components.todo_app import ToDoApp
from gui.task_frame import TaskFrame


class Window(QWidget):
    def __init__(self, todo_app: ToDoApp) -> None:
        super().__init__()
        self.setMinimumWidth(400)
        self.todo_app = todo_app

        self.setLayout(QVBoxLayout(self))

        self.tasks_scroll_area = QScrollArea(self)
        self.tasks_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tasks_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tasks_scroll_area.setWidgetResizable(True)

        self.tasks_widget = QWidget(self)
        self.tasks_widget.setLayout(QVBoxLayout(self.tasks_widget))
        self.tasks_widget.layout().setAlignment(Qt.AlignTop)
        self.tasks_scroll_area.setWidget(self.tasks_widget)

        self.layout().addWidget(self.tasks_scroll_area)

        self.new_task_line_edit = QLineEdit(self)
        self.layout().addWidget(self.new_task_line_edit)

        self.new_task_line_edit.returnPressed.connect(lambda: (
            self.create_new_task(self.new_task_line_edit.text()),
            self.new_task_line_edit.setText("")
        ))

        self.new_task_line_edit.setFocus()

    def create_new_task(self, task_title: str) -> None:
        self.todo_app.create_new_task(task_title)
        self.update_tasklist()

    def delete_task(self, task_id: int) -> None:
        self.todo_app.delete_task(task_id)
        self.update_tasklist()

    def toggle_task(self, task_id: int) -> None:
        self.todo_app.toggle_task(task_id)
        self.update_tasklist()

    def rename_task(self, task_id: int, new_title: str) -> None:
        self.todo_app.rename_task(task_id, new_title)
        self.update_tasklist()

    def update_tasklist(self) -> None:
        for i in reversed(range(self.tasks_widget.layout().count())):
            self.tasks_widget.layout().itemAt(i).widget().setParent(None)
        for task in self.todo_app.get_tasks():
            self.tasks_widget.layout().addWidget(TaskFrame(task, self.tasks_widget, self))
