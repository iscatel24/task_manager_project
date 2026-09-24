from buttoms import show_all_tasks as show_tasks
from buttoms import (update_task,delete_task,add_task,mark_task,save_tasks,load_tasks
,show_incomplete,tasks_counter)

if __name__ == "__main__":
    def main_menu(choice=None):
        tasks = load_tasks()
        while True:
            promt = (f"\n=== DAILY TASK MANAGER ===\n\n"
                     f"1. Show all tasks\n"
                     f"2. Add task\n"
                     f"3. Update task\n"
                     f"4. Delete task\n"
                     f"5. Mark task\n"
                     f"6. Count tasks\n"
                     f"7. Incompleted tasks\n"
                     f"8. Exite\n\n"
                     f"Choose an option: ")

            choice = input(promt)

            if choice == "1":
                tasks_0 = show_tasks(tasks)
                if tasks_0 == None:
                    print("No tasks here")
                else:
                    for task in tasks_0:
                        print(task)

            elif choice == "2":
                while True:
                    title = input("Enter task title:")
                    if title == "":
                        print("Invalid input try again")
                        continue
                    else:
                        break

                while True:
                    priority = input("Choice priority (high/medium/low) h/m/l: ")
                    if priority == "h" or priority == "m" or priority == "l":
                        break
                    else:
                        print(priority)
                        print("Invalid choice try again")
                        continue

                new_task = add_task(tasks,title,priority)
                tasks.insert(new_task["id"],new_task)
                save_tasks(tasks)
                print(f"Task successfully added")

            elif choice == "3":
                tasks_0 = show_tasks(tasks)
                if tasks_0 == None:
                    print("No tasks here")
                else:
                    for task in tasks_0:
                        print(task)
                    while True:
                        id = int(input("Write task id: "))
                        for task in tasks:
                            id_status = 0
                            if task["id"] == id:
                                break
                            elif task["id"] != id:
                                id_status = None

                        if id_status == None:
                            print("Invalid input")
                            continue
                        elif id_status != None:
                            break
                    while True:
                        title = input("Enter task title:")
                        if title == "":
                            print("Invalid input try again")
                            continue
                        else:
                            break

                    while True:
                        priority = input("Choice priority (high/medium/low) h/m/l: ")
                        if priority == "h" or priority == "m" or priority == "l":
                            break
                        else:
                            print(priority)
                            print("Invalid choice try again")
                            continue
                    update_task(tasks,id,title,priority)
                    save_tasks(tasks)
            elif choice == "4":
                tasks_0 = show_tasks(tasks)
                if tasks_0 == None:
                    print("No tasks here")
                else:
                    for task in tasks_0:
                        print(task)
                    while True:
                        id = int(input("Write task id: "))
                        for task in tasks:
                            id_status = 0
                            if task["id"] == id:
                                break
                            elif task["id"] != id:
                                id_status = None
                        if id_status == None:
                            print("Invalid input")
                            continue
                        elif id_status != None:
                            break
                    while True:
                        choice = input("Do you really want to delete(y/n):")
                        if choice == "y":
                            delete_task(tasks, id,choice)
                            break
                        elif choice == "n":
                            break
                        else:
                            print("Invalid input")
                            continue

                    save_tasks(tasks)
            elif choice == "5":
                tasks_0 = show_tasks(tasks)
                if tasks_0 == None:
                    print("No tasks here")
                else:
                    for task in tasks_0:
                        print(task)
                    while True:
                        id = int(input("Write task id: "))
                        for task in tasks:
                            id_status = 0
                            if task["id"] == id:
                                break
                            elif task["id"] != id:
                                id_status = None
                        if id_status == None:
                            print("Invalid input")
                            continue
                        elif id_status != None:
                            break
                    while True:
                        choice = input("do you want mark task as completed or not (c/n):")
                        if choice == "c":
                            break
                        elif choice == "n":
                            break
                        else:
                            print("Invalid input")
                            continue
                    mark_task(tasks,id,choice)
                    save_tasks(tasks)
            elif choice == "6":
                counting = tasks_counter(tasks)
                print(f"Total: {counting["total"]}\n"
                  f"Completed: {counting["completed"]}\n"
                  f"Incompleted: {counting["incompleted"]}")
            elif choice == "7":
                show_incomplete(tasks)
            elif choice == "8":
                print(f"Have a good day")
                save_tasks(tasks)
                exit()
            else:
                print(f"Invalid input please try again. ")


    main_menu()