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
import mp4boxes


class Edts(Box):
    """
    aligned(8) class EditBox extends Box(‘edts’) {
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.elst = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = Box.Size(self) - Box.GetLength(self)
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Elst:
                self.elst = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.elst.decode(file_strm)
                self.offset += self.elst.Size()
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def __str__(self):
        logstr = "\t%s\n\t%s\n" % (Box.__str__(self), self.elst)
        return logstr
