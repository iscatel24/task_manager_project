import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from buttoms import (update_task, delete_task, add_task, mark_task, save_tasks, load_tasks
, show_incomplete, tasks_counter, show_all_tasks)


window = tk.Tk()
window.title("Task_manager")
window.geometry("800x400")


class Tasks_manger():
    def __init__(self):
        self.tasks = []
        try:
            self.tasks = load_tasks()
        except ValueError:
            messagebox.showerror("Error", "File is damaged you need to fix it or delete file")
        self.choice = tk.StringVar()
        self.frame_3 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
        self.frame_3.grid(row=1, column=2, padx=10, pady=10)
        self._ = 0
        self.comp = tasks_counter(self.tasks)

    def add(self):
        try:
            if self.choice.get() == "High":
                choice = "h"
            elif self.choice.get() == "Medium":
                choice = "m"
            elif self.choice.get() == "Low":
                choice = "l"
            if entry_0.get() == "":
                messagebox.showerror("error", "You need write task or choice priority")
            else:
                new_task = add_task(self.tasks, entry_0.get(), choice)
                task = f"{new_task["id"]}", f"{new_task["title"].title()}", f"{new_task["priority"]}", f"[ ]"
                tree_0.insert(parent="", index="end", values=task)
                self.choice.set("Medium")
                self.tasks.append(new_task)
                self.comp = tasks_counter(self.tasks)
                label_1.config(text=f"Tasks saved:{len(tree_0.get_children())}\n"
                                    f"Tasks completed:{self.comp["completed"]}\n"
                                    f"Tasks uncompleted:{self.comp["incompleted"]} ")
                entry_0.delete(0, tk.END)
                messagebox.showinfo(title="✅", message="Tasks successfully added")
                save_tasks(self.tasks)
        except:
            messagebox.showerror("error", "You need choice priority")


    def update(self):
        if entry_0.get() == "" or self.choice.get() == 0:
            messagebox.showerror("error", "You need write task or choice priority")
        if self.choice.get() == "High":
            choice = "h"
        elif self.choice.get() == "Medium":
            choice = "m"
        elif self.choice.get() == "Low":
            choice = "l"
        id = tree_0.item(tree_0.selection()[0], "values")
        upd = update_task(self.tasks, int(id[0]), entry_0.get(),choice)
        task = f"{upd["id"]}", f"{upd["title"].title()}", f"{upd["priority"]}", f"[ ]"
        tree_0.item(tree_0.selection()[0], values=task)
        self.comp = tasks_counter(self.tasks)
        label_1.config(text=f"Tasks saved:{len(tree_0.get_children())}\n"
                            f"Tasks completed:{self.comp["completed"]}\n"
                            f"Tasks uncompleted:{self.comp["incompleted"]} ")
        button_3.pack(before=button_0)
        button_4.pack(after=button_3)
        button_0.config(text="Add", command=self.add)
        button_2.config(text="Delete", command=self.delete)
        self.choice.set("Medium")
        entry_0.delete(0, tk.END)
        save_tasks(self.tasks)

    def edit(self):
        try:
            task_index = tree_0.index(tree_0.selection()[0])
            self._ = task_index
            entry_0.insert(self._,string=self.tasks[self._]["title"])
            if self.tasks[task_index]["priority"] == "low":
                combo_box_0.current(2)
            elif self.tasks[task_index]["priority"] == "medium":
                combo_box_0.current(1)
            elif self.tasks[task_index]["priority"] == "high":
                combo_box_0.current(0)
            button_3.pack_forget()
            button_4.pack_forget()
            button_0.config(text="Update", command=self.update)
            button_2.config(text="Cancel", command=self.cancel)
        except :
            messagebox.showerror("error", "You need to select task")

    def cancel(self):
        tree_0.selection_remove(tree_0.selection()[0])
        button_3.pack(before=button_0)
        button_4.pack(after=button_3)
        button_0.config(text="Add", command=self.add)
        button_2.config(text="Delete", command=self.delete)
        entry_0.delete(0, tk.END)
        self._ = 0
        self.choice.set("Medium")

    def delete(self):
        try:
            choice = "y"
            id = tree_0.item(tree_0.selection()[0], "values")
            new_list = delete_task(self.tasks,int(id[0]),choice)
            if new_list == None:
                pass
            elif new_list != None:
                self.tasks = new_list
            tree_0.delete(tree_0.selection()[0])
            self.comp = tasks_counter(self.tasks)
            label_1.config(text=f"Tasks saved:{len(tree_0.get_children())}\n"
                                f"Tasks completed:{int(self.comp["completed"])}\n"
                                f"Tasks uncompleted:{int(self.comp["incompleted"])} ")
            messagebox.showinfo(title="🗑️", message="Tasks successfully deleted ")
            save_tasks(self.tasks)
        except:
            messagebox.showerror("error", "You need to select task")


    def completed(self):
        try:
            self._ = "c"
            object_0 = []
            id = tree_0.item(tree_0.selection()[0], "values")
            self.tasks = mark_task(self.tasks,int(id[0]),self._)
            upd = tree_0.item(tree_0.selection()[0], "values")
            for i in range(0,len(upd)) :
                object_0.append(upd[i])
            object_0[3] = "[X]"
            tree_0.item(tree_0.selection()[0],values=object_0)
            self.comp = tasks_counter(self.tasks)
            label_1.config(text=f"Tasks saved:{len(tree_0.get_children())}\n"
                                f"Tasks completed:{self.comp["completed"]}\n"
                                f"Tasks uncompleted:{self.comp["incompleted"]} ")
            save_tasks(self.tasks)
        except:
            messagebox.showerror("error", "You need to select task")

    def uncompleted(self):
        try:
            self._ = "n"
            object_0 = []
            id = tree_0.item(tree_0.selection()[0], "values")
            self.tasks = mark_task(self.tasks, int(id[0]), self._)
            upd = tree_0.item(tree_0.selection()[0], "values")
            for i in range(0, len(upd)):
                object_0.append(upd[i])
            object_0[3] = "[ ]"
            tree_0.item(tree_0.selection()[0], values=object_0)
            self.comp = tasks_counter(self.tasks)
            label_1.config(text=f"Tasks saved:{len(tree_0.get_children())}\n"
                                f"Tasks completed:{self.comp["completed"]}\n"
                                f"Tasks uncompleted:{self.comp["incompleted"]} ")
            save_tasks(self.tasks)
        except False:
            messagebox.showerror("error", "You need to select task")


