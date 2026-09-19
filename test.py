import tkinter as tk
from tkinter import Listbox, messagebox

from buttoms import (update_task, delete_task, add_task, mark_task, save_tasks, load_tasks
, show_incomplete, tasks_counter, show_all_tasks)

tasks = []

window = tk.Tk()
window.title("Task_manager")
window.geometry("500x500")


class Task_manager:
    def __init__(self):
        self.tasks = []
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
        self.comp = 0

    def add(self):
        try:
            if entry_0.get() == "" or self.choice.get() == 0:
                messagebox.showerror("error", "You need write task or choice priority")
            else:
                max_id = 0
                for task in self.tasks:
                    if task["id"] > max_id:
                        max_id = task["id"]
                new_task = {"id": max_id + 1,
                            "title": entry_0.get(),
                            "completed": False,
                            }
                if self.choice.get() == 3:
                    new_task["priority"] = "high"

                elif self.choice.get() == 2:
                    new_task["priority"] = "medium"
                elif self.choice.get() == 1:
                    new_task["priority"] = "low"
            self.choice.set(0)
            self.tasks.append(new_task)
            entry_0.delete(0, tk.END)
            task = f"{new_task["id"]}.{"[ ]"} {new_task["title"].title()} ({new_task["priority"]})"
            list_box_0.insert(new_task["id"], task)
            label_1.config(text=f"Tasks saved:{list_box_0.size()}\n"
                                f"Tasks completed:{self.comp}\n"
                                f"Tasks uncompleted:{list_box_0.size() - self.comp} ")
            messagebox.showinfo(title="", message="Tasks successfully added ✅")
        except:
            pass

    def delete(self):
        try:
            remove = list_box_0.index(list_box_0.curselection())
            self.tasks.pop(remove)
            list_box_0.delete(remove)
            label_1.config(text=f"Tasks saved:{list_box_0.size()}\n"
                                f"Tasks completed:{self.comp}\n"
                                f"Tasks uncompleted:{list_box_0.size() - self.comp} ")
            messagebox.showinfo(title="", message="Tasks successfully deleted 🗑️")
        except:
            messagebox.showerror("error", "You need to select task")

    def update(self):
        try:
            if entry_0.get() == "" or self.choice.get() == 0:
                messagebox.showerror("error", "You need write task or choice priority")
            else:
                new_task = {"id": self.tasks[self._]["id"],
                            "title": entry_0.get(),
                            "completed": self.tasks[self._]["completed"],
                            }
                if self.choice.get() == 3:
                    new_task["priority"] = "high"

                elif self.choice.get() == 2:
                    new_task["priority"] = "medium"
                elif self.choice.get() == 1:
                    new_task["priority"] = "low"

                self.tasks.pop(self._)
                self.tasks.insert(self._, new_task)
                entry_0.delete(0, tk.END)
                if new_task["completed"] == True:
                    self.comp = "[X]"
                elif new_task["completed"] == False:
                    self.comp = "[ ]"
                task = f"{new_task["id"]}.{self.comp} {new_task["title"].title()} ({new_task["priority"]})"
                list_box_0.insert(new_task["id"], task)
                print(self.tasks, self.choice.get())
                list_box_0.delete(self._)
                label_1.config(text=f"Tasks saved:{list_box_0.size()}\n"
                                    f"Tasks completed:{self.comp}\n"
                                    f"Tasks uncompleted:{list_box_0.size() - self.comp} ")
                button_3.pack(before=button_0)
                button_0.config(text="Add", command=self.add)
                button_2.config(text="Delete", command=self.delete)
                self._ = 0
                self.choice.set(0)
        except:
            pass

    def edit(self):
        try:
            remove = list_box_0.index(list_box_0.curselection())
            self._ = remove
            entry_0.insert(list_box_0.index(list_box_0.curselection()),
                           string=self.tasks[remove]["title"])
            print(list_box_0.get(remove))
            if self.tasks[remove]["priority"] == "low":
                self.radiobt_0.invoke()
            elif self.tasks[remove]["priority"] == "medium":
                self.radiobt_1.invoke()
            elif self.tasks[remove]["priority"] == "high":
                self.radiobt_2.invoke()
            self._ = remove
            button_3.pack_forget()
            button_0.config(text="Update", command=self.update)
            button_2.config(text="Cancel", command=self.cancel)
        except:
            messagebox.showerror("error", "You need to select task")

    def cancel(self):
        list_box_0.select_clear(self._)
        button_3.pack(before=button_0)
        button_0.config(text="Add", command=self.add)
        button_2.config(text="Delete", command=self.delete)
        entry_0.delete(0, tk.END)
        self._ = 0
        self.choice.set(0)

    def completed(self):
        for task in self.tasks:
            if task["completed"] == True:
                self.comp += 1

    # do this thing!
    def complete(self):
        _ = list_box_0.index(list_box_0.curselection())
        self.comp = "[X]"
        self.tasks[self._]["completed"] = True


if __name__ == "__main__":
    ts = Task_manager()

    frame_0 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
    label_0 = tk.Label(frame_0, text="Write your task and choice priority.", bg="white")
    entry_0 = tk.Entry(frame_0, bg="white")

    frame_1 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
    list_box_0 = tk.Listbox(frame_1)
    label_1 = tk.Label(frame_1, text=f"Tasks saved:{list_box_0.size()}\n"
                                     f"Tasks completed:{ts.comp}\n"
                                     f"Tasks uncompleted:{list_box_0.size() - ts.comp}", bg="white")

    frame_2 = tk.Frame(window, bd=4, bg="white", relief=tk.RIDGE)
    label_2 = tk.Label(frame_2, text=f"", bg="white")
    button_0 = tk.Button(frame_2, text="Add", width=15, relief=tk.RIDGE, command=ts.add)
    button_1 = tk.Button(frame_2, text="Edit", width=15, relief=tk.RIDGE, command=ts.edit)
    button_2 = tk.Button(frame_2, text="Delete", width=15, relief=tk.RIDGE, command=ts.delete)
    button_3 = tk.Button(frame_2, text="Complete", width=15, relief=tk.RIDGE, command=ts.delete)

    frame_1.grid(row=0, column=0, rowspan=2, pady=10, sticky="nw")
    list_box_0.pack()
    label_1.pack(padx=3)
    frame_0.grid(row=0, column=1, padx=10, pady=10, sticky="n")
    label_0.pack(pady=2)
    entry_0.pack()
    frame_2.grid(row=1, column=1, padx=10, pady=10)
    # label_2.pack()
    button_3.pack(pady=2)
    button_0.pack(pady=2)
    button_1.pack(pady=2)
    button_2.pack(pady=2)
    ts.radiobt_0.pack()
    ts.radiobt_1.pack()
    ts.radiobt_2.pack()

    window.mainloop()