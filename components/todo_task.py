class ToDoTask:
    __task_id: int
    __title: str
    __done: bool

    def __init__(self, task_id: int, title: str) -> None:
        self.__task_id = task_id
        self.__title = title
        self.__done = False

    def set_title(self, new_title: str) -> None:
        self.__title = new_title

    def get_title(self) -> str:
        return self.__title

    def toggle_done(self):
        self.__done = not self.__done

    def is_done(self):
        return self.__done

    def get_task_id(self):
        return self.__task_id
