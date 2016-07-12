#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # Administrator
__date__ = '2016/6/23 17:33'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"


# '$Source$'


class Stream(object):
    """
    some utility function
    """

    LittleEndian = 0
    BigEndian = 1

    def __init__(self, endian=LittleEndian):
        self.endian = endian

    def tell(self):
        pass

    def seek(self, offset, whence=None):
        pass

    def read_int_n(self, int_size):
        pass

    def read_uint_n(self, uint_size):
        pass

    def read_int64(self):
        pass

    def read_uint64(self):
        pass

    def read_int32(self):
        pass

    def read_uint32(self):
        pass

    def read_int16(self):
        pass

    def read_uint16(self):
        pass

    def read_int8(self):
        pass

    def read_uint8(self):
        pass

    def read_byte(self, size):
        pass

    def peek_int64(self):
        pass

    def peek_uint64(self):
        pass

    def peek_int32(self):
        pass

    def peek_uint32(self):
        pass

    def peek_int16(self):
        pass

    def peek_uint16(self):
        pass

    def peek_int8(self):
        pass

    def peek_uint8(self):
        pass

    def peek_byte(self, size):
        pass

    def __str__(self):
        return "%s" % str(Stream)
