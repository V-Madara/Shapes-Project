import turtle
import math

t = turtle.Turtle();
t.speed(0.1)
# x = int(input("Enter the x coordinate: "))
# y = int(input("Enter the y coordinate: "))

# if(x%10==x and y%10==y):
#     x*=10
#     y*=10
# elif(x%100==x and y%100==y):
#     x*=5
#     y*=5
# elif(x%1000==x and y%1000==y and x<=200 and y<=200):
#     x = x
#     y = y
# else:
#     x/=5
#     y/=5

x = 10
y= 20

t.goto((x+1)*(y+1),0)
t.teleport(0,0)
t.goto(0,(x+1)*(y+1))
t.teleport(x,y)
t.dot()
t.teleport(0,0)

t.goto(-(x+1)*(y+1),0)
t.teleport(0,0)
t.goto(0,-(x+1)*(y+1))
t.teleport(-x,-y)
t.dot()

const = x*y;
t.teleport(1,x*y)
# t.color("red")

t.color("darkOrchid4")
for i in range(1,x*y+1):
    if(const%i==0):
        gotoy = int(const/i)
        t.teleport(i,gotoy)
        t.dot()
        t.write(f"( {i} , {gotoy} )",font=("Arial",8,"normal"))

t.teleport(-1,-const)
for i in range(-1,-x*y-1,-1):
    if(const%i==0):
        gotoy = int(const/i)
        t.teleport(i,gotoy)
        t.dot()
        t.write(f"( {i} , {gotoy} )",font=("Arial",8,"normal"))

t.pensize(3)
t.color("red")
t.teleport(1,const)
for i in range(1,x*y):
    gotoy = const/i
    t.goto(i,gotoy)
t.teleport(-1,-const)

for i in range(-1,-x*y,-1):
    gotoy = const/i
    t.goto(i,gotoy)



t.hideturtle()

turtle.done();