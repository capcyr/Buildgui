import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Multiplication Table Generator")
root.geometry('200x200')

selected_number = tk.StringVar()
selected_range = tk.IntVar(value=10)


number_combo = ttk.Combobox(root, textvariable=selected_number)
number_combo['values']=tuple(range(1,101))
number_combo.grid(column=0,row=0,padx=10,pady=10)

radio_10 = tk.Radiobutton(root,text="Times 10", variable= selected_range, value=10)
radio_10.grid(column=0, row=1,padx=10,pady=5)
radio_20 = tk.Radiobutton(root,text="Times 20", variable= selected_range, value=10)
radio_20.grid(column=0, row=2,padx=10,pady=5)
radio_30 = tk.Radiobutton(root,text="Times 30", variable= selected_range, value=10)
radio_30.grid(column=0, row=3,padx=10,pady=5)







root.mainloop()