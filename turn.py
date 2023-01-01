from utils import global_utils
import os
import cv2
import config
import random


# Give a screenshot, returns the player turn
def get_turn(screenshot, screenshot_dimensions, show_image):
    start = global_utils.start_timer()
    turn = config.turn
    actual_turn = 0
    turn = screenshot[
        turn['y1']:
        screenshot_dimensions[0] -
        turn['y2'],
        turn['x1']:
        screenshot_dimensions[1] -
        turn['x2']
    ]
    for turn_haystack in os.listdir(config.turns_folder):
        # Searching for a field in the folder.
        searched_turn = global_utils.search(
            config.turns_folder+"\\"+turn_haystack, turn, 1)
        if searched_turn[0] == 1:
            searched_turn_image = global_utils.draw(
                turn, searched_turn, turn_haystack[:-4], [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)])
            if show_image:
                cv2.imshow(turn_haystack[:-4], searched_turn_image)
            if turn_haystack[0] != 'f' and turn_haystack[0] != "c":
                if int(turn_haystack[0]) > actual_turn:
                    actual_turn = int(turn_haystack[0])
            elif turn_haystack[0] == 'f':
                return -1
            else:
                return -2
    end = global_utils.end_timer()
    global_utils.log_time_elapsed(
        "get_turn", end-start)
    return actual_turn
