#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 17:31'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import os

from fullbox import *


class Hdlr(FullBox, object):
    """
    aligned(8) class HandlerBox extends FullBox(‘hdlr’, version = 0, 0) {
        unsigned int(32) pre_defined = 0;
        unsigned int(32) handler_type;
        const unsigned int(32)[3] reserved = 0;
        string name;
    }
    version – is an integer that specifies the version of this box
    handler_type
        – when present in a media box, contains a value as defined in clause 12,
          or a value from a derived specification, or registration.
        - when present in a meta box, contains an appropriate value to indicate
          the format of the meta box contents. The value ‘null’ can be used in
          the primary meta box to indicate that it is merely being used to
          hold resources.
    name – is a null‐terminated string in UTF‐8 characters which gives a human‐readable
           name for the track type (for debugging and inspection purposes).
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.pre_defined = 0
        self.handler_type = ''
        self.reserved = [0 for i in range(3)]
        self.name = ''

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.pre_defined = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        handler_type_ = file_strm.read_uint32()
        self.offset += UInt32ByteLen
        self.handler_type = parse_4cc(handler_type_)

        for i in range(len(self.reserved)):
            self.reserved[i] = file_strm.read_uint32()
            self.offset += UInt32ByteLen

        left_size = self.Size() - self.GetLength()
        left_size -= struct.calcsize('!I')  # sizeof(pre_defined)
        left_size -= struct.calcsize('!I')  # sizeof(handler_type)
        left_size -= 3 * struct.calcsize('!I')  # sizeof(reserved)
        self.name = file_strm.read_byte(left_size)
        self.name = self.name.rstrip('\0')
        self.offset += Int8ByteLen * left_size

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['pre_defined'] = str(self.pre_defined)
        dump_info['handler_type'] = self.handler_type
        dump_info['reserved'] = str(self.reserved)
        dump_info['name'] = self.name
        return dump_info

    def __str__(self):
        logstr = "\t\t%s\n\t\tpre_defined = %08ld(0x%016lx)" \
                 "\n\t\thandler_type = %s\n\t\treserved = [ " % \
                 (FullBox.__str__(self), self.pre_defined,
                  self.pre_defined, self.handler_type)
        for r in self.reserved:
            logstr += "%08ld(0x%016lx), " % (r, r)
        logstr += "]\n\t\tname = %s\n" % self.name
        return logstr
