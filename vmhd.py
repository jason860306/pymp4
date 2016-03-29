#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 18:08'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Vmhd(FullBox):
    """
    aligned(8) class VideoMediaHeaderBox extends FullBox(‘vmhd’, version = 0, 1) {
        template unsigned int(16) graphicsmode = 0; // copy, see below
        template unsigned int(16)[3] opcolor = {0, 0, 0};
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.graphicsmode = 0
        self.opcolor = [0 for i in range(3)]

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.graphicsmode = file_strm.ReadUInt16()
        self.offset += UInt16ByteLen

        for i in range(len(self.opcolor)):
            opcolor_ = file_strm.ReadUInt16()
            self.offset += UInt16ByteLen
            self.opcolor[i] = opcolor_

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def __str__(self):
        logstr = "%s, graphicsmode = %08ld(0x%016lx), opcolor = [" % \
                 (FullBox.__str__(self), self.graphicsmode, self.graphicsmode)
        for i in range(len(self.opcolor)):
            logstr += "%08ld(0x%016lx) " % (self.opcolor[i], self.opcolor[i])
        logstr += "]"
        return logstr
