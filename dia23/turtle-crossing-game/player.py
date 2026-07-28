from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.go_to_the_start()
        self.showturtle()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.forward(-MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_the_start(self):
        self.goto(STARTING_POSITION)



