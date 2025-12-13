import turtle
import math

t = turtle.Turtle()
t.color("gray")
radius = int(input("Enter the radius of the Spiral: "))

t.teleport(radius,0)
for i in range(0,361):
    varyingRadius = radius - (radius/360)*i
    if(i%45==0):
        t.teleport(0,0)
        t.setheading(i)
        t.forward(varyingRadius)
        t.backward(varyingRadius)

t.color("purple")
t.teleport(radius,0)
for i in range(0,361):
    varyingRadius = radius - (radius/360)*i
    theta = math.radians(i)
    x = varyingRadius*math.cos(theta)
    y = varyingRadius*math.sin(theta)
    t.goto(x,y)








turtle.done()

