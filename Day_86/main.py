from scoreboard import Scoreboard
from paddle import Paddle
from turtle import Screen
from ball import Ball
from bricks import Bricks
from lifecounter import Lifecounter
import time

# Screen settings
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Breakout")
screen.tracer(0)

# Creating objects
scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()
brick = Bricks()
lifecounter = Lifecounter()

# Keys to make the paddle move
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

# Methods that let the game work
game_is_on = True
# time.sleep(30)
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    paddle.paddle_ball(ball)

    # Ball hits the wall
    if ball.xcor() <= -580 or ball.xcor() >= 580:
        ball.bounce_x()

    # Scoring a point
    if brick.hit_brick(ball):
        scoreboard.point_score()
        ball.move_speed *= 0.97

    # Ball hits the ceeling
    if ball.ycor() >= 380:
        ball.bounce_y()

    # Losing a point
    if ball.ycor() < -390:
        ball.reset_position()
        lifecounter.live_lost()

    # Game over
    if lifecounter.lives == 0 or scoreboard.score == 580:
        game_is_on = False
        print(f"Game Over! You have {scoreboard.score} points")

screen.exitonclick()
