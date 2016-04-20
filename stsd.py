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


import os

from fullbox import *


class SampeEntry(Box):
    """
    aligned(8) abstract class SampleEntry (unsigned int(32) format) extends Box(format){
        const unsigned int(8)[6] reserved = 0;
        unsigned int(16) data_reference_index;
    }
    data_reference_index - is an integer that contains the index of the data reference
                           to use to retrieve data associated with samples that use
                           this sample description. Data references are stored in Data
                           Reference Boxes. The index ranges from 1 to the number of data
                           references.
    """

    def __init__(self, offset=0):
        Box.__init__(self, offset)
        self.reserved = [0 for i in range(6)]
        self.data_reference_index = 0

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
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
        logstr = "%s\n\t\t\t\t\t\treserved = [" % Box.__str__(self)
        for i in range(len(self.reserved)):
            logstr += "\n\t\t\t\t\t\t\t%08ld. %08ld(0x%016lx)" % \
                      (i, self.reserved[i], self.reserved[i])
        logstr += "\n\t\t\t\t\t\t]\n\t\t\t\t\t\tdata_reference_index = %08ld(0x%016lx)" % \
                  (self.data_reference_index, self.data_reference_index)
        return logstr


class Stsd(FullBox):
    """
    aligned(8) class SampleDescriptionBox (unsigned int(32) handler_type)
        extends FullBox('stsd', version, 0){
        int i;
        unsigned int(32) entry_count;
        for (i = 1 ; i <= entry_count ; i++){
             SampleEntry(); // an instance of a class derived from SampleEntry
        }
    }
    version - is set to zero unless the box contains an AudioSampleEntryV1,
              whereupon version must be 1
    entry_count - is an integer that gives the number of entries in the following table
    SampleEntry - is the appropriate sample entry.
    data_reference_index - is an integer that contains the index of the data reference
                           to use to retrieve data associated with samples that use
                           this sample description. Data references are stored in Data
                           Reference Boxes. The index ranges from 1 to the number of data
                           references.
    bufferSizeDB - gives the size of the decoding buffer for the elementary stream in bytes.
    maxBitrate - gives the maximum rate in bits/second over any window of one second.
    avgBitrate - gives the average rate in bits/second over the entire presentation.
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.entry_count = 0
        self.sample_entries = []

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        for i in range(self.entry_count):
            sample_entry = SampeEntry(self.offset)
            file_strm = sample_entry.decode(file_strm)
            self.offset += sample_entry.Size()
            self.sample_entries.append(sample_entry)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tentry_count = %08ld(0x%016lx)" \
                 "\n\t\t\t\tsample_entries = [" % \
                 (FullBox.__str__(self), self.entry_count, self.entry_count)
        for i in range(self.entry_count):
            logstr += "\n\t\t\t\t\t%08ld. %s" % (i, self.sample_entries[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
