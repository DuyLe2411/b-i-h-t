import turtle
import datetime




class Clock:
    def __init__(self, hour, minute, second) :
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def set_second(self):
        dt = datetime.datetime.now()
        return dt.second

    def set_minute(self):
        dt = datetime.datetime.now()
        return dt.minute + self.set_second() / 60
    
    def set_hour(self):
        dt = datetime.datetime.now()
        return dt.hour + self.set_minute() / 12 if dt.hour < 12 else dt.hour + self.set_minute() / 12 - 12

    def draw_clock(self,r): # Vẽ đồng hồ và vạch chi tiết
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.setup(800,800)
        turtle.bgcolor("light blue")
        t.speed(0)
        turtle.hideturtle()
        t.pencolor("black")
        t.fillcolor("white")
        turtle.tracer(0)
        t.begin_fill()
        t.penup()
        t.goto(0,r * (-1)) #Di xuống dưới để vẽ chuẩn với bán kính và khít tọa độ (0,0)
        t.pendown()
        t.circle(r) # Vẽ hình tròn của đồng hồ
        t.end_fill()
        t.penup()
        t.home()
        for i in range(60): #Vẽ các vạch 
            t.right(i*6)
            if i % 15 == 0: # Vạch bự
                t.pensize(5)
                t.penup()
                t.fd(0.75 * r)
                t.pendown()
                t.fd(0.15 * r)
                t.penup()
                t.home()
            elif i % 5 == 0: # Vạch vừa
                t.pensize(3)
                t.fd(0.8 * r)
                t.pendown()
                t.fd(0.2 * r)
                t.penup()
                t.home()
            else: # Vạch nhỏ nhất
                t.pensize(2)
                t.fd(0.9 * r)
                t.pendown()
                t.fd(0.1*r)
                t.penup()
                t.home()
        screen.update()
    def draw_hands(self,r):
        t = turtle.Turtle()
        t.pendown()
        #Vẽ kim giờ:
        t.lt(90)
        t.pensize(7)
        t.left(self.hour * 30)
        t.fd(0.5 * r)
        t.home()

        #Vẽ kim phút:
        t.lt(90)
        t.pensize(5)
        t.rt(self.minute * 6)
        t.fd(0.68 * r)
        t.home()

        #Vẽ kim giây:
        t.lt(90)
        t.pensize(3)
        t.pencolor("red")
        t.rt(self.second * 6)
        t.fd(0.68 * r)
        t.home()

        #Vẽ tâm đông hồ:
        t.pencolor("black")
        t.dot(20)
        t.penup()
        t.home()

        turtle.Screen().update()

        t.clear() # Xóa pen đã tồn tại trước đó

    def run_clock(self,r):
        while True:
            self.second = self.set_second()
            self.minute = self.set_minute()
            self.hour = self.set_hour()
            self.draw_hands(r)

Clock = Clock(6,53,30)
radius = 300
Clock.draw_clock(radius)
Clock.run_clock(radius)
turtle.done()