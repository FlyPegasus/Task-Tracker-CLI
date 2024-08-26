def add_tasks(task, filepath):
    with open(filepath, 'w') as f:
        f.write(task)
