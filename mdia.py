#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 16:29'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import mp4boxes
from box import *


class Mdia(Box):
    """
    aligned(8) class MediaBox extends Box(‘mdia’) {
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.mdhd = None
        self.hdlr = None
        self.minf = None

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Mdhd:
                self.mdhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mdhd.decode(file_strm)
                self.offset += self.mdhd.Size()
            elif tmp_box.type == FourCCMp4Hdlr:
                self.hdlr = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.hdlr.decode(file_strm)
                self.offset += self.hdlr.Size()
            elif tmp_box.type == FourCCMp4Minf:
                self.minf = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.minf.decode(file_strm)
                self.offset += self.minf.Size()
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def duration(self):
        return 0 if (self.minf == None) else self.minf.duration()

    def mediatype(self):
        return None if (self.hdlr == None) else self.hdlr.handler_type

    def sample_count(self):
        return 0 if (self.minf == None) else self.minf.sample_count()

    def bitsize(self):
        return 0 if (self.minf == None) else self.minf.bitsize()

    def find_sample_index(self, timestamp):
        return -1 if (self.minf == None) else self.minf.find_sample_index(timestamp)

    def get_sample_size(self, sample_index):
        return 0 if (self.minf == None) else self.minf.get_sample_size(sample_index)

    def find_chunk_index(self, sample_index):
        return -1 if (self.minf == None) else self.minf.find_chunk_index(sample_index)

    def chunk_last_sample_index(self, chunk_index):
        return -1 if (self.minf == None) else self.minf.chunk_last_sample_index(chunk_index)

    def chunk_offset(self, chunk_idx):
        return -1 if (self.minf == None) else self.minf.chunk_offset(chunk_idx)

    def __str__(self):
        logstr = "\t%s\n%s\n%s\n%s\n" % \
                 (Box.__str__(self), self.mdhd, self.hdlr, self.minf)
        return logstr
