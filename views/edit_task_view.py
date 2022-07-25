import datetime

from PySide6.QtGui import QPainter, Qt
from PySide6.QtWidgets import (QWidget, QStyleOption, QStyle, QVBoxLayout, QLineEdit, QDateTimeEdit, QScrollArea,
                               QPushButton, QHBoxLayout, QFrame)


class EditTaskView(QWidget):
    class ReminderWidget(QWidget):
        def __init__(self, due=None, parent=None):
            super().__init__(parent)

            self.setLayout(QHBoxLayout(self))

            self.due_datetimeedit = QDateTimeEdit(self)
            if due is not None:
                self.due_datetimeedit.setDateTime(due)
            self.due_datetimeedit.setDisplayFormat("MMMM d yyyy, h:mm ap")
            self.remove_button = QPushButton("Remove", self)
            self.remove_button.clicked.connect(lambda: self.setParent(None))

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
        self.due_datetimeedit.setDisplayFormat("MMMM d yyyy, h:mm ap")
        self.add_due_button = QPushButton('Add due', self)
        self.remove_due_button = QPushButton('Remove due', self)

        self.reminders_widget = QWidget(self)
        self.reminders_scrollarea = QScrollArea(self)
        self.new_reminder_button = QPushButton("New reminder", self)

        self.reminders_widget.setLayout(QVBoxLayout(self.reminders_widget))
        self.reminders_widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)

        self.reminders_scrollarea.setWidget(self.reminders_widget)
        self.reminders_scrollarea.setWidgetResizable(True)
        self.reminders_scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.reminders_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.buttonbox_frame = QFrame(self)
        self.cancel_button = QPushButton('Cancel', self)
        self.ok_button = QPushButton('Ok', self)

        self.buttonbox_frame.setLayout(QHBoxLayout(self.buttonbox_frame))
        self.buttonbox_frame.layout().addWidget(self.cancel_button)
        self.buttonbox_frame.layout().addWidget(self.ok_button)

        self.layout().addWidget(self.title_lineedit)
        self.layout().addWidget(self.add_due_button)
        self.layout().addWidget(self.due_datetimeedit)
        self.layout().addWidget(self.remove_due_button)
        self.layout().addWidget(self.reminders_scrollarea)
        self.layout().addWidget(self.new_reminder_button)
        self.layout().addWidget(self.buttonbox_frame)

        self.remove_due_button_clicked_handler()

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)

    def add_due_button_clicked_handler(self):
        self.add_due_button.hide()
        self.due_datetimeedit.show()
        self.remove_due_button.show()

    def remove_due_button_clicked_handler(self):
        self.add_due_button.show()
        self.due_datetimeedit.hide()
        self.remove_due_button.hide()

    def new_reminder_button_clicked_handler(self):
        self.reminders_widget.layout().addWidget(
            self.ReminderWidget(self.due_datetimeedit.dateTime().toPython(), self.reminders_widget))

    def reset_view(self):
        self.title_lineedit.setText('')
        self.due_datetimeedit.setDateTime(datetime.datetime.now())
        self.remove_due_button_clicked_handler()
        for i in reversed(range(self.reminders_widget.layout().count())):
            self.reminders_widget.layout().itemAt(i).widget().setParent(None)
