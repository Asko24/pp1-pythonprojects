import shapes
import turtle

pen = turtle.Turtle()

n=20
x=10
x1=x
x2=x
x3=x
x4=x
y=10
y2=y-n
y3=y-2*n
y4=y-3*n
y1=y

    
for i in range (0,4):

    shapes.drawSquare(x1,y1,n)
    x1+=n
    
for i in range (0,4):

    shapes.drawSquare(x2,y2,n)
    x2+=n
    
for i in range (0,4):

    shapes.drawSquare(x3,y3,n)
    x3+=n
    
for i in range (0,4):

    shapes.drawSquare(x4,y4,n)
    x4+=n


