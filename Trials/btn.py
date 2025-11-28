import turtle
import random

t = turtle.Turtle()
scr = turtle.Screen()

for i in range(2):
    t.forward(80)
    t.left(90)
    t.forward(30)
    t.left(90)

t.teleport(7,8)
t.write("Click me!",font=("Arial",12,"normal"))

def show_pos(x,y):
    print(x,y)

scr.onclick(show_pos)
scr.listen()

rdm = [1,-1,0]

def click(x,y):
    t.forward(70)
    t.left(random.choice(rdm)*90)
    t.forward(40)

t.onclick(click)


turtle.hideturtle()
turtle.done()