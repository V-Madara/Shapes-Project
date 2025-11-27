import turtle
import math


maj,min = 200,140

t = turtle.Turtle()
t.speed(1)

t.teleport(0,-min/2)
t.circle(min/2)
t.teleport(0,-maj/2)
t.circle(maj/2)
t.goto(0,maj/2)
t.teleport(-maj/2,0)
t.goto(maj/2,0)

t.teleport(0,0)
bch = 'A'
big = []
for i in range(1,6):
    t.setheading(30*(i))
    t.penup()
    t.goto(0,0)
    t.forward(-maj/2)
    t.dot()
    
    #Bottom Outward Lines
    if 90<30*i<180:
        t.setheading(90)
        t.pendown()
        t.forward(min/3)
        t.penup()
        t.forward(-min/3)
    else:
        t.setheading(90)
        t.pendown()
        if(30*i != 90):
            t.forward(min/3)
            t.penup()
            t.forward(-min/3)
    t.setheading(30*i)


    t.write(chr(ord(bch)+(i)),font=("Arial",8,"bold"))
    big.append(t.position())
    t.pendown()
    t.forward(maj)
    t.dot()

    # Top  Outward lines
    if 0 < 30*i < 90:
        t.setheading(90)
        t.pendown()
        t.forward(-min/3)
        t.penup()
        t.forward(min/3)
    else:
        t.setheading(90)
        t.pendown()
        if(30*i != 90):
            t.forward(-min/3)
            t.penup()
            t.forward(min/3)
    t.setheading(30*i)
    t.write(chr(ord(bch)+(i+5)),font=("Arial",8,"bold"))
    big.append(t.position())

t.penup()
small = []
sch = 'a'
for i in range(1,6):

    t.setheading(30*i)
    t.teleport(0,0)
    t.forward(-min/2)
    t.dot()

    #Bottom Outward Lines
    t.setheading(0)
    if 90<30*i<180:
        t.pendown()
        t.forward(min/2)
        t.penup()
        t.forward(-min/2)
    else:
        t.setheading(0)
        t.pendown()
        if(30*i != 90):
            t.forward(-min/2)
            t.penup()
            t.forward(min/2)
    t.setheading(30*i)

    t.write(chr(ord(sch)+(i-1)),font=("Arial",8,"bold"))
    small.append(t.position())
    t.forward(min)
    t.dot()

    t.setheading(0)
    # Top  Outward lines
    if 0 < 30*i < 90:
        t.pendown()
        t.forward(min/2)
        t.penup()
        t.forward(-min/2)
    else:
        t.setheading(180)
        t.pendown()
        if(30*i != 90):
            t.forward(min/2)
            t.penup()
            t.forward(-min/2)
    t.setheading(30*i)

    t.write(chr(ord(sch)+(i+4)),font=("Arial",8,"bold"))
    small.append(t.position())
    t.penup()

# Marking Points
t.color("red")
for i in range(0,10):
    t.teleport((big[i])[0],(small[i])[1])
    t.dot()

turtle.speed(1)
t.teleport(-maj/2,0)
t.pensize(2)
t.pendown()
for i in range(-100,0):
    t.goto(i,(math.sqrt(math.pow(min/2,2)*(1-(math.pow(i,2)/math.pow(maj/2,2))))))
    # t.dot()

for i in range(0,100):
    t.goto(i,math.sqrt((70*70)*(1-((i*i)/(100*100)))))
    # t.dot()

for i in range(100,0,-1):
    t.goto(i,-math.sqrt((70*70)*(1-((i*i)/(100*100)))))
    # t.dot()

for i in range(0,100):
    t.goto(-i,-math.sqrt((70*70)*(1-((i*i)/(100*100)))))
    # t.dot()
t.goto(-maj/2,0)

turtle.hideturtle()

turtle.done()
