#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 11:12'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import struct

INT8_BYTE_LEN = struct.calcsize('!s')
INT16_BYTE_LEN = struct.calcsize('!h')
INT32_BYTE_LEN = struct.calcsize('!i')
INT64_BYTE_LEN = struct.calcsize('!q')

UINT8_BYTE_LEN = INT8_BYTE_LEN
UINT16_BYTE_LEN = struct.calcsize('!H')
UINT32_BYTE_LEN = struct.calcsize('!I')
UINT64_BYTE_LEN = struct.calcsize('!Q')
