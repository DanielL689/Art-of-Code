
from random import*

import turtle
bob=turtle.Turtle()
turtle.colormode(255)
turtle.bgcolor("black")


turtle.tracer(False)

def drawSquare(size,size2):
     for times in range(4):
         bob.forward(size)
         bob.right(90)
         bob.circle(size2)
         bob.left(180)
        
def polygon(side,size,c):
     bob.color(c)
     bob.begin_fill()
     angle=360/side
     for times in range(side):
          bob.forward(size)
          bob.left(angle)
     bob.end_fill()

def circle(size,c):
     bob.color(c)
     bob.circle(size)
     
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def comet(size,angle,length):
     for times in range(length):
          bob.forward(size)
          bob.left(angle)
          bob.width(times)

def flower(c):
     bob.color(c)
     bob.begin_fill()
     for times in range(5):
         bob.circle(30)
         bob.left(50)
         bob.forward(1)
         

def flower(x,y,c):
     bob.color(c)
     jump(x,y)
     bob.begin_fill()
     for times in range(5):
         bob.circle(30)
         bob.left(1)
         bob.forward(10)


for times in range(254):
     n=randint(0,255)
     c=(n,times,n)
     polygon(9,255-times,c)
     comet(times,1,1)
     bob.left(90)


