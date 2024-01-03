import turtle as trtl
import random as rand

# maze configuration variables
num_sides = 25
path_width = 15
wall_color = "black"

# config maze
maze_painter = trtl.Turtle()
maze_painter.pensize(5)
maze_painter.pencolor(wall_color)
maze_painter.speed("fastest")


def drawSpiral():
    wall_len = path_width
    for w in range(num_sides):
        wall_len += path_width

        if w > 4:
            randomNum = rand.randint(0, 1)
            # Initial turn for painter to be in the correct direction
            maze_painter.left(90)

            if randomNum == 1:
                # Draw the door
                draw_door()
                # Draw the barrier
                draw_barrier()
            else:
                # Draw the barrier
                draw_barrier()
                # Draw the door
                draw_door()

            # Remember: you have to subtract the amount you drew for the wall and
            # barrier to avoid making the walls bigger.


def draw_door():
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()


def draw_barrier():
    # draw barrier wall
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.backward(path_width * 2)
    maze_painter.right(90)


drawSpiral()
maze_painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
