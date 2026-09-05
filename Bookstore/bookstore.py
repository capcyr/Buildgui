#Practice 5: Book Store Inventory
#Task: Create a data entry form for a bookstore using precise .place() coordinates to create neat rows.
#Set the window title to "Book Inventory".
#Create 3 rows of input fields:
#Row 1: Label "Book Title" and an Entry box.
#Row 2: Label "Author" and an Entry box.
#Row 3: Label "Price" and an Entry box.
#Add a "Save Book" button at the bottom centered under the fields.





from tkinter import *

root = Tk()
root.geometry('500x500')


bookti1 = Label(root, text="Book Title").place(x = 40, y = 40)

userentry = Entry(root, width=30).place(x=98,y=40)

root.config(background="brown")




author = Label(root,text="author").place(x = 40,y = 60)
author1 = Entry(root, width=30).place(x=81,y=60)

price1 = Label(root,text="price").place(x = 40,y = 80)
price2 = Entry(root, width=30).place(x=72,y=80)

save = Button(root,text="Save Book",bd = '5', background = "white", command = root.destroy ).place(x = 250,y = 120)


root.mainloop()