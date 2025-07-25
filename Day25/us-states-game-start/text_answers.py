from turtle import Turtle


class TextAnswers(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.up()
        self.speed("fastest")
        self.goto(x, y)
        self.write(state, align="center", font=("Arial", 12, "normal"))

