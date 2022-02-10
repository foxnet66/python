import turtle

turtle.title('Python Olympic Logos')

# The Olympic Logos And Symbols Colors with Hex & RGB Codes has 5 colors 
# which are:
# NCS Blue      (#0085C7)
# Golden Poppy  (#F4C300)
# Black         (#000000)
# Pantone Green (#009F3D) 
# Cadmium Red   (#DF0024)

turtle.speed(50)  # speed

# Olympic rings
turtle.width(10)
turtle.pencolor("#0085C7") # NCS Blue
turtle.penup()
turtle.goto(-120, 0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("#000000") # Black
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(50)


turtle.pencolor("#DF0024") # Cadmium Red
turtle.penup()
turtle.goto(120, 0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("#F4C300") # Golden Poppy
turtle.penup()
turtle.goto(-60, -50)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("#009F3D") # Pantone Green
turtle.penup()
turtle.goto(60, -50)
turtle.pendown()
turtle.circle(50)

turtle.done()
