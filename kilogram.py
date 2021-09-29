from tkinter import *

window = Tk()
window.title("Đổi đơn vị")
window.geometry('700x700')

can_nang_display = Label(master=window, text="Cân nặng (kg): ")
can_nang_display.place(x=50,y=100)

can_nang = Entry(master=window,width=30)
can_nang.place(x=150,y=100)

#kilo sang gram
gram_result = Label(master=window, text="GRAM")
gram_result.place(x=50,y=250)
def kg_to_gram():
    weight = can_nang.get()
    gram = round(float(weight) * 1000,2)
    return gram_result.config(text=gram)

#kilo sang ounch
pound_result = Label(master=window, text="POUND")
pound_result.place(x=150,y=250)
def kg_to_pound():
    weight = can_nang.get()
    pound = round(float(weight) * 2.20462,2)
    return pound_result.config(text=pound)

#kilo sang ounch
ounch_result = Label(master=window, text="OUNCH")
ounch_result.place(x=250,y=250)
def kg_to_ounch():
    weight = can_nang.get()
    ounch = round(float(weight) * 35.274,2)
    return ounch_result.config(text=ounch)

#BUTTON
function1 = Button(master=window, text="CONVERT", command=kg_to_gram)
function1.place(x=350,y=200)
function2 = Button(master=window, text="CONVERT", command=kg_to_pound)
function2.place(x=350,y=250)
function3 = Button(master=window, text="CONVERT", command=kg_to_ounch)
function3.place(x=350,y=300)

window.mainloop()




