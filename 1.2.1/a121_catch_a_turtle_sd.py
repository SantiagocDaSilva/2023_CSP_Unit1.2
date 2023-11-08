# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
t = trtl.Turtle()
import random as rand

#-----game configuration----
t_shape = "arrow"
t_color = "red"
t_shapesize = 5
new_xpos = 1
new_ypos = 100

#-----initialize turtle-----
t.shape(t_shape)
t.shapesize(t_shapesize)
t.fillcolor(t_color)

#-----game functions--------
def t_clicked(x,y):
    change_position()
def change_position():
    rand.randint(1,100)
    new_xpos = rand.randint(1,100)
    new_ypos =rand.randint(1,100)
    t.goto(new_xpos,new_xpos)





#-----events----------------
t.onclick(t_clicked)


wn = trtl.Screen()
wn.mainloop()