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


import os

from fullbox import *


class MediaSegmentEntry:
    """
        Each entry defines part of the track time‐line: by mapping
    part of the media time‐line, or by indicating ‘empty’ time, or
    by defining a ‘dwell’, where a single time‐point in the media is
    held for a period.
    """

    def __init__(self, offset=0, ver=0):
        self.box_offset = offset
        self.offset = offset
        self.version = ver

        self.segment_duration = 0
        self.media_time = 0
        self.media_rate_integer = 0
        self.media_rate_fraction = 0

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        if self.version == 1:
            self.segment_duration = file_strm.ReadUint64()
            self.offset += UInt64ByteLen

            self.media_time = file_strm.ReadInt64()
            self.offset += Int64ByteLen

        else:
            self.segment_duration = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen

            self.media_time = file_strm.ReadInt32()
            self.offset += Int32ByteLen

        self.media_rate_integer = file_strm.ReadInt16()
        self.offset += Int16ByteLen

        self.media_rate_fraction = file_strm.ReadInt16()
        self.offset += Int16ByteLen

        return file_strm

    def Size(self):
        size = 0
        if 1 == self.version:
            size += UInt64ByteLen
            size += Int64ByteLen
        else:
            size += UInt32ByteLen
            size += Int32ByteLen
        size += Int16ByteLen
        size += Int16ByteLen
        return size

    def dump(self):
        dump_info = {}
        dump_info['box_offset'] = self.box_offset
        dump_info['offset'] = self.offset
        dump_info['version'] = self.version
        dump_info['segment_duration'] = self.segment_duration
        dump_info['media_time'] = self.media_time
        dump_info['media_rate_integer'] = self.media_rate_integer
        dump_info['media_rate_fraction'] = self.media_rate_fraction
        return dump_info

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
    version - is an integer that specifies the version of this box (0 or 1)
    entry_count - is an integer that gives the number of entries in the following table
    segment_duration - is an integer that specifies the duration of this edit segment
                       in units of the timescale in the Movie Header Box
    media_time - is an integer containing the starting time within the media of this edit
                 segment (in media time scale units, in composition time). If this field
                 is set to –1, it is an empty edit. The last edit in a track shall never
                 be an empty edit. Any difference between the duration in the Movie Header
                 Box, and the track’s duration is expressed as an implicit empty edit at
                 the end.
    media_rate - specifies the relative rate at which to play the media corresponding to
                 this edit segment. If this value is 0, then the edit is specifying
                 a ‘dwell’: the media at media‐time is presented for the segment‐duration.
                 Otherwise this field shall contain the value 1.
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.entry_count = 0
        self.segment_entry = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        for i in range(self.entry_count):
            segment_entry_ = MediaSegmentEntry(self.offset, self.version)
            file_strm = segment_entry_.decode(file_strm)
            self.offset += segment_entry_.Size()
            self.segment_entry.append(segment_entry_)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['entry_count'] = self.entry_count
        if None != self.segment_entry:
            entries = {}
            for i in range(len(self.segment_entry)):
                entries['entry_{0}'.format(i)] = self.segment_entry[i].dump()
            dump_info['entries'] = entries
        return dump_info

    def __str__(self):
        logstr = "\t\t%s\n\t\tentry_count = %08ld(0x%016lx)\n\t\tentries = [" % \
                 (FullBox.__str__(self), self.entry_count, self.entry_count)
        for i in range(len(self.segment_entry)):
            logstr += "\n\t\t\t%08ld. %s" % (i + 1, self.segment_entry[i])
        logstr += "\n\t\t]\n"
        return logstr
