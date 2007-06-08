import housekeeper
import unittest
import os
import time
import random
from os.path import isdir,join

class TestHouseKeeper(unittest.TestCase):
    basedir = "/Users/rijam/Pictures/DailyComic/tests"
    curday = time.strftime("%Y/%m/%d")
    curmonth = time.strftime("%m")
    curyear = time.strftime("%Y")

    anothermonth = random.randint(1,12)
    anotherday = random.randint(1,31)
    anotheryear = 1977
    while (anothermonth == curmonth):
        anothermonth = random.randint(1,12)
    while (anotherday == curday):
        anotherday = random.randint(1,31)


    def setUp(self):
        try:
# make a current directory, 
            os.makedirs(join(TestHouseKeeper.basedir,TestHouseKeeper.curday))
# and old directory of the same month,
            os.makedirs(TestHouseKeeper.basedir+"/"+TestHouseKeeper.curyear+"/"+TestHouseKeeper.curmonth+"/"+str(TestHouseKeeper.anotherday))
# an older directory of another month
            os.makedirs(TestHouseKeeper.basedir+"/"+TestHouseKeeper.curyear+"/"+str(TestHouseKeeper.anothermonth)+"/"+"01")
# another from another year
            os.makedirs(TestHouseKeeper.basedir+"/"+str(TestHouseKeeper.anotheryear)+"/"+str(TestHouseKeeper.anothermonth)+"/"+"01")
        except OSError:
            print "error creating current directory"
        pass

    def tearDown(self):
# remove all directories in basedir
        os.system("rm -rf "+TestHouseKeeper.basedir) 
        pass

    def testSweepOldData(self):
        """test that housekeeper.SweepOldData remove old directories but not current day directories"""
        
# assert the state of the filesystem before calling the function to test
        self.failUnless(isdir(join(TestHouseKeeper.basedir,TestHouseKeeper.curday)))
        self.failUnless(isdir(TestHouseKeeper.basedir+"/"+TestHouseKeeper.curyear+"/"+TestHouseKeeper.curmonth+"/"+str(TestHouseKeeper.anotherday)))
        self.failUnless(isdir(TestHouseKeeper.basedir+"/"+TestHouseKeeper.curyear+"/"+str(TestHouseKeeper.anothermonth)+"/"+"01"))
        self.failUnless(isdir(TestHouseKeeper.basedir+"/"+str(TestHouseKeeper.anotheryear)+"/"+str(TestHouseKeeper.anothermonth)+"/"+"01"))

# calling the function to test
        housekeeper.sweepOldData(basedir=TestHouseKeeper.basedir)

# assert the state of the filesystem after function to test has been called
        self.failUnless(isdir(join(TestHouseKeeper.basedir,TestHouseKeeper.curday)))
        self.failIf(isdir(TestHouseKeeper.basedir+"/"+TestHouseKeeper.curyear+"/"+TestHouseKeeper.curmonth+"/"+str(TestHouseKeeper.anotherday)))
        self.failIf(isdir(TestHouseKeeper.basedir+"/"+TestHouseKeeper.curyear+"/"+str(TestHouseKeeper.anothermonth)+"/"+"01"))
        self.failIf(isdir(TestHouseKeeper.basedir+"/"+str(TestHouseKeeper.anotheryear)+"/"+str(TestHouseKeeper.anothermonth)+"/"+"01"))
        pass

if __name__ == '__main__':
    unittest.main()


