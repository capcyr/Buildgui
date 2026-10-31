import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Digital Clock") 
root.geometry('500x100')

def update_time():
    string = strftime("%H:%M:%S%p")
    t1.config(text=string)
    t1.after(1000,update_time)





t1 = tk.Label(root,font=("calibri",40, "bold"),background="black", foreground="white",height=10,width=18)
t1.pack(anchor="center")
update_time()
root.mainloop()