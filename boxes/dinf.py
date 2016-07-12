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


import mp4boxes
from box import *


class Dinf(object, Box):
    """
    aligned(8) class DataInformationBox extends Box(‘dinf’) {
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        self.dref = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Dref:
                self.dref = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.dref.decode(file_strm)
                self.offset += self.dref.Size()
            else:
                file_strm.seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def dump(self):
        dump_info = Box.dump(self)
        dump_info[self.dref.type] = self.dref.dump()
        return dump_info

    def __str__(self):
        logstr = "\t\t\t%s\n%s\n" % (Box.__str__(self), self.dref)
        return logstr
