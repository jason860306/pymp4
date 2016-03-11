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


from box import *


class Minf(Box):
    """
    aligned(8) class MediaInformationBox extends Box(‘minf’) {
    }
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)

        self.vmhd = None
        self.smhd = None
        self.dinf = None
        self.stbl = None

    def decode(self, file=None):
        file_strm = Box.decode(self, file)

        left_size = self.size() - self.get_size()
        while left_size > 0:
            tmp_box = Box()
            if tmp_box.type == FourCCMp4Vmhd:
                self.vmhd = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.vmhd.decode(file)
            elif tmp_box.type == FourCCMp4Smhd:
                self.smhd = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.smhd.decode(file)
            elif tmp_box.type == FourCCMp4Dinf:
                self.dinf = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.dinf.decode(file)
            elif tmp_box.type == FourCCMp4Stbl:
                self.stbl = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.stbl.decode(file)
            left_size -= tmp_box.size()

        return file_strm

    def __str__(self):
        logstr = "%s, vmhd = %s, smhd = %s, dinf = %s, stbl = %s" % \
                 (Box.__str__(self), self.vmhd, self.smhd, self.dinf, self.stbl)
        return logstr
