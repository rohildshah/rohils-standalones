import time
import turtle
print("\nThis is a drawing simulator")
time.sleep(0.75)
print("\nYou will be able to draw anything you want")
time.sleep(0.75)
print("\nControls:\nW, then enter to go forward\nA, then enter to turn left\nS, then enter to go backwards\nD, then enter to turn right\nQ, then enter for pen up\nE, then enter for pen down\n\nTo change the color of the pen, type it in, and press enter(make sure that your pen is down)\n\nTo change the width of the pen, type in a number and press enter(The larger the number, the thicker it is)\n\nPress Z, then enter for undo")
time.sleep(10)
print("\n\n--------------------------------------------------------------------------\n")
time.sleep(3)
print("\nThe actual drawing simualtor will pop up soon.\n\nTo enter in all of the commands, do it on this window, not the drawing simulator window.\n\nAlso, it might help if you keep both of the windows side by side. \n\n To exit, type in exit.")
time.sleep(5)
a = 3
while a != 0:
    a = a - 1
    print("\nLoading...")
    time.sleep(0.5)
time.sleep(1)
wn = turtle.Screen()
alex = turtle. Turtle()
turtle.colormode(255)
time.sleep(1)
print("\nGo ahead and start drawing")
alex.pendown()
a = 7
b = 7
while a == b:
    key = input()
    if key == "w":
        alex.forward(100)
    elif key == "a":
        alex.left(90)
    elif key == "s":
        alex.back(100)
    elif key == "d":
        alex.right(90)
    elif key == "q":
        alex.penup()
    elif key == "e":
        alex.pendown()
    elif key == "z":
        alex.undo()
    elif key == "red":
        alex.pencolor(255, 0, 0)
    elif key == "orange":
        alex.pencolor(255, 165, 0)
    elif key == "yellow":
        alex.pencolor(255, 255, 0)
    elif key == "green":
        alex.pencolor(0, 255, 0)
    elif key == "blue":
        alex.pencolor(0, 0, 255)
    elif key == "purple":
        alex.pencolor(160, 32, 240)
    else:
        alex.pensize(key)
    if key == "exit":
        turtle.bye()
        return
