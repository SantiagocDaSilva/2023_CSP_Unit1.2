import turtle as trtl
import random as rand

wn = trtl.Screen()
drawer = trtl.Turtle()
path_width = 22
wall_len = 8
door_width = 30
test = 200

def drawSpiral():
    drawer.speed(0)
    x = 10
    y = 10
    for step in range(25):
        drawer.left(90)
        drawer.forward(x + y)
        y += 10
        drawBarriers()
        drawDoors()
        drawer.hideturtle()


def drawDoors():
    drawer.speed(0)
    drawer.penup()
    drawer.forward(path_width)
    drawer.pendown()


def drawBarriers():
    drawer.speed()
    drawer.right(90)
    drawer.forward(wall_len*2)
    drawer.backward(wall_len*2)
    drawer.left(90)


for w in range(25):
    if w < 17:
        door = rand.randint(0,test/2)
        barrier = rand.randint(wall_len * 2, test - path_width * 2)
        if door < barrier:
            drawer.forward(door)
            drawDoors()
            drawer.forward(barrier - door - path_width)
            drawBarriers()
            drawer.forward(test - barrier)
        else:
            drawer.forward(barrier)
            drawBarriers()
            drawer.forward(door-barrier)
            drawDoors()
            drawer.forward(test - path_width - door)
        drawer.right(90)
        test = test - 8
drawSpiral()
