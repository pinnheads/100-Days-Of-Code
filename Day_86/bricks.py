from turtle import Turtle
import random

colors = [
    "green",
    "yellow",
    "red",
    "blue",
    "grey",
    "orange",
    "pink",
    "darkblue",
    "cyan",
    "brown",
    "peach puff",
    "purple",
    "lime",
    "aquamarine",
    "sandy brown",
    "dark red",
    "violet",
    "tomato",
    "green yellow",
]


# Create the bricks
class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bricks = []
        for i in range(200, 280, 20):
            for j in range(-580, 580, 40):
                brick = Turtle("square")
                brick.penup()
                brick.color(random.choice(colors))
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.setpos(j, i)
                self.all_bricks.append(brick)

    # Ball hits the brick
    def hit_brick(self, ball):
        for brick in self.all_bricks:
            if brick.isvisible() and brick.distance(ball) < 20:
                brick.hideturtle()
                ball.bounce_y()
                return True
        return False
