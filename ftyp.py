#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/1 17:22'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *
from constdef import *


class Ftyp(Box):
    """
    aligned(8) class FileTypeBox extends Box(‘ftyp’) {
        unsigned int(32) major_brand;
        unsigned int(32) minor_version;
        unsigned int(32) compatible_brands[]; // to end of the box
    }
    """

    def __init__(self, offset=0, box=None):
        Box.__init__(self, offset, box)

        self.major_brand = 0
        self.minor_brand = 0
        self.compatible_brands = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        major_brand_ = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen
        self.major_brand = ParseFourCC(major_brand_)

        self.minor_brand = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        left_size = Box.Size(self) - Box.GetLength(self)
        left_size -= UInt32ByteLen * 2
        count = left_size / UInt32ByteLen
        for idx in range(0, count):
            compatible_brand_ = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen
            compatible_brand = ParseFourCC(compatible_brand_)
            self.compatible_brands.append(compatible_brand)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def __str__(self):
        logstr = "%s\nmajor_brand = %s\nminor_brand = %08ld(0x%016lx)\ncompatible_brands = [" % \
                 (Box.__str__(self), self.major_brand, self.minor_brand, self.minor_brand)
        for brand in self.compatible_brands:
            logstr += "%s, " % brand
        logstr += "]\n"
        return logstr
