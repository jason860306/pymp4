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


from box import *
from mp4boxes import *


class Trak(Box):
    """
    aligned(8) class TrackBox extends Box(‘trak’) {
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)

        self.tkhd = None
        self.edts = None
        self.mdia = None

    def decode(self, file=None):
        file_strm = Box.decode(self, file)

        left_size = self.size() - self.get_size()
        while left_size > 0:
            tmp_box = Box()
            if tmp_box.type == FourCCMp4Tkhd:
                self.tkhd = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.tkhd.decode(file)
            elif tmp_box.type == FourCCMp4Edts:
                self.edts = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.edts.decode(file)
            elif tmp_box.type == FourCCMp4Mdia:
                self.mdia = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.mdia.decode(file)
            left_size -= tmp_box.size()

        return file_strm

    def __str__(self):
        logstr = "%s, tkhd = %s, edts = %s, mdia = %s" % \
                 (Box.__str__(self), self.tkhd, self.edts, self.mdia)
        return logstr
