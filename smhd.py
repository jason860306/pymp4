#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # user
__date__ = '2016/3/4 22:59'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *


class Smhd(Box):
    """
    aligned(8) class SoundMediaHeaderBox extends FullBox(‘smhd’) {
        template int(16) balance = 0;
        const unsigned int(16) reserved = 0;
    }
    """

    def __init__(self):
        Box.__init__(self)

        self.balance = 0
        self.reserved = 0

    def decode(self, file=None):
        Box.decode(self, file)

        file_strm = Util(file)

        self.balance = file_strm.read_uint16_lit()
        self.reserved = file_strm.read_uint16_lit()

    def __str__(self):
        logstr = "%s, balance = %d, reserved = %d" % \
                 (Box.__str__(self), self.balance, self.reserved)
        return logstr
