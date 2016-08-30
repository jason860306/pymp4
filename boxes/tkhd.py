#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 15:35'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import os

from fullbox import *
from util.util import Util


class Tkhd(object, FullBox):
    """
    aligned(8) class TrackHeaderBox extends FullBox(‘tkhd’, version, flags){
        if (version==1) {
            unsigned int(64) creation_time;
            unsigned int(64) modification_time;
            unsigned int(32) track_ID;
            const unsigned int(32) reserved = 0;
            unsigned int(64) duration;
        } else { // version==0
            unsigned int(32) creation_time;
            unsigned int(32) modification_time;
            unsigned int(32) track_ID;
            const unsigned int(32) reserved = 0;
            unsigned int(32) duration;
        }
        const unsigned int(32)[2] reserved = 0;
        template int(16) layer = 0;
        template int(16) alternate_group = 0;
        template int(16) volume = {if track_is_audio 0x0100 else 0};
        const unsigned int(16) reserved = 0;
        template int(32)[9] matrix=
            { 0x00010000,0,0,0,0x00010000,0,0,0,0x40000000 };
        // unity matrix
        unsigned int(32) width;
        unsigned int(32) height;
    }
    version - is an integer that specifies the version of this box (0 or 1 in this specification)
    flags - is a 24‐bit integer with flags; the following values are defined:
          - Track_enabled: Indicates that the track is enabled. Flag value is 0x000001.
            A disabled track (the low bit is zero) is treated as if it were not present.
          - Track_in_movie: Indicates that the track is used in the presentation. Flag value is 0x000002.
          - Track_in_preview: Indicates that the track is used when previewing the presentation.
            Flag value is 0x000004.
          - Track_size_is_aspect_ratio: Indicates that the width and height fields are not
            expressed in pixel units. The values have the same units but these units are not
            specified. The values are only an indication of the desired aspect ratio. If the
            aspect ratios of this track and other related tracks are not identical, then the
            respective positioning of the tracks is undefined, possibly defined by external
            contexts. Flag value is 0x000008.
    creation_time - is an integer that declares the creation time of this track (in seconds
                    since midnight, Jan. 1, 1904, in UTC time).
    modification_time - is an integer that declares the most recent time the track was modified
                        (in seconds since midnight, Jan. 1, 1904, in UTC time).
    track_ID - is an integer that uniquely identifies this track over the entire life‐time of
               this presentation. Track IDs are never re‐used and cannot be zero.
    duration - is an integer that indicates the duration of this track (in the timescale indicated
               in the Movie Header Box). The value of this field is equal to the sum of the
               durations of all of the track’s edits. If there is no edit list, then the duration
               is the sum of the sample durations, converted into the timescale in the Movie
               Header Box. If the duration of this track cannot be determined then duration is
               set to all 1s.
    layer - specifies the front‐to‐back ordering of video tracks; tracks with lower numbers
            are closer to the viewer. 0 is the normal value, and ‐1 would be in front of
            track 0, and so on.
    alternate_group - is an integer that specifies a group or collection of tracks. If this
                      field is 0 there is no information on possible relations to other tracks.
                      If this field is not 0, it should be the same for tracks that contain
                      alternate data for one another and different for tracks belonging to
                      different such groups. Only one track within an alternate group should be
                      played or streamed at any one time, and must be distinguishable from
                      other tracks in the group via attributes such as bitrate, codec,
                      language, packet size etc. A group may have only one member.
    volume - is a fixed 8.8 value specifying the track's relative audio volume. Full volume
             is 1.0 (0x0100) and is the normal value. Its value is irrelevant for a purely
             visual track. Tracks may be composed by combining them according to their volume,
             and then using the overall Movie Header Box volume setting; or more complex audio
             composition (e.g. MPEG‐4 BIFS) may be used.
    matrix - provides a transformation matrix for the video; (u,v,w) are restricted here to
             (0,0,1), hex (0,0,0x40000000).
    width and height - fixed‐point 16.16 values are track‐dependent as follows:
                       For text and subtitle tracks, they may, depending on the coding format,
                       describe the suggested size of the rendering area. For such tracks, the
                       value 0x0 may also be used to indicate that the data may be rendered at
                       any size, that no preferred size has been indicated and that the actual
                       size may be determined by the external context or by reusing the width
                       and height of another track. For those tracks, the flag
                       track_size_is_aspect_ratio may also be used. For non‐visual tracks
                       (e.g. audio), they should be set to zero. For all other tracks,
                       they specify the track's visual presentation size. These need not be
                       the same as the pixel dimensions of the images, which is documented in
                       the sample description(s); all images in the sequence are scaled to this
                       size, before any overall transformation of the track represented by the
                       matrix. The pixel dimensions of the images are the default values.
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.creation_time = 0
        self.creation_time_fmt = 0
        self.modification_time = 0
        self.modification_time_fmt = 0
        self.track_ID = 0
        self.reserved = 0
        self.duration = 0

        self.reserved1 = [0 for i in range(2)]
        self.layer = 0
        self.alternate_group = 0
        self.volume = 0
        self.volume_fmt = '1.0'
        self.reserved2 = 0
        self.matrix = [0 for i in range(9)]
        self.width = 0
        self.height = 0

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        if self.version == 1:
            self.creation_time = file_strm.read_uint64()
            self.creation_time -= UTC_MP4_INTERVAL
            self.offset += UInt64ByteLen
            if self.creation_time > 0:
                self.creation_time_fmt = Util.datetime_format(
                    self.creation_time)

            self.modification_time = file_strm.read_uint64()
            self.modification_time -= UTC_MP4_INTERVAL
            self.offset += UInt64ByteLen
            if self.modification_time > 0:
                self.modification_time_fmt = Util.datetime_format(
                    self.modification_time)

            self.track_ID = file_strm.read_uint32()
            self.offset += UInt32ByteLen

            self.reserved = file_strm.read_uint32()
            self.offset += UInt32ByteLen

            self.duration = file_strm.ReadUInt64()
            self.offset += UInt64ByteLen

        else:
            self.creation_time = file_strm.read_uint32()
            self.creation_time -= UTC_MP4_INTERVAL
            self.offset += UInt32ByteLen
            if self.creation_time > 0:
                self.creation_time_fmt = Util.datetime_format(
                    self.creation_time)

            self.modification_time = file_strm.read_uint32()
            self.modification_time -= UTC_MP4_INTERVAL
            self.offset += UInt32ByteLen
            if self.modification_time > 0:
                self.modification_time_fmt = Util.datetime_format(
                    self.modification_time)

            self.track_ID = file_strm.read_uint32()
            self.offset += UInt32ByteLen

            self.reserved = file_strm.read_uint32()
            self.offset += UInt32ByteLen

            self.duration = file_strm.read_uint32()
            self.offset += UInt32ByteLen

        for i in range(len(self.reserved1)):
            reserved1_ = file_strm.read_uint32()
            self.offset += UInt32ByteLen
            self.reserved1[i] = reserved1_

        self.layer = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.alternate_group = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.volume = file_strm.read_uint16()
        self.offset += UInt16ByteLen
        self.volume_fmt = "%d.%d" % (self.volume >> 8, self.volume & 0x00FF)

        self.reserved2 = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        for i in range(len(self.matrix)):
            matrix_ = file_strm.read_uint32()
            self.offset += UInt32ByteLen
            self.matrix[i] = matrix_

        self.width = file_strm.read_uint32()
        self.width = self.width >> 16
        self.offset += UInt32ByteLen

        self.height = file_strm.read_uint32()
        self.height = self.height >> 16
        self.offset += UInt32ByteLen

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['creation_time'] = self.creation_time_fmt
        dump_info['modification_time'] = self.modification_time_fmt
        dump_info['track_ID'] = self.track_ID
        dump_info['reserved'] = self.reserved
        dump_info['duration'] = self.duration
        dump_info['reserved1'] = self.reserved1
        dump_info['layer'] = self.layer
        dump_info['alternate_group'] = self.alternate_group
        dump_info['volume'] = self.volume_fmt
        dump_info['reserved2'] = self.reserved2
        dump_info['matrix'] = self.matrix
        dump_info['width'] = self.width
        dump_info['height'] = self.height
        return dump_info

    def __str__(self):
        logstr = "\t%s\n\tcreation_time = %s(%08ld)\n\tmodification_time = %s(%08ld)" % \
                 (Box.__str__(self), self.creation_time_fmt, self.creation_time,
                  self.modification_time_fmt, self.modification_time)
        logstr += "\n\ttrack_ID = %08ld(0x%016lx)\n\treserved = %08ld(0x%016lx)" \
                  "\n\tduration = %08ld(0x%016lx)\n\treserved1 = [ " % \
                  (self.track_ID, self.track_ID, self.reserved, self.reserved,
                   self.duration, self.duration)
        for i in range(len(self.reserved1)):
            logstr += "%08ld(0x%016lx), " % (self.reserved1[i], self.reserved1[i])
        logstr += "]\n\tlayer = %08ld(0x%016lx)\n\talternate_group = %08ld(0x%016lx)" \
                  "\n\tvolume = %s" % (self.layer, self.layer, self.alternate_group,
                                     self.alternate_group, self.volume_fmt)
        logstr += "\n\treserved2 = %08ld(0x%016lx)\n\tmatrix = [" % (self.reserved2, self.reserved2)
        for i in range(len(self.matrix)):
            if (0 == i) or (0 == i % 3):
                logstr += "\n\t\t"
            logstr += "%016ld(0x%016lx) " % (self.matrix[i], self.matrix[i])
        logstr += "\n\t]\n\twidth = %08ld(0x%016lx)\n\theight = %08ld(0x%016lx)\n" % \
                  (self.width, self.width, self.height, self.height)
        return logstr
