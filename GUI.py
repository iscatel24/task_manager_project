import tkinter as tk
from tkinter import messagebox

from buttoms import (update_task, delete_task, add_task, mark_task, save_tasks, load_tasks
, show_incomplete, tasks_counter, show_all_tasks)


window = tk.Tk()
window.title("Task_manager")
window.geometry("600x500")


class Tasks_manger():
    def __init__(self):
        self.tasks = []
        self.tasks = load_tasks()
        self.choice = tk.IntVar()
        self.frame_3 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
        self.frame_3.grid(row=1, column=2, padx=10, pady=10)
        self.radiobt_0 = tk.Radiobutton(self.frame_3, text="Low",
                                        value=1, variable=self.choice, bg="white")
        self.radiobt_1 = tk.Radiobutton(self.frame_3, text="Medium",
                                        value=2, variable=self.choice, bg="white")
        self.radiobt_2 = tk.Radiobutton(self.frame_3, text="High",
                                        value=3, variable=self.choice, bg="white")
        self._ = 0
        self.comp = tasks_counter(self.tasks)

    def add(self):
        try:
            if entry_0.get() == "" or self.choice.get() == 0:
                messagebox.showerror("error", "You need write task or choice priority")
            else:
                if self.choice.get() == 3:
                    choice = "h"
                elif self.choice.get() == 2:
                    choice = "m"
                elif self.choice.get() == 1:
                    choice = "l"
                new_task = add_task(self.tasks, entry_0.get(), choice)
                task = f"{new_task["id"]}.{"[ ]"} {new_task["title"].title()} ({new_task["priority"]})"
                list_box_0.insert(new_task["id"],task)
                self.choice.set(0)
                self.tasks.append(new_task)
                entry_0.delete(0, tk.END)
                self.comp = tasks_counter(self.tasks)
                label_1.config(text=f"Tasks saved:{list_box_0.size()}\n"
                                    f"Tasks completed:{self.comp["completed"]}\n"
                                    f"Tasks uncompleted:{self.comp["incompleted"]} ")
                messagebox.showinfo(title="✅", message="Tasks successfully added")
                save_tasks(self.tasks)
        except:
            pass

    def update(self):
        if entry_0.get() == "" or self.choice.get() == 0:
            messagebox.showerror("error", "You need write task or choice priority")
        if self.choice.get() == 3:
            choice = "h"
        elif self.choice.get() == 2:
            choice = "m"
        elif self.choice.get() == 1:
            choice = "l"
        id = list_box_0.index(list_box_0.curselection())
        upd = update_task(self.tasks, id + 1, entry_0.get(), choice)
        task = f"{upd["id"]}.{"[ ]"} {upd["title"].title()} ({upd["priority"]})"
        list_box_0.insert(upd["id"], task)

        list_box_0.delete(list_box_0.index(list_box_0.curselection()))
        self.comp = tasks_counter(self.tasks)
        label_1.config(text=f"Tasks saved:{list_box_0.size()}\n"
                            f"Tasks completed:{self.comp["completed"]}\n"
                            f"Tasks uncompleted:{self.comp["incompleted"]} ")
        button_3.pack(before=button_0)
        button_4.pack(after=button_3)
        button_0.config(text="Add", command=self.add)
        button_2.config(text="Delete", command=self.delete)
        self.choice.set(0)
        entry_0.delete(0, tk.END)
        save_tasks(self.tasks)

    def edit(self):
        try:
            edit = list_box_0.index(list_box_0.curselection())
            self._ = edit
            entry_0.insert(list_box_0.index(list_box_0.curselection()),
                           string=self.tasks[edit]["title"])
            if self.tasks[edit]["priority"] == "low":
                self.radiobt_0.invoke()
            elif self.tasks[edit]["priority"] == "medium":
                self.radiobt_1.invoke()
            elif self.tasks[edit]["priority"] == "high":
                self.radiobt_2.invoke()
            button_3.pack_forget()
            button_4.pack_forget()
            button_0.config(text="Update", command=self.update)
            button_2.config(text="Cancel", command=self.cancel)
        except:
            messagebox.showerror("error", "You need to select task")

    def cancel(self):
        list_box_0.select_clear(self._)
        button_3.pack(before=button_0)
        button_4.pack(after=button_3)
        button_0.config(text="Add", command=self.add)
        button_2.config(text="Delete", command=self.delete)
        entry_0.delete(0, tk.END)
        self._ = 0
        self.choice.set(0)

    def delete(self):
        try:
            choice = "y"
            id = list_box_0.index(list_box_0.curselection())
            new_list = delete_task(self.tasks,id +1,choice)
            if new_list == None:
                pass
            elif new_list != None:
                self.tasks = new_list
            list_box_0.delete(list_box_0.index(list_box_0.curselection()))
            self.comp = tasks_counter(self.tasks)
            label_1.config(text=f"Tasks saved:{list_box_0.size()}\n"
                                f"Tasks completed:{int(self.comp["completed"])}\n"
                                f"Tasks uncompleted:{int(self.comp["incompleted"])} ")
            messagebox.showinfo(title="🗑️", message="Tasks successfully deleted ")
            save_tasks(self.tasks)
        except:
            messagebox.showerror("error", "You need to select task")


    def completed(self):
        try:
            self._ = "c"
            id = list_box_0.index(list_box_0.curselection())
            self.tasks = mark_task(self.tasks,id +1,self._)
            tasks_new = show_all_tasks(self.tasks)
            for _ in range(0,list_box_0.size()) :
                list_box_0.delete(_)
                list_box_0.insert(_,tasks_new[_])
            self.comp = tasks_counter(self.tasks)
            label_1.config(text=f"Tasks saved:{list_box_0.size()}\n"
                                f"Tasks completed:{self.comp["completed"]}\n"
                                f"Tasks uncompleted:{self.comp["incompleted"]} ")
            save_tasks(self.tasks)
        except :
            messagebox.showerror("error", "You need to select task")

    def uncompleted(self):
        try:
            self._ = "n"
            id = list_box_0.index(list_box_0.curselection())
            self.tasks = mark_task(self.tasks, id + 1, self._)
            tasks_new = show_all_tasks(self.tasks)
            for _ in range(0, list_box_0.size()):
                list_box_0.delete(_)
                list_box_0.insert(_, tasks_new[_])
            self.comp = tasks_counter(self.tasks)
            label_1.config(text=f"Tasks saved:{list_box_0.size()}\n"
                                f"Tasks completed:{self.comp["completed"]}\n"
                                f"Tasks uncompleted:{self.comp["incompleted"]} ")
            save_tasks(self.tasks)
        except :
            messagebox.showerror("error", "You need to select task")

