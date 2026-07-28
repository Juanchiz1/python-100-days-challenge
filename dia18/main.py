from turtle import Turtle
from turtle import Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkOliveGreen3")
timmy.speed(1)
#for _ in range(4):
 #   timmy.forward(100)
  #  timmy.left(90)


for _ in range(25):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()




screen=Screen()
screen.exitonclick()