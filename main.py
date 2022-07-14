import sys

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction

from components.todo_app import ToDoApp
from gui.window import Window


def main():
    q_app = QApplication(sys.argv)
    q_app.setApplicationName("ToDo")
    todo_app = ToDoApp()
    q_app.setWindowIcon(todo_app.icon)
    window = Window(todo_app)
    tray = QSystemTrayIcon(todo_app.icon, q_app)
    if tray.isSystemTrayAvailable():
        q_app.setQuitOnLastWindowClosed(False)
        tray.setToolTip(q_app.applicationName())
        menu = QMenu()
        show_action = QAction("Show tasks")
        exit_action = QAction("Exit")
        show_action.triggered.connect(window.show)
        exit_action.triggered.connect(sys.exit)
        menu.addAction(show_action)
        menu.addAction(exit_action)
        tray.setContextMenu(menu)
        tray.show()
    window.show()
    q_app.exec()


if __name__ == '__main__':
    main()
