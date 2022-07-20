from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QStackedLayout, QStyleOption, QStyle

from views.edit_task_view import EditTaskView
from views.task_list_view import TaskListView


class TaskView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayout(QStackedLayout(self))

        self.task_list_view = TaskListView(self)
        self.edit_task_view = EditTaskView(self)

        self.layout().addWidget(self.task_list_view)
        self.layout().addWidget(self.edit_task_view)

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)
