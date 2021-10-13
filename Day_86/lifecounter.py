from turtle import Turtle


# Counter of the remaining lives
class Lifecounter(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.update_counter()

    # Update the counter
    def update_counter(self):
        self.clear()
        self.goto(-400, 320)
        self.write(
            f"Lives: {self.lives}",
            align="center",
            font=("Courier", 30, "normal"),
        )

    # Lose a point
    def live_lost(self):
        self.lives -= 1
        self.update_counter()
