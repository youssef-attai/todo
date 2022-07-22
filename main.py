from PySide6.QtWidgets import QApplication

from task_controller import TaskController
from task_model import TaskModel
from views.task_view import TaskView


def main():
    app = QApplication([])

    task_model = TaskModel()
    task_view = TaskView()
    task_controller = TaskController(task_model, task_view)
    task_view.show()

    app.exec()


if __name__ == '__main__':
    main()
