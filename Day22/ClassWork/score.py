from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 30, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.up()
        self.goto(0, 300)
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score1}        {self.score2}", align=ALIGNMENT, font=FONT)

    def player1_scored(self):
        self.score1 += 1

    def player2_scored(self):
        self.score2 += 1
