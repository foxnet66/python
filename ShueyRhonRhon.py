import turtle

turtle.title('PythonShueyRhonRhon')
turtle.hideturtle()
turtle.speed(100) # drawing speed, slow:50, normal: 100, fast: 200
 
 
# outline of head
turtle.penup()
turtle.goto(-145, 135)
turtle.pensize(5)
turtle.pencolor("#BB3529")
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(45)
turtle.circle(-150, 45)
turtle.forward(80)
turtle.circle(-150, 180)
turtle.forward(80)
turtle.circle(-150, 135)
turtle.end_fill()
 
 
#pattern
turtle.fillcolor("#FF9300")
turtle.begin_fill()
 
turtle.pensize(3)
turtle.setheading(15)
turtle.circle(-600, 28)
turtle.pencolor("#FF9300")
turtle.right(30)
turtle.circle(-150, -35)
turtle.setheading(180)
turtle.forward(100)
turtle.circle(150, 42)
turtle.end_fill()
 
turtle.pencolor("#DA2D20")
turtle.penup()
turtle.goto(-100, 160)
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.circle(4, 360)
turtle.end_fill()
 
turtle.penup()
turtle.goto(-40, 169)
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.circle(4, 360)
turtle.end_fill()
 
turtle.penup()
turtle.goto(20, 169)
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.circle(4, 360)
turtle.end_fill()
 
turtle.penup()
turtle.goto(80, 163)
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.circle(4, 360)
turtle.end_fill()

#inside
#from left to right
#1
turtle.pencolor("#FF9300")
turtle.penup()
turtle.goto(-130, 135)
turtle.setheading(52)
turtle.pendown()
turtle.circle(-175, -60)
turtle.circle(-125, -70)
#2
turtle.penup()
turtle.goto(-80, 150)
turtle.setheading(54)
turtle.pendown()
turtle.circle(-175, -40)
turtle.circle(-200, -50)
#3
turtle.penup()
turtle.goto(-10, 155)
turtle.setheading(75)
turtle.pendown()
turtle.circle(-480, -35)
#4
turtle.penup()
turtle.goto(50, 150)
turtle.setheading(115)
turtle.pendown()
turtle.circle(270, -40)
turtle.circle(500, -12)
#5
turtle.penup()
turtle.goto(120, 140)
turtle.setheading(130)
turtle.pendown()
turtle.circle(180, -40)
turtle.circle(145, -80)
 
#face
turtle.pensize(5)
turtle.pencolor("#BB3529")
turtle.penup()
turtle.goto(-125, 40)
turtle.setheading(216)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.circle(34, 170)

turtle.right(60)
turtle.circle(170, 63)
turtle.right(60)
turtle.circle(32, 158)
turtle.right(65)
turtle.circle(34, 157)
turtle.circle(-15, 155)
turtle.left(30)
turtle.circle(36, 127)
turtle.circle(-15, 45)
turtle.right(38)
turtle.circle(36, 107)
turtle.circle(-15, 55)
turtle.right(22)
turtle.circle(32, 120)
turtle.end_fill()
#cheek
#left
turtle.pencolor("#F44F39")
turtle.penup()
turtle.goto(-120, 5)
turtle.fillcolor("#F44F39")
turtle.begin_fill()
turtle.pendown()
turtle.circle(15, 360)
turtle.end_fill()
#right
turtle.penup()
turtle.goto(85, 0)
turtle.fillcolor("#F44F39")
turtle.begin_fill()
turtle.pendown()
turtle.circle(15, 360)
turtle.end_fill()
#eyes
turtle.pensize(1)
#right eye
turtle.pencolor("#534A49")
turtle.penup()
turtle.goto(65, 35)
turtle.fillcolor("#534A49")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(90)
turtle.circle(9, 180)
turtle.forward(9)
turtle.circle(9, 180)
turtle.forward(9)
turtle.end_fill()
#right eye highlight
turtle.penup()
turtle.pencolor("white")
turtle.goto(57, 36)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(90)
turtle.circle(3, 360)
turtle.end_fill()
#left eye
turtle.pencolor("#534A49")
turtle.penup()
turtle.goto(-51, 35)
turtle.fillcolor("#534A49")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(90)
turtle.circle(9, 180)
turtle.forward(9)
turtle.circle(9, 180)
turtle.forward(9)
turtle.end_fill()
#left eye highlight
turtle.penup()
turtle.pencolor("white")
turtle.goto(-58, 36)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(90)
turtle.circle(3, 360)
turtle.end_fill()
 
#top of head
turtle.pensize(3)
turtle.penup()
turtle.pencolor("#5FA8D2")
turtle.goto(-108, 170)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(24)
turtle.forward(70)
turtle.left(15)
turtle.circle(-68, 80)
turtle.left(22)
turtle.forward(78)
turtle.circle(-4, 175)
turtle.forward(40)
turtle.right(22)
turtle.circle(24, 62)
turtle.circle(-34, 62)
turtle.circle(34, 75)
turtle.circle(-34, 62)
turtle.circle(24, 72)
turtle.right(30)
turtle.forward(24)
turtle.circle(-4, 180)
turtle.forward(4)
turtle.end_fill()
 
#crown
turtle.pensize(5)
turtle.setheading(0)
turtle.penup()
turtle.pencolor("#E7A910")
turtle.goto(-15, 225)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.circle(-7, 260)
turtle.left(70)
turtle.circle(-11, 180)
turtle.left(52)
turtle.circle(-27, 93)
turtle.left(62)
turtle.circle(-10, 180)
turtle.left(70)
turtle.circle(-7, 260)
turtle.setheading(-135)
turtle.forward(15)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.end_fill()
 
