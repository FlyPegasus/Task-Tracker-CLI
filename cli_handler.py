'''import sys
print(sys.version)
for line in sys.stdin:
    if "exit" == line.rstrip():
        break
    print(f'Input : {line}')
print("Exit")'''


# without sys, pure python

print("Task Tracker Started...")
while True:
    line = input("task-cli> ")
    if "exit" == line.rstrip():
        break
    print(line)
print("Exit")
