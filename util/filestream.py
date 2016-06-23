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


import ctypes
import os
import struct

from pymp4def import (LittleEndian, Int8ByteLen, Int16ByteLen,
                      Int32ByteLen, Int64ByteLen, UInt8ByteLen,
                      UInt16ByteLen, UInt32ByteLen, UInt64ByteLen)
from stream import *


class FileStream(Stream):
    """
    some utility function
    """

    def __init__(self, file, endian=LittleEndian):
        if file is None:
            print "file is None"
            return
        Stream.__init__(self, endian)
        self.file = file

    def tell(self):
        if self.file is None:
            return 0
        return self.file.tell()

    def seek(self, offset, whence=None):
        if self.file is None:
            return
        self.file.seek(offset, whence)

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

        if self.file is not None:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int64(num[0]).value
            # return int(num[0])
        return 0

    def read_uint64(self):
        __FMT = '!Q' if (self.endian == LittleEndian) else '@Q'

        if self.file is not None:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint64(num[0]).value
            # return int(num[0])
        return 0

    def read_int32(self):
        __FMT = '!i' if (self.endian == LittleEndian) else '@i'

        if self.file is not None:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int32(num[0]).value
            # return int(num[0])
        return 0

    def read_uint32(self):
        __FMT = '!I' if (self.endian == LittleEndian) else '@I'

        if self.file is not None:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint32(num[0]).value
            # return int(num[0])
        return 0

    def read_int16(self):
        __FMT = '!h' if (self.endian == LittleEndian) else '@h'

        if self.file is not None:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int16(num[0]).value
            # return int(num[0])
        return 0

    def read_uint16(self):
        __FMT = '!H' if (self.endian == LittleEndian) else '@H'

        if self.file is not None:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint16(num[0]).value
            # return int(num[0])
        return 0

    def read_int8(self):
        __FMT = '!b' if (self.endian == LittleEndian) else '@b'

        if self.file is not None:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int8(num[0]).value
            # return int(num[0])
        return 0

    def read_uint8(self):
        __FMT = '!B' if (self.endian == LittleEndian) else '@B'

        if self.file is not None:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint8(num[0]).value
            # return int(num[0])
        return 0

    def read_byte(self, size):
        __FMT = '!%ds' % size if (self.endian == LittleEndian) else '@%ds' % size

        buf = ''
        if self.file is not None:
            buf = self.file.read(size)
            buf, = struct.unpack_from(__FMT, buf)
        return buf

    def peek_int64(self):
        __FMT = '!q' if (self.endian == LittleEndian) else '@q'

        if self.file is not None:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int64(num[0]).value
            # return int(num[0])
        return 0

    def peek_uint64(self):
        __FMT = '!Q' if (self.endian == LittleEndian) else '@Q'

        if self.file is not None:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint64(num[0]).value
            # return int(num[0])
        return 0

    def peek_int32(self):
        __FMT = '!i' if (self.endian == LittleEndian) else '@i'

        if self.file is not None:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int32(num[0]).value
            # return int(num[0])
        return 0

    def peek_uint32(self):
        __FMT = '!I' if (self.endian == LittleEndian) else '@I'

        if self.file is not None:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int32(num[0]).value
            # return int(num[0])
        return 0

    def peek_int16(self):
        __FMT = '!h' if (self.endian == LittleEndian) else '@h'

        if self.file is not None:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int16(num[0]).value
            # return int(num[0])
        return 0

    def peek_uint16(self):
        __FMT = '!H' if (self.endian == LittleEndian) else '@H'

        if self.file is not None:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint16(num[0]).value
            # return int(num[0])
        return 0

    def peek_int8(self):
        __FMT = '!b' if (self.endian == LittleEndian) else '@b'

        if self.file is not None:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int8(num[0]).value
            # return int(num[0])
        return 0

    def peek_uint8(self):
        __FMT = '!B' if (self.endian == LittleEndian) else '@B'

        if self.file is not None:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint8(num[0]).value
            # return int(num[0])
        return 0

    def peek_byte(self, size):
        __FMT = '!%ds' % size if (self.endian == LittleEndian) else '@%ds' % size

        buf = ''
        if self.file is not None:
            buf = self.file.read(size)
            self.file.seek(size * -1, os.SEEK_CUR)

            buf, = struct.unpack_from(__FMT, buf)
        return buf

    def __str__(self):
        return "%s" % str(FileStream)
