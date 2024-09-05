from turtle import Turtle
from player import Player
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "Gray"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """
    Manages the creation and movement of cars in the game.

    Attributes:
        cars (list): A list holding all the car objects.
        car_speed (int): The current speed of the cars.
    """

    def __init__(self):
        """Initializes the CarManager with an empty car list and sets the initial car speed."""
        self.cars = []  # Holds all active car objects
        self.create_car()  # Creates the first car when the manager is initialized
        self.car_speed = STARTING_MOVE_DISTANCE  # Set initial car speed

    def create_car(self):
        """Randomly creates a car and adds it to the car list."""
        # Random chance to create a new car (1 in 3 chance)
        chance = random.randint(0, 2)
        if chance == 1:
            # Create new car (turtle object)
            new_car = Turtle()
            new_car.penup()  # Disable drawing when the car moves
            new_car.shapesize(1, random.randint(1, 3))  # Randomize car length
            new_car.goto(300, random.randint(-260, 260))  # Start position
            new_car.shape("square")
            new_car.setheading(180)  # Move towards the left side of the screen
            new_car.color(random.choice(COLORS))  # Random car color
            self.cars.append(new_car)  # Add the new car to the list

    def move(self):
        """Moves all cars to the left and removes them if they move off-screen."""
        for car in self.cars:
            car.forward(self.car_speed)  # Move car by the current speed
            # If the car moves off the screen (past x = -280), delete it
            if car.xcor() < -280:
                self.cars.remove(car)  # Remove the car from the list

    def level_up(self):
        """Increases car speed for higher levels."""
        self.car_speed += MOVE_INCREMENT
