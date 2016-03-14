#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/8 23:23'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Stts(FullBox):
    """
    aligned(8) class TimeToSampleBox extends FullBox(’stts’, version = 0, 0) {
        unsigned int(32) entry_count;
        int i;
        for (i=0; i < entry_count; i++) {
            unsigned int(32) sample_count;
            unsigned int(32) sample_delta;
        }
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)
        elif type(box) is FullBox:
            FullBox.__init__(self, box)

        self.entry_count = 0
        self.sample_count = []  # 0 for i in range(self.entry_count)
        self.sample_delta = []  # 0 for i in range(self.entry_count)

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.ReadUInt32()
        for i in range(self.entry_count):
            self.sample_count[i] = file_strm.ReadUInt32()
            self.sample_delta[i] = file_strm.ReadUInt32()

        return file_strm

    def __str__(self):
        logstr = "%s, sample = [" % FullBox.__str__(self)
        for i in range(self.entry_count):
            logstr += "%d. (%d %d)], [" % \
                      (i, self.sample_count[i], self.sample_delta[i])
        return logstr
