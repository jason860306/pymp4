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

    def __init__(self):
        Box.__init__(self)

        self.data = ""

    def decode(self, file=None):
        Box.decode(self, file)

        file_strm = Util(file)

        left_size = Box.size(self) - Box.get_size(self)
        self.data = file_strm.read_buf(left_size)

    def __str__(self):
        logstr = "%s, data = %s" % (Box.__str__(self), self.data)
        return logstr
