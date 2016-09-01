#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # Administrator
__date__ = '2016/6/23 17:40'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import ctypes
import os
import struct

from pymp4def import (Int8ByteLen, Int16ByteLen,
                      Int32ByteLen, Int64ByteLen, UInt8ByteLen,
                      UInt16ByteLen, UInt32ByteLen, UInt64ByteLen)
from stream import *


class ByteStream(Stream, object):
    """
    some utility function
    """

    def __init__(self, byte_data, byte_size, endian=LittleEndian):
        if byte_data is None:
            print "byte_strm is None"
            return
        super(ByteStream, self).__init__(self, endian)
        self.byte_offset = 0
        self.byte_data = byte_data
        self.byte_size = byte_size

    def tell(self):
        return self.byte_offset

    def seek(self, offset, whence=None):
        if self.byte_data is None:
            return
        if whence == os.SEEK_SET:
            if offset < self.byte_size:
                self.byte_offset = offset
        elif whence == os.SEEK_CUR:
            if self.byte_offset + offset < self.byte_size:
                self.byte_offset += offset
        elif whence == os.SEEK_END:
            if offset < self.byte_size + 1:
                self.byte_offset = -1 * offset

    def read_int_n(self, int_size):
        value = 0
        if int_size == Int8ByteLen:
            value = self.read_int8()
        elif int_size == Int16ByteLen:
            value = self.read_int16()
        elif int_size == Int32ByteLen:
            value = self.read_int32()
        elif int_size == Int64ByteLen:
            value = self.read_int64()
        return value

    def read_uint_n(self, uint_size):
        value = 0
        if uint_size == UInt8ByteLen:
            value = self.read_uint8()
        elif uint_size == UInt16ByteLen:
            value = self.read_uint16()
        elif uint_size == UInt32ByteLen:
            value = self.read_uint32()
        elif uint_size == UInt64ByteLen:
            value = self.read_uint64()
        return value

    def read_int64(self):
        __FMT = '!q' if (self.endian == LittleEndian) else '@q'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            self.byte_offset += size
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int64(num[0]).value
            # return int(num[0])
        return 0

    def read_uint64(self):
        __FMT = '!Q' if (self.endian == LittleEndian) else '@Q'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            self.byte_offset += size
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint64(num[0]).value
            # return int(num[0])
        return 0

    def read_int32(self):
        __FMT = '!i' if (self.endian == LittleEndian) else '@i'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            self.byte_offset += size
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int32(num[0]).value
            # return int(num[0])
        return 0

    def read_uint32(self):
        __FMT = '!I' if (self.endian == LittleEndian) else '@I'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            self.byte_offset += size
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint32(num[0]).value
            # return int(num[0])
        return 0

    def read_int16(self):
        __FMT = '!h' if (self.endian == LittleEndian) else '@h'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            self.byte_offset += size
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int16(num[0]).value
            # return int(num[0])
        return 0

    def read_uint16(self):
        __FMT = '!H' if (self.endian == LittleEndian) else '@H'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            self.byte_offset += size
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint16(num[0]).value
            # return int(num[0])
        return 0

    def read_int8(self):
        __FMT = '!b' if (self.endian == LittleEndian) else '@b'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            self.byte_offset += size
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int8(num[0]).value
            # return int(num[0])
        return 0

    def read_uint8(self):
        __FMT = '!B' if (self.endian == LittleEndian) else '@B'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            self.byte_offset += size
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint8(num[0]).value
            # return int(num[0])
        return 0

    def read_byte(self, size):
        __FMT = '!%ds' % size if (self.endian == LittleEndian) else '@%ds' % size

        buf = ''
        if self.byte_data is not None:
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            self.byte_offset += size
            buf, = struct.unpack_from(__FMT, buf)
        return buf

    def peek_int64(self):
        __FMT = '!q' if (self.endian == LittleEndian) else '@q'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0

            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int64(num[0]).value
            # return int(num[0])
        return 0

    def peek_uint64(self):
        __FMT = '!Q' if (self.endian == LittleEndian) else '@Q'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0

            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint64(num[0]).value
            # return int(num[0])
        return 0

    def peek_int32(self):
        __FMT = '!i' if (self.endian == LittleEndian) else '@i'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0

            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int32(num[0]).value
            # return int(num[0])
        return 0

    def peek_uint32(self):
        __FMT = '!I' if (self.endian == LittleEndian) else '@I'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0

            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int32(num[0]).value
            # return int(num[0])
        return 0

    def peek_int16(self):
        __FMT = '!h' if (self.endian == LittleEndian) else '@h'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0

            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int16(num[0]).value
            # return int(num[0])
        return 0

    def peek_uint16(self):
        __FMT = '!H' if (self.endian == LittleEndian) else '@H'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0

            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint16(num[0]).value
            # return int(num[0])
        return 0

    def peek_int8(self):
        __FMT = '!b' if (self.endian == LittleEndian) else '@b'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0

            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int8(num[0]).value
            # return int(num[0])
        return 0

    def peek_uint8(self):
        __FMT = '!B' if (self.endian == LittleEndian) else '@B'

        if self.byte_data is not None:
            size = struct.calcsize(__FMT)
            if self.byte_offset + size > self.byte_size:
                return 0

            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint8(num[0]).value
            # return int(num[0])
        return 0

    def peek_byte(self, size):
        __FMT = '!%ds' % size if (self.endian == LittleEndian) else '@%ds' % size

        buf = ''
        if self.byte_data is not None:
            if self.byte_offset + size > self.byte_size:
                return 0
            buf = self.byte_data[self.byte_offset:self.byte_offset + size]
            buf, = struct.unpack_from(__FMT, buf)
        return buf

    def __str__(self):
        return "%s" % str(Stream)
