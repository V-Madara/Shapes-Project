import turtle
import math


maj,min=200,140
t = turtle.Turtle()
t.color("Pink")
t.pendown()

# * Making the Box
t.goto(maj,0)
t.goto(maj,min)
t.goto(0,min)
t.goto(0,0)
t.penup()

# *Box Partitions
t.goto(maj/2,0)
t.pendown()
t.color("Red")
t.goto(maj/2,min)
t.penup()


t.goto(0,min/2)
t.pendown()
t.goto(maj,min/2)
t.penup()
t.color("green")

# * Making Dots
for i in range(4,9):
    t.goto(0,(min/8)*i)
    t.dot()

t.color("aqua")
for i in range(0,5):
    t.goto((maj/8)*i,min/2)
    t.dot()

# *Making Intersections











turtle.done()