from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scores = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scores.add_score()
        scores.update_score()

    if snake.head.xcor() > 330 or snake.head.xcor() < -350 or snake.head.ycor() > 350 or snake.head.ycor() < -330:
        scores.refresh()
        snake.refresh()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scores.refresh()
            snake.refresh()

screen.exitonclick()
