from turtle import Turtle, Screen
import random

# tur = Turtle(shape="turtle")
screen = Screen()
tur_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Choose color", prompt="Which turtle will win? Enter a color: ")

is_race_on = False
y = -100

turtles = []

for i in range(len(tur_colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(tur_colors[i])
    turtles[i].up()
    turtles[i].goto(x=-230, y=y)
    y += 45

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The winning turtle is {winning_color}")
            else:
                print(f"You have lost! The winning turtle is {winning_color}")
        rnd_distance = random.randint(0, 10)
        turtle.forward(rnd_distance)

# def move_forwards():
#     tur.forward(10)
#
#
# def move_backwards():
#     tur.forward(-10)
#
#
# def move_clockwise():
#     tur.left(-10)
#
#
# def move_counter_clockwise():
#     tur.left(10)
#
#
# def clear():
#     screen.resetscreen()
#
#
# tur.speed("fastest")
#
# screen.listen()
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=move_counter_clockwise)
# screen.onkeypress(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()
