#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 15:35'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Tkhd(FullBox):
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
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)
        elif type(box) is FullBox:
            FullBox.__init__(self, box)

        self.creation_time = 0
        self.modification_time = 0
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

    def decode(self, file=None):
        file_strm = FullBox.decode(self, file)

        if self.version == 1:
            self.creation_time = file_strm.ReadUint64()
            self.modification_time = file_strm.ReadUint64()
            self.track_ID = file_strm.ReadUInt32()
            self.reserved = file_strm.ReadUInt32()
            self.duration = file_strm.ReadUint64()
        else:
            self.creation_time = file_strm.ReadUInt32()
            self.modification_time = file_strm.ReadUInt32()
            self.track_ID = file_strm.ReadUInt32()
            self.reserved = file_strm.ReadUInt32()

        for i in range(len(self.reserved1)):
            reserved1_ = file_strm.ReadUInt32()
            self.reserved1[i] = reserved1_

        self.layer = file_strm.ReadUInt16()
        self.alternate_group = file_strm.ReadUInt16()
        self.volume = file_strm.ReadUInt16()
        self.volume_fmt = str(self.volume >> 8) + '.' + str(self.volume << 8)
        self.reserved2 = file_strm.ReadUInt16()

        for i in range(len(self.matrix)):
            matrix_ = file_strm.ReadUInt32()
            self.matrix[i] = matrix_

        self.width = file_strm.ReadUInt32()
        self.height = file_strm.ReadUInt32()

        return file_strm

    def __str__(self):
        logstr = "%s, creation_time = %d, modification_time = %d, " % \
                 (Box.__str__(self), self.creation_time, self.modification_time)
        logstr += "track_ID = %d, reserved = %d, duration = %d, reserved1 = [" % \
                  (self.track_ID, self.reserved, self.duration)
        for i in range(len(self.reserved1)):
            logstr += "%d, " % self.reserved1[i]
        logstr += "], layer = %d, alternate_group = %d, volume = %s, " % \
                  (self.layer, self.alternate_group, self.volume_fmt)
        logstr += "reserved2 = %d, matrix = [["
        for i in range(len(self.matrix)):
            logstr += "%d " % self.matrix[i]
            if 0 == i % 3:
                logstr += "], ["
        logstr += "]], width = %d, height = %d" % (self.width, self.height)
        return logstr
