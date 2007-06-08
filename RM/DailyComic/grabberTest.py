import housekeeper
import unittest
import os
import time
import random
from os.path import isdir,join

class TestGrabber(unittest.TestCase):
    basedir = "/Users/rijam/Pictures/DailyComic/tests"

    def setUp(self):
        pass
    def tearDown(self):
# remove all directories in basedir
        os.system("rm -rf "+TestGrabber.basedir) 
        pass
    def testDownloadPicture(self):
        pass

if __name__ == '__main__':
    unittest.main()

