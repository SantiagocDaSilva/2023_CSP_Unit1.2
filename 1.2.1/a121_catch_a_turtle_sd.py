# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
t = trtl.Turtle()
import random as rand

#-----game configuration----
t_shape = "arrow"
t_color = "red"
t_shapesize = 5
global score = 0
speed = 0


#-----initialize turtle-----
t.shape(t_shape)
t.shapesize(t_shapesize)
t.fillcolor(t_color)

#-----game functions--------
def t_clicked(x,y):
    change_position()
def update_score():


def change_position():
    t.penup()
    new_xpos = rand.randint(-350,300)
    new_ypos = rand.randint(300, 300)
    t.goto(new_xpos, new_ypos)



#-----events----------------
t.onclick(t_clicked)


wn = trtl.Screen()
wn.mainloop()