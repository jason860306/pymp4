#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 16:29'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import mp4boxes
from box import *


class Mdia(Box):
    """
    aligned(8) class MediaBox extends Box(‘mdia’) {
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.mdhd = None
        self.hdlr = None
        self.minf = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Mdhd:
                self.mdhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mdhd.decode(file_strm)
                self.offset += self.mdhd.Size()
            elif tmp_box.type == FourCCMp4Hdlr:
                self.hdlr = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.hdlr.decode(file_strm)
                self.offset += self.hdlr.Size()
            elif tmp_box.type == FourCCMp4Minf:
                self.minf = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.minf.decode(file_strm)
                self.offset += self.minf.Size()
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def __str__(self):
        logstr = "%s, mdhd = %s, hdlr = %s, minf = %s" % \
                 (Box.__str__(self), self.mdhd, self.hdlr, self.minf)
        return logstr
