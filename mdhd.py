#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 16:30'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import time

from fullbox import *


class Mdhd(FullBox):
    """
    aligned(8) class MediaHeaderBox extends FullBox(‘mdhd’, version, 0) {
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
        bit(1) pad = 0;
        unsigned int(5)[3] language; // ISO-639-2/T language code
        unsigned int(16) pre_defined = 0;
    }
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
        self.timescale = 0
        self.duration = 0

        self.pad = 0
        self.language_code = 0
        self.language = ['0' for i in range(3)]
        self.pre_defined = 0

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        if self.version == 1:
            self.creation_time = file_strm.ReadUInt64()
            self.offset += UInt64ByteLen
            self.creation_time_fmt = time.ctime(self.creation_time)

            self.modification_time = file_strm.ReadUInt64()
            self.offset += UInt64ByteLen
            self.modification_time_fmt = time.ctime(self.modification_time)

            self.timescale = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen

            self.duration = file_strm.ReadUInt64()
            self.offset += UInt64ByteLen

        else:
            self.creation_time = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen
            self.creation_time_fmt = time.ctime(self.creation_time)

            self.modification_time = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen
            self.modification_time_fmt = time.ctime(self.modification_time)

            self.timescale = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen

            self.duration = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen

        """
        ISO Language Codes

            Because the language codes specified by ISO 639-2/T are three
        characters long, they must be packed to fit into a 16-bit field.
        The packing algorithm must map each of the three characters, which
        are always lowercase, into a 5-bit integer and then concatenate
        these integers into the least significant 15 bits of a 16-bit
        integer, leaving the 16-bit integer’s most significant bit set
        to zero.

        One algorithm for performing this packing is to treat each ISO
        character as a 16-bit integer. Subtract 0x60 from the first
        character and multiply by 2^10 (0x400), subtract 0x60 from the
        second character and multiply by 2^5 (0x20), subtract 0x60 from
        the third character, and add the three 16-bit values. This will
        result in a single 16-bit value with the three codes correctly
        packed into the 15 least significant bits and the most significant
        bit set to zero.

        Example: The ISO language code 'jpn' consists of the three hexadecimal
        values 0x6A, 0x70, 0x6E. Subtracting 0x60 from each value yields the
        values 0xA, 0x10, 0xE, as shown in Table 5-2.

        Table 5-2  5-bit values of UTF-8 characters

        Character   UTF-8 code      5-bit value     Shifted value
            j           0x6A        0xA (01010)     0x2800 (01010..........)
            p           0x70        0x10 (10000)    0x200 (.....10000.....)
            n           0x6E        0xE (01110)     0xE (..........01110)

        The first value is shifted 10 bits to the left (multiplied by 0x400)
        and the second value is shifted 5 bits to the left (multiplied by 0x20).
        This yields the values 0x2800, 0x200, 0xE. When added, this results in
        the 16-bit packed language code value of 0x2A0E
        """
        self.language_code = file_strm.ReadUInt16()
        self.offset += UInt16ByteLen

        self.pad = self.language_code >> 15 & 0x01
        for i in range(len(self.language)):
            lang_ = ((self.language_code >> ((2 - i) * 5)) & 0x1F) + 0x60
            self.language[i] = chr(lang_)

        self.pre_defined = file_strm.ReadUInt16()
        self.offset += UInt16ByteLen

        return file_strm

    def __str__(self):
        logstr = "%s, creation_time = %d, modification_time = %d, " % \
                 (FullBox.__str__(self), self.creation_time, self.modification_time)
        logstr += "timescale = %d, duration = %d, language = [" % \
                  (self.timescale, self.duration)
        for language_ in self.language:
            logstr += "%s, " % language_
        logstr += "], pre_defined = %d" % self.pre_defined
        return logstr
