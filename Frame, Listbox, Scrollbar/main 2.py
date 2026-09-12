from tkinter import*
from tkinter import ttk

root = Tk()
root.title('Frame')
root.geometry("300x250")


listbox = Listbox(root, height=10, width = 15, bg = "grey", activestyle='dotbox', font = "Helvetica", fg = "yellow")
label = Label(root, text = "FOOD ITEMS")
listbox.insert(1,"Noodles")
listbox.insert(2,"Burger")
listbox.insert(3,"Fries")
listbox.insert(4,"Chicken wings")
label.pack()
listbox.pack()

root.mainloop()