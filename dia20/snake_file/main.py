import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

segments=[]






game_on=True

while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()







screen.exitonclick()