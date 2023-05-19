import customtkinter as ctk
from tkinter import messagebox
import sqlite3
import datetime

root = ctk.CTk()
root.title("TODO APP")
root.geometry("600x450")

label = None
label_list = []
dt = datetime.datetime.now()
con = sqlite3.connect("todo.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS Action_performed (matter TEXT, x DATETIME)")  # thopu syntax


def add_todo():
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    global label_list
    global label
    todo = entry.get()

    if todo != "":
        label = ctk.CTkLabel(scrollable_frame, text=todo)
        label.pack()
        label_list.append(label)
        inserted_at = "Task added at " + str(dt)
        cur.execute("INSERT INTO Action_performed(matter,x) values(?,?)",
                    (todo, inserted_at))
        messagebox.showinfo("Task update", "Task added successfully")

    else:
        messagebox.showerror("Error", "Plz enter a valid task")
    entry.delete(0, ctk.END)

    con.commit()
    cur.execute("select * from Action_performed")
    ll = cur.fetchall()
    for i in ll:
        print(i)
    con.close()


def delete():
    # cur.execute("DELETE FROM Action")
    # con.commit()
    # con.close()
    # global label
    # label.configure(text="")
    global label_list

    if label_list:
        la = label_list[0]  # Get the last label in the list
        la.pack_forget()  # Remove the label from the GUI
        label_list.pop(0)  # Remove the label from the list

        messagebox.showinfo("Task update", "Task deleted successfully")
    else:
        messagebox.showinfo("Task update", "No tasks to delete")


title_lable = ctk.CTkLabel(root, text="Daily tasks",
                           font=ctk.CTkFont(size=30, weight="bold"))
title_lable.pack(padx=10, pady=(30, 20))


scrollable_frame = ctk.CTkScrollableFrame(root, width=(400), height=(150))
scrollable_frame.pack()


entry = ctk.CTkEntry(scrollable_frame, placeholder_text="ADD ToDo")
entry.pack(fill="x")


add_button = ctk.CTkButton(root, text="ADD TASK",
                           width=(400), command=add_todo)
add_button.pack(pady=15)


delete_button = ctk.CTkButton(root, text="Delete Task",
                              width=(400), command=delete)
delete_button.pack(pady=10)

con.commit()
con.close()
# root.deiconify()

root.mainloop()
