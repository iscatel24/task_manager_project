from buttoms import show_all_tasks as show_tasks
from buttoms import (update_task,delete_task,add_task,mark_task,save_tasks,load_tasks
,show_incomplete,tasks_counter)


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
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            mark_task(tasks)
            save_tasks(tasks)
        elif choice == "6":
            tasks_counter(tasks)
        elif choice == "7":
            show_incomplete(tasks)
        elif choice == "8":
            print(f"Have a good day")
            save_tasks(tasks)
            exit()
        else:
            print(f"Invalid input please try again. ")


main_menu()