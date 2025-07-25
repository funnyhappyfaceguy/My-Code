import turtle
import random
screen = turtle.Screen()
screen.colormode(255)
x=random.randint(-400,400)
y=random.randint(-400,400)
t=turtle.Turtle()
t.speed(0)
for i in range(100):
    size=random.randint(1,100)
    t.pensize(size)
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    t.pencolor((red,green,blue))
    x=random.randint(-400,400)
    y=random.randint(-400,400)
    t.goto(x,y)
    t.pencolor((red,green,blue))
    t.pensize(size)
    t.circle(size)
    
# for i in range(4):
#     t.left(90)
#     t.color("orange")
#     t.forward(200)
# t.goto(50,50)
turtle.done()

# while True:
#     pass