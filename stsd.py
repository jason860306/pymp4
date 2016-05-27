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


import mp4boxes
from fullbox import *
from sample_entry import *


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
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Avc1:
                sample_entry = mp4boxes.MP4Boxes[tmp_box.type](
                    self.offset, tmp_box)
                # sample_entry = SampeEntry(self.offset, tmp_box)
                file_strm = sample_entry.decode(file_strm)
                self.offset += sample_entry.Size()
                self.sample_entries.append(sample_entry)
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['entry_count'] = self.entry_count
        if None != self.sample_entries:
            entries = {}
            for i in range(len(self.sample_entries)):
                entry = self.sample_entries[i]
                entries[entry.type] = self.sample_entries[i].dump()
            dump_info['sample_entries'] = entries
        return dump_info

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tentry_count = %08ld(0x%016lx)" \
                 "\n\t\t\t\tsample_entries = [" % \
                 (FullBox.__str__(self), self.entry_count, self.entry_count)
        for i in range(len(self.sample_entries)):
            logstr += "\n\t\t\t\t\t%08ld. %s" % (i, self.sample_entries[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
