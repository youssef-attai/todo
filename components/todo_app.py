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
        print(f"NEW TASK {tid} {task_name}")
        StorageClient.save_tasks(self.__tasks)

    def toggle_task(self, task_id: float) -> None:
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                task.toggle_done()
                print(f"SET TASK {task_id} {task.get_title()} {task.is_done()}")
                break
        StorageClient.save_tasks(self.__tasks)

    def rename_task(self, task_id: float, new_name: str) -> None:
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                print(f"RENAME TASK {task_id} FROM {task.get_title()} TO {new_name}")
                task.set_title(new_name)
                break
        StorageClient.save_tasks(self.__tasks)

    def delete_task(self, task_id: float) -> None:
        self.__tasks = list(filter(lambda t: t.get_task_id() != task_id, self.__tasks))
        print(f"DELETE TASK {task_id}")
        StorageClient.save_tasks(self.__tasks)

    def get_tasks(self) -> list[ToDoTask]:
        return self.__tasks
