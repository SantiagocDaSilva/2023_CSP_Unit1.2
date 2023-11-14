# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
t = trtl.Turtle()
import random as rand
score_writer = trtl.Turtle()

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  trtl.Turtle()


#-----game configuration----
t_shape = "arrow"
t_color = "red"
t_shapesize = 5
score = 0
font_setup = ("Arial", 20, "normal")


#-----initialize turtle-----
t.shape(t_shape)
t.shapesize(t_shapesize)
t.fillcolor(t_color)

score_writer.penup()
score_writer.goto(-150,200)
score_writer.hideturtle()

counter.penup()
counter.goto(150,200)

#-----game functions--------
def t_clicked(x,y):
    change_position()
    update_score()
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


def change_position():
    t.penup()
    new_xpos = rand.randint(-350,300)
    new_ypos = rand.randint(300, 300)
    t.goto(new_xpos, new_ypos)



#-----events----------------
t.onclick(t_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()