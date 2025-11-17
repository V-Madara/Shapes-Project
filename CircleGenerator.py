import turtle
import math

class  Shapes():
        
    # length = int(input("Enter the length: "))
    # sides = int(input("Enter the Number of sides: "))
    def draw(self,length,sides):
        self.length = length
        self.sides = sides
        turtle.setup(width=600,height=700)
        screen = turtle.Screen()
        screen.cv._rootwindow.geometry("600x700+400+100")
        t = turtle.Turtle()
        t.speed(3)
        t.pensize(2)

        t.penup()
        t.goto(0, 0)
        A = t.position()          
        t.pendown()
        t.color("black")
        t.forward(length)
        t.color("cadetblue2")
        B = t.position()          


        t.left(90)
        t.forward(length)
        C = t.position()        

        t.goto(A)

        t.penup()
        # t.goto(B[0]+length,B[1])
        t.goto(B)
        t.pendown()



        t.color("aquamarine3")

        t.circle(length)  

        t.penup()

        t.color("deeppink")
        t.goto(A[0], A[1] - 30); t.write("A", align="center", font=("Arial", 14, "bold"))
        t.goto(B[0], B[1] - 30); t.write("B", align="center", font=("Arial", 14, "bold"))
        t.goto(C[0], C[1] + 10); t.write("C", align="center", font=("Arial", 14, "bold"))

        # My continueation
        t.goto((A[0]+B[0])/2 , 0)
        t.pendown()
        t.color("papayawhip")

        ps = []
        yc6 = math.sqrt(math.pow(length,2)-math.pow((length)/2,2)) # -> need Editing
        if sides == 4:
            ps = [length/2,length/2]
        elif sides == 5:
            ps = [(length/2),(length/2)+(yc6-(length/2))/2]
        elif sides == 6:
            ps = [(length/2),yc6]
        else:
            ps = [(length/2), yc6+(yc6-(length/2))/2*(sides-6)]


        t.forward(ps[1]+10)
        t.penup()

        t.goto((length/2),(length/2))
        t.color("deeppink")
        t.dot()
        t.write("4", align="center", font=("Arial", 14,"bold"))

        t.goto((length/2),yc6)
        t.dot()
        t.write("6",align="center", font=("Arial", 14,"bold"))

        t.goto((length/2),(length/2)+(yc6-(length/2))/2)
        t.dot()
        t.write("5", align="center", font=("Arial", 14,"bold"))

        # this is for a general point other than 4,5 and 6
        t.goto(ps)
        t.dot()
        t.write(f"{sides}", align="center", font=("Arial", 14,"bold"))

        sidecircle = math.sqrt(math.pow((length/2),2)+math.pow(ps[1],2))
        t.goto((length/2)+sidecircle,ps[1])
        t.pendown()
        t.color("palegreen")
        t.circle(sidecircle)
        t.penup()
        t.goto(length,0) 

        # circle Division - Start here 
        angles = 2*math.pi/sides
        cx,cy = ps[0],ps[1]
        t.color("deeppink")
        t.goto(length,0)
        for i in range(0,sides):
            x = cx+sidecircle*math.cos(i*angles-(math.pi/2 - math.asin((length/2)/sidecircle)))
            y = cy+sidecircle*math.sin(i*angles-(math.pi/2 - math.asin((length/2)/sidecircle)))
            t.goto(x,y)
            t.dot()

        t.color("Black")
        for i in range(0,sides):
            x = cx+sidecircle*math.cos(i*angles-(math.pi/2 - math.asin((length/2)/sidecircle)))
            y = cy+sidecircle*math.sin(i*angles-(math.pi/2 - math.asin((length/2)/sidecircle)))
            t.pendown()
            t.goto(x,y)
            







        turtle.done()


if __name__=="__main__":
    Shapes().draw(100,8)