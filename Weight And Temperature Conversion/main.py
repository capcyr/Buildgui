from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Weight Conversion") 
root.geometry("500x500")


def kg_conversion():
    global grams
    kg = e2_value.get()
    grams = float(e2_value.get())*1000

    pound = float(e2_value.get())*2.20462

    ounce=float(e2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END,grams)
    t2.delete("1.0",END)
    t2.insert(END,pound)
    t3.delete("1.0",END)
    t3.insert(END,ounce)
    


  
#description equals

kg_label = Label(root, text="Enter the weight in Kg:")
kg_label.grid(row=0,column=0)
e2_value = StringVar()
e2 = Entry(root, textvariable=e2_value)
e3_label = Label(root,text = "Gram")
e4_label = Label(root,text = "Pounds")
e5_label = Label(root, text="Ounce")
e2.grid(row=0,column=1)
e3_label.grid(row=1,column=0)
e4_label.grid(row=1, column=1)
e5_label.grid(row=1, column=2)
t1 = Text(root,height=1,width=20)
t1.grid(row=2,column=0)
t2 = Text(root,height=1,width=20)
t2.grid(row=2,column=1)
t3 = Text(root,height=1,width=20)
t3.grid(row=2,column=2)





btn = Button(root,text="Convert", font= 2, command= kg_conversion)
btn.grid(row=0,column=2)

root.mainloop()