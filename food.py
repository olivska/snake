from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.refresh()

    def refresh(self):
        food_x = random.randint(-280, 280)
        food_y = random.randint(-280, 280)
        self.setposition(food_x, food_y)
