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


from fullbox import *


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

        Fields shown as “template” in the box descriptions are optional in the
    specifications that use this specification. If the field is used in another
    specification, that use must be conformant with its definition here, and
    the specification must define whether the use is optional or mandatory.
    """

    def __init__(self, box=None):
        if type(box) is Box:
            Box.__init__(self, box)
        elif type(box) is FullBox:
            FullBox.__init__(self, box)

        self.creation_time = 0
        self.modification_time = 0
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

    def decode(self, file=None):
        file_strm = FullBox.decode(self, file)

        if self.version == 1:
            self.creation_time = file_strm.ReadUint64()
            self.modification_time = file_strm.ReadUint64()
            self.timescale = file_strm.ReadUInt32()
            self.duration = file_strm.ReadUint64()
        else:
            self.creation_time = file_strm.ReadUInt32()
            self.modification_time = file_strm.ReadUInt32()
            self.timescale = file_strm.ReadUInt32()
            self.duration = file_strm.ReadUInt32()

        self.rate = file_strm.ReadUInt32()
        self.rate_fmt = str(self.rate >> 16) + '.' + str(self.rate << 16)
        self.volume = file_strm.ReadUInt16()
        self.volume_fmt = str(self.volume >> 8) + '.' + str(self.volume << 8)
        self.reserved = file_strm.ReadUInt16()
        for idx in range(len(self.reserved1)):
            reserved1_ = file_strm.ReadUInt32()
            self.reserved1[idx] = reserved1_
        for idx in range(len(self.matrix)):
            matrix_ = file_strm.ReadUInt32()
            self.matrix[idx] = matrix_
        for idx in range(len(self.pre_defined)):
            pre_defined_ = file_strm.ReadUInt32()
            self.pre_defined[idx] = pre_defined_
        self.next_track_ID = file_strm.ReadUInt32()

        return file_strm

    def __str__(self):
        logstr = "%s, creation_time = %d, modification_time = %d, " % \
                 (FullBox.__str__(self), self.creation_time, self.modification_time)
        logstr += "timescale = %d, duration = %d, rate = %s, " % \
                  (self.timescale, self.duration, self.rate_fmt)
        logstr += "volume = %s, reserved = %d, reserved1 = [" % \
                  (self.volume, self.reserved)
        for r in self.reserved1:
            logstr += "%d, " % r
        logstr += "], matrix: [["
        for i in range(len(self.matrix)):
            logstr += "%d " % self.matrix[i]
            if 0 == i % 3:
                logstr += "], ["
        logstr += "]], pre_defined: [["
        for j in range(len(self.pre_defined)):
            logstr += "%d " % self.pre_defined[j]
            if 0 == j % 3:
                logstr += "], ["
        logstr += "]], next_track_ID = %d" % self.next_track_ID
        return logstr
