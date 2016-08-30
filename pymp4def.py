#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 11:12'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import ctypes
# import struct


LittleEndian = 0
BigEndian = 1


Int8ByteLen = ctypes.sizeof(ctypes.c_int8)  # struct.calcsize('!s')
Int16ByteLen = ctypes.sizeof(ctypes.c_int16)  # struct.calcsize('!h')
Int32ByteLen = ctypes.sizeof(ctypes.c_int32)  # struct.calcsize('!i')
Int64ByteLen = ctypes.sizeof(ctypes.c_int64)  # struct.calcsize('!q')

UInt8ByteLen = ctypes.sizeof(ctypes.c_uint8)  # Int8ByteLen
UInt16ByteLen = ctypes.sizeof(ctypes.c_uint16)  # struct.calcsize('!H')
UInt32ByteLen = ctypes.sizeof(ctypes.c_uint32)  # struct.calcsize('!I')
UInt64ByteLen = ctypes.sizeof(ctypes.c_uint64)  # struct.calcsize('!Q')

VideTrackType = 'vide'
SounTrackType = 'soun'
HintTrackType = 'hint'

DUMP_TYPE_JSON = "json"
DUMP_TYPE_XML = "xml"

UTC_NONE_TIME = 'UTC 1904-01-01 00:00:00'
UTC_MP4_INTERVAL = (((1970 - 1904) * 365) + 17) * 24 * 60 * 60

H264_START_CODE = ['\0', '\0', '\0', '\1']


# NALU_BYTE_SIZE = [1, 2, 4]

# """
# inline MP4Timestamp MP4GetAbsTimestamp() {
# 	struct timeval tv;
# 	gettimeofday(&tv, NULL);
# 	MP4Timestamp ret;
# 	ret = tv.tv_sec;
# 	ret += 2082844800;
# 	return ret;	// MP4 start date is 1/1/1904
# 	// 208284480 is (((1970 - 1904) * 365) + 17) * 24 * 60 * 60
# }
# """


def parse_4cc(four_cc_num):
    num1 = (four_cc_num & 0xFF000000) >> 24
    num2 = (four_cc_num & 0x00FF0000) >> 16
    num3 = (four_cc_num & 0x0000FF00) >> 8
    num4 = (four_cc_num & 0x000000FF)
    return chr(num1) + chr(num2) + chr(num3) + chr(num4)


def parse_descr_len(strm):
    descr_len = 0

    hdr_size = 0
    num_bytes = Int32ByteLen
    tmp_bytes = 0
    while tmp_bytes & 0x80 != 0 and hdr_size < num_bytes:
        tmp_bytes = strm.read_uint8()
        descr_len = (descr_len << 7) | (tmp_bytes & 0x7F)
        hdr_size += 1

    return descr_len, hdr_size
