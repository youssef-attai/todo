from components.todo_task import ToDoTask


class JSONTaskConverter:
    @classmethod
    def task_to_json(cls, task: ToDoTask) -> dict:
        return {
            'tid': task.get_task_id(),
            'title': task.get_title(),
            'done': task.is_done(),
            'reminder': task.get_reminder() if task.has_reminder() else None,
        }

    @classmethod
    def json_to_task(cls, task_dict: dict) -> ToDoTask:
        return ToDoTask(task_dict["tid"], task_dict["title"], task_dict["done"], task_dict.get("reminder"))
