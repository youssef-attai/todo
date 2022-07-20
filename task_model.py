import os.path
import platform
import sqlite3


class TaskModel:
    @staticmethod
    def db_path():
        return os.path.join(TaskModel.get_appdata_dir(), 'todo.db')

    @staticmethod
    def get_appdata_dir():
        p = None
        match platform.system():
            case "Linux":
                p = os.path.expanduser("~/.local/share")
            case "Windows":
                p = os.getenv("LOCALAPPDATA")
            case "Darwin":
                p = os.path.expanduser("~/Library/Application Support")
        return os.path.join(p, "todo")

    def __init__(self):
        self.connection = sqlite3.connect(self.db_path())
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks
(
    TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title  TEXT NOT NULL,
    Due    TEXT,
    Done   INTEGER CHECK ( Done == 0 or Done == 1 )
);''')
        self.connection.commit()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Reminders
(
    TaskID INTEGER NOT NULL,
    Due    TEXT    NOT NULL,
    FOREIGN KEY (TaskID) REFERENCES Tasks (TaskID),
    PRIMARY KEY (TaskID, Due)
);''')
        self.connection.commit()

    def new_task(self, title, due, reminders_dues):
        new_task_id = self.cursor.execute('''INSERT INTO Tasks (Title, Due, Done)
VALUES (:title, :due, 0)
RETURNING TaskID;''', {
            'title': title,
            'due': due
        }).fetchone()[0]
        self.connection.commit()

        for reminder_due in reminders_dues:
            self.cursor.execute('''INSERT INTO Reminders (TaskID, Due)
VALUES (:tid, :due);''', {
                'tid': new_task_id,
                'due': reminder_due
            })
            self.connection.commit()

    def remove_task(self, tid):
        self.cursor.execute('''DELETE
FROM Tasks
WHERE TaskID == :tid;''', {
            'tid': tid
        })
        self.connection.commit()

        self.cursor.execute('''DELETE
FROM Reminders
WHERE TaskID == :tid;''', {
            'tid': tid
        })
        self.connection.commit()

    def edit_task(self, tid, title, due, reminders_dues):
        self.cursor.execute('''UPDATE Tasks
SET Title=:title,
    Due=:due
WHERE TaskID == :tid;''', {
            'tid': tid,
            'title': title,
            'due': due
        })
        self.connection.commit()

        self.cursor.execute('''DELETE
FROM Reminders
WHERE TaskID == :tid;''', {
            'tid': tid
        })
        self.connection.commit()

        for reminder_due in reminders_dues:
            self.cursor.execute('''INSERT INTO Reminders (TaskID, Due)
        VALUES (:tid, :due);''', {
                'tid': tid,
                'due': reminder_due
            })
            self.connection.commit()
