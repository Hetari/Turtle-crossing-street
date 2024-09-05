from turtle import Turtle

# Font settings for the scoreboard text
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    """
    A class to display and update various text elements on the screen, such as scores and game-over messages.

    Attributes:
        text (str): The text to be displayed.
        align (str): The alignment of the text (e.g., 'center', 'left', 'right').
        pos (tuple): The position where the text will appear on the screen.
    """

    def __init__(self, text: str, align: str, pos: tuple):
        """
        Initializes the scoreboard with text, alignment, and position.

        Args:
            text (str): The initial text to display.
            align (str): The alignment of the text (e.g., 'center').
            pos (tuple): The (x, y) position of the text on the screen.
        """
        super().__init__()
        self.penup()  # Disable drawing line when the turtle moves
        self.goto(pos)  # Move the turtle to the specified position
        self.hideturtle()  # Hide the turtle so that only text is visible
        # Display the initial text with alignment and font settings
        self.write(f"{text}", align=f"{align}", font=FONT, move=True)

    def update(self, text: str, pos: tuple):
        """
        Updates the text on the screen and moves to the new position.

        Args:
            text (str): The text to display.
            pos (tuple): The (x, y) position where the updated text should appear.
        """
        self.clear()  # Clear the previous text
        self.goto(pos)  # Move to the new position
        self.write(f"{text}", align='center', font=FONT, move=True)  # Display the updated text

    def timing(self, text: str, pos: tuple):
        """
        Displays text without clearing the previous text (used for timers or real-time updates).

        Args:
            text (str): The text to display.
            pos (tuple): The (x, y) position where the text should appear.
        """
        # self.clear()  # Commented out as timing doesn't clear previous text
        self.goto(pos)  # Move to the specified position
        self.write(f"{text}", align='center', font=FONT, move=True)  # Display the timer text

    def game_over(self, pos: tuple):
        """
        Displays the "Game Over" message when the game ends.

        Args:
            pos (tuple): The (x, y) position where the message should appear.
        """
        self.goto(pos)  # Move to the position
        self.write("Game Over...", align='center', font=FONT, move=True)  # Display "Game Over" message
