#!/usr/bin/env python

from RM.DailyComic import grabber
from RM.DailyComic import housekeeper

housekeeper.sweepOldData()
grabber.downloadPicture()
