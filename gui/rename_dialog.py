import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QWidget, QDialogButtonBox, QVBoxLayout, QLineEdit


class RenameDialog(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.setLayout(QVBoxLayout(self))
        self.rename_line_edit = QLineEdit(self)
        self.layout().addWidget(self.rename_line_edit)
        self.layout().addWidget(self.buttonBox)
