# Import required modules and classes
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


def main():
    """
    The main function to set up the game environment, control game flow, and handle user interactions.
    It creates instances of Player, CarManager, and Scoreboard, handles screen events, and runs the game loop.
    """
    # Setting up the game window
    screen = Screen()
    screen.setup(width=600, height=600)  # Set screen dimensions
    screen.tracer(0)  # Disable automatic screen updates for smoother animations

    # Create instances of CarManager, Player, and Scoreboard
    cars = CarManager()  # Manages the cars in the game
    player = Player()  # Controls the player's turtle
    level = Scoreboard(f'Level {player.level}', 'center', (-240, 260))  # Display the current level on the screen

    # Set up keyboard controls
    screen.listen()  # Start listening for keyboard inputs
    screen.onkeypress(player.up, 'Up')  # Move the player upward when the up arrow is pressed

    # Game state variables
    game_is_on = True  # Boolean to track if the game is running
    start_time = time.time()  # Start the game timer

    # Main game loop
    while game_is_on:
        end_time = time.time()  # Track the current time
        screen.update()  # Manually update the screen
        time.sleep(0.1)  # Pause the loop briefly to control the speed of the game

        # Update the level display and timing
        level.update(f'Level {player.level}', (-240, 260))  # Update the current level display
        timing = end_time - start_time  # Calculate the elapsed time
        level.timing(f'{timing:.1f}', (240, 260))  # Display the timer on the screen

        # Create and move cars
        cars.create_car()  # Randomly create new cars
        cars.move()  # Move the cars across the screen

        # Check if the player has reached the finish line and proceed to the next level
        if player.is_finish_line():
            player.go_to_start()  # Reset player to the starting position
            cars.level_up()  # Increase car speed as the game progresses

        # Detect collision between the player and cars
        for car in cars.cars:
            if car.distance(player) < 20:  # Check if the player is too close to a car
                level.game_over((0, 0))  # Display the "Game Over" message
                game_is_on = False  # End the game

    # Exit the game when the user clicks on the screen
    screen.exitonclick()


if __name__ == '__main__':
    # Main program execution with exception handling for interruptions or other issues
    try:
        main()

    except KeyboardInterrupt:
        pass  # Handle keyboard interruption (Ctrl+C)

    except Exception:
        pass  # Handle any other exceptions

    finally:
        print("Exit...")  # Print exit message when the game ends
