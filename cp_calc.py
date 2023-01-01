import cp_list
import field_cp


def check_field_available(field):
    for tile in field:
        if tile != 'x':
            return True
    return False


def remove_full_fields(play_info):
    first_field_available = check_field_available(
        play_info['player_played_cards'][0:4])
    second_field_available = check_field_available(
        play_info['player_played_cards'][4:8])
    third_field_available = check_field_available(
        play_info['player_played_cards'][8:12])
    active_fields = play_info['active_fields']
    if not first_field_available:
        active_fields.pop('first_field', None)
    if not second_field_available:
        active_fields.pop('second_field', None)
    if not third_field_available:
        active_fields.pop('third_field', None)
    return active_fields


# Given the field info, calculate the next play
# Returns the card coords and the field coords
def calc_play(play_info):
    max_cp_play = 0
    card_to_play = None

    # Pick the card to play
    for hand_card in play_info['my_hand_cards']:
        if cp_list.cps[hand_card[0]]['average_cp'] > max_cp_play and cp_list.cps[hand_card[0]]['mana'] <= play_info['mana']:
            max_cp_play = cp_list.cps[hand_card[0]]['average_cp']
            card_to_play = hand_card
    if not card_to_play:
        return [0, 0, 0]
    print(card_to_play)

    # Pick field to play the card
    active_fields = remove_full_fields(play_info)
    priority = -10
    priority_field = None
    if len(active_fields.keys()) > 1:
        for field in active_fields:
            field_name = active_fields[field]['name']
            print(field_name)
            if field_cp.field_list[field_name]['priority'] > priority and field_cp.field_list[field_name]['min_play'] == 1:
                priority = field_cp.field_list[field_name]['priority']
                priority_field = active_fields[field]
        return [1, card_to_play[1], priority_field['move_to']]
    elif len(active_fields.keys()) == 1:
        for field in active_fields.keys():
            field_name = active_fields[field]['name']
            if field_cp.field_list[field_name]['min_play'] == 1:
                return [1, card_to_play[1], active_fields[field]['move_to']]
            else:
                return [0, 0, 0]
    else:
        return [0, 0, 0]
    return 1
