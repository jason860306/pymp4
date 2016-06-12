#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '5/10/0010 19:11:51'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *


class Btrt(Box):
    """
    class Btrt extends Box(‘btrt’){
        unsigned int(32) bufferSizeDB;
        unsigned int(32) maxBitrate;
        unsigned int(32) avgBitrate;
    }

    5.3.4.1.3 Semantics
    bufferSizeDB gives the size of the decoding buffer for the elementary stream in bytes.
    maxBitrate gives the maximum rate in bits/second over any window of one second.
    avgBitrate gives the average rate in bits/second over the entire presentation.
    """

    def __init__(self, offset=0, box=None):
        Box.__init__(self, offset, box)
        self.bufferSizeDB = 0
        self.maxBitrate = 0
        self.avgBitrate = 0

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        self.bufferSizeDB = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        self.maxBitrate = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        self.avgBitrate = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = Box.dump(self)
        dump_info['bufferSizeDB'] = self.bufferSizeDB
        dump_info['maxBitrate'] = self.maxBitrate
        dump_info['avgBitrate'] = self.avgBitrate
        return dump_info

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t\tbufferSizeDB = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\tmaxBitrate = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\tavgBitrate = %08ld(0x%016lx)" % \
                 (Box.__str__(self), self.bufferSizeDB, self.bufferSizeDB,
                  self.maxBitrate, self.maxBitrate, self.avgBitrate, self.avgBitrate)
        return logstr
