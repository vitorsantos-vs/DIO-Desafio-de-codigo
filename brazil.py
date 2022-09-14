import turtle

obj=turtle.Turtle()
obj.speed(3)

win=turtle.Screen()
win.bgcolor("white")

obj.pencolor("seagreen")

obj.penup()
obj.goto(-100,200)
obj.pendown()
obj.begin_fill()
obj.fillcolor("seagreen")
obj.setheading(0)
obj.forward(300)
obj.setheading(270)
obj.forward(200)
obj.setheading(180)
obj.forward(300)
obj.setheading(90)
obj.forward(200)
obj.end_fill()

obj.setheading(270)
obj.forward(180)
obj.setheading(360)

obj.penup()
obj.forward(150)
obj.pendown()

obj.begin_fill()
obj.fillcolor("yellow")
obj.setheading(142)
obj.forward(120)
obj.setheading(40)
obj.forward(120)

obj.setheading(-40)
obj.forward(120)
obj.setheading(-141)
obj.forward(117)
obj.end_fill()



obj.penup()
obj.setheading(141)
obj.forward(70)


obj.setheading(90)
obj.forward(30)
obj.pendown()

obj.begin_fill()
obj.fillcolor("#002776")
obj.circle(-50)
obj.end_fill()
obj.penup()
obj.setheading(345)
obj.forward(95)
obj.pendown()
obj.setheading(120)
obj.pencolor("white")
obj.pensize(10)
obj.circle(70,85)
obj.penup()
obj.pensize(8)
obj.forward(105)
obj.pendown()

obj.begin_fill()
obj.fillcolor("seagreen")

obj.setheading(90)
obj.pencolor("seagreen")
obj.forward(200)
obj.setheading(180)
obj.forward(10)
obj.setheading(270)
obj.forward(500)


obj.setheading(180)
obj.forward(80)
obj.setheading(270)
obj.forward(20)
obj.setheading(360)
obj.forward(180)

obj.setheading(90)
obj.forward(20)
obj.setheading(180)
obj.forward(90)
obj.setheading(90)
obj.forward(500)

obj.end_fill()
obj.hideturtle()

turtle.done()