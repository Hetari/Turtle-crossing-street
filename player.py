from turtle import Turtle
import time


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        self.level = 1
        print(f"Level: {self.level}")
        super().__init__()
        # self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        if self.ycor() <= 280:
            self.forward(MOVE_DISTANCE)

    def winning(self, level):
        t = '0.'
        for digit in range(level):
            if digit == level - 1:
                t += '1'
            else:
                t += '0'

        time.sleep(float(t))
        if self.ycor() > 280.0:
            self.level += 1
            print(f"Level: {self.level}")
            self.goto(STARTING_POSITION)
