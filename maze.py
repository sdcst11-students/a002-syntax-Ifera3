import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.bgpic('maze.gif')
t.pensize(10)
t.color("#5F5F5F")

xlist = [-206,-160,-160,-206,-206,-70,-70,-20,-20,-70,-70,20,20,70,70,206,206,160,160,120,120,208,208,265,265,-206]
ylist = [0,0,-45,-45,-90,-90,-45,-45,45,45,90,90,45,45,90,90,45,45,-45,-45,-90,-90,-150,-150,150,150]

t.penup()
t.goto(-206, 150)
t.pendown()
if len(xlist)==len(ylist):
    for i in range(len(xlist)):
        t.goto(xlist[i], ylist[i])
