import turtle

length = 400
breadth = 240
t = turtle.Turtle()

t.speed(3)
t.pensize(2)

t.penup()
t.goto(-200,50)
t.pendown()
t.dot()
t.write("A",font=("Arial",12,"bold"))
A = t.position()

t.forward(length)
t.write("B",font=("Arial",12,"bold"))
B = t.position()

t.penup()
t.left(90)
t.forward(breadth/2)
t.setheading(0)
t.backward(length/2)

t.pendown()
t.dot()
t.write("C",font=("Arial",12,"bold"))
C = t.position()

t.right(90)
t.forward(breadth)
t.dot()
t.write("D",font=("Arial",12,"bold"))
D = t.position()

t.penup()
t.goto(C)
t.setheading(0)
t.backward(length/2)
t.setheading(0)

t.pendown()
t.right(90)
t.forward(breadth)
t.setheading(0)
t.forward(length)
t.left(90)
t.forward(breadth)
t.setheading(0)
t.backward(length)

t.penup()
t.goto(A)


# Now dividing the line front of  A into 4 parts


t.setheading(0)
t.forward(length/8)
t.dot()
t.write("p1" , font=("Arial",10,"bold"))
p1 = t.position()

t.forward(length/8)
t.dot()
t.write("p2" , font=("Arial",10,"bold"))
p2 = t.position()

t.forward(length/8)
t.dot()
t.write("p3" , font=("Arial",10,"bold"))
p3 = t.position()

t.forward(length/8)
t.dot()
t.write("p4" , font=("Arial",10,"bold"))
p4 = t.position()

t.goto(D)
t.pendown()

# Now joing points to D and extending----

heading_to_p1 = t.towards(p1)  
t.goto(p1)
t.setheading(heading_to_p1)
t.forward(length / 2)

t.penup()
t.goto(D)
t.pendown()

heading_to_p2 = t.towards(p2)  
t.goto(p2)
t.setheading(heading_to_p2)
t.forward(length / 2)

t.penup()
t.goto(D)
t.pendown()

heading_to_p3 = t.towards(p3)  
t.goto(p3)
t.setheading(heading_to_p3)
t.forward(length / 2)

t.penup()
t.goto(D)
t.pendown()

heading_to_p4 = t.towards(p4)  
t.goto(p4)
t.setheading(heading_to_p4)
t.forward(length / 2)

# Now dividing the line above A and joining to C
t.penup()
t.goto(A)
t.pendown 


t.setheading(0)
t.left(90)
t.forward(breadth/8)
t.dot()
t.write("q1" , font=("Arial",10,"bold"))
q1 = t.position()

t.forward(breadth/8)
t.dot()
t.write("q2" , font=("Arial",10,"bold"))
q2 = t.position()

t.forward(breadth/8)
t.dot()
t.write("q3" , font=("Arial",10,"bold"))
q3 = t.position()

t.forward(breadth/8)
t.dot()
t.write("q4" , font=("Arial",10,"bold"))
q4 = t.position()

t.goto(C)
t.pendown()
t.goto(q1)
t.penup()

t.goto(C)
t.pendown()
t.goto(q2)
t.penup()

t.goto(C)
t.pendown()
t.goto(q3)
t.penup()

t.goto(C)
t.pendown()
t.goto(q4)
t.penup()

# boring calculations 

import math

# ---- Intersection dots X1…X4 (same as before) ----
point_pairs = [
    (p1, q1, "X1"),
    (p2, q2, "X2"),
    (p3, q3, "X3"),
    (p4, q4, "X4")
]

# First collect all intersection points in order
intersections = []

for p_pt, q_pt, label in point_pairs:
    dx1 = D[0] - p_pt[0]
    dy1 = D[1] - p_pt[1]
    dx2 = C[0] - q_pt[0]
    dy2 = C[1] - q_pt[1]

    denom = dx1 * dy2 - dy1 * dx2

    if math.fabs(denom) > 1e-8:
        t_val = ((q_pt[0] - p_pt[0]) * dy2 - (q_pt[1] - p_pt[1]) * dx2) / denom
        ix = p_pt[0] + t_val * dx1
        iy = p_pt[1] + t_val * dy1

        t.penup()
        t.goto(ix, iy)
        t.pendown()
        t.dot(8, "red")
        t.write(f" {label}", font=("Arial", 9, "bold"))
        
        intersections.append((ix, iy))

# ---- NEW: Red dot at point A (same style) ----
t.penup()
t.goto(A)
t.pendown()
t.dot(8, "red")
t.write(" A", font=("Arial", 9, "bold"))

# BEAUTIFUL FRENCH CURVE CONNECTING ALL RED POINTS (A → X1 → X2 → X3 → X4)

red_points = [A] + intersections  # Exactly 5 points in correct order

# Cardinal spline function (true French curve feel)
def draw_french_curve(points, tension=0.5, segments=50):
    if len(points) < 3:
        return
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.pencolor("red")
    t.pensize(4)

    for i in range(len(points) - 1):
        # Define control points
        p0 = points[max(i-1, 0)]
        p1 = points[i]
        p2 = points[min(i+1, len(points)-1)]
        p3 = points[min(i+2, len(points)-1)]

        for j in range(1, segments + 1):
            t_val = j / segments
            t2 = t_val * t_val
            t3 = t2 * t_val

            h1 =  2*t3 - 3*t2 + 1
            h2 = -2*t3 + 3*t2
            h3 =     t3 - 2*t2 + t_val
            h4 =     t3 -    t2

            x = h1*p1[0] + h2*p2[0] + h3*(p2[0] - p0[0])*tension + h4*(p3[0] - p1[0])*tension
            y = h1*p1[1] + h2*p2[1] + h3*(p2[1] - p0[1])*tension + h4*(p3[1] - p1[1])*tension

            t.goto(x, y)

# Draw the final smooth artistic curve
draw_french_curve(red_points, tension=0.5, segments=60)

t.hideturtle()
turtle.done()