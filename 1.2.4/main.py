import turtle as drawer
'''
x = starting distance
y = incremental distance

In a loop:
    1. go forward x
    2. turn left 90 degrees
    3. go forward x + y
    2. turn left 90 degrees
'''
def drawSpiral():
    drawer.speed(0)
    x = 10
    y = 10
    for step in range(25):
        drawer.left(90)
        drawer.forward(x+y)
        y += 10
        drawDoor()
        drawer.hideturtle()
def drawDoor():
    drawer.speed(0)
    drawer.forward(10)
    drawer.penup()
    drawer.forward(6 * 2)
    drawer.pendown()



drawSpiral()

