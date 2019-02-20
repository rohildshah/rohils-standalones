import turtle
import time
wn = turtle. Screen()
alex = turtle. Turtle()
alex.speed(0)
turtle.speed(0)
alex.hideturtle()
turtle.hideturtle()
turtle.penup()
turtle.forward(10)
alex.pendown()
alex.forward(300)
alex.back(600)
alex.forward(300)
alex.right(90)
alex.back(300)
alex.forward(600)
alex.back(300)
alex.left(180)
alex.forward(300)
alex.right(180)
a = int(31)
home = 300
while a !=0:
    x_pos = turtle.xcor()
    y_pos = turtle.ycor()
    alex.pendown()
    alex.goto(x_pos, y_pos)
    alex.penup()                #delete this line for darker effect
    alex.goto(0, home)
    turtle.forward(10)
    home = home - 10
    a = a - 1
a = int(31)
home = 300
alex.penup()
alex.goto(home, 0)
turtle.goto(0, -10)
turtle.right(90)
while a !=0:
    x_pos = turtle.xcor()
    y_pos = turtle.ycor()
    alex.pendown()
    alex.goto(x_pos, y_pos)
    alex.penup()                #delete this line for darker effect
    alex.goto(home, 0)
    turtle.forward(10)
    home = home - 10
    a = a - 1
a = int(31)
home = -300
alex.penup()
alex.goto(0, home)
turtle.goto(-10, 0)
turtle.right(90)
while a !=0:
    x_pos = turtle.xcor()
    y_pos = turtle.ycor()
    alex.pendown()
    alex.goto(x_pos, y_pos)
    alex.penup()                #delete this line for darker effect
    alex.goto(0, home)
    turtle.forward(10)
    home = home + 10
    a = a - 1
a = int(31)
home = -300
alex.penup()
alex.goto(home, 0)
turtle.goto(0, 10)
turtle.right(90)
while a !=0:
    x_pos = turtle.xcor()
    y_pos = turtle.ycor()
    alex.pendown()
    alex.goto(x_pos, y_pos)
    alex.penup()                #delete this line for darker effect
    alex.goto(home, 0)
    turtle.forward(10)
    home = home + 10
    a = a - 1
