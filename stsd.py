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

    def __init__(self):
        Box.__init__(self)
        self.reserved = [0 for i in range(6)]
        self.data_reference_index = 0

    def decode(self, file=None):
        Box.decode(self, file)

        file_strm = Util(file)

        for i in range(len(self.reserved)):
            self.reserved[i] = file_strm.read_uint8_lit()
        self.data_reference_index = file_strm.read_uint16_lit()

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

    def __init__(self):
        FullBox.__init__(self)
        self.entry_count = 0
        self.sample_entries = []

    def decode(self, file=None):
        FullBox.decode(self, file)

        file_strm = Util(file)

        self.entry_count = file_strm.read_uint32_lit()
        for i in range(self.entry_count):
            sample_entry = SampeEntry()
            sample_entry.decode(file)
            self.sample_entries.append(sample_entry)

    def __str__(self):
        logstr = "%s, entry_count = %d, sample_entries = [" % \
                 (FullBox.__str__(self), self.entry_count)
        for i in range(self.entry_count):
            logstr += "%d. %s" % (i, self.sample_entries[i])
        logstr += "]"
        return logstr
