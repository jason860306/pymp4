#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 5:51 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Stsz(FullBox):
    """
    aligned(8) class SampleSizeBox extends FullBox(‘stsz’, version = 0, 0) {
        unsigned int(32) sample_size;
        unsigned int(32) sample_count;
        if (sample_size==0) {
            for (i=1; i <= sample_count; i++) {
                 unsigned int(32) entry_size;
            }
        }
    }
    """

    def __init__(self):
        FullBox.__init__(self)

        self.sample_size = 0
        self.sample_count = 0
        self.entry_size = []  # for i in range(self.sample_count) when sample_size==0

    def decode(self, file=None):
        FullBox.decode(self, file)

        file_strm = Util(file)

        self.sample_size = file_strm.read_uint32_lit()
        self.sample_count = file_strm.read_uint32_lit()
        if 0 == self.sample_size:
            for i in range(self.sample_count):
                entry_size_ = file_strm.read_uint32_lit()
                self.entry_size.append(entry_size_)

    def __str__(self):
        logstr = "%s, sample_size = %d, sample_count = %d" % \
                 (FullBox.__str__(self), self.sample_size, self.sample_count)
        if 0 == self.sample_size:
            logstr += ", entry_size = ["
            for i in range(self.sample_count):
                logstr += "[%d. %d], " % (i, self.entry_size[i])
            logstr += "]"
        return logstr
