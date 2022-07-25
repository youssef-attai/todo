from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QScrollArea, QPushButton, QStyleOption, QStyle, QFrame, QLabel,
                               QCheckBox, QHBoxLayout, QDateTimeEdit)


class TaskListView(QWidget):
    class TaskWidget(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

            self.setLayout(QVBoxLayout(self))

            self.header_frame = QFrame(self)
            self.footer_frame = QFrame(self)

            self.header_frame.setLayout(QHBoxLayout(self.header_frame))
            self.footer_frame.setLayout(QHBoxLayout(self.footer_frame))

            self.title_label = QLabel(self.header_frame)
            self.done_checkbox = QCheckBox(self.header_frame)
            self.remove_button = QPushButton("Remove", self.header_frame)

            self.header_frame.layout().addWidget(self.title_label)
            self.header_frame.layout().addWidget(self.done_checkbox)
            self.header_frame.layout().addWidget(self.remove_button)

            self.due_datetimeedit = QDateTimeEdit(self.footer_frame)
            self.due_datetimeedit.setDisplayFormat("MMMM d yyyy, h:mm ap")
            self.due_datetimeedit.setReadOnly(True)

            self.footer_frame.layout().addWidget(self.due_datetimeedit)

            self.layout().addWidget(self.header_frame)
            self.layout().addWidget(self.footer_frame)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(400, 400)
        self.setLayout(QVBoxLayout(self))

        self.tasks_widget = QWidget(self)
        self.tasks_scrollarea = QScrollArea(self)
        self.new_task_button = QPushButton("New task", self)

        self.tasks_widget.setLayout(QVBoxLayout(self.tasks_widget))
        self.tasks_widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)

        self.tasks_scrollarea.setWidget(self.tasks_widget)
        self.tasks_scrollarea.setWidgetResizable(True)
        self.tasks_scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tasks_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.layout().addWidget(self.tasks_scrollarea)
        self.layout().addWidget(self.new_task_button)

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)
