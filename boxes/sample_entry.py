#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '5/10/0010 18:57:14'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *


class SampeEntry(object, Box):
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

    def __init__(self, offset=0, box=None):
        Box.__init__(self, offset, box)
        self.reserved = [0 for i in range(6)]
        self.data_reference_index = 0

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        for i in range(len(self.reserved)):
            self.reserved[i] = file_strm.read_uint8()
            self.offset += UInt8ByteLen

        self.data_reference_index = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        # tmp_size = self.offset - self.box_offset
        # if tmp_size != self.Size():
        #     file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def GetLength(self):
        size_ = self.offset - self.box_offset
        return size_

    def dump(self):
        dump_info = Box.dump(self)
        dump_info['reserved'] = self.reserved
        dump_info['data_reference_index'] = self.data_reference_index
        return dump_info

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t\treserved = [" % Box.__str__(self)
        for i in range(len(self.reserved)):
            logstr += "\n\t\t\t\t\t\t\t%08ld. %08ld(0x%016lx)" % \
                      (i, self.reserved[i], self.reserved[i])
        logstr += "\n\t\t\t\t\t\t]\n\t\t\t\t\t\tdata_reference_index = %08ld(0x%016lx)" % \
                  (self.data_reference_index, self.data_reference_index)
        return logstr
