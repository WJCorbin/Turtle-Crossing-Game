from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")
player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    score.display_score()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.ycor() > 280:
        score.increase_score()
        player.goto_start()
        car_manager.move_faster()


screen.exitonclick()