ts = Tasks_manger()

frame_0 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
label_0 = tk.Label(frame_0, text="Write your task and choice priority.", bg="white")
entry_0 = tk.Entry(frame_0, bg="white")

frame_1 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
list_box_0 = tk.Listbox(frame_1, width=40)
l_taks = show_all_tasks(ts.tasks)
for task in range(0,len(l_taks)):
    list_box_0.insert(task, l_taks[task])
label_1 = tk.Label(frame_1, text=f"Tasks saved:{list_box_0.size()}\n"
                                f"Tasks completed:{int(ts.comp["completed"])}\n"
                                f"Tasks uncompleted:{int(ts.comp["incompleted"])}", bg="white")

frame_2 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
label_2 = tk.Label(frame_2, text=f"", bg="white")
button_0 = tk.Button(frame_2, text="Add", width=15, relief=tk.RIDGE,command=ts.add )
button_1 = tk.Button(frame_2, text="Edit", width=15, relief=tk.RIDGE,command=ts.edit )
button_2 = tk.Button(frame_2, text="Delete", width=15, relief=tk.RIDGE,command=ts.delete )
button_3 = tk.Button(frame_2, text="Complete", width=15, relief=tk.RIDGE,command=ts.completed)
button_4 = tk.Button(frame_2, text="Uncompleted", width=15, relief=tk.RIDGE,command=ts.uncompleted)



frame_1.grid(row=0, column=0, rowspan=2, pady=10, sticky="nw")
list_box_0.pack()
label_1.pack(padx=3)
frame_0.grid(row=0, column=1, padx=10, pady=10, sticky="n")
label_0.pack(pady=2)
entry_0.pack()
frame_2.grid(row=1, column=1, padx=10, pady=10)
# label_2.pack()
button_3.pack(pady=2)
button_4.pack(pady=2, after=button_3)
button_0.pack(pady=2)
button_1.pack(pady=2)
button_2.pack(pady=2)
ts.radiobt_0.pack()
ts.radiobt_1.pack()
ts.radiobt_2.pack()

window.mainloop()