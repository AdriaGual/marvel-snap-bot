from utils import global_utils
import os
import cv2
import config
import random
import logging


# Given a screenshot, returns a list of the detected fields
def get_fields(screenshot, screenshot_dimensions, show_image):
    start = global_utils.start_timer()
    fields = config.fields
    for field in fields.keys():
        fields[field]['image'] = screenshot[
            fields[field]['x1']:
            screenshot_dimensions[0] - fields[field]['x2'],
            fields[field]['y1']:
            screenshot_dimensions[1]-fields[field]['y2']
        ]
        for available_field in os.listdir(config.fields_folder):
            # Searching for a field in the folder.
            searched_field = global_utils.search(
                config.fields_folder+"\\"+available_field, fields[field]['image'])
            if searched_field[0] == 1:
                fields[field]['name'] = available_field[:-4]
                fields[field]['image'] = global_utils.draw(
                    fields[field]['image'], searched_field, available_field[:-4], [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)])
                cv2.imwrite(config.project_path+"\\tmp\\" +
                            available_field[:-4]+".png", fields[field]['image'])
        if show_image:
            cv2.imshow(field, fields[field]['image'])
    end = global_utils.end_timer()
    global_utils.log_time_elapsed(
        "get_fields", end-start)
    return fields


# Outputs the fields found
def log_fields(fields):
    logging.info('Acive fields: ')
    available_fields = []
    for field in fields.keys():
        available_fields.append(field + ": " + fields[field]['name'])
    logging.info(available_fields)
