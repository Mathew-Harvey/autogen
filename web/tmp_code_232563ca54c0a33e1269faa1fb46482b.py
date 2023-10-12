import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
draw = turtle.Turtle()

# Draw a square
for i in range(4):
    draw.forward(100)
    draw.right(90)

# Hide the turtle
draw.hideturtle()

# Save the screen as a .eps file
screen.getcanvas().postscript(file="square.eps")

# Close the turtle screen
turtle.done()