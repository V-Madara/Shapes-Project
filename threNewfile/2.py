import turtle
import math


maj,min=200,140
t = turtle.Turtle()
# t.color("Pink")
t.pendown()

# * Making the Box
t.goto(maj,0)

t.goto(maj,min)
t.right(90)
t.forward(min/2)
t.dot()
t.write("A")
A = t.position()
t.backward(min/2)
t.goto(0,min)
t.left(90)
t.forward(maj/2)
t.dot()
t.write("B")
B = t.position()
t.right(90)
t.forward(min/2)
t.dot()
t.write("O")
O = t.position()
t.teleport(0,min)
t.pendown()
t.goto(0,0)
t.penup()

# *Box Partitions
t.goto(maj/2,0)
t.pendown()
# t.color("Red")
t.goto(maj/2,min)
t.penup()


t.goto(0,min/2)
t.pendown()
t.goto(maj,min/2)
t.penup()
# t.color("green")

# * Making Dots
for i in range(4,9):
    t.goto(0,(min/8)*i)
    t.dot()

# t.color("brown")
for i in range(0,5):
    t.goto((maj/8)*i,min/2)
    t.dot()

# *Making Intersections

t.goto(maj/2,min)
for i in range(4,9):
    t.pendown()
    t.goto(0,min/8*i)
    t.penup()
    t.goto(maj/2,min)

t.goto(maj/2,0)
for i in range(0,5):
    t.pendown()
    head = t.towards((maj/8)*i,min/2)
    t.goto((maj/8)*i,min/2)
    t.setheading(head)
    t.forward(100)
    t.penup()
    t.goto(maj/2,0)
    


#! Finding Intersectons
t.color("red")
t.penup()
t.goto(4,448/5)
t.dot()
t.goto(20,112)

t.dot()
t.goto(6300/119,4480/34)
t.dot()
t.goto(100,140)
t.dot()

#? Making Curve 

t.goto(O)
print(O)
radius_x = t.distance(A)
radius_y = t.distance(B)

t.pendown()
steps = 120
# t.teleport(maj,min/2)
for i in range(steps + 1):
    
    angle = i * 360 / steps
    t.setheading(angle)
    dx = radius_x * math.cos(math.radians(angle))
    dy = radius_y * math.sin(math.radians(angle))
    t.goto(-(dx-O[0]), (O[1] + dy))

turtle.done()