#!/usr/bin/python
# encoding: utf-8

"""

"""

import sys

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/11/16 5:30 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from root import *
from filestream import *


class PyMp4:
    """
    the main class to parse a mp4 file
    """

    def __init__(self, file):
        if file is None:
            print "file is None"
            return

        self.file = file
        self.root = None

    def ParseMp4(self):
        self.root = Root()

        file_strm = FileStream(self.file)
        self.root.decode(file_strm)

    def __str__(self):
        logstr = "file = %s, root = %s" % (self.file, self.root)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: %s mp4_file\n" % sys.argv[0]
        sys.exit(0)

    file_name = sys.argv[1]

    with open(file_name, 'rb') as mp4_file:
        pymp4 = PyMp4(mp4_file)
        pymp4.ParseMp4()
