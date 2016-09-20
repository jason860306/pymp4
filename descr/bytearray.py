#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:31:47'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from pymp4def import *
from util.bytestream import *


class ByteArray(object):
    """
    7.2.6.14.3.4 ByteArray
    This Subclause defines syntax and semantics to carry a generic string or
    array of bytes which is used extensively throughout the IPMP specifications.

    7.2.6.14.3.4.1 Syntax
    expandable class ByteArray
    {
        bit(8) data[sizeOfInstance()];
    }
    7.2.6.14.3.4.2 Semantics
    data - the string or array of bytes carried.
    """

    def __init__(self):
        self.len = 0
        self.data = ''

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        self.len = parse_descr_len(file_strm)
        self.data = file_strm.read_byte(self.len)

    def gen_strm(self):
        return ByteStream(self.data, self.len)

    def dump(self):
        dump_info = dict()
        dump_info['len'] = str(self.len)
        dump_info['data'] = self.data
        return dump_info

    def __str__(self):
        log_str = ''
        return log_str
