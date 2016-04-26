#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/11/16 5:30 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import json
import sys

from root import *


class PyMp4:
    """
    the main class to parse a mp4 file
    """

    def __init__(self, fname):
        if fname == None:
            print "file == None"
            return

        self.filename = fname
        self.root = None

    def ParseMp4(self):
        filesize = os.path.getsize(self.filename)
        with open(self.filename, 'rb') as mp4_file:
            file_strm = FileStream(mp4_file)
            self.root = Root(file_strm, filesize)
            self.root.decode()

    def __str__(self):
        meta_data = json.dumps(self.root.get_meta_data(), indent=4)
        logstr = "file = %s\nMetaData = %s\n%s" % \
                 (self.filename, meta_data, self.root)
        return logstr


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: %s mp4_file\n" % sys.argv[0]
        sys.exit(0)

    filename = sys.argv[1]
    pymp4 = PyMp4(filename)
    pymp4.ParseMp4()

    print "mp4info: %s\n" % str(pymp4)
