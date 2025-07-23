from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rnd_x = random.randint(-200, 200)
        rnd_y = random.randint(-200, 200)
        self.goto(rnd_x, rnd_y)
