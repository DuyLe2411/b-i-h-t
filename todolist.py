from tkinter import *
from tkinter import messagebox
from tkinter import font
from typing import Literal
#Spectify the appearance of the simple app.
win = Tk()
win.title("Todo list 💖")

win.config(bg='pink')
win.geometry('600x600')

#Create frame:
frame = Frame(master=win)
frame.pack(pady=5)

#Create Label Today:
td = Label(frame,text="TODAY'WORKS")
td.pack(pady=10)
#Creat Listbox:
lb = Listbox(
    frame,
    width=30,
    height=10,
    font= ('Times New Roman', 17),
    bg='light blue',
    border= 10,
    fg='navy',
    activestyle='none',
    highlightthickness=0
)
lb.pack(side=LEFT,fill=BOTH)

#Create a scroll
sb1 = Scrollbar(frame)
sb1.pack(side=RIGHT,fill=BOTH)
#Glu a scroll in Listbox:
lb.config(yscrollcommand=sb1.set)
sb1.config(command=lb.yview)


#Add frame to button
entry = Entry(
    win,
    font=('Times New Roman',15),
    fg='dark blue',
    bg='light green'
)
entry.pack(pady=20)

button = Frame(win)
button.pack(pady=20,padx=10)

#Create button
def add_func():
    task = entry.get()
    if task != '':
        lb.insert(END,f'\N{RIGHTWARDS BLACK ARROW} {task}')
        entry.delete(0,'end')
    else:
        messagebox.showwarning('Warning 📢', "Write your today'activity here")
add_button = Button(master=button,text="Add today's activity ",command=add_func,padx=10,pady=20,bg='yellow')
add_button.pack(side=LEFT,expand=True,fill=BOTH)

def del_func():
    lb.delete(ANCHOR)
del_button = Button(master=button,text="Delete today's activity ",command=del_func,padx=10,pady=20,bg='red')
del_button.pack(side=RIGHT,expand=True,fill=BOTH)

#checkboxes
def show():
    my_Label = Label(win,font=7,bg='pink',fg='navy',text=var.get()).place(x=107,y=560)
    
    

var = StringVar()
check =  Checkbutton(win,border=0,bg='pink', text="Did you complete all of your works today? ", variable=var,onvalue="That's great.Keep being perfect!💕",offvalue="That's OK. Try more tomorrow!")
check.place(x=107,y=510)

submit_button = Button(win,text='Submit',command=show).place(x=107,y=530)

win.mainloop()