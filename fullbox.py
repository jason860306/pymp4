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


from box import *


class FullBox(Box):
    """
    aligned(8) class FullBox(unsigned int(32) boxtype, unsigned int(8) v, bit(24) f) extends Box(boxtype) {
        unsigned int(8) version = v;
        bit(24) flags = f;
    }
    """

    def __init__(self, box=None):
        Box.__init__(self, box)
        if type(box) is FullBox and box is not None:
            self.large_size = box.large_size
            self.user_type = box.user_type
        else:
            self.version = 0
            self.flags = ''

    def decode(self, file=None):
        file_strm = Box.decode(self)

        self.version = file_strm.ReadUInt8()
        self.flags = file_strm.ReadByte(3)

        return file_strm

    def get_size(self):
        box_size = Box.get_size(self)
        ver_size = struct.calcsize('!s')
        flags_size = struct.calcsize('!3s')
        return (box_size + ver_size + flags_size)

    def __str__(self):
        return "%s, version = %d, flags = %s" % (
            Box.__str__(self), self.version, self.flags)
