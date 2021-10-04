from tkinter import *
from tkinter import font


win = Tk()
win.title("Máy tính cá nhân")
win.resizable(False,False)
first_number = ''
second_number = ''
operator = ''

def plus(first_number,second_number):
    return first_number + second_number

def sub(first_number,second_number):
    return first_number - second_number

def divide(first_number,second_number):
    return first_number / second_number

def mul(first_number,second_number):
    if second_number == 0:
        raise Exception("Không đc chia cho 0")
    return first_number * second_number

def calculate(operator,first_number, second_number):
    if operator == '+':
        return plus(first_number,second_number)
    elif operator == '-':
        return sub(first_number,second_number)
    elif operator == '*':
        return mul(first_number,second_number)
    elif operator == '/':
        return divide(first_number,second_number)

def press_number(widget, number):# ĐI TỪ DƯỚI LÊN
    global operator, first_number, second_number
    if operator != '' and second_number == '':
        first_number = widget.get()
        widget.delete(0,'end')
        widget.insert(0, number)
        second_number = number
    elif second_number != '':
        widget.insert(len(widget.get()), number)
        second_number = widget.get()
    else:
        widget.insert(len(widget.get()), number)

def press_operation(clicked_operator):
    global operator
    operator = clicked_operator

def press_equal():
    global operator, first_number, second_number
    txt_display.delete(0, len(txt_display.get()))
    txt_display.insert(0, calculate(operator, int(first_number), int(second_number)))

txt_display = Entry(master=win,bg='black',fg='white')
txt_display.pack(fill='x')

frame1 = Frame(master=win,border=4)
frame1.pack(fill='x')


def AC_button(widget):
    global first_number, second_number
    widget.delete(0,'end')


#DÒNG ĐẦU
button1 = Button(master=frame1,text='AC',width=5,height=2,bg="brown",fg='white' ,pady=10,command=lambda: AC_button(txt_display))
button1.grid(row=1,column=0)

button2 = Button(master=frame1,text='+/-',width=5,height=2,bg="brown",fg='white',pady=10)
button2.grid(row=1,column=1)

button3 = Button(master=frame1,text='%',width=5,height=2,bg="brown",fg='white',pady=10)
button3.grid(row=1,column=2)

button4 = Button(master=frame1,text='/',width=5,height=2,bg="orange",fg='white',pady=10,command=lambda: press_operation('/'))
button4.grid(row=1,column=3)

#DÒNG HAI
button5 = Button(master=frame1,text='7',width=5,height=2,bg="silver",fg='white',pady=10,command=lambda: press_number(txt_display,'7'))
button5.grid(row=2,column=0)

button6 = Button(master=frame1,text='8',width=5,height=2,bg="silver",fg='white',pady=10,command=lambda: press_number(txt_display,'8'))
button6.grid(row=2,column=1)

button7 = Button(master=frame1,text='9',width=5,height=2,bg="silver",fg='white',pady=10,command=lambda: press_number(txt_display,'9'))
button7.grid(row=2,column=2)

button8 = Button(master=frame1,text='*',width=5,height=2,bg="orange",fg='white',pady=10,command=lambda: press_operation('*'))
button8.grid(row=2,column=3)

#Dòng 3
button9 = Button(master=frame1,text='4',width=5,height=2,bg="silver",fg='white',pady=10,command=lambda: press_number(txt_display,'4'))
button9.grid(row=3,column=0)

button4 = Button(master=frame1,text='5',width=5,height=2,bg="silver",fg='white',pady=10,command=lambda: press_number(txt_display,'5'))
button4.grid(row=3,column=1)

button11 = Button(master=frame1,text='6',width=5,height=2,bg="silver",fg='white',pady=10,command=lambda: press_number(txt_display,'6'))
button11.grid(row=3,column=2)

button12 = Button(master=frame1,text='-',width=5,height=2,bg="orange",fg='white',pady=10,command=lambda: press_operation('-'))
button12.grid(row=3,column=3)

#DÒNG 4
button13 = Button(master=frame1,text='1',width=5,height=2,bg="silver",fg='white',pady=10,command=lambda: press_number(txt_display,'1'))
button13.grid(row=4,column=0)

button14 = Button(master=frame1,text='2',width=5,height=2,bg="silver",fg='white',pady=10,command=lambda: press_number(txt_display,'2'))
button14.grid(row=4,column=1)

button15 = Button(master=frame1,text='3',width=5,height=2,bg="silver",fg='white',pady=10,command=lambda: press_number(txt_display,'3'))
button15.grid(row=4,column=2)

button16 = Button(master=frame1,text='+',width=5,height=2,bg="orange",fg='white',pady=10,command=lambda: press_operation('+'))
button16.grid(row=4,column=3)

#DÒNG 5
button14 = Button(master=frame1,bg='silver',fg='white',width=12,height=2,text='0',pady=10,command=lambda: press_number(txt_display,'0'))
button14.grid(row=5,columnspan=2)

button18 = Button(master=frame1,text=',',width=5,height=2,bg="silver",fg='white',pady=10)
button18.grid(row=5,column=2)

button19 = Button(master=frame1,text='=',width=5,height=2,bg="orange",fg='white',pady=10,command=lambda: press_equal())
button19.grid(row=5,column=3)





#Hiển thị màn hình kết quả



win.mainloop()