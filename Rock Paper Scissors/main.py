from tkinter import *
import random

humanmove = "none"
aimove = "none"



root = Tk()
root.title("Rock,Paper,Scissors") 
root.geometry('200x200')

def select_move(move):
    global humanmove
    humanmove = move

def aidec():
    global aimove
    moves = ["Paper","Rock","Scissors"]
    aimove = random.choice(moves)

def whowins():
    if humanmove=="Rock" and aimove=="Scissors":
         t1.insert(END,"You Win")
    elif humanmove=="Paper" and aimove=="Rock":
         t1.insert(END,"You Win")
    elif humanmove=="Scissors" and aimove=="Paper":
         t1.insert(END,"You Win")

    elif humanmove=="Rock" and aimove=="Rock":
         t1.insert(END,"You Tie")
    elif humanmove=="Scissors" and aimove=="Scissors":
         t1.insert(END,"You Tie")

    elif humanmove=="Paper" and aimove=="Paper":
          t1.insert(END,"You Tie")
    
    
    elif humanmove=="Rock" and aimove=="Paper":
          t1.insert(END,"You Lose")
    elif humanmove=="Paper" and aimove=="Scissors":
         t1.insert(END,"You Lose")
    elif humanmove=="Scissors" and aimove=="Rock":
         t1.insert(END,"You Lose")

aidec()

btn = Button(root, text = 'Rock',command=lambda: select_move("Rock"))
btn.grid(row=0,column=0)

btn1 = Button(root, text = 'Scissors',command=lambda: select_move("Scissors"))
btn1.grid(row=0,column=1)

btn2 = Button(root, text = 'Paper',command=lambda: select_move("Paper"))
btn2.grid(row=0,column=2)
btn3 = Button(root, text='Confirm', command=whowins)
btn3.grid(row=3,column=1)

t1 = Text(root,height=1,width=8)
t1.grid(row=18, column=0)



root.mainloop()

