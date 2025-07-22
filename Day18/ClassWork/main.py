from turtle import Turtle, Screen
import turtle as t
import random

t_turtle = Turtle()
screen = Screen()

# for _ in range(4):
#     t_turtle.forward(100)
#     t_turtle.right(90)

# for _ in range(10):
#     t_turtle.forward(10)
#     t_turtle.penup()
#     t_turtle.forward(10)
#     t_turtle.pendown()


# def draw_shape(sides):
#     for _ in range(sides):
#         t_turtle.forward(100)
#         t_turtle.right(360/sides)
#
#
# draw_shape(3)
# draw_shape(4)
# draw_shape(5)
# draw_shape(6)
# draw_shape(7)
# draw_shape(8)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgbTuple = (r, g, b)
    return rgbTuple


# def turn():
#     return random.choice([0, 90, 180, 270])


def random_walk():
    t_turtle.color(random_color())
    t_turtle.circle(100)
    t_turtle.left(4)


t.colormode(255)
t_turtle.speed("fastest")
for step in range(90):
    random_walk()


screen.exitonclick()
