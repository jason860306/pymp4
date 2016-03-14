#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 18:17'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Nmhd(FullBox):
    """
    aligned(8) class NullMediaHeaderBox
        extends FullBox(’nmhd’, version = 0, flags) {
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)
        elif type(box) is FullBox:
            FullBox.__init__(self, box)

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        return file_strm

    def __str__(self):
        logstr = "%s" % FullBox.__str__(self)
        return logstr
