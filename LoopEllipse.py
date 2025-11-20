import turtle
import math


maj,min = 200,140

t = turtle.Turtle()
t.speed(0.5)

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
t.speed(1.2)

print(small)
print(big)
t.color("red")
for i in range(1,6,2):
    x , y = small[i-1]
    X , Y = big[i-1]
    per= 30*math.cos(30*i)
    cood_y = Y+per
    t.teleport(X,cood_y)
    t.dot()




turtle.done()