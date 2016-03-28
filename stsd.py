#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/8 23:09'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class SampeEntry(Box):
    """
    aligned(8) abstract class SampleEntry (unsigned int(32) format) extends Box(format){
        const unsigned int(8)[6] reserved = 0;
        unsigned int(16) data_reference_index;
    }
    """

    def __init__(self, offset=0):
        Box.__init__(self, offset)
        self.reserved = [0 for i in range(6)]
        self.data_reference_index = 0

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        for i in range(len(self.reserved)):
            self.reserved[i] = file_strm.ReadUInt8()
            self.offset += UInt8ByteLen

        self.data_reference_index = file_strm.ReadUInt16()
        self.offset += UInt16ByteLen

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def __str__(self):
        logstr = "%s, reserved = [" % Box.__str__(self)
        for i in range(len(self.reserved)):
            logstr += "%d. %d], [" % (i, self.reserved[i])
        logstr += "], data_reference_index = %d" % self.data_reference_index
        return logstr


class Stsd(FullBox):
    """
    aligned(8) class SampleDescriptionBox (unsigned int(32) handler_type) extends FullBox('stsd', version, 0){
        int i;
        unsigned int(32) entry_count;
        for (i = 1 ; i <= entry_count ; i++){
             SampleEntry(); // an instance of a class derived from SampleEntry
        }
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.entry_count = 0
        self.sample_entries = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.ReadUInt32()
        for i in range(self.entry_count):
            sample_entry = SampeEntry()
            file_strm = sample_entry.decode(file_strm)
            self.offset += sample_entry.Size()
            self.sample_entries.append(sample_entry)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def __str__(self):
        logstr = "%s, entry_count = %d, sample_entries = [" % \
                 (FullBox.__str__(self), self.entry_count)
        for i in range(self.entry_count):
            logstr += "%d. %s" % (i, self.sample_entries[i])
        logstr += "]"
        return logstr
