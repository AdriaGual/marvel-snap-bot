from utils import android_connection, global_utils
import logging
import info

logging.basicConfig(filename='log.txt', filemode='w', format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

android_connection.connect()

counter = 0
while 1:
    play_info = info.get_info(counter)
    counter = play_info['counter']
