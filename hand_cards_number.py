from utils import global_utils
from PIL import Image
import cv2
import config
from rembg import remove

condition_blue_range = {
    'red': [5, 50],
    'green': [20, 60],
    'blue': [60, 150],
}

condition_light_blue_range = {
    'red': [7, 30],
    'green': [55, 90],
    'blue': [145, 250],
}

condition_sky_blue_range = {
    'red': [20, 60],
    'green': [70, 110],
    'blue': [185, 255],
}

condition_dark_blue_range = {
    'red': [10, 35],
    'green': [10, 45],
    'blue': [40, 80],
}

condition_brown_range = {
    'red': [30, 75],
    'green': [15, 50],
    'blue': [30, 60],
}

condition_dark_brown_range = {
    'red': [5, 25],
    'green': [5, 25],
    'blue': [5, 60],
}

condition_purple_range = {
    'red': [30, 45],
    'green': [15, 25],
    'blue': [35, 60],
}

condition_dark_purple_range = {
    'red': [50, 90],
    'green': [30, 60],
    'blue': [95, 150],
}

condition_light_pink_range = {
    'red': [100, 255],
    'green': [20, 100],
    'blue': [40, 255],
}

condition_red_range = {
    'red': [70, 110],
    'green': [20, 65],
    'blue': [40, 70],
}

condition_white_range = {
    'red': [250, 255],
    'green': [250, 255],
    'blue': [250, 255],
}

blue_exact = [0, 0, 192]


# Colors to clear the background
def is_in_color_range(r, g, b):
    condition_blue = (r >= condition_blue_range['red'][0] and r <= condition_blue_range['red'][1]
                      and g >= condition_blue_range['green'][0] and g <= condition_blue_range['green'][1]
                      and b >= condition_blue_range['blue'][0] and b <= condition_blue_range['blue'][1])

    condition_light_blue = (r >= condition_light_blue_range['red'][0] and r <= condition_light_blue_range['red'][1]
                            and g >= condition_light_blue_range['green'][0] and g <= condition_light_blue_range['green'][1]
                            and b >= condition_light_blue_range['blue'][0] and b <= condition_light_blue_range['blue'][1])

    condition_sky_blue = (r >= condition_sky_blue_range['red'][0] and r <= condition_sky_blue_range['red'][1]
                          and g >= condition_sky_blue_range['green'][0] and g <= condition_sky_blue_range['green'][1]
                          and b >= condition_sky_blue_range['blue'][0] and b <= condition_sky_blue_range['blue'][1])

    condition_dark_blue = (r >= condition_dark_blue_range['red'][0] and r <= condition_dark_blue_range['red'][1]
                           and g >= condition_dark_blue_range['green'][0] and g <= condition_dark_blue_range['green'][1]
                           and b >= condition_dark_blue_range['blue'][0] and b <= condition_dark_blue_range['blue'][1])

    condition_brown = (r >= condition_brown_range['red'][0] and r <= condition_brown_range['red'][1]
                       and g >= condition_brown_range['green'][0] and g <= condition_brown_range['green'][1]
                       and b >= condition_brown_range['blue'][0] and b <= condition_brown_range['blue'][1])

    condition_dark_brown = (r >= condition_dark_brown_range['red'][0] and r <= condition_dark_brown_range['red'][1]
                            and g >= condition_dark_brown_range['green'][0] and g <= condition_dark_brown_range['green'][1]
                            and b >= condition_dark_brown_range['blue'][0] and b <= condition_dark_brown_range['blue'][1])

    condition_purple = (r >= condition_purple_range['red'][0] and r <= condition_purple_range['red'][1]
                        and g >= condition_purple_range['green'][0] and g <= condition_purple_range['green'][1]
                        and b >= condition_purple_range['blue'][0] and b <= condition_purple_range['blue'][1])

    condition_dark_purple = (r >= condition_dark_purple_range['red'][0] and r <= condition_dark_purple_range['red'][1]
                             and g >= condition_dark_purple_range['green'][0] and g <= condition_dark_purple_range['green'][1]
                             and b >= condition_dark_purple_range['blue'][0] and b <= condition_dark_purple_range['blue'][1])

    condition_light_pink = (r >= condition_light_pink_range['red'][0] and r <= condition_light_pink_range['red'][1]
                            and g >= condition_light_pink_range['green'][0] and g <= condition_light_pink_range['green'][1]
                            and b >= condition_light_pink_range['blue'][0] and b <= condition_light_pink_range['blue'][1])

    condition_red = (r >= condition_red_range['red'][0] and r <= condition_red_range['red'][1]
                     and g >= condition_red_range['green'][0] and g <= condition_red_range['green'][1]
                     and b >= condition_red_range['blue'][0] and b <= condition_red_range['blue'][1])

    condition_white = (r >= condition_white_range['red'][0] and r <= condition_white_range['red'][1]
                       and g >= condition_white_range['green'][0] and g <= condition_white_range['green'][1]
                       and b >= condition_white_range['blue'][0] and b <= condition_white_range['blue'][1])
    condition_blue_exact = r == blue_exact[0] and g == blue_exact[1] and b == blue_exact[2]

    # if condition_blue or condition_light_blue or condition_sky_blue or condition_dark_blue or condition_dark_brown or condition_purple or condition_brown or condition_dark_purple or condition_light_pink or condition_red or condition_white or condition_blue_exact:
    if condition_dark_brown or condition_brown or condition_dark_purple or condition_light_pink or condition_red or condition_purple or condition_white or condition_blue_exact:
        return True
    else:
        return False


# Card ranges
def cards_range(x, y):
    if x < 200:
        return 1
    elif x > 200 and x < 400:
        return 2
    elif x > 400 and x < 600:
        return 3
    elif x > 600 and x < 700:
        return 4
    elif x > 700 and x < 730:
        return 6
    else:
        if y > 200:
            return 5
        else:
            return 7


# Get the number of cards
def get_hand_cards_number(show_images, screenshot, screenshot_dimensions, full_screen):
    start = global_utils.start_timer()

    if full_screen:
        my_cards = screenshot[config.card_hand['x']:screenshot_dimensions[0] -
                              config.card_hand['y'], 0:screenshot_dimensions[1]]
    else:
        my_cards = screenshot

    cv2.imwrite(config.tmp_hand_cards_number_path, my_cards)
    image = Image.open(config.tmp_hand_cards_number_path)
    image_data = image.load()
    height, width = image.size

    for loop1 in range(height):
        for loop2 in range(width):
            r, g, b = image_data[loop1, loop2]
            if is_in_color_range(r, g, b):
                image_data[loop1, loop2] = 0, 0, 0
    image = remove(image)
    image.save(config.tmp_image_without_bg_path)
    img_1 = cv2.imread(config.tmp_image_without_bg_path)

    imgray_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(imgray_1, 0, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key=cv2.contourArea)
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    cv2.drawContours(img_1, [c], contourIdx=-1,
                     color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

    if show_images:
        cv2.imshow('Image', img_1)
        image = cv2.imread(config.tmp_image_without_bg_path)
        cv2.imshow('Image2', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    end = global_utils.end_timer()
    global_utils.log_time_elapsed(
        "get_my_hand_cards_number", end-start)
    return cards_range(extRight[0]-extLeft[0], extBot[1]-extTop[1])
