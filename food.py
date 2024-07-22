import turtle as t
import random


class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        self.change_position()

    def change_position(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))

