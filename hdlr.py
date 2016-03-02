#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 17:31'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Hdlr(FullBox):
    """
    aligned(8) class HandlerBox extends FullBox(‘hdlr’, version = 0, 0) {
        unsigned int(32) pre_defined = 0;
        unsigned int(32) handler_type;
        const unsigned int(32)[3] reserved = 0;
        string name;
    }
    """

    def __init__(self):
        FullBox.__init__(self)

        self.pre_defined = 0
        self.handler_type = ''
        self.reserved = [0 for i in range(3)]
        self.name = ''

    def decode(self, file=None):
        FullBox.decode(self, file)

        file_strm = Util(file)

        self.pre_defined = file_strm.read_uint32_lit()
        handler_type_ = file_strm.read_uint32_lit()
        self.handler_type = str(handler_type_)

        for i in range(len(self.reserved)):
            self.reserved[i] = file_strm.read_uint32_lit()

        left_size = Box.size(self) - FullBox.get_size(self)
        left_size -= struct.calcsize('!I')  # sizeof(pre_defined)
        left_size -= struct.calcsize('!I')  # sizeof(handler_type)
        left_size -= 3 * struct.calcsize('!I')  # sizeof(reserved)
        self.name = str(file_strm.read_buf(left_size))

    def __str__(self):
        logstr = "%s, pre_defined = %d, handler_type = %s, reserved = [" % \
                 (FullBox.__str__(self), self.pre_defined, self.handler_type)
        for r in self.reserved:
            logstr += "%d, " % r
        logstr += "], name = %s" % self.name
        return logstr
