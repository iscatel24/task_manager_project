

def add_task(tasks):
    while True:
        title = input("Enter task title:")
        if title == "":
            print("Invalid input try again")
            continue

        else:
            max_id = 0
            for task in tasks:
                if task["id"] > max_id:
                    max_id = task["id"]
            new_task = {"id": max_id+1,
                        "title": title,
                        "completed": False,
                        }
            break
    while True:
        priority = input("Choice priority (high/medium/low) h/m/l: ")
        if priority == "h":
            new_task["priority"] = "high"
            break
        elif priority == "m":
            new_task["priority"] = "medium"
            break
        elif priority == "l":
            new_task["priority"] = "low"
            break
        else:
            print("Invalid choice try again")
            continue
    tasks.append(new_task)
    print(f"Task successfully added")


def show_all_tasks(tasks):
    if tasks:
        for task in tasks:
                stat = ""
                if task["completed"]:
                    stat += "X"
                elif task["completed"] == False:
                    stat += " "
                print(f"{task["id"]}. [{stat}] {task["title"].title()} ({task["priority"]})")
    else:
        print("No tasks here.")



def find_task(tasks,id):
    for task in tasks:
        id_status = 0
        if task["id"] != id:
            id_status = None
        elif task["id"] == id:
            cor_task = task
            return cor_task
    if id_status == None:
        print("Task not founded")
        return None


def update_task(tasks,id=None):
    show_all_tasks(tasks)
    id = int(input("Write task id: "))
    cor_task = find_task(tasks,id)
    if cor_task in tasks:
        choice = input("What do you want update (priority/name) p/n:")
        if choice == "n":
            new_title = input("Write new title: ")
            cor_task["title"] = new_title
            print(f"Task successfully updated")
        elif choice == "p":
            while True:
                priority = input("Choice priority (high/medium/low) h/m/l: ")
                if priority == "h":
                    cor_task["priority"] = "high"
                    print(f"Task successfully updated")
                    break
                elif priority == "m":
                    cor_task["priority"] = "medium"
                    print(f"Task successfully updated")
                    break
                elif priority == "l":
                    cor_task["priority"] = "low"
                    print(f"Task successfully updated")
                    break
                elif priority != "l" or  "m" or "h":
                    print("Invalid choice try again")
                    continue
        else:
            print("invalid input")


def delete_task(tasks):
    show_all_tasks(tasks)
    id = int(input("Write task id: "))
    cor_task = find_task(tasks, id)
    if cor_task in tasks:
        choice = input("Are you sure (y/n): ")
        if choice == "y":
            tasks.remove(cor_task)
            print("Task successfully removed")
        elif choice == "n":
            return
        else:
            print("Invalid input")

def mark_task(tasks):
    show_all_tasks(tasks)
    id = int(input("Write task id: "))
    cor_task = find_task(tasks, id)
    if cor_task in tasks:
        action = input("What do you want to do mark as completed or not (c/n): ")
        if action == "c":
            cor_task["completed"] = True
            print("Task completed!")
        elif action == "n":
            cor_task["completed"] = False
            print("Task is not completed")
        else:
            print("Invalid input")


def save_tasks(tasks):
    with open("tasks","w") as file:
        for task in tasks:
            file.write(f"{task["id"]}|{task["title"]}|{task["completed"]}|{task["priority"]}\n")


def load_tasks():
    tasks = []
    with open("tasks") as file:
        for line in file:
            line = line.strip()
            parts = line.split("|")
            task_id = int(parts[0])
            title = parts[1]
            completed = parts[2] == "True"
            piority = parts[3]
            task = {"id": task_id, "title": title, "completed": completed,"priority": piority, }
            tasks.append(task)
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
                incompleted += 1
        print(f"Total: {len(tasks)}\n"
              f"Completed: {completed}\n"
              f"Incompleted: {incompleted}")
    else:
        print("Tasks not founded")




# def load_tasks(tasks=None):
#     with open("tasks") as file:
#         tks = []
#         id = []
#         ts = ""
#         count_1 = 0
#         for task in file:
#             for p in task:
#                 if p != "|":
#                   ts += p
#                 elif p == "|":
#                     id.append(ts)
#                     ts = ""
#                     continue
#             count_1 += 1
#         for task in range(len(file)):
#             pr = {}
#             id_2 = id.pop(0)
#             pr["id"] = int(id_2[0])
#             id_2 = id.pop(0)
#             pr["title"] = id_2
#             id_2 = id.pop(0)
#             if id_2 == "True":
#                 pr["completed"] = True
#             elif id_2 == "False":
#                 pr["completed"] = False
#             tks.append(pr)
#         print(tks)



