#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 6:09 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *


class Udat(Box):
    """
    aligned(8) class UserDataBox extends Box(‘udta’) {
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)

    def decode(self, file=None):
        file_strm = Box.decode(self, file)

        return file_strm

    def __str__(self):
        logstr = "%s" % Box.__str__(self)
        return logstr
