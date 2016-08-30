#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 5:33 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import os

from fullbox import *


class Ctts(object, FullBox):
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
    version ‐ is an integer that specifies the version of this box.
    entry_count ‐ is an integer that gives the number of entries in the following table.
    sample_count ‐ is an integer that counts the number of consecutive samples that have
                   the given offset.
    sample_offset ‐ is an integer that gives the offset between CT and DT, such that
                    CT(n) = DT(n) + CTTS(n).
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.entry_count = 0
        self.sample_count = []  # 0 for i in range(self.entry_count)
        self.sample_offset = []  # 0 for i in range(self.entry_count)

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

            sample_offset_ = 0
            if 0 == self.version:
                sample_offset_ = file_strm.read_uint32()
                self.offset += UInt32ByteLen
            else:
                sample_offset_ = file_strm.read_int32()
                self.offset += Int32ByteLen
            self.sample_offset.append(sample_offset_)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['entry_count'] = self.entry_count

        samples = {}
        sample_offset = zip(self.sample_count, self.sample_offset)
        # for i in range(len(sample_offset)):
        #     # cnt, offset, = sample_offset[i] # the key in dict must be unique
        #     samples['offset_{0}'.format(i)] = sample_offset[i]
        dump_info['samples_offset'] = sample_offset
        return dump_info

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tentry_count = %08ld(0x%016lx)\n\t\t\t\tsample = [" % \
                 (FullBox.__str__(self), self.entry_count, self.entry_count)

        j = 0
        for i in range(self.entry_count):
            if (0 == i) or (0 == i % 4):
                logstr += "\n\t\t\t\t\t%08ld. " % j
                j += 1
            logstr += "%08ld(0x%016lx) " % (self.sample_count[i], self.sample_offset[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
