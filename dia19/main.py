from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_up():
    tim.right(10)

def move_down():
    tim.left(10)

def reset():
    tim.setheading(90)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="a",fun=move_up)
screen.onkey(key="d",fun=move_down)
screen.onkey(key="c",fun=clear)
screen.exitonclick()