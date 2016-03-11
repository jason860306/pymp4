#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 6:06 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Stss(FullBox):
    """
    aligned(8) class SyncSampleBox extends FullBox(‘stss’, version = 0, 0) {
        unsigned int(32) entry_count;
        int i;
        for (i=0; i < entry_count; i++) {
            unsigned int(32) sample_number;
        }
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)
        elif type(box) is FullBox:
            FullBox.__init__(self, box)

        self.entry_count = 0
        self.sample_number = []

    def decode(self, file=None):
        file_strm = FullBox.decode(self, file)

        self.entry_count = file_strm.ReadUInt32()
        for i in range(self.entry_count):
            sample_number_ = file_strm.ReadUInt32()
            self.sample_number.append(sample_number_)

        return file_strm

    def __str__(self):
        logstr = "%s, entry_count = %d, sample_number = [" % \
                 (FullBox.__str__(self), self.entry_count)
        for i in range(self.entry_count):
            logstr += "[%d. %d], " % (i, self.sample_number[i])
        logstr += "]"
        return logstr
