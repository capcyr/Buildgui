from tkinter import *


root = Tk()

root.title("Login In Page")

root.geometry('500x500')

root.config(background="green")

newname = Label(root,text="username").place(x = 40,y = 40)

userentry = Entry(root, width=30).place(x=95,y=40)

newpass = Label(root,text="password").place(x = 40,y = 60)

userpass = Entry(root, width=30).place(x=95,y=60)

newname = Button(root,text="Submit",bd = '5', background = "white", command = root.destroy ).place(x = 250,y = 80)





root.mainloop()
