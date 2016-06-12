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


import os

from fullbox import *
from util import Util


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
    version - is an integer that specifies the version of this box (0 or 1)
    creation_time - is an integer that declares the creation time of the media in this
                    track (in seconds since midnight, Jan. 1, 1904, in UTC time).
    modification_time - is an integer that declares the most recent time the media in
                        this track was modified (in seconds since midnight,
                        Jan. 1, 1904, in UTC time).
    timescale - is an integer that specifies the time‐scale for this media; this is
                the number of time units that pass in one second. For example,
                a time coordinate system that measures time in sixtieths of a second
                has a time scale of 60.
    duration - is an integer that declares the duration of this media (in the scale
               of the timescale). If the duration cannot be determined then duration
               is set to all 1s.
    language - declares the language code for this media. See ISO 639‐2/T for the set
               of three character codes. Each character is packed as the difference
               between its ASCII value and 0x60. Since the code is confined to being
               three lower‐case letters, these values are strictly positive.
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
            self.creation_time -= UTC_MP4_INTERVAL
            self.offset += UInt64ByteLen
            if self.creation_time > 0:
                self.creation_time_fmt = Util.datetime_format(
                    self.creation_time)

            self.modification_time = file_strm.ReadUInt64()
            self.modification_time -= UTC_MP4_INTERVAL
            self.offset += UInt64ByteLen
            if self.modification_time > 0:
                self.modification_time_fmt = Util.datetime_format(
                    self.modification_time)

            self.timescale = file_strm.ReadUInt32()
            self.offset += UInt32ByteLen

            self.duration = file_strm.ReadUInt64()
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
            if self.modification_time > 0:
                self.modification_time_fmt = Util.datetime_format(
                    self.modification_time)

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

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def duration(self):
        return 1.0 * self.duration / self.timescale

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['creation_time'] = self.creation_time_fmt
        dump_info['modification_time'] = self.modification_time_fmt
        dump_info['timescale'] = self.timescale
        dump_info['duration'] = self.duration
        dump_info['pad'] = self.pad
        dump_info['language_code'] = self.language_code
        dump_info['language'] = self.language
        dump_info['pre_defined'] = self.pre_defined
        return dump_info

    def __str__(self):
        logstr = "\t\t%s\n\t\tcreation_time = %s(%08ld)\n\t\tmodification_time = %s(%08ld)" % \
                 (FullBox.__str__(self), self.creation_time_fmt, self.creation_time,
                  self.modification_time_fmt, self.modification_time)
        logstr += "\n\t\ttimescale = %08ld\n\t\tduration = %08ld\n\t\tlanguage = [" % \
                  (self.timescale, self.duration)
        for language_ in self.language:
            logstr += "%s" % language_
        logstr += "]\n\t\tpre_defined = %08ld(0x%016lx)\n" % (self.pre_defined, self.pre_defined)
        return logstr
