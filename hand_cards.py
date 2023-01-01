from utils import global_utils
import os
import cv2
import config
import random
import logging


# Given a screenshot of the hand cards, returns a list of the detected cards
def get_my_hand_cards(screenshot, screenshot_dimensions, counter, show_image):
    start = global_utils.start_timer()
    file_name = config.project_path+"\\tmp\\hand_cards_" + str(counter)+".png"
    my_cards = screenshot[config.card_hand['x']:screenshot_dimensions[0] -
                          config.card_hand['y'], 0:screenshot_dimensions[1]]
    cv2.imwrite(file_name, my_cards)
    found_cards = []
    for card_folder in os.listdir(config.data_folder):
        card_folder_path = config.data_folder+"\\"+card_folder
        searched_card = global_utils.search_in_folder(
            card_folder_path, my_cards)
        if searched_card[0] == 1:
            my_cards = global_utils.draw(
                my_cards, searched_card, card_folder, [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)])
            cv2.imwrite(file_name, my_cards)
            found_cards.append(card_folder)
    if show_image:
        cv2.imshow("My cards", my_cards)
    end = global_utils.end_timer()
    global_utils.log_time_elapsed(
        "get_my_hand_cards", end-start)
    return found_cards


# Outputs the hand cards
def log_hand_cards(hand_cards):
    logging.info("Hand_cards: ")
    logging.info(hand_cards)
