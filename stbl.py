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


from mp4boxes import *
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

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)

        self.stts = None
        self.ctts = None
        self.stss = None
        self.stsd = None
        self.stsz = None
        self.stsc = None
        self.stco = None
        self.co64 = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.size() - self.get_size()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Stts:
                self.stts = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.stts.decode(file_strm)
            elif tmp_box.type == FourCCMp4Ctts:
                self.ctts = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.ctts.decode(file_strm)
            elif tmp_box.type == FourCCMp4Stss:
                self.stss = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.stss.decode(file_strm)
            elif tmp_box.type == FourCCMp4Stsd:
                self.stsd = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.stsd.decode(file_strm)
            elif tmp_box.type == FourCCMp4Stsz:
                self.stsz = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.stsz.decode(file_strm)
            elif tmp_box.type == FourCCMp4Stsc:
                self.stsc = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.stsc.decode(file_strm)
            elif tmp_box.type == FourCCMp4Stco:
                self.stco = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.stco.decode(file_strm)
            elif tmp_box.type == FourCCMp4Co64:
                self.co64 = MP4Boxes[tmp_box.type](tmp_box)
                file_strm = self.co64.decode(file_strm)
            left_size -= tmp_box.size()

        return file_strm

    def __str__(self):
        logstr = "%s, stts = %s, ctts = %s, stss = %s, stsd = %s, " \
                 "stsz = %s, stsc = %s, stco = %s, co64 = %s" % \
                 (Box.__str__(self), self.stts, self.ctts, self.stss,
                  self.stsd, self.stsz, self.stsc, self.stco, self.co64)
        return logstr
