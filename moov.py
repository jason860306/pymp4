#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/1 17:22'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import mp4boxes
from box import *


class Moov(Box):
    """
    aligned(8) class MovieBox extends Box(‘moov’){
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.mvhd = None
        self.trak = []

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Mvhd:
                self.mvhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mvhd.decode(file_strm)
                self.offset += self.mvhd.Size()
            elif tmp_box.type == FourCCMp4Trak:
                trak_ = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = trak_.decode(file_strm)
                self.offset += trak_.Size()
                self.trak.append(trak_)
            elif tmp_box.type == FourCCMp4Mdia:
                self.mdia = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mdia.decode(file_strm)
                self.offset += self.mdia.Size()
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def vide_duration(self):
        vide_duration_ = 0
        for trk in self.trak:
            if trk.mediatype() == VideTrackType:
                vide_duration_ = trk.duration()
        return vide_duration_

    def soun_duration(self):
        soun_duration_ = 0
        for trk in self.trak:
            if trk.mediatype() == SounTrackType:
                soun_duration_ = trk.duration()
        return soun_duration_

    def duration(self):
        vduration = self.vide_duration()
        sduration = self.soun_duration()
        duration_ = self.mvhd.duration()
        return max(vduration, sduration, duration_)

    def width(self):
        width_ = 0
        for trk in self.trak:
            if trk.mediatype() == VideTrackType:
                width_ = trk.width()
                break
        return width_

    def height(self):
        height_ = 0
        for trk in self.trak:
            if trk.mediatype() == VideTrackType:
                height_ = trk.height()
                break
        return height_

    def sample_size(self):
        sample_size_ = 0
        for trk in self.trak:
            if trk.mediatype() == VideTrackType:
                sample_size_ = trk.sample_size()
                break
        return sample_size_

    def fps(self):
        duration_ = 0
        for trk in self.trak:
            if trk.mediatype() == VideTrackType:
                duration_ = trk.duration()
                break
        sample_size_ = self.sample_size()
        return 0.0 if (duration_) == 0 else (1.0 * sample_size_ / duration_)

    def bitrate(self):
        bsize = 0
        duration_ = 0
        for trk in self.trak:
            bsize += trk.bitsize()
            duration_ += trk.duration()
        return 0.0 if (duration_ == 0) else (1.0 * bsize / duration_)

    def find_sample_index(self, utc_timestamp, track_type=VideTrackType):
        mp4_timestamp = utc_timestamp + UTC_MP4_INTERVAL
        for trk in self.trak:
            if trk.mediatype == track_type:
                return trk.find_sample_index(mp4_timestamp)
        else:
            pass  # raise

    def __str__(self):
        logstr = "%s\n%s\n" % (Box.__str__(self), self.mvhd)
        for i in range(len(self.trak)):
            logstr += "\t%08ld. %s" % (i, self.trak[i])
        logstr += "\n"
        return logstr
