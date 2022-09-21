# To-do app

Basic to-do app for desktop. Tested on both Windows and Linux. *Not* tested on MacOS, but should work fine.

## How to run on your machine

### Requirements
- Python 3.x

### Steps
Open a terminal window, and run the following commands:
1. `git clone https://github.com/youssef-attai/todo.git`
2. `cd todo`
3. Make sure you have `virtualenv` installed, then run `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `python main.py`

## Notes
- When you run the app, it will check for an existing sqlite database, to load previously added to-dos. If no such database is found, it is created in your **persistent application data** directory:
  - On Windows: `C:\Users\<USER>\AppData\Local\todo`
  - On Linux:   `~/.local/share/todo`
  - on MacOS:   `~/Library/Application Support/todo`
