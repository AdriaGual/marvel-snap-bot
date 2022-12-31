import os
import subprocess
import time
import config
import logging


def connect():
    os.chdir(config.adb_path)
    connect_result = os.popen("adb connect 127.0.0.1:5555").read()
    logging.info('Connection result: %s', connect_result)
