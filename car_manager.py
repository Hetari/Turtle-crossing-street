from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "Gray"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new = Turtle()
            new.penup()
            new.shapesize(1, random.randint(1, 3))
            new.goto(300, random.randint(-260, 260))
            new.shape("square")
            new.setheading(180)
            new.color(random.choice(COLORS))
            self.cars.append(new)

    def move(self):
        for i in self.cars:
            i.forward(STARTING_MOVE_DISTANCE)
            if i.xcor() < -280:
                del i
