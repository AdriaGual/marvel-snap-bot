from utils import global_utils
import os
import config


# Give a screenshot, returns the player mana
def get_mana(screenshot, screenshot_dimensions):
    start = global_utils.start_timer()
    remaining_mana = 0
    mana = config.mana
    mana = screenshot[
        mana['y1']:
        screenshot_dimensions[0] -
        mana['y2'],
        mana['x1']:
        screenshot_dimensions[1] -
        mana['x2']
    ]
    for mana_haystack in os.listdir(config.mana_folder):
        # Searching for a field in the folder.
        searched_mana = global_utils.search(
            config.mana_folder+"\\"+mana_haystack, mana, 1)
        if searched_mana[0] == 1:
            remaining_mana = int(mana_haystack[0])
    end = global_utils.end_timer()
    global_utils.log_time_elapsed(
        "get_mana", end-start)
    return remaining_mana
