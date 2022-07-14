from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLineEdit


class RenameDialog(QDialog):
    def __init__(self, title, parent) -> None:
        super().__init__(parent)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.setLayout(QVBoxLayout(self))
        self.rename_line_edit = QLineEdit(self)
        self.rename_line_edit.setText(title)
        self.layout().addWidget(self.rename_line_edit)
        self.layout().addWidget(self.buttonBox)
