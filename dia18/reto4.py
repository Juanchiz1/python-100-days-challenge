import random
import turtle as t
from turtle import Screen

tim=t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tupla=(r, g, b)
    return tupla

directions=[0,90,180,270]
tim.pensize(12)
tim.speed(100)
tim.shape('turtle')

for _ in range(200):
    tim.forward(30)
    tim.setheading(directions[random.randint(0,len(directions)-1)])
    tim.color(random_color())



