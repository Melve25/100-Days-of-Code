from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.up()
        self.shapesize(0.8, 1.6)
        self.move_speed = 0.1

    def generate_car(self):
        self.color(random.choice(COLORS))
        self.goto(310, random.randint(-250, 250))
        return self

    def move(self):
        self.forward(-MOVE_INCREMENT)

    def increase_speed(self):
        self.move_speed *= 0.9

