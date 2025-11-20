import turtle
import math


maj,min=200,140
t = turtle.Turtle()
# t.color("Pink")
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

t.goto(0,70)
t.dot()

turtle.speed(0)
for i in range(-100,0):
    t.goto(100+i,70+(math.sqrt(math.pow(min/2,2)*(1-(math.pow(i,2)/math.pow(maj/2,2))))))
    t.dot()

for i in range(0,100):
    t.goto(100+i,70+math.sqrt((70*70)*(1-((i*i)/(100*100)))))
    t.dot()

for i in range(100,0,-1):
    t.goto(100+i,70-math.sqrt((70*70)*(1-((i*i)/(100*100)))))
    t.dot()

for i in range(0,100):
    t.goto(100-i,70-math.sqrt((70*70)*(1-((i*i)/(100*100)))))
    t.dot()

# # Vivek Logic

# def draw_curve(points):
#     t.penup(); t.goto(points[0]); t.pendown()
#     t.pencolor("red"); t.pensize(4)
#     for i in range(len(points)-1):
#         p0 = points[max(i-1,0)]
#         p1 = points[i]
#         p2 = points[i+1]
#         p3 = points[min(i+2,len(points)-1)]
#         for j in range(1,61):
#             tv = j/60; t2 = tv*tv; t3 = t2*tv
#             x = (2*t3-3*t2+1)p1[0] + (-2*t3+3*t2)*p2[0] + (t3-2*t2+tv)(p2[0]-p0[0])0.5 + (t3-t2)(p3[0]-p1[0])*0.5
#             y = (2*t3-3*t2+1)p1[1] + (-2*t3+3*t2)*p2[1] + (t3-2*t2+tv)(p2[1]-p0[1])0.5 + (t3-t2)(p3[1]-p1[1])*0.5
#             t.goto(x,y)

# draw_curve(left_points)





turtle.done()