from turtle import Screen, Turtle
from player import Player
from pong import Pong
from score import Score
import time

screen = Screen()
screen.setup(width=1100, height=700)
screen.bgcolor("black")
screen.tracer(0)

y = -340

pong = Pong()
score = Score()
dashed_line = Turtle()
dashed_line.speed("fastest")
dashed_line.up()
dashed_line.goto(0, y)
dashed_line.color("white")
dashed_line.hideturtle()


for _ in range(20):
    dashed_line.down()
    y += 20
    dashed_line.goto(0, y)
    dashed_line.up()
    y += 20
    dashed_line.goto(0, y)

player1 = Player((-530, 0))
player2 = Player((530, 0))

screen.listen()
screen.onkeypress(key="w", fun=player1.move_up)
screen.onkeypress(key="s", fun=player1.move_down)
screen.onkeypress(key="Up", fun=player2.move_up)
screen.onkeypress(key="Down", fun=player2.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.01)
    pong.move()
    if pong.ycor() > 340 or pong.ycor() < -340:
        pong.reflect_y()

    if pong.xcor() > 510 and pong.distance(player2) < 70 or pong.xcor() < -510 and pong.distance(player1) < 70:
        pong.reflect_x()

    if pong.xcor() > 550:
        score.player1_scored()
        score.update_score()
        pong.def_position()
        pong.reflect_x()
        player1.def_position()
        player2.def_position()
    elif pong.xcor() < -550:
        score.player2_scored()
        score.update_score()
        pong.def_position()
        pong.reflect_x()
        player1.def_position()
        player2.def_position()


screen.exitonclick()
