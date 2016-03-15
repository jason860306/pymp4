#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 6:20 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *


class Mdat(Box):
    """
    aligned(8) class MediaDataBox extends Box(‘mdat’) {
        bit(8) data[];
    }
    """

    def __init__(self, box=None):
        if isinstance(box, Box):
            Box.__init__(self, box)

        self.data = ""

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = Box.Size(self) - Box.GetLength(self)
        self.data = file_strm.ReadByte(left_size)

        return file_strm

    def __str__(self):
        logstr = "%s, data = %s" % (Box.__str__(self), self.data)
        return logstr
