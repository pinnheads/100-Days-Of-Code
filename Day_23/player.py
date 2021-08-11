from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def reached_finishline(self):
        current_pos = self.ycor()
        if current_pos > 280:
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.reached_finishline()
        self.goto(0, new_y)

