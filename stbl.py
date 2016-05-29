#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/8 22:59'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import mp4boxes
from mp4boxdesc import *
from stts import *


class Stbl(Box):
    """
    aligned(8) class SampleTableBox extends Box(‘stbl’) {
    }

    stbl        sample table atom, container for the time/space map
        stts    (decoding) time-to-sample
        ctts    composition time-to-sample table
        stss    sync (key, I-frame) sample map
        stsd    sample descriptions (codec types, initialization etc.)
        stsz    sample sizes (framing)
        stsc    sample-to-chunk, partial data-offset information
        stco    chunk offset, partial data-offset information
        co64    64-bit chunk offset
        stsh    shadow sync
        stdp    degradation priority
    """

    def __init__(self, offset=0, box=None, handler_type=''):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.handler_type = handler_type

        self.stts = None
        self.ctts = None
        self.stss = None
        self.stsd = None
        self.stsz = None
        self.stsc = None
        self.stco = None
        self.co64 = None

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Stts:
                self.stts = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.stts.decode(file_strm)
                self.offset += self.stts.Size()
            elif tmp_box.type == FourCCMp4Ctts:
                self.ctts = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.ctts.decode(file_strm)
                self.offset += self.ctts.Size()
            elif tmp_box.type == FourCCMp4Stss:
                self.stss = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.stss.decode(file_strm)
                self.offset += self.stss.Size()
            elif tmp_box.type == FourCCMp4Stsd:
                self.stsd = mp4boxes.MP4Boxes[tmp_box.type](
                    self.offset, tmp_box, self.handler_type)
                file_strm = self.stsd.decode(file_strm)
                self.offset += self.stsd.Size()
            elif tmp_box.type == FourCCMp4Stsz:
                self.stsz = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.stsz.decode(file_strm)
                self.offset += self.stsz.Size()
            elif tmp_box.type == FourCCMp4Stsc:
                self.stsc = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.stsc.decode(file_strm)
                self.offset += self.stsc.Size()
            elif tmp_box.type == FourCCMp4Stco:
                self.stco = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.stco.decode(file_strm)
                self.offset += self.stco.Size()
            elif tmp_box.type == FourCCMp4Co64:
                self.co64 = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.co64.decode(file_strm)
                self.offset += self.co64.Size()
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def sample_count(self):
        return 0 if (self.stsz == None) else self.stsz.sample_count

    def bitsize(self):
        return 0 if (self.stsz == None) else self.stsz.bitsize()

    def find_sample_index(self, timestamp):
        return -1 if (self.stts == None) else self.stts.find_sample_index(timestamp)

    def get_sample_size(self, sample_index):
        return -1 if (self.stsz == None) else self.stsz.get_sample_size(sample_index)

    def find_chunk_index(self, sample_index):
        return -1 if (self.stsc == None) else self.stsc.find_chunk_index(sample_index)

    def chunk_last_sample_index(self, chunk_index):
        return -1 if (self.stsc == None) else self.stsc.chunk_last_sample_index(chunk_index)

    def chunk_offset(self, chunk_idx):
        return -1 if (self.stco == None) else self.stco.chunk_offset(chunk_idx)

    def find_sync_sample_index(self, sample_index):
        return -1 if (self.stss == None) else self.stss.find_sync_sample_index(sample_index)

    def dump(self):
        dump_info = Box.dump(self)
        if None != self.stts:
            dump_info[self.stts.type] = self.stts.dump()
        if None != self.ctts:
            dump_info[self.ctts.type] = self.ctts.dump()
        if None != self.stss:
            dump_info[self.stss.type] = self.stss.dump()
        if None != self.stsd:
            dump_info[self.stsd.type] = self.stsd.dump()
        if None != self.stsz:
            dump_info[self.stsz.type] = self.stsz.dump()
        if None != self.stsc:
            dump_info[self.stsc.type] = self.stsc.dump()
        if None != self.stco:
            dump_info[self.stco.type] = self.stco.dump()
        if None != self.co64:
            dump_info[self.co64.type] = self.co64.dump()
        return dump_info

    def __str__(self):
        logstr = "\t\t\t%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % \
                 (Box.__str__(self), self.stts, self.ctts, self.stss,
                  self.stsd, self.stsz, self.stsc, self.stco, self.co64)
        return logstr
