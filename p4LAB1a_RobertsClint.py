
import turtle

# Draw a square
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

# Move to a new position for the triangle
turtle.penup()
turtle.goto(150,0)
turtle.pendown()

# Draw a triangle
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.done()
