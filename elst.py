#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 15:59'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class MediaSegmentEntry:
    """
        Each entry defines part of the track time‐line: by mapping
    part of the media time‐line, or by indicating ‘empty’ time, or
    by defining a ‘dwell’, where a single time‐point in the media is
    held for a period.
    """

    def __init__(self, ver):
        self.version = ver

        self.segment_duration = 0
        self.media_time = 0
        self.media_rate_integer = 0
        self.media_rate_fraction = 0

    def decode(self, file=None):
        file_strm = Util(file)

        if self.version == 1:
            self.segment_duration = file_strm.read_uint64_lit()
            self.media_time = file_strm.read_int64_lit()
        else:
            self.segment_duration = file_strm.read_uint32_lit()
            self.media_time = file_strm.read_int32_lit()
        self.media_rate_integer = file_strm.read_int16_lit()
        self.media_rate_fraction = file_strm.read_int16_lit()

    def __str__(self):
        logstr = "segment_duration = %d, media_time = %d, " % \
                 (self.segment_duration, self.media_time)
        logstr += "media_rate_integer = %d, media_rate_fraction = %d" % \
                  (self.media_rate_integer, self.media_rate_fraction)
        return logstr


class Elst(FullBox):
    """
    aligned(8) class EditListBox extends FullBox(‘elst’, version, 0) {
        unsigned int(32) entry_count;
        for (i=1; i <= entry_count; i++) {
            if (version==1) {
                unsigned int(64) segment_duration;
                int(64) media_time;
            } else { // version==0
                unsigned int(32) segment_duration;
                int(32) media_time;
            }
            int(16) media_rate_integer;
            int(16) media_rate_fraction = 0;
        }
    }
    """

    def __init__(self):
        FullBox.__init__(self)

        self.entry_count = 0
        self.segment_entry = []

    def decode(self, file=None):
        FullBox.decode(self, file)

        file_strm = Util(file)

        self.entry_count = file_strm.read_uint32_lit()
        for i in range(self.entry_count):
            segment_entry_ = MediaSegmentEntry(self.version)
            segment_entry_.decode(file)
            self.segment_entry[i] = segment_entry_

    def __str__(self):
        logstr = "%s, entry_count = %d, entries: [" % \
                 (Box.__str__(self), self.entry_count)
        for i in range(len(self.segment_entry)):
            logstr += "%d. %s, " % (i + 1, self.segment_entry[i])
        return logstr
