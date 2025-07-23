from turtle import Turtle


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.x = 5
        self.y = 5
        self.shape("circle")

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def reflect_x(self):
        self.x *= -1

    def reflect_y(self):
        self.y *= -1

    def def_position(self):
        self.goto(0, 0)

