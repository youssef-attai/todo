class ToDoTask:
    __reminder: float
    __task_id: float
    __title: str
    __done: bool

    def __init__(self, task_id: float, title: str, done: bool = False, reminder: float = None) -> None:
        self.__task_id = task_id
        self.__title = title
        self.__done = done
        self.__reminder = reminder

    def set_title(self, new_title: str) -> None:
        self.__title = new_title

    def get_title(self) -> str:
        return self.__title

    def toggle_done(self) -> None:
        self.__done = not self.__done

    def is_done(self) -> bool:
        return self.__done

    def get_task_id(self) -> float:
        return self.__task_id

    def has_reminder(self) -> bool:
        return self.__reminder is not None

    def get_reminder(self) -> float:
        return self.__reminder

    def set_reminder(self, reminder: float) -> None:
        self.__reminder = reminder
