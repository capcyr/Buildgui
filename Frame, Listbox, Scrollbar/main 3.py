from tkinter import*
from tkinter import ttk

root = Tk()
root.title('Frame')
root.geometry("300x250")


w = Label(root, text= 'HelloHello', font = "50")
w.pack()
scroll_bar = Scrollbar(root)
scroll_bar.pack(side=LEFT, fill = X)
mylist = Listbox(root, yscrollcommand=scroll_bar.set)

for line in range(1,26):
    mylist.insert(END, "Hi " + str(line))


mylist.pack(side=LEFT, fill=BOTH)
scroll_bar.config(command=mylist.yview)

root.mainloop()