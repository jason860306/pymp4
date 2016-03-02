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

from util import *


class Box:
    """
    aligned(8) class Box (unsigned int(32) boxtype, optional unsigned int(8)[16] extended_type) {
        unsigned int(32) size;
        unsigned int(32) type = boxtype;
        if (size==1) {
             unsigned int(64) largesize;
        } else if (size==0) {
             // box extends to end of file
        }
        if (boxtype==‘uuid’) {
             unsigned int(8)[16] usertype = extended_type;
        }
    }
    """

    __USER_TYPE = 'uuid'

    def __init__(self):
        self.size = 0
        self.type = ''
        self.large_size = 0
        self.user_type = ''

    def decode(self, file=None):
        if file:
            self.size = Util(file).read_uint32_lit()
            type_ = Util(file).read_uint32_lit()
            self.type = str(type_)
            if self.size == 1:
                self.large_size = Util(file).read_uint64_lit()
            if self.type == self.__USER_TYPE:
                user_type_ = Util(file).read_uint16_lit()
                self.user_type = str(user_type_)

    def size(self):
        return self.size if (self.size == 1) else self.large_size

    def get_size(self):
        large_size_ = struct.calcsize('!Q') if (self.size == 1) else 0
        user_type_ = struct.calcsize('!16s') if (self.type == self.__USER_TYPE) else 0
        size_ = struct.calcsize('!II') + large_size_ + user_type_
        return size_

    def __str__(self):
        return "size = %ld, type = %s" % (self.size, self.type)
