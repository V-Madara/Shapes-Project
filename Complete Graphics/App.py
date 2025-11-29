import turtle

t = turtle.Turtle()
scr = turtle.Screen()
scr.setup(1100,700,250,50)

t.teleport(-100,-30)
def button(btn_length,btn_breadth,btn_label,btn_bg,text_hight):
    pos = t.position()
    t.fillcolor(btn_bg)
    t.begin_fill()
    for i in range(2):
        t.forward(btn_length)
        t.left(90)
        t.forward(btn_breadth)
        t.left(90)
    t.end_fill()
    t.teleport(pos[0]+10,pos[1]+10)
    t.write(btn_label,font=("Arial",text_hight,"bold"))


button(200,60,"Welcome to Graphics \n            click me","red",13)

def clickPos(x,y):
    if -100<x<100 and -30<y<30:
        scr.clear()


scr.onclick(clickPos)
scr.listen()




t.hideturtle()
turtle.done()