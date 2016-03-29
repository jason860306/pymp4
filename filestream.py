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


class FileStream:
    """
    some utility function
    """

    __LittleEndian = int(0)
    __BigEndian = int(1)

    def __init__(self, file, endian=__LittleEndian):
        if file is None:
            print "file is None"
            return

        self.file = file
        self.endian = endian

    def Tell(self):
        if self.file is None:
            return 0
        return self.file.tell()

    def Seek(self, offset, whence=None):
        if self.file is None:
            return
        self.file.seek(offset, whence)

    def ReadInt64(self):
        __FMT = '!q' if (self.endian == FileStream.__LittleEndian) else '@q'

        if self.file:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int64(num[0]).value
            # return int(num[0])
        return 0

    def ReadUint64(self):
        __FMT = '!Q' if (self.endian == FileStream.__LittleEndian) else '@Q'

        if self.file:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint64(num[0]).value
            # return int(num[0])
        return 0

    def ReadInt32(self):
        __FMT = '!i' if (self.endian == FileStream.__LittleEndian) else '@i'

        if self.file:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int32(num[0]).value
            # return int(num[0])
        return 0

    def ReadUInt32(self):
        __FMT = '!I' if (self.endian == FileStream.__LittleEndian) else '@I'

        if self.file:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint32(num[0]).value
            # return int(num[0])
        return 0

    def ReadInt16(self):
        __FMT = '!h' if (self.endian == FileStream.__LittleEndian) else '@h'

        if self.file:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int16(num[0]).value
            # return int(num[0])
        return 0

    def ReadUInt16(self):
        __FMT = '!H' if (self.endian == FileStream.__LittleEndian) else '@H'

        if self.file:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint16(num[0]).value
            # return int(num[0])
        return 0

    def ReadInt8(self):
        __FMT = '!b' if (self.endian == FileStream.__LittleEndian) else '@b'

        if self.file:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int8(num[0]).value
            # return int(num[0])
        return 0

    def ReadUInt8(self):
        __FMT = '!B' if (self.endian == FileStream.__LittleEndian) else '@B'

        if self.file:
            size = struct.calcsize(__FMT)
            buf = self.file.read(size)
            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint8(num[0]).value
            # return int(num[0])
        return 0

    def ReadByte(self, size):
        __FMT = '!%ds' % size if (self.endian == FileStream.__LittleEndian) else '@%ds' % size

        buf = ''
        if self.file:
            buf = self.file.read(size)
            buf = struct.unpack_from(__FMT, buf)
        return buf

    def PeekInt64(self):
        __FMT = '!q' if (self.endian == FileStream.__LittleEndian) else '@q'

        if self.file:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.Seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int64(num[0]).value
            # return int(num[0])
        return 0

    def PeekUint64(self):
        __FMT = '!Q' if (self.endian == FileStream.__LittleEndian) else '@Q'

        if self.file:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.Seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint64(num[0]).value
            # return int(num[0])
        return 0

    def PeekInt32(self):
        __FMT = '!i' if (self.endian == FileStream.__LittleEndian) else '@i'

        if self.file:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.Seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int32(num[0]).value
            # return int(num[0])
        return 0

    def PeekUInt32(self):
        __FMT = '!I' if (self.endian == FileStream.__LittleEndian) else '@I'

        if self.file:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.Seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int32(num[0]).value
            # return int(num[0])
        return 0

    def PeekInt16(self):
        __FMT = '!h' if (self.endian == FileStream.__LittleEndian) else '@h'

        if self.file:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.Seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int16(num[0]).value
            # return int(num[0])
        return 0

    def PeekUInt16(self):
        __FMT = '!H' if (self.endian == FileStream.__LittleEndian) else '@H'

        if self.file:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.Seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint16(num[0]).value
            # return int(num[0])
        return 0

    def PeekInt8(self):
        __FMT = '!b' if (self.endian == FileStream.__LittleEndian) else '@b'

        if self.file:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.Seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_int8(num[0]).value
            # return int(num[0])
        return 0

    def PeekUInt8(self):
        __FMT = '!B' if (self.endian == FileStream.__LittleEndian) else '@B'

        if self.file:
            size = struct.calcsize(__FMT)

            buf = self.file.read(size)
            self.file.Seek(size * -1, os.SEEK_CUR)

            num = struct.unpack_from(__FMT, buf)
            return ctypes.c_uint8(num[0]).value
            # return int(num[0])
        return 0

    def PeekByte(self, size):
        __FMT = '!%ds' % size if (self.endian == FileStream.__LittleEndian) else '@%ds' % size

        buf = ''
        if self.file:
            buf = self.file.read(size)
            self.file.Seek(size * -1, os.SEEK_CUR)

            buf = struct.unpack_from(__FMT, buf)
        return buf

    def __str__(self):
        return "%s" % str(FileStream)
