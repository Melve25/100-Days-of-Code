from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seq_num - 1].xcor()
            new_y = self.segments[seq_num - 1].ycor()
            self.segments[seq_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_tur = Turtle(shape="square")
        new_tur.color("white")
        new_tur.up()
        new_tur.goto(position)
        self.segments.append(new_tur)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
