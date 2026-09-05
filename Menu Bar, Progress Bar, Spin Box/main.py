from tkinter import*
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title('Menu Demo')

menubar= Menu(root)

file = Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit',command = root.destroy)

root.config(menu=menubar)
root.mainloop()



