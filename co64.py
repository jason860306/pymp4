#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 6:03 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Co64(FullBox):
    """
    aligned(8) class ChunkLargeOffsetBox extends FullBox(‘co64’, version = 0, 0) {
        unsigned int(32) entry_count;
        for (i=1; i <= entry_count; i++) {
             unsigned int(64) chunk_offset;
        }
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)
        elif type(box) is FullBox:
            FullBox.__init__(self, box)

        self.entry_count = 0
        self.chunk_offset = []

    def decode(self, file=None):
        file_strm = FullBox.decode(self, file)

        self.entry_count = file_strm.ReadUInt32()
        for i in range(self.entry_count):
            chunk_offset_ = file_strm.ReadUint64()
            self.chunk_offset.append(chunk_offset_)

        return file_strm

    def __str__(self):
        logstr = "%s, entry_count = %d, chunk_offset = [" % \
                 (FullBox.__str__(self), self.entry_count)
        for i in range(self.entry_count):
            logstr += "[%d. %ld], " % (i, self.chunk_offset[i])
        logstr += "]"
        return logstr
