from utils import android_connection, global_utils
import logging
import info
import hand_cards
import time
import config
import turn
import clear_tmp
import sys

logging.basicConfig(
    filename=config.project_path + "\\log.txt",
    filemode="w",
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG,
)
logging.getLogger().addHandler(logging.StreamHandler())

android_connection.connect()

counter = 0
last_move = [0, 0, 0]
while 1:
    global_utils.click([284, 46])
    # Take a screenhot and get its dimensions
    screenshot = global_utils.take_screenshot("tmp\\" + str(counter) + ".png")
    screenshot_dimensions = screenshot.shape

    # Click the icon menu to go to play if its in the screen
    global_utils.find_and_click(
        config.project_path + "\\images\\go_to_play_button.png", screenshot
    )

    # Click the play button if its in the screen
    global_utils.find_and_click(
        config.project_path + "\\images\\play_button.png", screenshot
    )

    # Click the next button if its in the screen
    global_utils.find_and_click(
        config.project_path + "\\images\\next_button.png", screenshot
    )

    # Click the collect rewards button if its in the screen
    global_utils.find_and_click(
        config.project_path + "\\images\\turns\\collect_rewards.png", screenshot
    )

    # Get the turn information, 0 if not found
    player_turn = turn.get_turn(screenshot, screenshot_dimensions, False)

    # While turn not found
    while player_turn == 0:
        # Take a screenshot of the actual field
        screenshot = global_utils.take_screenshot("tmp\\" + str(counter) + ".png")
        screenshot_dimensions = screenshot.shape

        # Get the turn information, 0 if not found
        player_turn = turn.get_turn(screenshot, screenshot_dimensions, False)

        # Click the play button if its in the screen
        global_utils.find_and_click(
            config.project_path + "\\images\\play_button.png", screenshot
        )

        # Click the next button if its in the screen
        global_utils.find_and_click(
            config.project_path + "\\images\\next_button.png", screenshot
        )

    # Click the End Turn button
    global_utils.click([755, 1487])

    counter += 1
    # if False:
    clear_tmp.clear()
