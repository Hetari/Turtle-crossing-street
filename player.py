from turtle import Turtle

STARTING_POSITION = (0, -280)  # Starting point at the bottom center of the screen
MOVE_DISTANCE = 10  # The distance the player moves with each step
FINISH_LINE_Y = 280  # The y-coordinate representing the finish line


class Player(Turtle):
    """
    Player class represents the turtle controlled by the user.

    Attributes:
        level (int): Keeps track of the current level of the player.
    """
    level = 0  # Class-level variable to track the player's level

    def __init__(self):
        """
        Initializes the player as a turtle-shaped object and sets its starting position.
        """
        super().__init__()  # Initialize the Turtle superclass
        self.shape("turtle")  # Set the player's shape to a turtle
        self.penup()  # Disable drawing when moving the player
        self.go_to_start()  # Place the player at the starting position
        self.setheading(90)  # Face the turtle upwards (towards the top of the screen)

    def up(self):
        """
        Moves the player upwards by a defined MOVE_DISTANCE.
        Ensures the player does not go beyond the finish line.
        """
        if self.ycor() <= FINISH_LINE_Y:  # Make sure the player doesn't go past the finish line
            self.forward(MOVE_DISTANCE)

    def is_finish_line(self):
        """
        Checks if the player has crossed the finish line.

        Returns:
            bool: True if the player has reached or crossed the finish line, otherwise False.
        """
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        """
        Moves the player back to the starting position and increases the player's level.
        """
        self.level += 1  # Increment the player's level
        self.goto(STARTING_POSITION)  # Move the player to the starting position
