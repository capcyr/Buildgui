from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Secure Login") 
root.geometry("300x250")


def check_login():
    username = username_entry.get()
    password = password_entry.get()
    

    if username == "" or password == "":
        messagebox.showerror("Error", "Fields cannot be empty!")
    else:
        messagebox.showinfo("Login Success", "Login Successful!")


username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()


password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()


login_button = Button(root, text="Login", command=check_login)
login_button.pack()

root.mainloop()