import os
import time
import urllib
from xml.dom import minidom
import re

def downloadPicture():
    """This method will download the latest comic from xkcd.org
    """
# creating target directory
    basedir = "/Users/rija/Pictures/DailyComic/"
    curday = time.strftime("%Y/%m/%d")
    targetdir = basedir + curday
    print targetdir
    try:
        os.makedirs(targetdir)
    except OSError:
        print "Directory already exists"
    else:
        print "Directory created"


# downloading the ressource
    url = "http://www.xkcd.org"
    sock = urllib.urlopen(url)
    webpage = sock.read()
    sock.close()

# parsing the ressource for the image
    targetelt = "h3"
    dom = minidom.parseString(webpage)
    results = []
    rawtext = ''
    imageurl = ''
    for node in dom.getElementsByTagName(targetelt):
        rawtext =  node.firstChild.data
        break

    pattern = re.compile('.*?: (.*)$')
    match = pattern.match(rawtext)
    if match:
        imageurl = match.group(1)
    else:
        print "No match"

# retrieving image data

    url = imageurl
    sock = urllib.urlopen(url)
    imagedata = sock.read()
    sock.close()

# Write the image in the directory
    print targetdir
    try:
        try:
            out = open(targetdir + '/' + 'xkcd.png','w')
            out.write(imagedata)
        finally:
            out.close()
    except IOError:
        print "Can't write the file"

    pass
