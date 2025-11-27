import turtle
import math

t = turtle.Turtle();

# x = int(input("Enter the x coordinate: "))
# y = int(input("Enter the y coordinate: "))

# if(x%10==x and y%10==y):
#     x*=50
#     y*=50
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

const = x*y;
t.teleport(1,x*y)
t.color("red")
t.pensize(2)
for i in range(1,x*y):
    gotoy = const/i
    t.goto(i,gotoy)





turtle.done();