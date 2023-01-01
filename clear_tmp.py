import os
import glob
import config

files = glob.glob(config.tmp_path+'/*')
for f in files:
    os.remove(f)
