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


import os

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
    version - is an integer that specifies the version of this box
    sample_size - is integer specifying the default sample size. If all the samples are
                  the same size, this field contains that size value. If this field is
                  set to 0, then the samples have different sizes, and those sizes are
                  stored in the sample size table. If this field is not 0, it specifies
                  the constant sample size, and no array follows.
    sample_count - is an integer that gives the number of samples in the track; if
                   sample‐size is 0, then it is also the number of entries in the following table.
    entry_size - is an integer specifying the size of a sample, indexed by its number.
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.sample_size = 0
        self.sample_count = 0
        self.entry_size = []  # for i in range(self.sample_count) when sample_size==0

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.sample_size = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        self.sample_count = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        if 0 == self.sample_size:
            for i in range(self.sample_count):
                entry_size_ = file_strm.ReadUInt32()
                self.offset += UInt32ByteLen
                self.entry_size.append(entry_size_)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def bitsize(self):
        bsize = 0
        if 0 == self.sample_size:
            for size in self.entry_size:
                bsize += size
        else:
            bsize = self.sample_count * self.sample_size
        return bsize

    def get_sample_size(self, sample_index):
        if sample_index >= len(self.entry_size):
            pass  # raise
        return self.sample_size if (0 != self.sample_size) else \
            self.entry_size[sample_index]

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['sample_size'] = self.sample_size
        dump_info['sample_count'] = self.sample_count
        dump_info['entry_size'] = self.entry_size
        return dump_info

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tsample_size = %08ld(0x%016lx)" \
                 "\n\t\t\t\tsample_count = %08ld(0x%016lx)" % \
                 (FullBox.__str__(self), self.sample_size, self.sample_size,
                  self.sample_count, self.sample_count)
        if 0 == self.sample_size:
            logstr += "\n\t\t\t\tentry_size = ["
            j = 0
            for i in range(self.sample_count):
                if (0 == i) or (0 == i % 4):
                    logstr += "\n\t\t\t\t\t%08ld. " % j
                    j += 1
                logstr += "%08ld(0x%016lx) " % (self.entry_size[i], self.entry_size[i])
            logstr += "\n\t\t\t\t]\n"
        return logstr
