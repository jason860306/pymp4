#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/8 23:23'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import os

from fullbox import *


class Stts(FullBox, object):
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

        The atom contains time deltas:
            DT(n+1) = DT(n) + STTS(n)
    here STTS(n) is the (uncompressed) table entry for sample n and DT is the display
    time for sample (n).
        DT(i) = SUM (for j=0 to i-1 of delta(j))
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
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        for i in range(self.entry_count):
            sample_count_ = file_strm.read_uint32()
            self.sample_count.append(sample_count_)
            self.offset += UInt32ByteLen

            sample_delta_ = file_strm.read_uint32()
            self.sample_delta.append(sample_delta_)
            self.offset += UInt32ByteLen

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def find_sample_index(self, timestamp):
        for i in range(self.entry_count):
            sample_cnt = self.sample_count[i]
            sample_duration = self.sample_delta[i]
            for j in range(sample_cnt):
                if (j * sample_duration) >= timestamp:
                    return i * j + 1
        else:
            pass  # raise

    def get_sample_duration(self, sample_idx):
        sample_idx_ = 0
        for i in range(self.entry_count):
            sample_idx_ += self.sample_count[i]
            if sample_idx < sample_idx_:
                return self.sample_delta[i]
        return -1

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['entry_count'] = self.entry_count
        dump_info['sample_count'] = self.sample_count
        dump_info['sample_delta'] = self.sample_delta
        return dump_info

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tsample = [" % FullBox.__str__(self)
        for i in range(self.entry_count):
            logstr += "\n\t\t\t\t\t%08ld. %08ld(0x%016lx) %08ld(0x%016lx)" % \
                      (i, self.sample_count[i], self.sample_count[i],
                       self.sample_delta[i], self.sample_delta[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
