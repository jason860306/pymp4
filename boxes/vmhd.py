#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 18:08'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import os

from fullbox import *


class Vmhd(object, FullBox):
    """
    aligned(8) class VideoMediaHeaderBox extends FullBox(‘vmhd’, version = 0, 1) {
        template unsigned int(16) graphicsmode = 0; // copy, see below
        template unsigned int(16)[3] opcolor = {0, 0, 0};
    }
    version - is an integer that specifies the version of this box
    graphicsmode - specifies a composition mode for this video track, from the
                   following enumerated set, which may be extended by derived
                   specifications: copy = 0 copy over the existing image
    opcolor - is a set of 3 colour values (red, green, blue) available for use
              by graphics modes
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

        self.graphicsmode = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        for i in range(len(self.opcolor)):
            opcolor_ = file_strm.read_uint16()
            self.offset += UInt16ByteLen
            self.opcolor[i] = opcolor_

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['graphicsmode'] = self.graphicsmode
        dump_info['opcolor'] = self.opcolor
        return dump_info

    def __str__(self):
        logstr = "\t\t\t%s\n\t\t\tgraphicsmode = %08ld(0x%016lx)" \
                 "\n\t\t\topcolor = [" % \
                 (FullBox.__str__(self), self.graphicsmode, self.graphicsmode)
        for i in range(len(self.opcolor)):
            logstr += "\n\t\t\t\t%08ld(0x%016lx) " % (self.opcolor[i], self.opcolor[i])
        logstr += "\n\t\t\t]\n"
        return logstr
