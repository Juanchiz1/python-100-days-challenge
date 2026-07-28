from turtle import Turtle

ALLIGMENT="center"
FONT=("Courier",20,"bold")


class ScorecardBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.score=0
        self.update_scoreboard()

        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALLIGMENT, font=FONT)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALLIGMENT, font=FONT)

