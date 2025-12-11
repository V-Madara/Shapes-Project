import turtle
import math

t = turtle.Turtle()
t2 = turtle.Turtle()
t.speed(0)
t2.hideturtle()
d = 100;
t.color("gray")
t2.color("gray")
pie = math.pi

t.teleport(0,0)
t.forward(2*math.pi*50)
t.teleport(0,100)
t.forward(2*math.pi*50)

# Background Drawings
t.teleport(0,0)
t.circle(50)
t.color("red")
t.dot()
t.write("P-start",font=("Arial",10,"bold"))
t.color("gray")
# t2.color("red")
t2.teleport(0,50)
t2.showturtle()
yCoord = []
for i in range(0,6):
    t2.setheading(30*i)
    t2.forward(50)
    if(i>3):
        pos = t2.position()
        yCoord.append(pos[1])
        t2.teleport(pos[0],pos[1])
        t2.goto(2*pie*50,pos[1])
        t2.teleport(pos[0],pos[1])
    t2.backward(100)
    if(i<=3):
        pos2 = t2.position()
        yCoord.append(pos2[1])
        t2.goto(2*pie*50,pos2[1])
        t2.teleport(pos2[0],pos2[1])
    t2.forward(50)
t2.hideturtle()
print(yCoord.sort())
t.color("red")
# print(yCoord)
for i in range(0,6):
    h=i*((pie*100)/12)
    k=50
    y = yCoord[i]
    x = -math.sqrt(2500 - math.pow(y-k,2))+h
    t.teleport(x-1.5*i,y)
    t.dot()
    t.write(f"P{i+2}",font=("Arial",10,"bold"))

for i in range(5,-1,-1):
    h=i*((pie*100)/12)
    k=50
    y = yCoord[i]
    x = -math.sqrt(2500 - math.pow(y-k,2))+h
    t.teleport((pie*100)-(x-1.5*i),y)
    t.dot()
    t.write(f"P{13-i}",font=("Arial",10,"bold"))

t.color("gray")
t.teleport(math.pi*100,0)
t.circle(50)
t.color("red")
t.dot()
t.write("P-end",font=("Arial",10,"bold"))
t.color("gray")

t.teleport(math.pi*50,0)
t.circle(50)
t.color("red")
t.teleport(math.pi*50,100)
t.dot()
t.write("P-mid",font=("Arial",10,"bold"))
t.color("gray")


# Curve tracing
t.teleport(0,0)
t.pensize(3)
t.color("purple")
for i in range(50,-1,-1):
    pX = -(math.pi*i)
    pY = 2*((math.sqrt(math.pow(50,2)-math.pow(i,2)))-50)
    t.goto((math.pi*50)+pX,pY+100)

for i in range(0,51):
    pX = (math.pi*i)
    pY = 2*((math.sqrt(math.pow(50,2)-math.pow(i,2)))-50)
    t.goto((math.pi*50)+pX,pY+100)

# Concept Trying -> ON normal Circle
# for i in range(0,51):
#     y = math.sqrt(50*50 - i*i)
#     t.goto(-i,y)








turtle.done();