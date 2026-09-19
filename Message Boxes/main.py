from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")

w = Label(root, text= 'I am a message box', font = "50")
w.pack()

messagebox.showinfo("showinfo","Information")
messagebox.showerror("ERROR","its not working")
messagebox.showwarning("WARNING","CANCEL NOW")
messagebox.askquestion("ARE YOU OVER 18","IF SO WELCOME")
messagebox.askokcancel("PLACEHOLDER","PLACEHOLDER")
messagebox.askyesno("PLACEHOLDER","PLACEHOLDER")
messagebox.askretrycancel("PLACEHOLDER","PLACEHOLDER")

root.mainloop()