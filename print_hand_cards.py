from utils import android_connection, global_utils
import config
import cv2


# Prints the current turn screenshot on the screen
android_connection.connect()
counter = 0
while True:
    screenshot = global_utils.take_screenshot("tmp\\"+str(counter+1)+".png")
    screenshot_dimensions = screenshot.shape

    my_cards = screenshot[config.card_hand['x']:screenshot_dimensions[0] -
                          config.card_hand['y'], 0:screenshot_dimensions[1]]
    cv2.imshow("My cards", my_cards)
    cv2.imwrite(config.project_path+"\\hand_cards_1.png", my_cards)
    cv2.waitKey(1)
    counter += 1
