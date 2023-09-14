import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def background():
    s.bgcolor("#84F3F7")
    t.goto(-300, 0)
    t.pendown()
    t.color("#68F520")
    t.begin_fill()
    t.goto(300, 0)
    t.goto(300, -300)
    t.goto(-300, -300)
    t.goto(-300, 0)
    t.end_fill()
    t.penup()

def tree_trunck():
    t.goto(-90, 0)
    t.pendown()
    t.color("#C66A08")
    t.begin_fill()
    t.goto(-50, 0)
    t.goto(-50, 170)
    t.goto(-90, 170)
    t.end_fill()
    t.penup()

def tree_leaves():
    t.goto(-110, 170)
    t.color("#3B8F07")
    t.dot(80)
    t.goto(-70, 190)
    t.dot(80)
    t.goto(-30, 170)
    t.dot(80)

def sun():
    t.goto(300, 300)
    t.color("yellow")
    t.dot(120)


def cloud(cx, cy):
    t.goto(cx-40, cy-20)
    t.color("white")
    t.dot(90)
    t.goto(cx, cy)
    t.dot(90)
    t.goto(cx+40, cy-20)
    t.dot(90)

def main():
    t.penup()
    background()
    tree_trunck()
    tree_leaves()
    sun()
    cloud(90, 260)

main()