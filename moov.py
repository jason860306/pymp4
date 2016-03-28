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


import mp4boxes
from box import *


class Moov(Box):
    """
    aligned(8) class MovieBox extends Box(‘moov’){
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.mvhd = None
        self.trak = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Mvhd:
                self.mvhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mvhd.decode(file_strm)
                self.offset += self.mvhd.Size()
            elif tmp_box.type == FourCCMp4Trak:
                trak_ = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = trak_.decode(file_strm)
                self.offset += trak_.Size()
                self.trak.append(trak_)
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
        logstr = "%s, mvhd = %s, trak = [" % (Box.__str__(self), self.mvhd)
        for i in range(len(self.trak)):
            logstr += "[%d. %s], " % (i, self.trak[i])
        logstr += "]"
        return logstr
