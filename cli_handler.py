import os
cwd = os.getcwd()
# print("Current Directory path: ", cwd)

# create Json file if not exists
filepath = os.path.join(cwd, 'task_db.json')
# print(filepath)
# with open()

# without sys, pure python

print("Task Tracker Started...")
while True:
    line = input("task-cli> ")
    if "exit" == line.rstrip():
        break
    print(line)
print("Exited")
