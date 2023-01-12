from utils import android_connection, global_utils
import config
import cv2


# Prints the current turn screenshot on the screen
android_connection.connect()
counter = 0
while True:
    screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
    screenshot_dimensions = screenshot.shape
    fields = config.fields
    for field in fields.keys():
        fields[field]['image'] = screenshot[
            fields[field]['x1']:
            screenshot_dimensions[0] - fields[field]['x2'],
            fields[field]['y1']:
            screenshot_dimensions[1]-fields[field]['y2']
        ]
        cv2.imshow(fields[field]['name'], fields[field]['image'])
    cv2.waitKey(1)
    counter += 1
