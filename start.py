from utils import android_connection, global_utils
import logging
import cv2
import time
import hand_cards
import fields
import field_cards
import mana
import turn


logging.basicConfig(filename='log.txt', filemode='w', format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

android_connection.connect()

counter = 0
while 1:
    # Printing information
    logging.info("---------------------")
    logging.info("Picture: " + str(counter))

    # Take a screenhot and get its dimensions
    screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
    screenshot_dimensions = screenshot.shape

    # Detect my cards
    my_hand_cards = hand_cards.get_my_hand_cards(
        screenshot, screenshot_dimensions, counter, False)
    hand_cards.log_hand_cards(my_hand_cards)

    # Detect fields
    active_fields = fields.get_fields(screenshot, screenshot_dimensions, False)
    fields.log_fields(active_fields)

    # Detect field cards
    player_played_cards = field_cards.get_player_fields_cards(
        screenshot, screenshot_dimensions)
    field_cards.log_player_fields_cards(player_played_cards)

    # Detect mana
    remaining_mana = mana.get_mana(screenshot, screenshot_dimensions)
    logging.info('remaining_mana: ' + str(remaining_mana))

    # Detect turn
    player_turn = turn.get_turn(screenshot, screenshot_dimensions, False)
    logging.info('turn: ' + str(player_turn))

    cv2.waitKey(10)
    time.sleep(2)
    counter += 1
