#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 12:34'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import os

from fullbox import *
from util import Util


class Mvhd(FullBox):
    """
    aligned(8) class MovieHeaderBox extends FullBox(‘mvhd’, version, 0) {
        if (version==1) {
            unsigned int(64) creation_time;
            unsigned int(64) modification_time;
            unsigned int(32) timescale;
            unsigned int(64) duration;
        } else { // version==0
            unsigned int(32) creation_time;
            unsigned int(32) modification_time;
            unsigned int(32) timescale;
            unsigned int(32) duration;
        }
        template int(32) rate = 0x00010000; // typically 1.0
        template int(16) volume = 0x0100; // typically, full volume
        const bit(16) reserved = 0;
        const unsigned int(32)[2] reserved = 0;
        template int(32)[9] matrix =
            { 0x00010000,0,0,0,0x00010000,0,0,0,0x40000000 };
        // Unity matrix
        bit(32)[6] pre_defined = 0;
        unsigned int(32) next_track_ID;
    }
    version - is an integer that specifies the version of this box (0 or 1 in this specification)
    creation_time - is an integer that declares the creation time of the presentation (in seconds
                    since midnight, Jan. 1, 1904, in UTC time)
    modification_time - is an integer that declares the most recent time the presentation was
                        modified (in seconds since midnight, Jan. 1, 1904, in UTC time)
    timescale - is an integer that specifies the time‐scale for the entire presentation;
                this is the number of time units that pass in one second.
                For example, a time coordinate system that measures time in sixtieths of
                a second has a time scale of 60.
    duration - is an integer that declares length of the presentation (in the indicated
               timescale). This property is derived from the presentation’s tracks:
               the value of this field corresponds to the duration of the longest track
               in the presentation. If the duration cannot be determined then duration
               is set to all 1s.
    rate - is a fixed point 16.16 number that indicates the preferred rate to play the
           presentation; 1.0 (0x00010000) is normal forward playback
    volume - is a fixed point 8.8 number that indicates the preferred playback volume.
             1.0 (0x0100) is full volume.
    matrix - provides a transformation matrix for the video; (u,v,w) are restricted here
             to (0,0,1), hex values (0,0,0x40000000).
    next_track_ID - is a non‐zero integer that indicates a value to use for the track ID of
                    the next track to be added to this presentation. Zero is not a valid
                    track ID value. The value of next_track_ID shall be larger than the
                    largest track‐ID in use. If this value is equal to all 1s (32‐bit
                    maxint), and a new media track is to be added, then a search must be
                    made in the file for an unused track identifier.

        Fields shown as “template” in the box descriptions are optional in the
    specifications that use this specification. If the field is used in another
    specification, that use must be conformant with its definition here, and
    the specification must define whether the use is optional or mandatory.
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.creation_time = 0
        self.creation_time_fmt = ''
        self.modification_time = 0
        self.modification_time_fmt = ''
        self.timescale = 0
        self.duration = 0

        self.rate = 0
        self.rate_fmt = '1.0'
        self.volume = 0
        self.volume_fmt = '1.0'
        self.reserved = 0
        self.reserved1 = [0 for i in range(2)]
        self.matrix = [0 for i in range(9)]
        self.pre_defined = [0 for i in range(6)]
        self.next_track_ID = 0

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        if self.version == 1:
            self.creation_time = file_strm.ReadUint64()
            self.creation_time -= UTC_MP4_INTERVAL
            self.offset += UInt64ByteLen
            if self.creation_time > 0:
                self.creation_time_fmt = Util.datetime_format(
                    self.creation_time)

            self.modification_time = file_strm.ReadUint64()
            self.modification_time -= UTC_MP4_INTERVAL
            self.offset += UInt64ByteLen
            if self.modification_time > 0:
                self.modification_time_fmt = Util.datetime_format(
                    self.modification_time)

            self.timescale = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen

            self.duration = file_strm.ReadUint64()
            self.offset += UInt64ByteLen

        else:
            self.creation_time = file_strm.ReadUInt32()
            self.creation_time -= UTC_MP4_INTERVAL
            self.offset += UInt32ByteLen
            if self.creation_time > 0:
                self.creation_time_fmt = Util.datetime_format(
                    self.creation_time)

            self.modification_time = file_strm.ReadUInt32()
            self.modification_time -= UTC_MP4_INTERVAL
            self.offset += UInt32ByteLen
            if self.creation_time > 0:
                self.modification_time = Util.datetime_format(
                    self.modification_time)

            self.timescale = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen

            self.duration = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen

        self.rate = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen
        self.rate_fmt = "%d.%d" % (self.rate >> 16, self.rate & 0x0000FFFF)

        self.volume = file_strm.ReadUInt16()
        self.offset += UInt16ByteLen
        self.volume_fmt = "%d.%d" % (self.volume >> 8, self.volume & 0x00FF)

        self.reserved = file_strm.ReadUInt16()
        self.offset += UInt16ByteLen

        for idx in range(len(self.reserved1)):
            reserved1_ = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen
            self.reserved1[idx] = reserved1_

        for idx in range(len(self.matrix)):
            matrix_ = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen
            self.matrix[idx] = matrix_

        for idx in range(len(self.pre_defined)):
            pre_defined_ = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen
            self.pre_defined[idx] = pre_defined_

        self.next_track_ID = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def movie_duration(self):
        return 0.0 if (self.timescale == 0) else 1.0 * self.duration / self.timescale

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['creation_time'] = self.creation_time_fmt
        dump_info['modification_time'] = self.modification_time_fmt
        dump_info['timescale'] = self.timescale
        dump_info['duration'] = self.duration
        dump_info['rate'] = self.rate_fmt
        dump_info['volume'] = self.volume_fmt
        dump_info['reserved'] = self.reserved
        dump_info['reserved1'] = self.reserved1
        dump_info['matrix'] = self.matrix
        dump_info['pre_defined'] = self.pre_defined
        dump_info['next_track_ID'] = self.next_track_ID
        return dump_info

    def __str__(self):
        logstr = "\t%s\n\tcreation_time = %s(%08ld)\n\tmodification_time = %s(%08ld)" % \
                 (FullBox.__str__(self), self.creation_time_fmt, self.creation_time,
                  self.modification_time_fmt, self.modification_time)
        logstr += "\n\ttimescale = %08ld(0x%016lx)\n\tduration = %s(0x%08ld)\n\trate = %s" % \
                  (self.timescale, self.timescale, Util.time_format(self.movie_duration()),
                   self.movie_duration(), self.rate_fmt)
        logstr += "\n\tvolume = %s\n\treserved = %08ld(0x%016lx)\n\treserved1 = [ " % \
                  (self.volume, self.reserved, self.reserved)
        for r in self.reserved1:
            logstr += "%08ld(0x%016lx), " % (r, r)
        logstr += "]\n\tmatrix = ["
        for i in range(len(self.matrix)):
            if (0 == i) or (0 == i % 3):
                logstr += "\n\t\t"
            logstr += "%016ld(0x%016lx) " % (self.matrix[i], self.matrix[i])
        logstr += "\n\t]\n\tpre_defined = ["
        for j in range(len(self.pre_defined)):
            if (0 == j) or (0 == j % 3):
                logstr += "\n\t\t"
            logstr += "%08ld(0x%016lx) " % (self.pre_defined[j], self.pre_defined[j])
        logstr += "\n\t]\n\tnext_track_ID = %08ld(0x%016lx)\n" % (
            self.next_track_ID, self.next_track_ID)
        return logstr
