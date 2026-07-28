import random
from turtle import Turtle,Screen

is_race_on=False
screen = Screen()
y_positions=[-10,-60,-30,-80,-100,-110]
color=["red","blue","green","yellow","cyan","magenta"]
screen.setup(width=800,height=600)
all_turtles=[]




for turtle in range(0,6):
    new_turtle = Turtle()
    new_turtle.color(color[turtle])
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(-380, y_positions[turtle])
    all_turtles.append(new_turtle)


user_bet = screen.textinput("Welcome to Turtle Races!!!!🐢🐢", prompt="Which turtle will win the race?"

                                                                    "Enter a color:  ")

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>380:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win!!! The {winning_color} turtle is the winner")
            else:
                print(f"You Lose!!! The {winning_color} turtle is the winner")
        ran_distance=random.randint(0,10)
        turtle.forward(ran_distance)






screen.exitonclick()
