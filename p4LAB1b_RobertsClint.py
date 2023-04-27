
import turtle

# create turtle object
t = turtle.Turtle()

# set the pen size and color
t.pensize(20)
t.pencolor("purple")

# move turtle to starting position
t.penup()
t.goto(-50, -150)
t.pendown()

# draw the letter "C"
t.circle(180, -100)
t.circle(180, -80)

# move turtle to R position
t.penup()
t.goto(50, -150)
t.pendown()

# draw the letter "R"
t.right(90)
t.forward(350)
t.right(90)
t.circle(-100, 180)
t.right(240)
t.forward(170)

# hide the turtle
t.hideturtle()

# keep the turtle window open until manually closed
turtle.done()
