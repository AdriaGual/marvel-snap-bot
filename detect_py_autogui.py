from utils import global_utils, android_connection
import pyautogui
import os
import config
from rembg import remove
import cv2
from hand_cards_number import get_hand_cards_number
import numpy as np
import logging


def get_hand_cards(screenshot, screenshot_dimensions):
    screenshot = screenshot[config.card_hand['x']:screenshot_dimensions[0] -
                            config.card_hand['y'], 0:screenshot_dimensions[1]]
    cv2.imwrite(config.tmp_path+"\\"+str(0)+".png", screenshot)

    haystack = config.tmp_path+"\\"+str(0)+".png"

    # Detect which cards are on my hand
    cards = {}
    for card_folder in os.listdir(config.data_folder):
        card_folder_path = config.data_folder+"\\"+card_folder
        for card_haystack in os.listdir(card_folder_path):
            card_needle = card_folder_path+"\\"+card_haystack
            card_location = pyautogui.locate(
                card_needle, haystack, grayscale=True, confidence=0.6)
            if not card_location is None:
                if (not card_folder in cards) or (card_folder in cards and abs(cards[card_folder]['pos_left']-card_location[0]) > 100):
                    cards[card_folder] = {
                        'pos_left': card_location[0],
                    }
    detected_n_cards = len(cards.keys())

    # Detect the number of cards
    screenshot = cv2.imread(haystack)
    screenshot_dimensions = screenshot.shape
    n_cards = get_hand_cards_number(
        False, screenshot, screenshot_dimensions, False)[0]
    return [cards, n_cards, detected_n_cards]
