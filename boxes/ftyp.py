#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/1 17:22'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *
from pymp4def import *


class Ftyp(Box, object):
    """
    aligned(8) class FileTypeBox extends Box(‘ftyp’) {
        unsigned int(32) major_brand;
        unsigned int(32) minor_version;
        unsigned int(32) compatible_brands[]; // to end of the box
    }
    major_brand – is a brand identifier
    minor_version – is an informative integer for the minor version of the major brand
    compatible_brands – is a list, to the end of the box, of brands
    """

    def __init__(self, offset=0, box=None):
        Box.__init__(self, offset, box)

        self.major_brand = 0
        self.minor_brand = 0
        self.compatible_brands = []

    def get_major_brand(self):
        return self.major_brand

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        major_brand_ = file_strm.read_uint32()
        self.offset += UInt32ByteLen
        self.major_brand = parse_4cc(major_brand_)

        self.minor_brand = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        left_size = self.Size() - self.GetLength()
        left_size -= UInt32ByteLen * 2
        count = left_size / UInt32ByteLen
        for idx in range(0, count):
            compatible_brand_ = file_strm.read_uint32()
            self.offset += UInt32ByteLen
            compatible_brand = parse_4cc(compatible_brand_)
            self.compatible_brands.append(compatible_brand)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = Box.dump(self)
        dump_info['major_brand'] = self.major_brand
        dump_info['minor_brand'] = self.minor_brand
        dump_info['minor_brand'] = self.compatible_brands
        return dump_info

    def __str__(self):
        logstr = "%s\nmajor_brand = %s\nminor_brand = %08ld(0x%016lx)\ncompatible_brands = [" % \
                 (Box.__str__(self), self.major_brand, self.minor_brand, self.minor_brand)
        for brand in self.compatible_brands:
            logstr += "%s, " % brand
        logstr += "]\n"
        return logstr
