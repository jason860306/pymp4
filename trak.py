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


import mp4boxes
from box import *


class Trak(Box):
    """
    aligned(8) class TrackBox extends Box(‘trak’) {
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.tkhd = None
        self.edts = None
        self.mdia = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Tkhd:
                self.tkhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.tkhd.decode(file_strm)
                self.offset += self.tkhd.Size()
            elif tmp_box.type == FourCCMp4Edts:
                self.edts = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.edts.decode(file_strm)
                self.offset += self.edts.Size()
            elif tmp_box.type == FourCCMp4Mdia:
                self.mdia = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mdia.decode(file_strm)
                self.offset += self.mdia.Size()
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def track_id(self):
        return -1 if (self.tkhd is None) else self.tkhd.track_ID

    def create_time(self):
        return UTC_NONE_TIME if (self.tkhd is None) else self.tkhd.creation_time_fmt

    def modify_time(self):
        return UTC_NONE_TIME if (self.tkhd is None) else self.tkhd.modification_time_fmt

    def track_duration(self):
        return (0 if (self.tkhd is None) else self.tkhd.duration)

    def media_duration(self):
        return (0 if (self.mdia is None) else self.mdia.duration())

    def width(self):
        return self.tkhd.width

    def height(self):
        return self.tkhd.height

    def mediatype(self):
        return None if (self.mdia is None) else self.mdia.mediatype()

    def sample_count(self):
        return 0 if (self.mdia is None) else self.mdia.sample_count()

    def bitsize(self):
        return 0 if (self.mdia is None) else self.mdia.bitsize()

    def find_sample_index(self, timestamp):
        return -1 if (self.mdia is None) else self.mdia.find_sample_index(timestamp)

    def get_sample_duration(self, sample_idx):
        return -1 if (self.mdia is None) else self.mdia.get_sample_duration(sample_idx)

    def get_sample_size(self, sample_index):
        return 0 if (self.mdia is None) else self.mdia.get_sample_size(sample_index)

    def find_chunk_index(self, sample_index):
        return -1 if (self.mdia is None) else self.mdia.find_chunk_index(sample_index)

    def chunk_1st_sample_index(self, chunk_index):
        return -1 if (self.mdia is None) else self.mdia.chunk_1st_sample_index(chunk_index)

    def chunk_last_sample_index(self, chunk_index):
        return -1 if (self.mdia is None) else self.mdia.chunk_last_sample_index(chunk_index)

    def chunk_sample_index_diff(self, chunk_index, sample_index):
        return -1 if (self.mdia is None) else self.mdia.chunk_sample_index_diff(
            chunk_index, sample_index)

    def chunk_offset(self, chunk_idx):
        return -1 if (self.mdia is None) else self.mdia.chunk_offset(chunk_idx)

    def get_chunk_offset_list(self):
        return -1 if (self.mdia is None) else self.mdia.get_chunk_offset_list()

    def get_sample_per_chunk(self, chunk_idx):
        return -1 if (self.mdia is None) else self.mdia.get_sample_per_chunk(chunk_idx)

    def find_sync_sample_index(self, sample_index):
        return -1 if (self.mdia is None) else self.mdia.find_sync_sample_index(sample_index)

    def get_sps(self):
        return None if (self.mdia is None) else self.mdia.get_sps()

    def get_pps(self):
        return None if (self.mdia is None) else self.mdia.get_pps()

    def get_spse(self):
        return None if (self.mdia is None) else self.mdia.get_spse()

    def dump(self):
        dump_info = Box.dump(self)
        if None != self.tkhd:
            dump_info[self.tkhd.type] = self.tkhd.dump()
        if None != self.edts:
            dump_info[self.edts.type] = self.edts.dump()
        if None != self.mdia:
            dump_info[self.mdia.type] = self.mdia.dump()
        return dump_info

    def __str__(self):
        logstr = "%s\n%s\n%s\n%s\n" % \
                 (Box.__str__(self), self.tkhd, self.edts, self.mdia)
        return logstr
