import turtle
import math

t = turtle.Turtle();



x = 12
y= 16

t.goto((x+2)*(y+2),0)
t.teleport(0,0)
t.goto(0,(x+2)*(y+2))
t.teleport(x*5,y*5)
t.dot()
t.goto(0,y*5)
t.teleport(x*5,y*5)
t.goto(x*5,0)

for i in range(0,20,4):
    t.teleport(x*5,i*5)
    t.dot()
    t.teleport(0,i*5)
    t.goto((x+2)*(y+2),i*5)

for i in range(0,16,4):
    t.teleport(i*5,y*5)
    t.dot()
    t.teleport(i*5,0)
    t.goto(i*5,(x+2)*(y+2))
 
 
for i in range(4,16,4):
    t.teleport(0,0)
    p = t.towards(i*5,y*5)
    t.goto(i*5,y*5)
    t.setheading(p)
    t.forward(200)

for i in range(4,20,4):
    t.teleport(0,0)
    q = t.towards(x*5,i*5)
    t.goto(x*5,i*5)
    t.setheading(q)
    t.forward(200)

t.color("darkviolet")
t.teleport(x*5,(x+1.5)*(y+1.5))
t.dot()
t.goto(0,(x+1.5)*(y+1.5))

# t.goto()




t.hideturtle()
turtle.done()