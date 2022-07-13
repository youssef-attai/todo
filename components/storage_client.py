import json
import os.path
import platform

from components.json_task_converter import JSONTaskConverter
from components.todo_task import ToDoTask


class StorageClient:
    @classmethod
    def get_platform_specific_data_location(cls) -> str:
        match platform.system():
            case "Linux":
                return os.path.expanduser("~/.local/share")
            case "Windows":
                return os.getenv("LOCALAPPDATA")
            case "Darwin":
                return os.path.expanduser("~/Library/Application Support")

    @classmethod
    def get_storage_location(cls) -> str:
        return os.path.join(cls.get_platform_specific_data_location(), "todo")

    @classmethod
    def get_storage_file_location(cls) -> str:
        return os.path.join(cls.get_storage_location(), "tasks.json")

    @classmethod
    def load_tasks(cls):
        cls.assert_storage_location()
        with open(cls.get_storage_file_location()) as tasks_json:
            return list(map(JSONTaskConverter.json_to_task, json.load(tasks_json).values()))

    @classmethod
    def save_tasks(cls, tasks: list[ToDoTask]) -> None:
        cls.assert_storage_location()
        with open(cls.get_storage_file_location(), 'w') as tasks_json:
            json.dump({task.get_task_id(): JSONTaskConverter.task_to_json(task) for task in tasks}, tasks_json)

    @classmethod
    def assert_storage_location(cls):
        if not os.path.exists(cls.get_storage_file_location()):
            if not os.path.exists(cls.get_storage_location()):
                os.mkdir(cls.get_storage_location())
            with open(cls.get_storage_file_location(), 'w') as tasks_json:
                json.dump(dict(), tasks_json)
