#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 15:56'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *


class Edts(Box):
    """
    aligned(8) class EditBox extends Box(‘edts’) {
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)

        self.elst = None

    def decode(self, file=None):
        file_strm = Box.decode(self, file)

        left_size = self.size() - self.get_size()
        while left_size > 0:
            tmp_box = Box()
            if tmp_box.type == FourCCMp4Elst:
                self.elst = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.elst.decode(file)
            left_size -= tmp_box.size()

        return file_strm

    def __str__(self):
        logstr = "%s, elst = %s" % (Box.__str__(self), self.elst)
        return logstr
