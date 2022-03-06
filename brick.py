from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.color(color)
        self.speed("fastest")
        self.goto(x, y)
