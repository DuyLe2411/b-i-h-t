from tkinter import *
import mysql.connector
from tkinter import messagebox

#Thiết lập giao diện
win = Tk()
win.title("shopping")
win.geometry('700x300')


title = Label(win,bg='navy',fg='pink',font=('Times News Roman',18),text='ỨNG DỤNG TÍNH TOÁN SẢN PHẨM')
title.pack(side=TOP,fill=BOTH)
#Tạo Input, Frame, Label
frame1 = Frame(master=win,bg='pink',pady=20,padx=0)
frame1.pack(fill=BOTH)
#1
product_label = Label(frame1,text='Loại sản phẩm:', bg='pink',pady=20,padx=0)
product_label.grid(row=0,column=0)

pro_entry = Entry(frame1,width=50,bg='light green')
pro_entry.grid(row=0,column=1)

#2
line = Label(frame1,text='-'*80,pady=10,bg='pink')
line.grid(row=1,column=1)


#3
name_label = Label(frame1,bg='pink',text='Tên sản phẩm giá thành thấp/cao nhất:',pady=20)
name_label.grid(row=2,column=0)

name_entry = Entry(frame1,bg='light green',width=100)
name_entry.grid(row=2,column=1)

#4
price_label = Label(frame1,bg='pink',text='Giá tiền:',pady=20)
price_label.grid(row=3,column=0)

price_entry = Entry(frame1,bg='light green',width=50)
price_entry.grid(row=3,column=1)

#Tạo button
def calculate_highest_price(specific_database):
    global myresult,name_entry,price_entry
    name_entry.delete(0,'end')
    price_entry.delete(0,'end') 
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nicknilacuabon",
    database= specific_database
    )
    mycursor = mydb.cursor()
    sql = "SELECT name_product, price FROM products ORDER BY price DESC LIMIT 1"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    name_product = myresult[0][0]
    price = myresult[0][1]
    name_entry.insert(0,name_product)
    price_entry.insert(0,price)

def find_highest_price():
    if pro_entry.get() not in ["laptop","shoes","fridge","phone"]:
        messagebox.showwarning('Warning 📢', "We dont have this sort of product")
    else:
        calculate_highest_price(pro_entry.get())

def calculate_lowest_price(specific_database):
    global myresult,name_entry,price_entry
    name_entry.delete(0,'end')
    price_entry.delete(0,'end') 
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nicknilacuabon",
    database= specific_database
    )
    mycursor = mydb.cursor()
    sql = "SELECT name_product, price FROM products ORDER BY price LIMIT 1"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    name_product = myresult[0][0]
    price = myresult[0][1]
    name_entry.insert(0,name_product)
    price_entry.insert(0,price)

def find_lowest_price():
    if pro_entry.get() not in ["laptop","shoes","fridge","phone"]:
        messagebox.showwarning('Warning 📢', "We dont have this sort of product")
    else:
        calculate_lowest_price(pro_entry.get())
   

button1 = Button(frame1,text="Xem tên sản phẩm thấp tiền nhất",bg='yellow',command=find_lowest_price)
button1.grid(row=4,column=0)


button2 = Button(frame1,text="Xem tên sản phẩm đắt tiền nhất",bg='yellow',command=find_highest_price)
button2.grid(row=4,column=1)

#Tạo list để chọn tên loại sản phẩm:
clicked = StringVar()
clicked.set("Kinds of products")
drop = OptionMenu(frame1, clicked, "fridge","shoes","phone","laptop")
drop.grid(row=1,column=0)
#CHỨC NĂNG

win.mainloop()