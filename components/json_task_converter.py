import json

from components.todo_task import ToDoTask


class JSONTaskConverter:
    @classmethod
    def task_to_json(cls, task: ToDoTask) -> dict:
        return {
            'tid': task.get_task_id(),
            'title': task.get_title(),
            'done': task.is_done()
        }

    @classmethod
    def json_to_task(cls, task_dict: dict) -> ToDoTask:
        return ToDoTask(task_dict["tid"], task_dict["title"], task_dict["done"])
