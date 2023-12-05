# -----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
t=trtl.Turtle()
score_writer = trtl.Turtle()
# -----game configuration-----
# To view in trinket change the values of font_size, spot_size, and
# screen_size by half
colors = ["black", "sky blue", "salmon", "orchid", "pale green"]
font_setup = ("Arial", 20, "normal")
t_size = 2
t_color = 'pink'
t_shape = "turtle"

# Changed from 30 to 5 for testing purposes
#timer = 30
timer = 15

counter_interval = 1000
timer_up = False
score = 0
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("What is your name?")

# -----initialize the turtles-----
t = trtl.Turtle()
t.shape(t_shape)
t.shapesize(t_size)
t.fillcolor(t_color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(160, 160)  # x,y set to fit on smaller screen
score_writer.pendown()
# score_writer.showturtle()

counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-160, 160)  # x,y set to fit on smaller screen
counter.pendown()


# counter.showturtle()

# -----game functions-----

# countdown function
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

    # update and display the score


def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)


# what happens when the spot is clicked
def t_clicked(x, y):
    global timer_up
    if (not timer_up):
        update_score()
        change_position()
    else:
        t.hideturtle()


# resize the turtle
def resize():
    sizes = [.5, 1, 1.5, 2]
    t.shapesize(rand.choice(sizes))


# stamp turtle
def leave_a_mark():
    t.fillcolor(rand.choice(colors[1:]))
    t.stamp()
    t.fillcolor(colors[0])  # comment out for more a more difficult game


# change the position of spot
def change_position():
    leave_a_mark()  # challenge to add color
    resize()  # challenge to change size of turtle
    new_xpos = rand.randint(-150, 150)  # x,y set to fit on smaller screen
    new_ypos = rand.randint(-150, 150)  # x,y set to fit on smaller screen
    t.penup()  # 2nd step in moving
    t.hideturtle()  # 3rd step in moving
    t.goto(new_xpos, new_ypos)  # 1st step in moving
    t.showturtle()
    t.pendown()


# manages the leaderboard for top 5 scorers
def manage_leaderboard():
    global score
    global t

    # get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)

    # show the leaderboard with or without the current player
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, t, score)

    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, t, score)


# starting the game
def start_game():
    t.onclick(t_clicked)
    counter.getscreen().ontimer(countdown, counter_interval)


# ----------events----------
start_game()
wn = trtl.Screen()
wn.bgcolor("white smoke")
wn.mainloop()