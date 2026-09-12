from tkinter import*
from tkinter import ttk

root = Tk()
root.title('Frame')
root.geometry("300x150")
Label(root,text="chocolate and icecreams",font = "50").pack()

frame = Frame(root)
frame.pack()

b1_button = Button(frame, text ="Choco", fg="red", bg="beige")
b1_button.pack(side=LEFT)

b1_button = Button(frame, text ="Vanilla", fg="black", bg="beige")
b1_button.pack(side=LEFT)


b1_button = Button(frame, text ="Caramel", fg="brown", bg="beige")
b1_button.pack(side=LEFT)


b1_button = Button(frame, text ="Cherry", fg="red", bg="beige")
b1_button.pack(side=BOTTOM)


b1_button = Button(frame, text ="wafer", fg="brown", bg="beige")
b1_button.pack(side=BOTTOM)


root.mainloop()

