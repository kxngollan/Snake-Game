from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-26, 26)*10
        y = random.randint(-26, 26)*10
        self.goto(x, y)