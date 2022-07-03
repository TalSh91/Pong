from turtle import Turtle
from scoreboard import Scoreboard



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ymove = 10
        self.xmove = 10
        self.scoreboard = Scoreboard()


    def ball_move(self):
            new_x = self.xcor() + self.xmove
            new_y = self.ycor() + self.ymove
            self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1

    def ball_reset(self):
        if self.xcor() > 390:
            self.goto(0,0)
            self.xmove *= -1
            self.scoreboard.l_point()


        elif self.xcor() < -390:
            self.goto(0, 0)
            self.ymove *= -1
            self.xmove *= -1
            self.scoreboard.r_point()




