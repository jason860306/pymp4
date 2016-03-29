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

    def __init__(self, fname):
        if fname is None:
            print "file is None"
            return

        self.filename = fname
        self.root = None

    def ParseMp4(self):
        self.root = Root()
        self.root.decode(self.filename)

    def __str__(self):
        logstr = "file = %s\n%s" % (self.filename, self.root)
        return logstr


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: %s mp4_file\n" % sys.argv[0]
        sys.exit(0)

    filename = sys.argv[1]
    pymp4 = PyMp4(filename)
    pymp4.ParseMp4()

    print "mp4info: %s\n" % str(pymp4)
