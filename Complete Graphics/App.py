import turtle

t = turtle.Turtle()
scr = turtle.Screen()
scr.setup(1100,700,250,50)

t.teleport(-100,-30)
def button(l,b,txt,bg):
    pos = t.position()
    t.fillcolor(bg)
    t.begin_fill()
    for i in range(2):
        t.forward(l)
        t.left(90)
        t.forward(b)
        t.left(90)
    t.end_fill()
    t.teleport(pos[0]+10,pos[1]+10)
    t.write(txt,font=("Arial",18,"bold"))


button(200,60,"Welcome to Graphics \n            click me","red")

def clickPos(x,y):
    pos = [x,y]
    return pos


scr.onclick(clickPos)
scr.listen()




t.hideturtle()
turtle.done()