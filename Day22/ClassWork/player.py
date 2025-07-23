from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.up()
        self.shape("square")
        self.position = position
        self.goto(position)
        self.shapesize(5, 0.8)

    def move_up(self):
        if self.ycor() < 285:
            self.sety(self.ycor() + 25)

    def move_down(self):
        if self.ycor() > -285:
            self.sety(self.ycor() - 25)

    def def_position(self):
        self.goto(self.position)
