from os import write
from tokenize import String
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("data.txt") as file:
    data = file.read()
score_int=int(data)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score =score_int
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()



    def increase_score(self):
        self.score += 1
        self.update_scoreboard()