ts = Tasks_manger()

frame_0 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
label_0 = tk.Label(frame_0, text="Write your task and choice priority.", bg="white")
entry_0 = tk.Entry(frame_0, bg="white")

frame_1 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
scrollbar_0 = tk.Scrollbar(frame_1)
columns = "ID","TASK","PRIORITY","STATUS"
tree_0 = ttk.Treeview(frame_1,columns=columns,show="headings",yscrollcommand=scrollbar_0.set)
tree_0.heading("ID",text="ID")
tree_0.heading("TASK",text="TASK")
tree_0.heading("PRIORITY",text="PRIORITY")
tree_0.heading("STATUS",text="STATUS")
tree_0.column("ID",width=30)
tree_0.column("TASK",width=300)
tree_0.column("PRIORITY",width=60)
tree_0.column("STATUS",width=50)
scrollbar_0.config(command=tree_0.yview)




l_taks = load_tasks()
if l_taks:
    for task in l_taks:
        stat = ""
        if task["completed"]:
            stat += "X"
        elif task["completed"] == False:
            stat += " "
        new_task = f"{task["id"]}",f"{task["title"].title()}",f"{task["priority"]}",f"[{stat}]"
        tree_0.insert(parent="",index="end", values=new_task)
label_1 = tk.Label(frame_1, text=f"Tasks saved:{len(tree_0.get_children())}\n"
                                f"Tasks completed:{int(ts.comp["completed"])}\n"
                                f"Tasks uncompleted:{int(ts.comp["incompleted"])}", bg="white")

frame_2 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
button_0 = tk.Button(frame_2, text="Add", width=15, relief=tk.RIDGE,command=ts.add )
button_1 = tk.Button(frame_2, text="Edit", width=15, relief=tk.RIDGE,command=ts.edit )
button_2 = tk.Button(frame_2, text="Delete", width=15, relief=tk.RIDGE,command=ts.delete )
button_3 = tk.Button(frame_2, text="Complete", width=15, relief=tk.RIDGE,command=ts.completed)
button_4 = tk.Button(frame_2, text="Uncompleted", width=15, relief=tk.RIDGE,command=ts.uncompleted)

label_2 = tk.Label(ts.frame_3, text=f"Priority", bg="white")

combo_box_0 = ttk.Combobox(ts.frame_3,textvariable=ts.choice,state="readonly")
combo_box_0["values"] = ("High",
                         "Medium",
                         "Low")



frame_1.grid(row=0, column=0, rowspan=2, pady=10, sticky="nw")
scrollbar_0.pack(side="right",fill="y")
tree_0.pack()
label_1.pack(padx=3)
frame_0.grid(row=0, column=1, padx=10, pady=10, sticky="n")
label_0.pack(pady=2)
entry_0.pack()
frame_2.grid(row=1, column=1, padx=10, pady=10)
button_3.pack(pady=2)
button_4.pack(pady=2, after=button_3)
button_0.pack(pady=2)
button_1.pack(pady=2)
button_2.pack(pady=2)
label_2.pack()
combo_box_0.pack()
combo_box_0.current(1)

window.mainloop()