#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 5:59 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Stco(FullBox):
    """
    aligned(8) class ChunkOffsetBox extends FullBox(‘stco’, version = 0, 0) {
        unsigned int(32) entry_count;
        for (i=1; i <= entry_count; i++) {
            unsigned int(32) chunk_offset;
        }
    }
    """

    def __init__(self, box=None):
        if isinstance(box, Box):
            Box.__init__(self, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, box)

        self.entry_count = 0
        self.chunk_offset = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.ReadUInt32()
        for i in range(self.entry_count):
            chunk_offset_ = file_strm.ReadUInt32()
            self.chunk_offset.append(chunk_offset_)

        return file_strm

    def __str__(self):
        logstr = "%s, entry_count = %d, chunk_offset = [" % \
                 (FullBox.__str__(self), self.entry_count)
        for i in range(self.entry_count):
            logstr += "[%d. %d], " % (i, self.chunk_offset[i])
        logstr += "]"
        return logstr
