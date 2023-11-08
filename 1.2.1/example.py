import turtle as trtl
test = trtl.Turtle()
def drawTriangle():
    test.pendown()
    test.fd(100)
    test.right(120)
    test.fd(100)
    test.right(120)
    test.fd(100)

def drawTriangle(long,x,y):
    test.penup()
    test.goto(x,y)
    test.pendown()
    test.fd(long)
    test.right(120)
    test.fd(long)
    test.right(120)
    test.fd(long)

x = 100
y = 100
length = 43
for tri in range(100):
    drawTriangle(length,x,y)
    x += length * 1.25
    y += length * 1.25
    length += 1



wn = trtl.Screen()
wn.mainloop()