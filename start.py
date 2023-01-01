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


# Outputs the hand cards
def print_hand_cards(hand_cards):
    print('hand_cards: ')
    print(hand_cards)


# Given a screenshot, returns a list of the detected terrains
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


# Outputs the terrains found
def print_fields(fields):
    for field in fields.keys():
        print(field + ": " + fields[field]['name'])


# Checks a pixel radius for each card field position in order to determine which ones are already filled
def detect_player_field_cards():
    # Detect field cards
    terrains_my_played_cards = config.terrains_my_played_cards
    player_played_cards = []
    for my_played_cards in terrains_my_played_cards.keys():
        terrains_my_played_cards[my_played_cards]['image'] = screenshot[
            terrains_my_played_cards[my_played_cards]['y1']:
            screenshot_dimensions[0] -
            terrains_my_played_cards[my_played_cards]['y2'],
            terrains_my_played_cards[my_played_cards]['x1']:
            screenshot_dimensions[1] -
            terrains_my_played_cards[my_played_cards]['x2']
        ]
        for card in terrains_my_played_cards[my_played_cards]['cards']:
            max_score = 0
            for x in range(10):
                for y in range(10):
                    score = screenshot[terrains_my_played_cards[my_played_cards]['cards'][card]
                                       [1]+x, terrains_my_played_cards[my_played_cards]['cards'][card][0]+y][2]
                    if score > max_score:
                        max_score = score
            if max_score > 200:
                player_played_cards.append("x")
            else:
                player_played_cards.append("-")
    return player_played_cards


# Outputs field cards
def print_player_field_cards(player_played_cards):
    print("Player field cards")
    print("-------------------")
    print("||" + str(player_played_cards[0])+"|"+str(player_played_cards[1]) +
          "||"+"|" + str(player_played_cards[4])+"|"+str(player_played_cards[5])+"||"+"|" + str(player_played_cards[8])+"|"+str(player_played_cards[9]) +
          "||")
    print("||" + str(player_played_cards[2])+"|"+str(player_played_cards[3]) +
          "||"+"|" + str(player_played_cards[6])+"|"+str(player_played_cards[7])+"||"+"|" + str(player_played_cards[10])+"|"+str(player_played_cards[11]) +
          "||")
    print("-------------------")


# Give a screenshot, returns the player mana
def detect_mana(screenshot):
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
        # Searching for a terrain in the folder.
        searched_mana = global_utils.search(
            config.mana_folder+"\\"+mana_haystack, mana, 1)
        if searched_mana[0] == 1:
            remaining_mana = int(mana_haystack[0])
    return remaining_mana


# Give a screenshot, returns the player turn
def detect_turn(screenshot):
    turn = config.turn
    turn = screenshot[
        turn['y1']:
        screenshot_dimensions[0] -
        turn['y2'],
        turn['x1']:
        screenshot_dimensions[1] -
        turn['x2']
    ]
    cv2.imshow('turn', turn)
    for turn_haystack in os.listdir(config.turn_folder):
        # Searching for a terrain in the folder.
        searched_turn = global_utils.search(
            config.turn_folder+"\\"+turn_haystack, turn, 1)
        if searched_turn[0] == 1:
            return searched_turn
    return 0


logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

android_connection.connect()

counter = 0
while 1:
    screenshot = global_utils.take_screenshot("\\tmp\\"+str(counter)+".png")
    cv2.imwrite(config.project_path + "\\tmp\\" +
                "_" + str(counter) + ".png", screenshot)
    screenshot_dimensions = screenshot.shape

    # Detect my cards
    # hand_cards = detect_my_hand_cards(screenshot, screenshot_dimensions)
    # print_hand_cards(hand_cards)

    # Detect terrains
    #fields = detect_terrains(screenshot, screenshot_dimensions)
    # print_fields(fields)

    # Detect field cards
    #player_played_cards = detect_player_field_cards()
    # print_player_field_cards(player_played_cards)

    # Detect mana
    #remaining_mana = detect_mana(screenshot)

    # Detect turn
    #turn = detect_turn(screenshot)

    # Printing information
    print("---------------------")
    print("Picture: " + str(counter))

    cv2.waitKey(10)
    counter += 1
