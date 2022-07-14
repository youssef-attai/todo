import datetime

from components.storage_client import StorageClient
from components.todo_task import ToDoTask


class ToDoApp:
    __tasks: list[ToDoTask]

    def __init__(self) -> None:
        self.__tasks = list()

        self.load_existing(StorageClient.load_tasks())

    def load_existing(self, tasks: list[ToDoTask]) -> None:
        self.__tasks = tasks

    def create_new_task(self, task_name: str) -> None:
        tid = datetime.datetime.now().timestamp()
        self.__tasks.append(ToDoTask(tid, task_name))
        StorageClient.save_tasks(self.__tasks)

    def toggle_task(self, task_id: float) -> None:
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                task.toggle_done()
                break
        StorageClient.save_tasks(self.__tasks)

    def rename_task(self, task_id: float, new_name: str) -> None:
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                task.set_title(new_name)
                break
        StorageClient.save_tasks(self.__tasks)

    def delete_task(self, task_id: float) -> None:
        self.__tasks = list(filter(lambda t: t.get_task_id() != task_id, self.__tasks))
        StorageClient.save_tasks(self.__tasks)

    def get_tasks(self) -> list[ToDoTask]:
        return self.__tasks

    def set_task_reminder(self, task_id: float, reminder: float):
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                task.set_reminder(reminder)
                break
        StorageClient.save_tasks(self.__tasks)
