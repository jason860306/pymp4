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


from box import *
from mp4boxes import *


class Mdia(Box):
    """
    aligned(8) class MediaBox extends Box(‘mdia’) {
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)

        self.mdhd = None
        self.hdlr = None
        self.minf = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.size() - self.get_size()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Mdhd:
                self.mdhd = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.mdhd.decode(file_strm)
            elif tmp_box.type == FourCCMp4Hdlr:
                self.hdlr = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.hdlr.decode(file_strm)
            elif tmp_box.type == FourCCMp4Minf:
                self.minf = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.minf.decode(file_strm)
            left_size -= tmp_box.size()

        return file_strm

    def __str__(self):
        logstr = "%s, mdhd = %s, hdlr = %s, minf = %s" % \
                 (Box.__str__(self), self.mdhd, self.hdlr, self.minf)
        return logstr
