from utils import android_connection, global_utils
import logging
import info
import cp_calc
import hand_cards

logging.basicConfig(filename='log.txt', filemode='w', format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

android_connection.connect()

counter = 0
while 1:
    play_info = info.get_info(counter)
    """ return {
        'player_turn': player_turn,
        'mana': remaining_mana,
        'my_hand_cards': my_hand_cards,
        'active_fields': active_fields,
        'player_played_cards': player_played_cards,
        'counter': counter
    } """
    counter = play_info['counter']
    if play_info['mana'] > 0 and play_info['player_turn'] != 0:
        play_to_make = cp_calc.calc_play(play_info)
        if play_to_make[0] == 1:
            global_utils.drag(
                [play_to_make[1][0]+20, play_to_make[1][1]+1200], play_to_make[2])
        else:
            hand_cards.try_to_play_every_card(
                play_info['my_hand_cards'], play_info['active_fields'])
            global_utils.click([755, 1487])
    else:
        hand_cards.try_to_play_every_card(
            play_info['my_hand_cards'], play_info['active_fields'])
        global_utils.click([755, 1487])
