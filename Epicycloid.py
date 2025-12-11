import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("gray")

radiusSmall = 50
radiusBig = 100
posC = []

t.teleport(0,-100)
t.circle(radiusBig)

# Making Smaller Circles
t.teleport(0,100)
t.circle(radiusSmall)
t.teleport(0,radiusBig+radiusSmall)
t.dot("red")
posC.append(t.position())
t.write("C1",font=("Arial",8,"bold"))

t.teleport(0,0)
t.setheading(-30)
t.penup()
t.forward(radiusBig+radiusSmall)
t.dot("red")
posC.append(t.position())
t.write("C2",font=("Arial",8,"bold"))
t.backward(radiusSmall)
t.pendown()
t.setheading(60)
t.circle(-radiusSmall)
t.penup()
t.teleport(0,0)
t.setheading(200)
t.forward(radiusBig+radiusSmall)
t.dot("red")
posC.append(t.position())
t.write("C3",font=("Arial",8,"bold"))
t.backward(radiusSmall)
t.pendown()
t.setheading(-60)
t.circle(-radiusSmall)
t.teleport(0,0)


#* Making Outline of the First Quadrant Circle

#? upper border
t.setheading(0)
t.teleport(0,radiusBig+2*radiusSmall)
t.circle(-(radiusBig+2*radiusSmall),120)
#? middle border
t.setheading(0)
t.teleport(0,radiusBig+radiusSmall)
t.circle(-(radiusBig+radiusSmall),120)

#? Middle Circle
t.penup()
t.teleport(0,0)
t.setheading(30)
t.forward(radiusBig+radiusSmall)
t.dot("red")
posC.append(t.position())
t.write("C4",font=("Arial",8,"bold"))
t.backward(radiusSmall)
t.pendown()
t.setheading(-60)
t.circle(radiusSmall)
t.teleport(0,0)

#? Now Diving the Circle C1
posYC1 = []
for i in range(0,6):
    t.setheading(30*i)
    t.teleport(posC[0][0],posC[0][1])
    t.forward(radiusSmall)
    posYC1.append(t.position()[1])
    t.backward(2*radiusSmall)
    posYC1.append(t.position()[1])

for i in range(0,6):
    t.setheading(30*i)
    t.teleport(posC[1][0],posC[1][1])
    t.forward(radiusSmall)
    t.backward(2*radiusSmall)

#? Making Lines
posYC1.sort()
# print(posYC1)

for i in range(0,12):
    t.setheading(0)
    t.teleport(0,posYC1[i])
    t.circle(-(posYC1[i]),120)

for i in range(0,13):
    t.teleport(0,0)
    t.setheading(10*i-30)
    t.penup()
    t.forward(radiusBig)
    t.pendown()
    t.forward(2*radiusSmall)

# ? Points Labeling
t.teleport(0,radiusBig)
t.dot("red")
t.write("P1")
t.teleport(0,0)
t.setheading(30)
t.penup()
t.forward(radiusBig+2*radiusSmall)
t.pendown()
t.dot("red")
t.write("P2")
t.teleport(0,0)
t.setheading(-30)
t.penup()
t.forward(radiusBig)
t.pendown()
t.dot("red")
t.write("P3")



#! Curve tracing
t.teleport(0,radiusBig)
t.pensize(3)
t.color("purple")
for i in range(0,61):
    r = radiusBig + (radiusSmall/30)*i
    theta = math.radians(i)
    gx = r*math.sin(theta)
    gy = r*math.cos(theta)
    t.goto(gx,gy)

for i in range(60,-1,-1):
    r = radiusBig + (radiusSmall/30)*i
    theta = math.radians(60+i)
    gx = r*math.sin(theta)
    gy = -r*math.cos(theta)
    t.goto(gx,gy)





t.hideturtle()
turtle.done()