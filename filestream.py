#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/1 18:15'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import struct

global LittleEndian
global BigEndian


class FileStream:
    """
    some utility function
    """

    LittleEndian = 0
    BigEndian = 1

    def __init__(self, file=None, endian=LittleEndian):
        self.file = None
        self.endian = endian

    def ReadInt64(self):
        __ENDIAN = '!q'
        if self.endian == BigEndian:
            __ENDIAN = '@q'

        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def ReadUint64(self):
        __ENDIAN = '!Q'
        if self.endian == BigEndian:
            __ENDIAN = '@Q'

        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def ReadInt32(self):
        __ENDIAN = '!i'
        if self.endian == BigEndian:
            __ENDIAN = '@i'

        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def ReadUInt32(self):
        __ENDIAN = '!I'
        if self.endian == BigEndian:
            __ENDIAN = '@I'

        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def ReadInt16(self):
        __ENDIAN = '!h'
        if self.endian == BigEndian:
            __ENDIAN = '@h'

        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def ReadUInt16(self):
        __ENDIAN = '!H'
        if self.endian == BigEndian:
            __ENDIAN = '@H'

        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def ReadInt8(self):
        __ENDIAN = '!b'
        if self.endian == BigEndian:
            __ENDIAN = '@b'

        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def ReadUInt8(self):
        __ENDIAN = '!B'
        if self.endian == BigEndian:
            __ENDIAN = '@B'

        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def ReadByte(self, size):
        __ENDIAN = '!%ds' % size
        if self.endian == BigEndian:
            __ENDIAN = '@%ds' % size

        buf = ''
        if self.file:
            buf = self.file.read(size)
            buf = struct.unpack_from(__ENDIAN, buf)
        return buf

    def __str__(self):
        return "%s" % str(FileStream)
