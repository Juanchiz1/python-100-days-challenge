import time
from turtle import Screen,Turtle
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball=Ball()
scoreboard = Scoreboard()




screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

screen.onkeypress(l_paddle.go_up,"w ")
screen.onkeypress(l_paddle.go_down,"s ")





game_is_on = True

scoreboard.update_scoreboard()
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()



    #Detect collition with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        print("Made Contact")
        ball.bounce_x()

        #Detect when r paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()


    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

