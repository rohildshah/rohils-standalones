import time         #importing time for rest
import turtle       #importing turtle for drawing
from random import randint      #importing random for variables
print("This is a graphing calculator")  #intro
time.sleep(1)
unit_val = input("Please enter the unit value: ")     #asking for the value between each segment in a graph
unit_val = int(unit_val)
time.sleep(1)
print("The graphing will now begin. ")
wn = turtle. Screen()
alex = turtle. Turtle()
turtle.penup()
alex.pendown()
alex.speed(0)
turtle.speed(0)
#we want the turtle's speed to be set to 0(the fastest) for the final product
#segment one: bare axes with arrows
alex.pendown()
alex.forward(300)
alex.back(600)
alex.forward(300)
alex.left(90)
alex.forward(300)
alex.back(600)
alex.forward(300)  #end of building axes, arrows after this
alex.left(90)
alex.forward(300)
alex.penup()
alex.forward(10)
alex.right(135)
alex.pendown()
alex.forward(15)
alex.back(15)
alex.right(90)
alex.forward(15)
alex.back(15)
alex.left(45)       #first arrow done(left)
alex.penup()
alex.forward(620)
alex.right(135)
alex.pendown()
alex.forward(15)
alex.back(15)
alex.right(90)
alex.forward(15)
alex.back(15)
alex.left(45)      #second arrow completed(right)
alex.penup()
alex.forward(310)
alex.right(90)
alex.forward(310)
alex.right(135)
alex.pendown()
alex.forward(15)
alex.back(15)
alex.right(90)
alex.forward(15)
alex.back(15)
alex.left(45)       #third arrow completed(top)
alex.penup()
alex.forward(620)
alex.right(135)
alex.pendown()
alex.forward(15)
alex.back(15)
alex.right(90)
alex.forward(15)
alex.back(15)
alex.left(45)       #fourth arrow completed(last and bottom)
alex.penup()
alex.forward(310)
alex.pendown()
#segment two: dashes on all lines w/ numbers
dash_amnt = 10
while dash_amnt != 0:
    dash_amnt = dash_amnt - 1
    alex.forward(30)
    alex.right(90)
    alex.forward(5)
    alex.back(10)
    alex.forward(5)
    alex.left(90)             #top dashes done
dash_amnt = 10
alex.back(300)
alex.right(90)
while dash_amnt !=0 :
    dash_amnt = dash_amnt - 1
    alex.forward(30)
    alex.right(90)
    alex.forward(5)
    alex.back(10)
    alex.forward(5)
    alex.left(90)             #right dashes done
dash_amnt = 10
alex.back(300)
alex.right(90)
while dash_amnt !=0 :
    dash_amnt = dash_amnt - 1
    alex.forward(30)
    alex.right(90)
    alex.forward(5)
    alex.back(10)
    alex.forward(5)
    alex.left(90)              #bottom dashes done
dash_amnt = 10
alex.back(300)
alex.right(90)
while dash_amnt !=0 :
    dash_amnt = dash_amnt - 1
    alex.forward(30)
    alex.right(90)
    alex.forward(5)
    alex.back(10)
    alex.forward(5)
    alex.left(90)
alex.penup()
alex.right(180)
alex.forward(300)
alex.left(90)
#segment three: all numbers on dashes using unit_val
dash_amnt = int(0)
while dash_amnt !=10 :
    dash_amnt = dash_amnt + 1
    alex.penup()
    alex.forward(22)
    alex.left(90)
    alex.forward(15)
    alex.right(180)
    temp_numb = (dash_amnt*unit_val)
    alex.write(temp_numb, False, align="right", font=("Times New Roman", 12, "normal"))
    alex.forward(15)
    alex.left(90)
    alex.forward(8)         #done with top numbers
alex.back(300)
alex.right(90)
dash_amnt = int(0)
while dash_amnt !=10 :
    dash_amnt = dash_amnt + 1
    alex.penup()
    alex.forward(26)
    alex.left(90)
    alex.forward(10)
    alex.right(180)
    temp_numb = (dash_amnt*unit_val)
    alex.write(temp_numb, False, align="left", font=("Times New Roman", 12, "normal"))
    alex.forward(10)
    alex.left(90)
    alex.forward(4)           #done with right numbers
alex.back(300)
alex.right(90)
dash_amnt = int(0)
while dash_amnt !=10 :
    dash_amnt = dash_amnt + 1
    alex.penup()
    alex.forward(37)
    alex.left(90)
    alex.forward(15)
    alex.right(180)
    temp_numb = (dash_amnt*unit_val)
    temp_numb = temp_numb - (2*temp_numb)
    alex.write(temp_numb, False, align="left", font=("Times New Roman", 12, "normal"))
    alex.forward(15)
    alex.left(90)
    alex.back(7)           #done with bottom numbers
alex.back(300)
alex.right(90)
dash_amnt = int(0)
while dash_amnt !=10 :
    dash_amnt = dash_amnt + 1
    alex.penup()
    alex.forward(33)
    alex.left(90)
    alex.forward(20)
    alex.right(180)
    temp_numb = (dash_amnt*unit_val)
    temp_numb = temp_numb - (2*temp_numb)
    alex.write(temp_numb, False, align="left", font=("Times New Roman", 12, "normal"))
    alex.forward(20)
    alex.left(90)
    alex.back(3)           #done with left numbers
#segment four: input for graph
print("The graph has now been created")
time.sleep(1)
print("This will only graph equations in slope-intercept form, or y=mx+b")
time.sleep(1)
top_m_val = input("Please enter the top value of 'm', or the rise: ")
bottom_m_val = input("Please enter the bottom value of 'm' or the run: ")
top_m_val = int(top_m_val)
bottom_m_val = int(bottom_m_val)
b_val = input("Please enter the value of 'b', or the y-intercept: ")
b_val = int(b_val)
#segment five: graph y-intercept
get_pix = 30/unit_val        #finding ratio between numbers on graph and pixels
y_int_pix = get_pix*b_val
alex.penup()
alex.goto(0, y_int_pix)
alex.right(180)
#segment six: find next point
bottom_m_val_pix = get_pix*bottom_m_val
top_m_val_pix = get_pix*top_m_val
turtle.forward(bottom_m_val_pix)
turtle.left(90)
rise_from_bottom = y_int_pix + top_m_val_pix
turtle.forward(rise_from_bottom)
#segment seven: draw line(yay finally)
a = 10
while a != 0:
    x_pos = turtle.xcor()
    y_pos = turtle.ycor()
    alex.pendown()
    alex.goto(x_pos, y_pos)
    turtle.right(90)
    turtle.forward(bottom_m_val_pix)
    turtle.left(90)
    turtle.forward(top_m_val_pix)
    a = a - 1
a = 10
turtle.left(90)
alex.penup()
alex.goto(0, y_int_pix)
turtle.goto(0, y_int_pix)
while a != 0:
    turtle.forward(bottom_m_val_pix)
    turtle.left(90)
    turtle.forward(top_m_val_pix)
    x_pos = turtle.xcor()
    y_pos = turtle.ycor()
    alex.pendown()
    alex.goto(x_pos, y_pos)
    turtle.right(90)
    a = a - 1
