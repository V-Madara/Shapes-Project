import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create turtle
t = turtle.Turtle()
t.speed(0)

# Parameters
x, y = 0, 0          # Point through which the line passes
angle = 45           # Angle in degrees
length = 300         # Total length of the extended line

# Move to starting point of the line
t.penup()
t.goto(x, y)
t.setheading(angle + 180)  # Reverse direction
t.forward(length / 2)      # Move half length backward

# Draw the line
t.pendown()
t.forward(length)          # Draw full line forward

# Hide turtle and finish
t.hideturtle()
screen.mainloop()