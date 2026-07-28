import random
from turtle import Turtle

from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
num1 = 1
num2 = 6


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_chance=random.randint(num1,num2)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.hideturtle()
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            random_y=random.randint(-240,240)
            new_car.goto(300,random_y)
            new_car.showturtle()
            self.all_cars.append(new_car)



    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT

