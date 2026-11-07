import tkinter as tk
from tkinter import messagebox
import time


root = tk.Tk()
root.title("Stopwatch") 
root.geometry('360x260')
hour = tk.StringVar()
minute = tk.StringVar()
second = tk. StringVar()

#hour = String.Var()
hourent= tk.Entry(root, width= 4, textvariable=hour)
hourent.place(x=80,y=90)

minuteent= tk.Entry(root, width= 4,textvariable=minute)
minuteent.place(x=140,y=90)

secondent= tk.Entry(root, width= 4,textvariable=second)
secondent.place(x=200,y=90)

hour.set("00")
minute.set("00")
second.set("00")


def timestuff():
    hourent.config(state="disabled")
    minuteent.config(state="disabled")
    secondent.config(state="disabled")
    btn.config(state="disabled")

    temp = int(hour.get()) *3600+int(minute.get())*60+int(second.get())
    while temp != 0:
        mins,sec = divmod(temp,60)

        hours,mins = divmod(mins,60)


        hour.set("{:02d}".format(hours))
        minute.set("{:02d}".format(mins))
        second.set("{:02d}".format(sec))
        root.update()
        time.sleep(1)
        temp-=1
    else:
        hour.set("00")
        minute.set("00")
        second.set("00")
        hourent.config(state="normal")
        minuteent.config(state="normal")
        secondent.config(state="normal")
        btn.config(state="normal")

    messagebox.showinfo("Time Up","Time is Up")

    
    

btn = tk.Button(root, text = "Start Timer", command=timestuff)
btn.place(x=160,y=120)


root.mainloop()