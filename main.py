from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time


game_is_on = True
screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
paddle1 = Paddle(350,0)
paddle2 = Paddle(-350,0)
ball = Ball()
ball.ball_move()
screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    ball.ball_reset()

screen.exitonclick()