from utils import android_connection, global_utils
import logging
import os
from os import listdir
import cv2
import subprocess
import numpy as np
import config
import time
import random


# Given a screenshot of the hand cards, returns a list of the detected cards
def detect_my_hand_cards(screenshot, screenshot_dimensions):
    file_name = config.project_path+"\\tmp\\" + str(counter)+".png"
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
    cv2.imshow("My cards", my_cards)
    return found_cards


# Given a screenshot, returns a list of the detected cards
def detect_terrains(screenshot, screenshot_dimensions):
    fields = config.fields
    for field in fields.keys():
        fields[field]['image'] = screenshot[
            fields[field]['x1']:
            screenshot_dimensions[0] - fields[field]['x2'],
            fields[field]['y1']:
            screenshot_dimensions[1]-fields[field]['y2']
        ]
        for terrain in os.listdir(config.terrain_folder):
            # Searching for a terrain in the folder.
            searched_terrain = global_utils.search(
                config.terrain_folder+"\\"+terrain, fields[field]['image'])
            if searched_terrain[0] == 1:
                fields[field]['name'] = terrain[:-4]
                fields[field]['image'] = global_utils.draw(
                    fields[field]['image'], searched_terrain, terrain[:-4], [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)])
                cv2.imwrite(config.project_path+"\\tmp\\" +
                            terrain[:-4]+".png", fields[field]['image'])
        cv2.imshow(field, fields[field]['image'])
    return fields


# Given a screenshot of the player field cards, returns a list of the detected cards
def detect_cards(screenshot, name):
    file_name = config.project_path+"\\tmp\\" + str(counter)+".png"
    cv2.imwrite(file_name,screenshot)
    found_cards = []
    for card_folder in os.listdir(config.data_folder):
        card_folder_path = config.data_folder+"\\"+card_folder
        searched_card = global_utils.search_in_folder(
            card_folder_path, screenshot)
        if searched_card[0] == 1:
            screenshot = global_utils.draw(
                screenshot, searched_card, card_folder, [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)])
            cv2.imwrite(file_name, screenshot)
            found_cards.append(card_folder)
    cv2.imshow(name, screenshot)
    return found_cards


logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

android_connection.connect()

counter = 0
while 1:
    screenshot = global_utils.take_screenshot("\\tmp\\"+str(counter)+".png")
    screenshot_dimensions = screenshot.shape
    # Detect my cards
    hand_cards = detect_my_hand_cards(screenshot, screenshot_dimensions)

    # Detect terrains
    fields = detect_terrains(screenshot, screenshot_dimensions)

    # Detect field cards
    terrains_my_played_cards = config.terrains_my_played_cards
    for my_played_cards in terrains_my_played_cards.keys():
        terrains_my_played_cards[my_played_cards]['image'] = screenshot[
            terrains_my_played_cards[my_played_cards]['y1']:
            screenshot_dimensions[0] -
            terrains_my_played_cards[my_played_cards]['y2'],
            terrains_my_played_cards[my_played_cards]['x1']:
            screenshot_dimensions[1] -
            terrains_my_played_cards[my_played_cards]['x2']
        ]
        terrains_my_played_cards[my_played_cards]['cards'] = detect_cards(
            terrains_my_played_cards[my_played_cards]['image'], my_played_cards)

    # Printing information
    print("---------------------")
    print("Picture: " + str(counter))
    print('hand_cards: ')
    print(hand_cards)
    for field in fields.keys():
        print(field + ": " + fields[field]['name'])
    for my_played_cards in terrains_my_played_cards.keys():
        print(terrains_my_played_cards[my_played_cards]['cards'])
    cv2.waitKey(10)
    counter += 1
