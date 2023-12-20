import turtle as trtl
import random as rand

wn = trtl.Screen()
drawer = trtl.Turtle()
path_width = 20
numBarriers = 30
wall_len = 15
door_width = 30


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
    drawer.forward(10)
    drawer.penup()
    drawer.forward(path_width * 2)
    drawer.pendown()


def drawBarriers():
    drawer.speed()
    drawer.left(90)
    drawer.forward(path_width)
    drawer.backward(path_width)
    drawer.right(90)


def randomBarriers():
    for w in range(numBarriers):
        if w < numBarriers - 5:
            door = rand.randint(path_width*2, (wall_len - path_width*2))
            barrier = rand.randint(path_width * 2, (wall_len - path_width * 2))


drawSpiral()
