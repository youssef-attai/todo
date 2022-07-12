import sys

from PyQt5.QtWidgets import QApplication

from components.todo_app import ToDoApp
from gui.window import Window


def main():
    q_app = QApplication(sys.argv)
    todo_app = ToDoApp()
    window = Window(todo_app)
    window.show()
    q_app.exec()


if __name__ == '__main__':
    main()
