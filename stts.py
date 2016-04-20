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


import os

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
    version ‐ is an integer that specifies the version of this box.
    entry_count ‐ is an integer that gives the number of entries in the following table.
    sample_count ‐ is an integer that counts the number of consecutive samples that
                   have the given duration.
    sample_delta ‐ is an integer that gives the delta of these samples in the time‐scale
                   of the media.
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.entry_count = 0
        self.sample_count = []  # 0 for i in range(self.entry_count)
        self.sample_delta = []  # 0 for i in range(self.entry_count)

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        for i in range(self.entry_count):
            sample_count_ = file_strm.ReadUInt32()
            self.sample_count.append(sample_count_)
            self.offset += UInt32ByteLen

            sample_delta_ = file_strm.ReadUInt32()
            self.sample_delta.append(sample_delta_)
            self.offset += UInt32ByteLen

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def duration(self):
        duration_ = 0
        for i in range(self.entry_count):
            duration_ += (self.sample_count[i] * self.sample_delta[i])
        return (1.0 * duration_)

    def find_sample_index(self, timestamp):
        for i in range(self.entry_count):
            sample_cnt = self.sample_count[i]
            sample_duration = self.sample_delta[i]
            for j in range(sample_cnt):
                if (j * sample_duration) >= timestamp:
                    return (i * j + 1)
        else:
            pass  # raise


    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tsample = [" % FullBox.__str__(self)
        for i in range(self.entry_count):
            logstr += "\n\t\t\t\t\t%08ld. %08ld(0x%016lx) %08ld(0x%016lx)" % \
                      (i, self.sample_count[i], self.sample_count[i],
                       self.sample_delta[i], self.sample_delta[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
