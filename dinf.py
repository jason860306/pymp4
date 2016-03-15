#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/8 22:08'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *
from mp4boxes import *


class Dinf(Box):
    """
    aligned(8) class DataInformationBox extends Box(‘dinf’) {
    }
    """

    def __init__(self, box=None):
        if isinstance(box, Box):
            Box.__init__(self, box)
        self.dref = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            if tmp_box.type == FourCCMp4Dref:
                self.dref = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.dref.decode(file_strm)
            left_size -= tmp_box.size()

        return file_strm

    def __str__(self):
        logstr = "%s, dref = %s" % (Box.__str__(self), self.dref)
        return logstr
