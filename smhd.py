#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 18:13'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Smhd(FullBox):
    """
    aligned(8) class SoundMediaHeaderBox extends FullBox(‘smhd’, version = 0, 0) {
        template int(16) balance = 0;
        const unsigned int(16) reserved = 0;
    }
    """

    def __init__(self):
        FullBox.__init__(self)

        self.balance = 0
        self.reserved = 0

    def decode(self, file=None):
        FullBox.decode(self, file)

        file_strm = Util(file)

        self.balance = file_strm.read_int16_lit()
        self.reserved = file_strm.read_uint16_lit()

    def __str__(self):
        logstr = "%s, balance = %d, reserved = %d" % \
                 (FullBox.__str__(self), self.balance, self.reserved)
        return logstr
