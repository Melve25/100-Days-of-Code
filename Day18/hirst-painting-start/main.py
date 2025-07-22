import turtle as t
from turtle import Screen
import random as rnd

rgb_colors = [(245, 243, 238), (246, 242, 244),
              (202, 164, 110), (240, 245, 241),
              (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
tur = t.Turtle()
screen = Screen()


def draw_circle():
    tur.color(rnd.choice(rgb_colors))
    tur.begin_fill()
    tur.circle(5)
    tur.end_fill()


def move(x, y):
    tur.up()
    tur.goto(x, y)
    tur.down()


t.colormode(255)
tur.speed("fastest")
x = -150
y = -150
count = 0

for i in range(100):

    if count == 10:
        count = 0
        x = -150
        y += 20

    move(x, y)
    draw_circle()
    x += 20
    count += 1

screen.exitonclick()
