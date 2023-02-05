# Importing the classes from the other files.
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


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
    start_time = time.time()
    while game_is_on:
        end_time = time.time()
        screen.update()
        time.sleep(float(0.1))
        level.update(f'Level {player.level}', (-240, 260))

        # timing.timer(mint)
        timing = end_time - start_time
        level.timing('{:.1f}'.format(timing), (240, 260))
        # a car, move the car, check if the player is winning.
        cars.create_car()
        cars.move()
        if player.is_finish_laine():
            player.go_to_start()
            cars.level_up()

        # Check if the player is colliding with a car. If the player is colliding with a car, the game will end.
        for car in cars.cars:
            if car.distance(player) < 20:
                level.game_over((0, 0))
                game_is_on = False

    # Allowing the user to click on the screen to exit the game.
    screen.exitonclick()


if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        main()

    except KeyboardInterrupt:
        pass

    # except Exception:
    #     pass

    finally:
        print("Exit...")
