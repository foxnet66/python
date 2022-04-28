from turtle import *

def go_to(x, y):
    penup()
    goto(x, y)
    pendown()

def help_do():
    go_to(-400, 0)
    forward(800)
    go_to(-400, 100)
    forward(800)
    go_to(-400,200)
    forward(800)
    go_to(-400, -100)
    forward(800)
    go_to(-400, -200)
    forward(800)
    left(90)
    go_to(0,-300)
    forward(600)
    go_to(100, -300)
    forward(600)
    go_to(-100, -300)
    forward(600)
    go_to(-200, -300)
    forward(600)
    go_to(200, -300)
    forward(600)

def head():
    go_to(-200, 180)
    fillcolor('yellow')
    begin_fill()
    seth(-30)
    for _ in range(6):
        circle(36, 60)
        circle(-36, 60)
    seth(-125)
    for _ in range(5):
        circle(40,60)
        circle(-40,60)
    seth(-210)
    for _ in range(4):
        circle(45,60)
        circle(-45,60)
    seth(65)
    for _ in range(5):
        circle(40,60)
        circle(-40,60)
    end_fill()

def eye():
    go_to(14, -5)
    fillcolor('#f0f0f0')
    begin_fill()
    circle(65, 360)
    end_fill()
    begin_fill()
    go_to(13,12)
    seth(98)
    circle(-65,360)
    end_fill()

    go_to(-10,20)
    fillcolor('blue')
    begin_fill()
    circle(20,360)
    end_fill()
    go_to(-22,20)
    fillcolor('black')
    begin_fill()
    circle(7,360)
    end_fill()
    go_to(40,15)
    fillcolor('blue')
    begin_fill()
    circle(-20, 360)
    end_fill()
    go_to(53,15)
    fillcolor('black')
    begin_fill()
    circle(-7,360)
    end_fill()

    go_to(-95,65)
    left(20)
    forward(40)
    go_to(-50,87)
    right(25)
    forward(32)
    go_to(0,70)
    right(25)
    forward(40)

    go_to(40, 75)
    left(35)
    forward(40)
    go_to(90, 87)
    right(18)
    forward(30)
    go_to(120, 70)
    right(25)
    forward(40)

def nose():
    fillcolor('yellow')
    go_to(0, -7)
    begin_fill()
    right(50)
    circle(-60, 30)
    color('yellow')
    goto(15,-40)
    end_fill()
    color('black')
    go_to(0, -7)
    seth(-75)
    forward(30)
    go_to(30,-7)
    seth(-105)
    forward(30)

def mouth():
    go_to(-120, - 60)
    seth(-45)
    circle(200, 30)
    seth(0)
    forward(100)
    seth(15)
    circle(200, 30)

def tooth():
    go_to(-30,-114)
    seth(-95)
    fillcolor('white')
    begin_fill()
    forward(30)
    seth(0)
    forward(40)
    seth(95)
    forward(30)
    go_to(-30,-114)
    end_fill()

    go_to(30, -114)
    seth(-95)
    fillcolor('white')
    begin_fill()
    forward(30)
    seth(0)
    forward(40)
    seth(95)
    forward(30)
    go_to(60, -114)
    end_fill()

def hole():
    go_to(-160,160)
    circle(30, 360)

def face():
    eye()
    nose()
    mouth()
    tooth()

def body():
    go_to(-170,-180)
    seth(-120)
    circle(150, 30)
    seth(0)
    forward(40)
    seth(100)
    forward(35)
    seth(-80)
    forward(100)
    fillcolor('brown')
    begin_fill()
    seth(0)
    forward(300)
    seth(80)
    forward(110)
    seth(-100)
    forward(65)
    seth(180)
    forward(315)
    go_to(-141,-322)
    end_fill()

    go_to(-170,-255)
    fillcolor('yellow')
    begin_fill()
    seth(-75)
    forward(80)
    seth(0)
    forward(17)
    seth(105)
    forward(85)
    end_fill()

    go_to(200, -170)
    seth(-60)
    circle(-150,30)
    seth(-180)
    forward(45)
    begin_fill()
    seth(0)
    forward(20)
    seth(-100)
    forward(85)
    seth(180)
    forward(20)
    end_fill()

def tie():
    go_to(-50,-225)
    seth(-40)
    forward(40)
    seth(30)
    forward(52)
    go_to(30,-225)
    seth(-30)
    forward(40)
    seth(40)
    forward(45)
    fillcolor('red')
    go_to(0, -240)
    begin_fill()
    seth(-60)
    forward(10)
    seth(0)
    forward(30)
    seth(60)
    forward(15)
    go_to(30,-225)
    end_fill()
    go_to(4,-250)
    begin_fill()
    seth(-100)
    forward(80)
    seth(0)
    forward(55)
    seth(100)
    forward(80)
    end_fill()

def spongeBob():
    head()
    face()
    body()
    tie()

if __name__=='__main__':
    screensize(800, 600, 'white')
    title('海绵宝宝')
    pensize(3)
    speed(90)
    go_to(0, 0)
    spongeBob()
    go_to(-100,240)
    write('海绵宝宝',font=('Arial.TTF', '50', 'bold'))
    go_to(230,200)
    mainloop()