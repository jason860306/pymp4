#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/9/16 5:44 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class SampleChunk:
    """
    unsigned int(32) first_chunk;
    unsigned int(32) samples_per_chunk;
    unsigned int(32) sample_description_index;
    """

    def __init__(self):
        self.first_chunk = 0
        self.samples_per_chunk = 0
        self.sample_description_index = 0

    def decode(self, file=None):
        file_strm = Util(file)

        self.first_chunk = file_strm.read_uint32_lit()
        self.samples_per_chunk = file_strm.read_uint32_lit()
        self.sample_description_index = file_strm.read_uint32_lit()

    def __str__(self):
        logstr = "first_chunk = %d, samples_per_chunk = %d, " \
                 "sample_description_index = %d" % \
                 (self.first_chunk, self.samples_per_chunk,
                  self.sample_description_index)
        return logstr


class Stsc(FullBox):
    """
    aligned(8) class SampleToChunkBox extends FullBox(‘stsc’, version = 0, 0) {
        unsigned int(32) entry_count;
        for (i=1; i <= entry_count; i++) {
            unsigned int(32) first_chunk;
            unsigned int(32) samples_per_chunk;
            unsigned int(32) sample_description_index;
        }
    }
    """

    def __init__(self):
        FullBox.__init__(self)

        self.entry_count = 0
        self.sample_chunks = []  # for i in range(self.entry_count)

    def decode(self, file=None):
        FullBox.decode(self, file)

        file_strm = Util(file)

        self.entry_count = file_strm.read_uint32_lit()
        for i in range(self.entry_count):
            sample_chunk_ = SampleChunk()
            sample_chunk_.decode(file)
            self.sample_chunks.append(sample_chunk_)

    def __str__(self):
        logstr = "%s, entry_count = %d, sample_chunks = [" % \
                 (FullBox.__str__(self), self.entry_count)
        for i in range(self.entry_count):
            logstr += "[%d. %s], " % (i, self.sample_chunks[i])
        logstr += "]"
        return logstr
