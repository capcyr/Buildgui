
from tkinter import Tk, StringVar, messagebox
import math
import tkinter
import random

root = tkinter.Tk()
root.title("Guess the number game from 1-20") 
root.geometry('360x260')








num1 = random.randint(1,21)


def numberstuff():
    global num3
    num3 = int(e2_value.get())
    if num3 == num1:
        messagebox.showinfo("Secret Number Guessing Game","You got it right")
    if num3 > num1:
        messagebox.showinfo("Secret Number Guessing Game","Too High")

    if num3 < num1:
        messagebox.showinfo("Secret Number Guessing Game","Too Low")



num1label = tkinter.Label(root, text="Guess The Number:")
num1label.grid(row=0,column=0)



e2_value = StringVar()
e2 = tkinter.Entry(root,width=30,textvariable=e2_value)
e2.grid(row=1,column=0)



btn1 = tkinter.Button(root,text="Confirm", command=numberstuff)
btn1.grid(row=2,column=0)




root.mainloop()
