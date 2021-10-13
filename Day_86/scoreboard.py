from turtle import Turtle


# Scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    # Update the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        self.write(self.score, align="center", font=("Courier", 60, "normal"))

    # Get a point
    def point_score(self):
        self.score += 5
        self.update_scoreboard()
