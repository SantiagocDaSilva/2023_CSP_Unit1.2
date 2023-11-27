# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
t = trtl.Turtle()
import random as rand
score_writer = trtl.Turtle()
import leaderboard as lb
counter = trtl.Turtle()

# -----game configuration----

score = 0
t_color = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "silver"]
t_size = [0.5, 0.75, 1, 1.5, 2, 2.5, 3]
bg_color = ["green", "blue", "purple"]
t_shape = "circle"
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000
timer_up = False

# -----initialize turtle-----
leaderboard_file_name = "leaderboard.py"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name:")

score_writer.speed(0)
score_writer.penup()
score_writer.goto(-250, 250)
score_writer.hideturtle()

counter.speed()
counter.penup()
counter.goto(-300, 350)
counter.hideturtle()


t.speed(0)
t.penup()
t.shape("circle")


# -----game functions--------
def manage_leaderboard():
    global leader_scores_list
    global leader_names_list
    global score
    global t

    # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    # TODO
    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, t, score)

    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, t, score)


def t_clicked(x, y):
    update_score(x, y)
    change_position()
    colorsize()


def change_position():
    new_xpos = rand.randint(-350, 350)
    new_ypos = rand.randint(-300, 300)
    t.goto(new_xpos, new_ypos)


def update_score(x, y):
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
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


def colorsize():
    t.shapesize(rand.choice(t_size))
    t.color(rand.choice(t_color))


# -----events----------------
t.onclick(t_clicked)
wn = trtl.Screen()
wn.bgcolor("white")
wn.ontimer(countdown, counter_interval)
wn.mainloop()

# ------high scores-------------
# 32

