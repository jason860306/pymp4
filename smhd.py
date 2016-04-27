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


import os

from fullbox import *


class Smhd(FullBox):
    """
    aligned(8) class SoundMediaHeaderBox extends FullBox(‘smhd’, version = 0, 0) {
        template int(16) balance = 0;
        const unsigned int(16) reserved = 0;
    }
    version - is an integer that specifies the version of this box
    balance - is a fixed‐point 8.8 number that places mono audio tracks in a stereo
              space; 0 is centre (the normal value); full left is ‐1.0 and full right is 1.0.
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.balance = 0
        self.reserved = 0

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.balance = file_strm.ReadInt16()
        self.offset += UInt16ByteLen

        self.reserved = file_strm.ReadUInt16()
        self.offset += UInt16ByteLen

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['balance'] = self.balance
        dump_info['reserved'] = self.reserved
        return dump_info

    def __str__(self):
        logstr = "\t\t\t%s\n\t\t\tbalance = %08ld(0x%016lx)\n\t\t\t" \
                 "reserved = %08ld(0x%016lx)\n" % \
                 (FullBox.__str__(self), self.balance, self.balance,
                  self.reserved, self.reserved)
        return logstr
