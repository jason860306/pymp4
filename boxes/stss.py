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


import os

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
    version ‐ is an integer that specifies the version of this box.
    entry_count ‐ is an integer that gives the number of entries in the following table.
                  If entry_count is zero, there are no sync samples within the stream and
                  the following table is empty.
    sample_number ‐ gives the numbers of the samples that are sync samples in the stream.
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.entry_count = 0
        self.sample_number = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        for i in range(self.entry_count):
            sample_number_ = file_strm.read_uint32()
            self.offset += UInt32ByteLen
            self.sample_number.append(sample_number_)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def find_sync_sample_index(self, sample_index):
        if 0 == self.entry_count:
            return -1
        for sample_idx in self.sample_number:
            if sample_idx >= sample_index:
                return sample_idx

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['entry_count'] = self.entry_count
        dump_info['sample_number'] = self.sample_number
        return dump_info

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tentry_count = %08ld(0x%016lx)" \
                 "\n\t\t\t\tsample_number = [" % \
                 (FullBox.__str__(self), self.entry_count, self.entry_count)

        j = 0
        for i in range(self.entry_count):
            if (0 == i) or (0 == i % 4):
                logstr += "\n\t\t\t\t\t%08ld. " % j
                j += 1
            logstr += "%08ld(0x%016lx) " % \
                      (self.sample_number[i], self.sample_number[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
