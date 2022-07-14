from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QDateTimeEdit, QPushButton


class ReminderDialog(QDialog):
    def __init__(self, reminder, parent) -> None:
        super().__init__(parent)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.setLayout(QVBoxLayout(self))
        self.reminder_datetime = QDateTimeEdit(self)
        if reminder is not None:
            self.reminder_datetime.setDateTime(QDateTime.fromMSecsSinceEpoch(int(round(reminder * 1000))))
        else:
            self.reminder_datetime.setDateTime(QDateTime.currentDateTime().addSecs(60))
        self.remove_reminder = QPushButton("remove", self)
        self.remove_reminder.pressed.connect(
            lambda: self.done(2)
        )
        self.layout().addWidget(self.reminder_datetime)
        self.layout().addWidget(self.remove_reminder)
        self.layout().addWidget(self.buttonBox)
