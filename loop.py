from utils import android_connection, global_utils
import logging
import os
import cv2
import subprocess
import numpy as np
import config
import time

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

android_connection.connect()

# Go to the play screen if not already
global_utils.find_and_click(
    config.project_path+'\\images\\go_to_play_button.png')

time.sleep(1)

# Go to the play
global_utils.find_and_click(
    config.project_path+'\\images\\play_button.png')

time.sleep(2)

# Wait until the game starts
global_utils.wait_until_gone(config.project_path+'\\images\\cancel_button.png')

time.sleep(2)
