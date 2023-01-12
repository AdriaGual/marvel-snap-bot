from utils import android_connection, global_utils
import config
import cv2


# Prints the current turn screenshot on the screen
android_connection.connect()
counter = 0
while True:
    screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
    screenshot_dimensions = screenshot.shape
    config_turn = config.turn
    turn_image = screenshot[
        config_turn['y1']:
        screenshot_dimensions[0] -
        config_turn['y2'],
        config_turn['x1']:
        screenshot_dimensions[1] -
        config_turn['x2']
    ]
    cv2.imshow('turn', turn_image)
    cv2.waitKey(1)
    counter += 1