#left hand
turtle.pensize(5)
turtle.penup()
turtle.pencolor("#BB3529")
turtle.goto(-60, -135)
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(150)
turtle.forward(50)
turtle.circle(25,110)
turtle.circle(32,90)
turtle.circle(332,10)
turtle.end_fill()
 
#right hand
turtle.pensize(5)
turtle.penup()
turtle.pencolor("#BB3529")
turtle.goto(80, -125)
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(-30)
turtle.forward(50)
turtle.circle(-25,110)
turtle.circle(-32,90)
turtle.end_fill()
 
#left foot
turtle.pensize(5)
turtle.penup()
turtle.pencolor("#BB3529")
turtle.goto(-62, -224)
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(-70)
turtle.forward(40)
turtle.circle(10,40)
turtle.circle(55,40)
turtle.circle(10,70)
turtle.forward(25)
turtle.end_fill()
 
#right foot
turtle.pensize(5)
turtle.penup()
turtle.pencolor("#BB3529")
turtle.goto(70, -225)
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(-110)
turtle.forward(40)
turtle.circle(-10,40)
turtle.circle(-50,40)
turtle.circle(-10,70)
turtle.forward(25)
turtle.end_fill()
 
#pattern of feet
turtle.pensize(5)
turtle.penup()
turtle.pencolor("#FF9300")
turtle.goto(-50, -255)
turtle.pendown()
turtle.setheading(-20)
turtle.circle(100,27)
 
turtle.pensize(5)
turtle.penup()
turtle.pencolor("#FF9300")
turtle.goto(15, -258)
turtle.pendown()
turtle.setheading(-10)
turtle.circle(80,28)
 
#body
turtle.pensize(5)
turtle.penup()
turtle.pencolor("#BB3529")
turtle.goto(-60, -125)
turtle.fillcolor("#DA2D20")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(-120)
turtle.circle(130,30)
turtle.circle(40,62)
turtle.circle(145,45)
turtle.circle(42,62)
turtle.circle(130,35)
turtle.end_fill()
#tummy
turtle.penup()
turtle.pencolor("white")
turtle.goto(45, -173)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.circle(38,360)
turtle.end_fill()
#logo
turtle.setheading(-138)
turtle.pensize(4)
turtle.penup()
turtle.pencolor("red")
turtle.goto(10, -162)
turtle.pendown()
turtle.forward(12)
 
turtle.setheading(18)
turtle.pencolor("blue")
turtle.forward(22)
 
turtle.setheading(-140)
turtle.pencolor("lightblue")
turtle.forward(34)
 
turtle.setheading(28)
turtle.pencolor("yellowgreen")
turtle.forward(24)
 
turtle.pencolor("yellow")
turtle.circle(-5,200)
 
turtle.pensize(2)
turtle.pencolor("lightblue")
turtle.circle(23,18)
 
turtle.penup()
turtle.setheading(135)
turtle.pencolor("red")
turtle.goto(0, -210)
turtle.pendown()
turtle.circle(-4,150)
 
turtle.penup()
turtle.setheading(175)
turtle.pencolor("blue")
turtle.goto(8, -215)
turtle.pendown()
turtle.circle(-5,120)
 
turtle.penup()
turtle.setheading(245)
turtle.pencolor("green")
turtle.goto(18, -210)
turtle.pendown()
turtle.circle(-4,180)
 
turtle.penup()
turtle.goto(-15, -199)
turtle.pencolor("black")
turtle.pendown()
turtle.write("BEIJING 2022", font=('Arial', 8, 'bold italic'))
turtle.penup()
 
#scarf
turtle.pensize(1)
turtle.penup()
turtle.pencolor("#FF9300")
turtle.goto(-74, -113)
turtle.fillcolor("#FF9300")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(5)
turtle.circle(-1000,3)
turtle.right(10)
turtle.circle(300,19)
turtle.right(30)
turtle.circle(-15,120)
turtle.circle(-100,4)
turtle.right(20)
turtle.circle(-300,25)
turtle.right(20)
turtle.circle(-65,23)
turtle.circle(-15,80)
turtle.end_fill()
 
turtle.pensize(1)
turtle.penup()
turtle.pencolor("#FF9300")
turtle.goto(-57, -135)
turtle.fillcolor("#FF9300")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(-105)
turtle.forward(50)
turtle.circle(5,80)
turtle.forward(28)
turtle.circle(5,100)
turtle.forward(60)
turtle.end_fill()
#lace of scarf
turtle.pensize(3)
turtle.penup()
turtle.pencolor("#DA2D20")
turtle.goto(-61, -175)
turtle.pendown()
turtle.setheading(-105)
turtle.forward(20)
 
turtle.penup()
turtle.pencolor("#DA2D20")
turtle.goto(-54, -178)
turtle.pendown()
turtle.setheading(-105)
turtle.forward(20)
 
turtle.penup()
turtle.pencolor("#DA2D20")
turtle.goto(-47, -181)
turtle.pendown()
turtle.setheading(-105)
turtle.forward(20)
 
turtle.penup()
turtle.pencolor("#DA2D20")
turtle.goto(-40, -184)
turtle.pendown()
turtle.setheading(-105)
turtle.forward(20)

turtle.hideturtle()

turtle.done()