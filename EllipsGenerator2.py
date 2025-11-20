import turtle


maj,min = 200,140

t = turtle.Turtle()

t.penup()
t.goto(0,-min/2)
t.pendown()
t.circle(min/2)
t.penup()
t.goto(0,-maj/2)
t.pendown()
t.circle(maj/2)
t.goto(0,maj/2)
t.penup()
t.goto(-maj/2,0)
t.pendown()
t.goto(maj/2,0)

t.penup()
t.goto(0,0)
# t.penup()
for i in range(1,6):
    t.setheading(30*i)
    t.penup()
    t.goto(0,0)
    t.forward(-maj/2)
    t.pendown()
    t.forward(maj)

t.penup()
for i in range(1,6):
    t.setheading(30*i)
    t.goto(0,0)
    t.forward(-min/2)
    t.pendown()
    t.setheading(180)
    t.forward(-min)
    t.penup()
    t.forward(min)
    t.pendown()
    t.forward(min)
    t.penup()






turtle.done()