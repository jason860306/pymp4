#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/1 17:22'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'

from constdef import *
from filestream import *


class Box:
    """
    aligned(8) class Box (unsigned int(32) boxtype, optional unsigned int(8)[16] extended_type) {
        unsigned int(32) size;
        unsigned int(32) type = boxtype;
        if (size==1) {
             unsigned int(64) largesize;
        } else if (size==0) {
             // box extends to end of file
        }
        if (boxtype==‘uuid’) {
             unsigned int(8)[16] usertype = extended_type;
        }
    }
    """

    def __init__(self, offset=0, box=None):
        self.box_offset = offset
        self.offset = offset
        if isinstance(box, Box) and box is not None:
            self.size = box.size
            self.type = box.type
            self.large_size = box.large_size
            self.user_type = box.user_type
        else:
            self.size = int(0)
            self.type = ''
            self.large_size = int(0)
            self.user_type = ''

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        self.size = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        type_ = file_strm.ReadUInt32()
        self.type = ParseFourCC(type_)
        self.offset += UInt32ByteLen

        if self.size == 1:
            self.large_size = file_strm.ReadUint64()
            self.offset += UInt64ByteLen

        if self.type == FourCCMp4Uuid:
            self.user_type = file_strm.ReadUInt16()
            self.offset += UInt16ByteLen

        return file_strm

    def peek(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        self.size = file_strm.ReadUInt32()
        # self.offset += UInt32ByteLen

        type_ = file_strm.ReadUInt32()
        self.type = ParseFourCC(type_)
        # self.offset += UInt32ByteLen

        if self.size == 1:
            self.large_size = file_strm.ReadUint64()
            # self.offset += UInt64ByteLen

        if self.type == FourCCMp4Uuid:
            self.user_type = file_strm.ReadUInt16()
            # self.offset += UInt16ByteLen

        file_strm.Seek(self.GetLength() * -1, os.SEEK_CUR)

        return file_strm

    def Size(self):
        return self.large_size if (self.size == 1) else self.size

    def GetLength(self):
        large_size_ = struct.calcsize('!Q') if (self.size == 1) else 0
        user_type_ = struct.calcsize('!16s') if (self.type == FourCCMp4Uuid) else 0
        size_ = struct.calcsize('!II') + large_size_ + user_type_
        return size_

    def __str__(self):
        return "offset = 0x%08x, size = %ld, type = %s" % \
               (self.offset, self.size, self.type)
