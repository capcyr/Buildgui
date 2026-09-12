from tkinter import*
from tkinter.ttk import*


root = Tk()
root.title('Menu Demo')

w = Spinbox(root, from_=0, to=10)
w.pack()
root.mainloop()
