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


from box import *
from mp4boxes import *


class Moov(Box):
    """
    aligned(8) class MovieBox extends Box(‘moov’){
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)

        self.mvhd = None
        self.trak = []

    def decode(self, file=None):
        file_strm = Box.decode(self, file)

        left_size = self.size() - self.get_size()
        while left_size > 0:
            tmp_box = Box()
            if tmp_box.type == FourCCMp4Mvhd:
                self.mvhd = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.mvhd.decode(file)
            elif tmp_box.type == FourCCMp4Trak:
                trak_ = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = trak_.decode(file)
                self.trak.append(trak_)
            elif tmp_box.type == FourCCMp4Mdia:
                self.mdia = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.mdia.decode(file)
            left_size -= tmp_box.size()

        return file_strm

    def __str__(self):
        logstr = "%s, mvhd = %s, trak = [" % (Box.__str__(self), self.mvhd)
        for i in range(len(self.trak)):
            logstr += "[%d. %s], " % (i, self.trak[i])
        logstr += "]"
        return logstr
