from utils import global_utils
import logging
import cv2
import hand_cards
import fields
import field_cards
import mana
import turn
import time
import config


# Gets all the possible information from the screen
# Actual turn
# Mana to spend
# Cards in hand
# Active fields
# Available fields to play
def get_info(counter):
    # Printing information
    logging.info("---------------------------")
    logging.info("Picture: " + str(counter))

    # Take a screenhot and get its dimensions
    screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
    screenshot_dimensions = screenshot.shape

    # Go to the play screen if not already
    global_utils.find_and_click(
        config.project_path+'\\images\\go_to_play_button.png', screenshot)

    # Go to the play
    global_utils.find_and_click(
        config.project_path+'\\images\\play_button.png', screenshot)

    global_utils.find_and_click(
        config.project_path+'\\images\\next_button.png', screenshot)

    global_utils.find_and_click(
        config.project_path+'\\images\\turns\\collect_rewards.png', screenshot)

    # Detect turn
    player_turn = turn.get_turn(screenshot, screenshot_dimensions, True)
    logging.info('* Turn: ' + str(player_turn))

    # Detect mana
    remaining_mana = mana.get_mana(screenshot, screenshot_dimensions)
    logging.info('* Mana: ' + str(remaining_mana))

    # Detect my cards
    my_hand_cards = hand_cards.get_my_hand_cards(
        screenshot, screenshot_dimensions, counter, True)
    hand_cards.log_hand_cards(my_hand_cards)

    # Detect fields
    active_fields = fields.get_fields(screenshot, screenshot_dimensions, True)
    fields.log_fields(active_fields)

    # Detect field cards
    player_played_cards = field_cards.get_player_fields_cards(
        screenshot, screenshot_dimensions)
    field_cards.log_player_fields_cards(player_played_cards)

    cv2.waitKey(10)
    counter += 1
    return {
        'player_turn': player_turn,
        'mana': remaining_mana,
        'my_hand_cards': my_hand_cards,
        'active_fields': active_fields,
        'player_played_cards': player_played_cards,
        'counter': counter
    }
