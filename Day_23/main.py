import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player_turtle = Player()
cars = CarManager()
player_level = Scoreboard()
screen.onkeypress(player_turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    cars.create_cars()
    cars.move_cars()

    time.sleep(0.1)
    screen.update()

    for car in cars.all_cars:
        if car.distance(player_turtle) < 20:
            game_is_on = False
            player_level.game_over()

    if player_turtle.reached_finishline():
        player_turtle.reset()
        cars.increase_speed()
        player_level.level_up()
