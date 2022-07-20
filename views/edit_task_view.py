from PySide6.QtGui import QPainter, Qt
from PySide6.QtWidgets import (QWidget, QStyleOption, QStyle, QVBoxLayout, QLineEdit, QDateTimeEdit, QScrollArea,
                               QPushButton, QHBoxLayout)


class EditTaskView(QWidget):
    class ReminderWidget(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

            self.setLayout(QHBoxLayout(self))

            self.due_datetimeedit = QDateTimeEdit(self)
            self.remove_button = QPushButton(self)

            self.layout().addWidget(self.due_datetimeedit)
            self.layout().addWidget(self.remove_button)

        def paintEvent(self, event):
            opt = QStyleOption()
            opt.initFrom(self)
            p = QPainter(self)
            self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayout(QVBoxLayout(self))

        self.title_lineedit = QLineEdit(self)
        self.due_datetimeedit = QDateTimeEdit(self)

        self.reminders_widget = QWidget(self)
        self.reminders_scrollarea = QScrollArea(self)
        self.new_reminder_button = QPushButton("New reminder", self)

        self.reminders_widget.setLayout(QVBoxLayout(self.reminders_widget))
        self.reminders_widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)

        self.reminders_scrollarea.setWidget(self.reminders_widget)
        self.reminders_scrollarea.setWidgetResizable(True)
        self.reminders_scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.reminders_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.layout().addWidget(self.title_lineedit)
        self.layout().addWidget(self.due_datetimeedit)
        self.layout().addWidget(self.reminders_scrollarea)
        self.layout().addWidget(self.new_reminder_button)

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)
