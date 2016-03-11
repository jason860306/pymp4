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

Int8ByteLen = struct.calcsize('!s')
Int16ByteLen = struct.calcsize('!h')
Int32ByteLen = struct.calcsize('!i')
Int64ByteLen = struct.calcsize('!q')

UInt8ByteLen = Int8ByteLen
UInt16ByteLen = struct.calcsize('!H')
UInt32ByteLen = struct.calcsize('!I')
UInt64ByteLen = struct.calcsize('!Q')
