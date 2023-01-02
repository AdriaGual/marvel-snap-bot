from utils import android_connection, global_utils
import logging
import info
import cp_calc
import hand_cards
import time
import config
import turn
import cv2

logging.basicConfig(filename='log.txt', filemode='w', format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

android_connection.connect()

counter = 0
last_move = []
while 1:
    global_utils.click([284, 46])
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

    player_turn = turn.get_turn(screenshot, screenshot_dimensions, False)
    while player_turn == 0:
        screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
        screenshot_dimensions = screenshot.shape
        player_turn = turn.get_turn(screenshot, screenshot_dimensions, False)
        global_utils.find_and_click(
            config.project_path+'\\images\\play_button.png', screenshot)

        global_utils.find_and_click(
            config.project_path+'\\images\\next_button.png', screenshot)
        time.sleep(0.5)

    play_info = info.get_info(
        counter, screenshot, screenshot_dimensions, player_turn)
    counter = play_info['counter']
    if play_info['player_turn'] != 0:
        if play_info['mana'] > 0:
            play_to_make = cp_calc.calc_play(play_info)
            if last_move != play_to_make:
                if play_to_make[0] == 1:
                    global_utils.drag(
                        [play_to_make[1][0]+20, play_to_make[1][1]+1200], play_to_make[2])
                    last_move = play_to_make
                else:
                    possible_fields = [[198, 1036], [455, 1036], [711, 1036]]
                    possible_cards = [[441, 1300], [700, 1300], [100, 1300]]
                    for possible_card in possible_cards:
                        for possible_field in possible_fields:
                            global_utils.drag(possible_card, possible_field)
            else:
                possible_fields = [[198, 1036], [455, 1036], [711, 1036]]
                for possible_field in possible_fields:
                    global_utils.drag(
                        [play_to_make[1][0]+20, play_to_make[1][1]+1200], possible_field)
        else:
            global_utils.click([755, 1487])
    time.sleep(1)
