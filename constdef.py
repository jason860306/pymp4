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

FourCCMp4Root = 'root'
FourCCMp4Uuid = 'uuid'

FourCCMp4Moov = 'moov'
FourCCMp4Mvhd = 'mvhd'
FourCCMp4Trak = 'trak'
FourCCMp4Tkhd = 'tkhd'
FourCCMp4Edts = 'edts'
FourCCMp4Elst = 'elst'
FourCCMp4Mdia = 'mdia'
FourCCMp4Mdhd = 'mdhd'
FourCCMp4Hdlr = 'hdlr'
FourCCMp4Minf = 'minf'
FourCCMp4Vmhd = 'vmhd'
FourCCMp4Smhd = 'smhd'
FourCCMp4Dinf = 'dinf'
FourCCMp4Dref = 'dref'
FourCCMp4Stbl = 'stbl'
FourCCMp4Stts = 'stts'
FourCCMp4Ctts = 'ctts'
FourCCMp4Stss = 'stss'
FourCCMp4Stsd = 'stsd'
FourCCMp4Stsz = 'stsz'
FourCCMp4Stsc = 'stsc'
FourCCMp4Stco = 'stco'
FourCCMp4Co64 = 'co64'
FourCCMp4Mdat = 'mdat'
FourCCMp4Udat = 'udat'
FourCCMp4Ftyp = 'ftyp'
FourCCMp4Free = 'free'
FourCCMp4Skip = 'skip'


def ParseFourCC(four_cc_num):
    num1 = (four_cc_num & 0xFF000000) >> 24
    num2 = (four_cc_num & 0x00FF0000) >> 16
    num3 = (four_cc_num & 0x0000FF00) >> 8
    num4 = (four_cc_num & 0x000000FF)
    return (chr(num1) + chr(num2) + chr(num3) + chr(num4))
