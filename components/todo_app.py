from components.todo_task import ToDoTask


class ToDoApp:
    __latest_task_id: int
    __tasks: list[ToDoTask]

    def __init__(self):
        self.__latest_task_id = 0
        self.__tasks = list()

    def create_new_task(self, task_name: str) -> None:
        self.__latest_task_id += 1
        self.__tasks.append(ToDoTask(self.__latest_task_id, task_name))
        print(f"NEW TASK {self.__latest_task_id} {task_name}")

    def toggle_task(self, task_id: int) -> None:
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                task.toggle_done()
                print(f"SET TASK {task_id} {task.get_title()} {task.is_done()}")
                break

    def rename_task(self, task_id: int, new_name: str) -> None:
        for task in self.__tasks:
            if task.get_task_id() == task_id:
                task.set_title(new_name)
                print(f"RENAME TASK {task_id} FROM {task.get_title()} TO {new_name}")
                break

    def delete_task(self, task_id: int) -> None:
        self.__tasks = list(filter(lambda t: t.get_task_id() != task_id, self.__tasks))
        print(f"DELETE TASK {task_id}")

    def get_tasks(self):
        return self.__tasks
