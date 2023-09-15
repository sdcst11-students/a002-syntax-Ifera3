import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def background():
    s.bgcolor("#84F3F7")
    t.goto(-400, 0)
    t.pendown()
    t.color("#68F520")
    t.begin_fill()
    t.goto(400, 0)
    t.goto(400, -400)
    t.goto(-400, -400)
    t.goto(-400, 0)
    t.end_fill()
    t.penup()

def tree_trunck():
    t.goto(-90, -10)
    t.pendown()
    t.color("#C66A08")
    t.begin_fill()
    t.goto(-50, -10)
    t.goto(-50, 170)
    t.goto(-90, 170)
    t.end_fill()
    t.penup()

def tree_leaves():
    t.goto(-100, 170)
    t.color("#3B8F07")
    t.dot(100)
    t.goto(-70, 190)
    t.dot(100)
    t.goto(-40, 170)
    t.dot(100)

def sun():
    t.goto(300, 300)
    t.color("yellow")
    t.dot(120)
    t.goto(230, 300)
    t.pendown()
    t.pensize(5)
    t.goto(190, 300)
    t.penup()
    t.goto(250, 250)
    t.pendown()
    t.goto(220, 220)
    t.penup()
    t.goto(300, 230)
    t.pendown()
    t.goto(300, 190)
    t.penup()
    t.pensize(1)

def cloud(cx, cy):
    t.goto(cx-30, cy-20)
    t.color("white")
    t.dot(90)
    t.goto(cx, cy)
    t.dot(90)
    t.goto(cx+30, cy-20)
    t.dot(90)
    t.goto(cx+60, cy)
    t.dot(90)

def main():
    t.penup()
    background()
    tree_trunck()
    tree_leaves()
    sun()
    cloud(90, 260)
    cloud(-200, 290)

main()