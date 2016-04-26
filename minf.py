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
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Vmhd:
                self.vmhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.vmhd.decode(file_strm)
                self.offset += self.vmhd.Size()
            elif tmp_box.type == FourCCMp4Smhd:
                self.smhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.smhd.decode(file_strm)
                self.offset += self.smhd.Size()
            elif tmp_box.type == FourCCMp4Dinf:
                self.dinf = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.dinf.decode(file_strm)
                self.offset += self.dinf.Size()
            elif tmp_box.type == FourCCMp4Stbl:
                self.stbl = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.stbl.decode(file_strm)
                self.offset += self.stbl.Size()
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def sample_count(self):
        return 0 if (self.stbl == None) else self.stbl.sample_count()

    def bitsize(self):
        return 0 if (self.stbl == None) else self.stbl.bitsize()

    def find_sample_index(self, timestamp):
        return -1 if (self.stbl == None) else self.stbl.find_sample_index(timestamp)

    def get_sample_size(self, sample_index):
        return 0 if (self.stbl == None) else self.stbl.get_sample_size(sample_index)

    def find_chunk_index(self, sample_index):
        return -1 if (self.stbl == None) else self.stbl.find_chunk_index(sample_index)

    def chunk_last_sample_index(self, chunk_index):
        return -1 if (self.stbl == None) else self.stbl.chunk_last_sample_index(chunk_index)

    def chunk_offset(self, chunk_idx):
        return -1 if (self.stbl == None) else self.stbl.chunk_offset(chunk_idx)

    def find_sync_sample_index(self, sample_index):
        return -1 if (self.stbl == None) else self.stbl.find_sync_sample_index(sample_index)

    def __str__(self):
        logstr = "\t\t%s\n%s\n%s\n%s\n%s\n" % \
                 (Box.__str__(self), self.vmhd, self.smhd, self.dinf, self.stbl)
        return logstr
