from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.goto(0, 320)
        self.hideturtle()
        self.score = 0
        with open("data.txt") as r:
            self.high_score = int(r.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as w:
                w.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
