#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 5:59 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import os

from fullbox import *


class Stco(object, FullBox):
    """
    aligned(8) class ChunkOffsetBox extends FullBox(‘stco’, version = 0, 0) {
        unsigned int(32) entry_count;
        for (i=1; i <= entry_count; i++) {
            unsigned int(32) chunk_offset;
        }
    }
    version - is an integer that specifies the version of this box
    entry_count - is an integer that gives the number of entries in the following table
    chunk_offset - is a 32 or 64 bit integer that gives the offset of the start of a
                   chunk into its containing media file.
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.entry_count = 0
        self.chunk_offset = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        for i in range(self.entry_count):
            chunk_offset_ = file_strm.read_uint32()
            self.offset += UInt32ByteLen
            self.chunk_offset.append(chunk_offset_)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def get_chunk_offset_list(self):
        return self.chunk_offset

    def chunk_offset(self, chunk_idx):
        if chunk_idx >= self.entry_count:
            pass  # raise
        return self.offset[chunk_idx]

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['entry_count'] = self.entry_count
        dump_info['chunk_offset'] = self.chunk_offset
        return dump_info

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tentry_count = %08ld(0x%016lx)" \
                 "\n\t\t\t\tchunk_offset = [" % \
                 (FullBox.__str__(self), self.entry_count, self.entry_count)

        j = 0
        for i in range(self.entry_count):
            if (0 == i) or (0 == i % 4):
                logstr += "\n\t\t\t\t\t%08ld. " % j
                j += 1
            logstr += "%08ld(0x%016lx) " % (self.chunk_offset[i], self.chunk_offset[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
