import turtle
pen=turtle.Turtle()
pen.width(1)

def drawSquare(x,y,n):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    
    for i in range (0,4):

        pen.forward(n)
        pen.right(90)
        

def drawCircle(x,y,r):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.circle(r)

def drawTriangle(x,y,m):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.seth(270)
    pen.right(30)
    pen.forward(m)
    pen.left(120)
    pen.forward(m)
    pen.left(120)
    pen.forward(m)
    
def drawStar(x):
    pen.penup()
    pen.goto(0,200)
    pen.pendown()
    pen.seth(270)
    pen.right(18)
    pen.forward(x)
    pen.seth(180)
    pen.forward(x)
    pen.left(144)
    pen.forward(x)
    pen.right(72)
    pen.forward(x)
    pen.left(144)
    pen.forward(x)
    pen.right(72)
    pen.forward(x)
    pen.left(144)
    pen.forward(x)
    pen.right(72)
    pen.forward(x)
    pen.left(144)
    pen.forward(x)
    pen.right(72)
    pen.forward(x)


def drawfilledSquare(x,y,m):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.begin_fill()
    drawSquare(x,y,m)
    pen.end_fill()
    
  
def chessboard(m):
    pen.speed(0)
    y=0
    for j in range(0,8):
        if j%2==0:
            for i in range(0,8):
                if i%2==0:
                    drawSquare(-350+i*m,350-y*m,m)
                else:
                    drawfilledSquare(-350+m+(i-1)*m,350-y*m,m)
        else:
            for i in range(0,8):
                if i%2==0:
                    drawfilledSquare(-350+i*m,350-y*m,m)
                else:
                    drawSquare(-350+m+(i-1)*m,350-y*m,m)
        y+=1

chessboard(50)
    
    
    

