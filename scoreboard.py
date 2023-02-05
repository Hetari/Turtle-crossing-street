from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self, text: str, align: str, pos: tuple):
        super().__init__()
        self.penup()
        self.goto(pos)
        self.hideturtle()
        self.write(f"{text}", align=f"{align}", font=FONT, move=True)

    def update(self, text: str, pos: tuple):
        self.clear()
        self.goto(pos)
        self.write(f"{text}", align='center', font=FONT, move=True)

    def timing(self, text: str, pos: tuple):
        # self.clear()
        self.goto(pos)
        self.write(f"{text}", align='center', font=FONT, move=True)

    def game_over(self, pos: tuple):
        self.goto(pos)
        self.write("Game Over...", align='center', font=FONT, move=True)
