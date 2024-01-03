#   a123_apple_1.py
import turtle as trtl
import random as rand

# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
pear_image = "pear.gif"
L = ""
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")
Letters = ["a", "b", "d", "f", "g", "h", "j", "k", "l"]
random_index = 0
apple = trtl.Turtle()
drawer = trtl.Turtle()
drawer.hideturtle()


# -----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_pear(active_pear):
    active_pear.shape(pear_image)
    wn.update()


def draw_apple(active_apple):
    active_apple.shape(apple_image)
    wn.update()


x = 0
y = 0
on = 1
int = 0


def reset_apple():
    global x, y, int
    apple.showturtle()
    int = rand.randint(-100, 100)
    apple.goto(int, 0)
    x = int
    y = 0
    choose_random_letter()
    draw_the_letter()


def apple_fall():
    drawer.clear()
    global x, y, on
    while (on == 1):
        if y == -170:
            apple.hideturtle()
            on = 0
            reset_apple()
        apple.penup()
        apple.goto(x, y)
        y -= 2


def draw_the_letter():
    drawer.color("white")
    drawer.write(L, font=("Arial", 50, "bold"))


def choose_random_letter():
    global random_index, L
    random_index = rand.randint(0, len(Letters) - 1)
    L = Letters[random_index]
    Letters.pop(random_index)


# -----function calls-----
draw_apple(apple)
drawer.penup()
drawer.goto(-20, -40)
choose_random_letter()
draw_the_letter()
wn.onkeypress(apple_fall, L)

wn.listen()
wn.mainloop()
