import os
import glob
import config


def clear():
    files = glob.glob(config.tmp_path+'/*')
    for f in files:
        os.remove(f)
