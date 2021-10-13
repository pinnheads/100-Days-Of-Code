from turtle import Turtle
from ball import Ball


# Create the paddle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -300)

    # Ball hits the paddle
    def paddle_ball(self, ball: Ball):
        if (
            abs(self.xcor() - ball.xcor()) < 30
            and abs(self.ycor() - ball.ycor()) < 50
            and ball.ycor() > -295
        ):
            ball.bounce_y()

    # Move the paddle right
    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    # Move the paddle left
    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
