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

from mp4boxdesc import *
from pymp4def import *
from util.filestream import *


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
    size – is an integer that specifies the number of bytes in this box, including all its
         fields and contained boxes; if size is 1 then the actual size is in the field
         largesize; if size is 0, then this box is the last one in the file, and its
         contents extend to the end of the file (normally only used for a Media Data Box)
    type – identifies the box type; standard boxes use a compact type, which is normally
         four printable characters, to permit ease of identification, and is shown so in
         the boxes below. User extensions use an extended type; in this case, the type
         field is set to ‘uuid’.
    """

    def __init__(self, offset=0, box=None):
        self.box_offset = offset
        self.offset = offset
        if isinstance(box, Box) and box != None:
            self.size = box.size
            self.type = box.type
            self.large_size = box.large_size
            self.user_type = box.user_type
            self.fullname = MP4BoxesFullName[box.type]
            self.desc = MP4BoxesDesc[box.type]
        else:
            self.size = int(0)
            self.type = ''
            self.large_size = int(0)
            self.user_type = ''
            self.fullname = ''
            self.desc = ''

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        self.size = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        type_ = file_strm.read_uint32()
        self.type = parse_4cc(type_)
        self.offset += UInt32ByteLen

        if self.size == 1:
            self.large_size = file_strm.read_uint64()
            self.offset += UInt64ByteLen

        if self.type == FourCCMp4Uuid:
            self.user_type = file_strm.read_uint16()
            self.offset += UInt16ByteLen

        return file_strm

    def peek(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        self.size = file_strm.read_uint32()
        # self.offset += UInt32ByteLen

        type_ = file_strm.read_uint32()
        self.type = parse_4cc(type_)
        # self.offset += UInt32ByteLen

        if self.size == 1:
            self.large_size = file_strm.read_uint64()
            # self.offset += UInt64ByteLen

        if self.type == FourCCMp4Uuid:
            self.user_type = file_strm.read_uint16()
            # self.offset += UInt16ByteLen

        file_strm.seek(self.GetLength() * -1, os.SEEK_CUR)

        return file_strm

    def Size(self):
        return self.large_size if (self.size == 1) else self.size

    def GetLength(self):
        large_size_ = struct.calcsize('!Q') if (self.size == 1) else 0
        user_type_ = struct.calcsize('!16s') if (self.type == FourCCMp4Uuid) else 0
        size_ = struct.calcsize('!II') + large_size_ + user_type_
        return size_

    def dump(self):
        dump_info = {}
        dump_info['offset'] = self.offset
        dump_info['size'] = self.size
        dump_info['type'] = self.type
        dump_info['fullname'] = self.fullname
        dump_info['desc'] = self.desc
        return dump_info

    def __str__(self):
        return "offset = 0x%016x, size = %08ld(0x%08lx), type = %s(%s: %s)" % \
               (self.offset, self.size, self.size, self.type, self.fullname, self.desc)
