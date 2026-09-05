from tkinter import *


root = Tk()

root.geometry('100x100')

btn = Button(root, text = 'click me !',bd = '5', background = "green", command = root.destroy  )


btn.pack(side="top")

root.mainloop()
