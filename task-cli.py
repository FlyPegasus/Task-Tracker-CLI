# take input as positional arguments from terminal
import commands as cmd
import utils.unique_identifier as uid
import sys
from datetime import date
import json
import os
cwd = os.getcwd()

# create Json file if not exists
filepath = os.path.join(cwd, 'task_db.json')

# Accessing arguments
operation = sys.argv[1]

allTasks = dict()

# performing operation
if operation == "add":
    desc = sys.argv[2]
    id = uid.unique_key(allTasks)
    status = "todo"
    created = modified = date.today()
    task = dict()
    task["id"] = id
    task["description"] = desc
    task["status"] = status
    task["createdAt"] = str(created)
    task["modifiedAt"] = str(modified)
    allTasks[id] = task
    # Serializing Json
    json_obj = json.dumps(allTasks, indent=5)
    cmd.add_tasks(json_obj, filepath)
elif operation == "update":
    pass
elif operation == "delete":
    pass
elif operation == "list":
    pass
elif operation == "help":
    if len(sys.argv) < 3:
        print("commands: add, delete, update, list")
    else:
        command = sys.argv[2]
        # all command descriptions/help
        if command == "add":
            pass
        elif command == "update":
            pass
        elif command == "delete":
            pass
        elif command == "list":
            pass
else:
    print("Enter Valid command")
