import turtle
pen=turtle.Turtle()

def drawSquare(x,y,n):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    
    for i in range (0,4):

        pen.forward(n)
        pen.right(90)