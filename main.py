# Importing the classes from the other files.
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    # Setting up the screen.
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Creating an instance of the Player, CarManager, and Scoreboard classes.
    cars = CarManager()
    player = Player()

    # Listening for the user to press the up arrow key only.
    screen.listen()
    screen.onkeypress(player.up, 'Up')
    level = Scoreboard(f'Level {player.level}', 'center', (-240, 260))

    # This is a while loop that is checking if the game is on. If it is, it will update the screen, create
    game_is_on = True
    while game_is_on:
        screen.update()
        level.update(f'Level {player.level}', (-240, 260))

        # a car, move the car, check if the player is winning.
        cars.create_car()
        cars.move()
        player.winning(player.level)

        # Check if the player is colliding with a car. If the player is colliding with a car, the game will end.
        for car in cars.cars:
            if car.distance(player) < 20:
                game_over = Scoreboard('Game Over...', 'center', (0, 0))
                game_is_on = False

    # Allowing the user to click on the screen to exit the game.
    screen.exitonclick()


if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        main()
    except Exception as _:
        pass
    finally:
        print("Exit...")
