import random
import turtle as t
from turtle import Screen

tim=t.Turtle()

colors=['red','blue','green','yellow','cyan','magenta']

def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        tim.forward(300)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

