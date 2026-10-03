from tkinter import *
from tkinter import messagebox 
import calendar

root = Tk()
root.geometry('500x500')



year = Entry(root, width=30)
year.place(x=95,y=90)
year1 = Label(root, text="Year",font=14).place(x = 40, y = 85)

def showCal():
    try:
        fetchhere = int(year.get())
        new_gui = Toplevel(root)
        new_gui.title(f"Calendar-{fetchhere}")
        new_gui.geometry("750x650")
        new_gui.config(bg="white")
        cal_content = calendar.calendar(fetchhere)
        heading = Label(new_gui, text=f"Calendar for {fetchhere}", font=("Arial", 16, "bold"), bg="white")
        heading.pack(pady=10)
        text_area = Text(new_gui, width=80, height=35, font = ("Courier",10))
        text_area.pack(padx=10,pady=10)
        text_area.insert(END,cal_content)
        text_area.config(state=DISABLED)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid year!")

bookti1 = Label(root, text="CALENDER",font=50).place(x = 210, y = 40)


btn = Button(root,text="Show Calender", font= 20, background="Blue", command=showCal).place(x = 170, y = 300)
btn2 = Button(root,text="EXIT", font = 20, background="Red").place(x = 210, y = 400)












root.mainloop()