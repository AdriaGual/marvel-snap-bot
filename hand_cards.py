from utils import global_utils
import os
import cv2
import config
import random
import logging
import cp_calc

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
            found_cards.append([card_folder, searched_card[1]])
    if show_image:
        cv2.imshow("My cards", my_cards)
    end = global_utils.end_timer()
    global_utils.log_time_elapsed(
        "get_my_hand_cards", end-start)
    return found_cards


# Outputs the hand cards
def log_hand_cards(hand_cards):
    logging.info("Hand_cards: ")
    for hand_card in hand_cards:
        logging.info(hand_card[0])


# Try every card
def try_to_play_every_card(cards, fields):
    for card in cards:
        for field in fields.keys():
            global_utils.drag(
                [card[1][0]+20, card[1][1]+1200], fields[field]['move_to'])


# Play a card to a certain field
def play_a_card_to_a_field(card_position, field):
    global_utils.drag([card_position[0]+20, card_position[1]+1200], field)
    global_utils.click([284, 46])


# Play every card in hand to every possible field
def play_random_cards():
    for possible_card in config.possible_cards:
        for possible_field in config.possible_fields:
            global_utils.drag(possible_card, possible_field)
            global_utils.click([284, 46])


# Play a certain card in hand to every possible field
def play_a_card_to_every_field(card_position):
    for possible_field in config.possible_fields:
        global_utils.drag(
            [card_position[0]+20, card_position[1]+1200], possible_field)
        global_utils.click([284, 46])


def play_cards(play_info, last_move):
    # If we have mana to play
    if play_info['mana'] > 0:
        # Get the best possible card and the field to play
        play_to_make = cp_calc.calc_play(play_info)
        # Check if we are trying to make the same play
        if last_move[1] != play_to_make[1] and last_move[2] != play_to_make[2]:
            # If we know the card and there's a field to play
            if play_to_make[0] == 1 and len(play_info['active_fields']) > 0:
                # Play the card
                play_a_card_to_a_field(
                    play_to_make[1], play_to_make[2])
                # Save the last_move
                last_move = play_to_make
            elif play_to_make[0] == 1:
                play_a_card_to_every_field(play_to_make[1])
                play_random_cards()
            else:
                play_random_cards()
        else:
            play_a_card_to_every_field(play_to_make[1])
            play_random_cards()
    else:
        global_utils.click([755, 1487])
    return last_move
