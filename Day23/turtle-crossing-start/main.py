import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = []
car_counter = 0
car_generation_delay = 5

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    if car_counter % car_generation_delay == 0:
        cars.append(CarManager().generate_car())
    time.sleep(cars[0].move_speed)
    screen.update()
    for c in cars:
        c.move()
        if player.distance(c) < 20 and player.ycor()-10 < c.ycor()+6:
            game_is_on = False
            scoreboard.game_over()
        if player.ycor() > 280:
            player.refresh()
            scoreboard.next_level()
            scoreboard.update()
            time.sleep(0.5)
            cars[0].increase_speed()

    car_counter += 1

screen.exitonclick()
