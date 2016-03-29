#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 15:34'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import mp4boxes
from box import *


class Trak(Box):
    """
    aligned(8) class TrackBox extends Box(‘trak’) {
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.tkhd = None
        self.edts = None
        self.mdia = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Tkhd:
                self.tkhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.tkhd.decode(file_strm)
                self.offset += self.tkhd.Size()
            elif tmp_box.type == FourCCMp4Edts:
                self.edts = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.edts.decode(file_strm)
                self.offset += self.edts.Size()
            elif tmp_box.type == FourCCMp4Mdia:
                self.mdia = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mdia.decode(file_strm)
                self.offset += self.mdia.Size()
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def __str__(self):
        logstr = "%s\n%s\n%s\n%s\n" % \
                 (Box.__str__(self), self.tkhd, self.edts, self.mdia)
        return logstr
