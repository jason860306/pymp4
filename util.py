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


class Util:
    """
    some utility function
    """

    def __init__(self, file=None):
        self.file = None

    def read_int64_lit(self):
        __ENDIAN = '!q'
        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def read_uint64_lit(self):
        __ENDIAN = '!Q'
        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def read_int32_lit(self):
        __ENDIAN = '!i'
        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def read_uint32_lit(self):
        __ENDIAN = '!I'
        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def read_int16_lit(self):
        __ENDIAN = '!h'
        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def read_uint16_lit(self):
        __ENDIAN = '!H'
        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def read_int8_lit(self):
        __ENDIAN = '!b'
        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def read_uint8_lit(self):
        __ENDIAN = '!B'
        if self.file:
            size = struct.calcsize(__ENDIAN)
            buf = self.file.read(size)
            num = struct.unpack_from(__ENDIAN, buf)
            return int(num)
        return 0

    def read_buf(self, size):
        buf = ''
        if self.file:
            buf = self.file.read(size)
        return buf

    def __str__(self):
        return "%s" % str(Util)
