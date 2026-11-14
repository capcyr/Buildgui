import tkinter as tk
from tkinter import filedialog, messagebox
import time
import threading


root = tk.Tk()
root.title("Memorizer App")
listbox = tk.Listbox(root,width=40,height=10)
listbox.pack(side=tk.LEFT,padx=10,pady=10)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.LEFT,fill=tk.Y)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command=listbox.yview)
entry = tk.Entry(root,width=30)
entry.pack(padx=10,pady=5)
reminder_message = tk.Entry(root,width=30)
reminder_message.pack(padx=10, pady=5)
reminder_message.insert(0,"Reminder Message")

#Entry for reminder time(HH:MM)
reminder_time = tk.Entry(root,width=30)
reminder_time.pack(padx=10,pady=5)
reminder_time.insert(0,"HH:MM")

def add_item():
    listbox.insert(tk.END,entry.get())
    entry.delete(0,tk.END)

def del_item():
    selected_item_index = listbox.curselection()
    if selected_item_index:
        listbox.delete(selected_item_index)

def save_item():
    file = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("Text files","*.txt"),("All files","*.*")])
    if file:
        items = listbox.get(0,tk.END)
    for item in items:
        file.write(item+"\n")
    file.close()

def remind_item(message,target_time):
    while True:
        now = time.strftime("%H:%M")
        if now == target_time:
            messagebox.showinfo("Reminder",message)
            break
        time.sleep(20)
def set_reminder():
    msg = reminder_message.get()
    r_time = reminder_time.get()
    if msg and r_time:
        threading.Thread(target=remind_item, args=(msg, r_time),daemon=True).start()
        messagebox.showinfo("Reminder Set",f"Reminder set for {r_time}")



btn_add = tk.Button(root,text="Add",command=add_item)
btn_add.pack(pady=5)

btn_del = tk.Button(root,text="Delete",command= del_item)
btn_del.pack(pady=10)

btn_save = tk.Button(root,text="Save", command=save_item)
btn_save.pack(pady=15)

btn_remind = tk.Button(root,text="Reminder",command=set_reminder)
btn_remind.pack(pady=20)




root.mainloop()