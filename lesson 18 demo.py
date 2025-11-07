
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

'''
bob.width(5)
bob.right(90)
bob.color("yellow")
bob.circle(10)
bob.color("green")
bob.forward(100)
    
     

for times in range(256):
     n=randint(0,255)
     c=(n,times,times)
     polygon(10,256-times,c)
     bob.left(5)

'''
for times in range(254):
     n=randint(0,255)
     c=(n,times,n)
     polygon(9,255-times,c)#best one
     comet(times,1,1)
     bob.left(90)
'''
for times in range(255):
     n=randint(0,255)
     c=(times,0,0)
     circle(1,c)
     comet(times+2,5,1)
     polygon(7,255-times,c)
     bob.left(50)
    
     


for times in range(100):
     x=randint(5,1000)
     y=randint(5,1000)
     size=randint(5,300)
     side=randint(1,15)
     length=randint(0,100)
     r=randint(0,255)
     g=randint(0,255)
     b=randint(0,255)
     c=(r,g,b)
     jump(x,y)
     bob.color(c)
     comet(size,side,length)


for times in range(500):
     n=randint(0,255)
     c=(0,n,n)
     r=randint(-300,300)
     i=randint(1,15)
     
     flower(r,r,c)
     bob.right(1)


for times in range(500):
     n=randint(0,255)
     c=(0,n,n)
     r=randint(-300,300)
     i=randint(1,15)
     flower(c)
     polygon(100,times,c)

for times in range(100):
     r=randint(0,255)
     c=("green")
     comet(10,3,100)
     bob.left(1)

for times in range(254):
     n=randint(0,255)
     c=(n,times,n)
     polygon(9,255-times,c)
     comet(times,1,1)
     bob.left(90)
     circle(1,c)
     comet(times+2,5,1)
     polygon(7,255-times,c)
     bob.left(50)
     
'''


