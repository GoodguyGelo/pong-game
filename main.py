from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()
screen.title("The Pong Game")

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_on = True
speed = 1
while game_on:
    time.sleep(0.1/speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddles

    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
        speed +=0.1

    # detect when the ball gets out of bounds

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        speed = 1

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        speed = 1

screen.exitonclick()
