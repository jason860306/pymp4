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


class PyMp4:
    """
    the main class to parse a mp4 file
    """

    def __init__(self, file=None):
        self.file = file
        self.root = None

    def ParseMp4(self):
        self.root = Root()
        self.root.decode(self.file)

    def __str__(self):
        logstr = "file = %s, root = %s" % (self.file, self.root)


if __name__ == "main":
    if len(sys.argv) != 2:
        print "usage: %s mp4_file\n" % sys.argv[0]
        sys.exit(0)

    file = sys.argv[0]
    pymp4 = PyMp4(file)
    pymp4.ParseMp4()
