#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 5:33 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Ctts(FullBox):
    """
    aligned(8) class CompositionOffsetBox extends FullBox(‘ctts’, version, 0) {
        unsigned int(32) entry_count;
        int i;
        if (version==0) {
            for (i=0; i < entry_count; i++) {
                unsigned int(32) sample_count;
                unsigned int(32) sample_offset;
            }
        }
        else if (version == 1) {
            for (i=0; i < entry_count; i++) {
                unsigned int(32) sample_count;
                signed int(32) sample_offset;
            }
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
        self.sample_offset = []  # 0 for i in range(self.entry_count)

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.ReadUInt32()
        for i in range(self.entry_count):
            sample_count_ = file_strm.ReadUInt32()
            self.sample_count.append(sample_count_)

            sample_offset_ = 0
            if 0 == self.version:
                sample_offset_ = file_strm.ReadUInt32()
            else:
                sample_offset_ = file_strm.ReadInt32()
            self.sample_offset.append(sample_offset_)

        return file_strm

    def __str__(self):
        logstr = "%s, entry_count = %d, sample = [" % \
                 (FullBox.__str__(self), self.entry_count)
        for i in range(self.entry_count):
            logstr += "[%d. %d %d], " % \
                      (i, self.sample_count[i], self.sample_offset[i])
        logstr += "]"
        return logstr
