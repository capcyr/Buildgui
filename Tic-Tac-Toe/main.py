import tkinter as tk
from functools import partial
import copy


root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry('600x600')
turn = "X"


board = [[''for _ in range(3)]for _ in range(3)]

def winnercheck():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] !='':
            return board [i][0]

        if board[0][i] == board[1][i] == board[2][i] !='':
            return board [0][i]
    
    if board[0][0] == board[1][1] == board[2][2] !='':
         return board [0][0]
    
    if board[0][2] == board[1][1] == board[2][0] !='':
         return board [0][2]
    
    

    return None




def playermove(row,col):
     global turn
     if board[row][col] =="":
        board[row][col] = turn

        buttons[row][col].config(text=turn)
        winner = winnercheck()
        if winner:
            result_label.config(text=f"{winner} wins!")
        elif all(all(cell != '' for cell in row) for row in board):
                result_label.config(text="It's a tie!")

        else:
            turn = "O" if turn == "X" else "X"



def commove(row,col):
     turn1 = "O"
     if board[row][col] =="":
        board[row][col] = turn1

        buttons[row][col].config(text=turn1)
     

buttons = [[None for _ in range(3)]for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j]=tk.Button(root,text="",font=('Arial',24), width=10, height=4,command=partial(playermove,i,j))
        buttons[i][j].grid(row=i,column=j)
result_label = tk.Label(root,text="",font=("Arial",18))
result_label.grid(row=3,column=0,columnspan=3)










root.mainloop()
