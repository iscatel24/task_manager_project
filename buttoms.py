def add_task(tasks, name, priority):
    title = name
    new_task = {"id": len(tasks) + 1,
                "title": title,
                "completed": False,
                }
    priority = priority
    if priority == "h":
        new_task["priority"] = "high"
    elif priority == "m":
        new_task["priority"] = "medium"
    elif priority == "l":
        new_task["priority"] = "low"
    return new_task


def show_all_tasks(tasks):
    if tasks:
        new_tasks = []
        for task in tasks:
            stat = ""
            if task["completed"]:
                stat += "X"
            elif task["completed"] == False:
                stat += " "
            new_task = (f"{task["id"]}. [{stat}] {task["title"].title()} ({task["priority"]})")
            new_tasks.insert(task["id"],new_task)
        return new_tasks
    else:
        return None


def find_task(tasks, id):
    if tasks:
        for task in tasks:
            id_status = 0
            if task["id"] != int(id):
                id_status = None
            elif task["id"] == id:
                cor_task = task
                return cor_task
        if id_status == None:
            return None
    else:
        return None


def update_task(tasks, id, new_title=None, priority=None):
    if tasks:
        id = id
        task = find_task(tasks, id)
        if task == None:
            return None
        new_title = new_title
        task["title"] = new_title
        priority = priority
        if priority == "h":
            task["priority"] = "high"
        elif priority == "m":
            task["priority"] = "medium"
        elif priority == "l":
            task["priority"] = "low"
        else:
            return None
        return task
    else:
        return None


def delete_task(tasks, id, choice=None):
    id = id
    cor_task = find_task(tasks, id)
    if cor_task in tasks:
        choice = choice
        if choice == "y":
            tasks.remove(cor_task)
            return tasks
        elif choice == "n":
            return None
        else:
            return None


def mark_task(tasks, id, action):
    id = id
    cor_task = find_task(tasks, id)
    if cor_task in tasks:
        # mark task as completed or not completed
        action = action
        if action == "c":
            cor_task["completed"] = True
            #status = "Task completed"
            return tasks
        elif action == "n":
            cor_task["completed"] = False
            #status = "Task is not completed"
            return tasks
        else:
            status = "Invalid input"
            return status

def save_tasks(tasks):
    with open("tasks", "w") as file:
        for task in tasks:
            file.write(f"{task["id"]}|{task["title"]}|{task["completed"]}|{task["priority"]}\n")


def load_tasks():
    tasks = []
    try:
        with open("tasks") as file:
            for line in file:
                line = line.strip()
                parts = line.split("|")
                task_id = int(parts[0])
                title = parts[1]
                completed = parts[2] == "True"
                piority = parts[3]
                task = {"id": task_id, "title": title, "completed": completed, "priority": piority, }
                tasks.append(task)
    except FileNotFoundError:
        with open("tasks", "w") as file:
            pass
    return tasks


def show_incomplete(tasks):
    if tasks:
        completed = False
        for task in tasks:
            if task["completed"]:
                completed = True
                stat = ""
                if task["completed"]:
                    stat += "X"
                print(f"{task["id"]}. [{stat}] {task["title"].title()} ({task["priority"]})")
        if completed == False:
            print("No completed tasks here")
    else:
        print("No tasks here.")


def tasks_counter(tasks):
    if tasks:
        completed = 0
        incompleted = 0
        for task in tasks:
            if task["completed"] == True:
                completed += 1
            elif task["completed"] == False:
                completed += 1
        counting = {"completed": completed,"incompleted": incompleted,"total": len(tasks)}
        return counting
    else:
        completed = 0
        incompleted = 0
        counting = {"completed": completed, "incompleted": incompleted, "total": len(tasks)}
        return counting
