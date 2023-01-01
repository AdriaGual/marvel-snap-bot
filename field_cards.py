from utils import global_utils
import config
import logging


# Checks a pixel radius for each card field position in order to determine which ones are already filled
def get_player_fields_cards(screenshot, screenshot_dimensions):
    start = global_utils.start_timer()
    # Detect field cards
    fields_my_played_cards = config.fields_my_played_cards
    player_played_cards = []
    for my_played_cards in fields_my_played_cards.keys():
        fields_my_played_cards[my_played_cards]['image'] = screenshot[
            fields_my_played_cards[my_played_cards]['y1']:
            screenshot_dimensions[0] -
            fields_my_played_cards[my_played_cards]['y2'],
            fields_my_played_cards[my_played_cards]['x1']:
            screenshot_dimensions[1] -
            fields_my_played_cards[my_played_cards]['x2']
        ]
        for card in fields_my_played_cards[my_played_cards]['cards']:
            max_score = 0
            for x in range(10):
                for y in range(10):
                    score = screenshot[fields_my_played_cards[my_played_cards]['cards'][card]
                                       [1]+x, fields_my_played_cards[my_played_cards]['cards'][card][0]+y][2]
                    if score > max_score:
                        max_score = score
            if max_score > 200:
                player_played_cards.append("x")
            else:
                player_played_cards.append("-")
    end = global_utils.end_timer()
    global_utils.log_time_elapsed(
        "get_player_fields_cards", end-start)
    return player_played_cards


# Outputs field cards
def log_player_fields_cards(player_played_cards):
    logging.info("Player field cards:")
    logging.info("---------------------------")
    logging.info("| |" + str(player_played_cards[0])+"|"+str(player_played_cards[1]) +
                 "| ||"+" |" + str(player_played_cards[4])+"|"+str(player_played_cards[5])+"| ||"+" |" + str(player_played_cards[8])+"|"+str(player_played_cards[9]) +
                 "| |")
    logging.info("| |" + str(player_played_cards[2])+"|"+str(player_played_cards[3]) +
                 "| ||"+" |" + str(player_played_cards[6])+"|"+str(player_played_cards[7])+"| ||"+" |" + str(player_played_cards[10])+"|"+str(player_played_cards[11]) +
                 "| |")
    logging.info("---------------------------")
