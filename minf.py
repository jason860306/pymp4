#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 18:06'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import mp4boxes
from box import *


class Minf(Box):
    """
    aligned(8) class MediaInformationBox extends Box(‘minf’) {
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.vmhd = None
        self.smhd = None
        self.dinf = None
        self.stbl = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Vmhd:
                self.vmhd = mp4boxes.MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.vmhd.decode(file_strm)
            elif tmp_box.type == FourCCMp4Smhd:
                self.smhd = mp4boxes.MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.smhd.decode(file_strm)
            elif tmp_box.type == FourCCMp4Dinf:
                self.dinf = mp4boxes.MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.dinf.decode(file_strm)
            elif tmp_box.type == FourCCMp4Stbl:
                self.stbl = mp4boxes.MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.stbl.decode(file_strm)
            else:
                file_strm.seek(tmp_box.Size(), os.SEEK_CUR)
            left_size -= tmp_box.Size()

        return file_strm

    def __str__(self):
        logstr = "%s, vmhd = %s, smhd = %s, dinf = %s, stbl = %s" % \
                 (Box.__str__(self), self.vmhd, self.smhd, self.dinf, self.stbl)
        return logstr
