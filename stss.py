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

    def __init__(self):
        FullBox.__init__(self)

        self.entry_count = 0
        self.sample_number = []

    def decode(self, file=None):
        FullBox.decode(self, file)

        file_strm = Util(file)

        self.entry_count = file_strm.read_uint32_lit()
        for i in range(self.entry_count):
            sample_number_ = file_strm.read_uint32_lit()
            self.sample_number.append(sample_number_)

    def __str__(self):
        logstr = "%s, entry_count = %d, sample_number = [" % \
                 (FullBox.__str__(self), self.entry_count)
        for i in range(self.entry_count):
            logstr += "[%d. %d], " % (i, self.sample_number[i])
        logstr += "]"
        return logstr
