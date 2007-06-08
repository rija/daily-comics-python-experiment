import os
import time
import time
from os.path import join, getsize

def sweepOldData(**keywords):
    """this method will remove all directories for past days
    """
# setting up basedir
    if('basedir' in keywords.keys()):
        basedir = keywords['basedir']
    else:
        basedir = "/Users/rijam/Pictures/DailyComic/"

# remove all past directories and files except current day
    curday = time.strftime("%Y/%m/%d")
    for root, dirs, files in os.walk(basedir,topdown=False):
        if(root == join(basedir,curday)):
            continue
        for file in  files:
            os.unlink(join(root,file))
        if(root == basedir):
            break
        try:
            os.rmdir(root)
        except OSError:
            pass


