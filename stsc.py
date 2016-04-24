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


import os

from fullbox import *


class SampleChunk:
    """
    unsigned int(32) first_chunk;
    unsigned int(32) samples_per_chunk;
    unsigned int(32) sample_description_index;

    first_chunk - is an integer that gives the index of the first chunk in this run of
                  chunks that share the same samples‐per‐chunk and sample‐description‐index;
                  the index of the first chunk in a track has the value 1 (the first_chunk
                  field in the first record of this box has the value 1, identifying that
                  the first sample maps to the first chunk).
    samples_per_chunk - is an integer that gives the number of samples in each of these chunks
    sample_description_index - is an integer that gives the index of the sample entry that
                               describes the samples in this chunk. The index ranges from 1
                               to the number of sample entries in the Sample Description Box
    """

    def __init__(self, offset=0):
        self.box_offset = offset
        self.offset = offset
        self.first_chunk = 0
        self.samples_per_chunk = 0
        self.sample_description_index = 0

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        self.first_chunk = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        self.samples_per_chunk = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        self.sample_description_index = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        return file_strm

    def Size(self):
        size = 0
        size += UInt32ByteLen
        size += UInt32ByteLen
        size += UInt32ByteLen
        return size

    def __str__(self):
        logstr = "first_chunk = %08ld(0x%016lx), samples_per_chunk = %08ld(0x%016lx), " \
                 "sample_description_index = %08ld(0x%016lx)" % \
                 (self.first_chunk, self.first_chunk, self.samples_per_chunk,
                  self.samples_per_chunk, self.sample_description_index,
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
    version - is an integer that specifies the version of this box
    entry_count - is an integer that gives the number of entries in the following table
    first_chunk - is an integer that gives the index of the first chunk in this run of
                  chunks that share the same samples‐per‐chunk and sample‐description‐index;
                  the index of the first chunk in a track has the value 1 (the first_chunk
                  field in the first record of this box has the value 1, identifying that
                  the first sample maps to the first chunk).
    samples_per_chunk - is an integer that gives the number of samples in each of these chunks
    sample_description_index - is an integer that gives the index of the sample entry that
                               describes the samples in this chunk. The index ranges from 1
                               to the number of sample entries in the Sample Description Box
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.entry_count = 0
        self.sample_chunks = []  # for i in range(self.entry_count)

    def decode(self, file_strm):
        if file_strm == None:
            print "file_strm == None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        for i in range(self.entry_count):
            sample_chunk_ = SampleChunk(self.offset)
            file_strm = sample_chunk_.decode(file_strm)
            self.offset += sample_chunk_.Size()

            self.sample_chunks.append(sample_chunk_)

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def find_chunk_index(self, sample_index):
        index = 0
        for i in range(self.entry_count):
            sample_chunk = self.sample_chunks[i]
            chunk_sample_max_index = \
                sample_chunk.first_chunk * sample_chunk.samples_per_chunk
            if sample_index > chunk_sample_max_index:
                index = chunk_sample_max_index
                continue
            chunk_sample_idx = (index for index in range(index, sample_index))
            return {sample_chunk.first_chunk: chunk_sample_idx}

    def chunk_last_sample_index(self, chunk_index):
        if chunk_index >= self.entry_count:
            pass  # raise
        sample_chunk = self.sample_chunks[chunk_index]
        return sample_chunk.first_chunk * sample_chunk.samples_per_chunk

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tentry_count = %08ld(0x%016lx)" \
                 "\n\t\t\t\tsample_chunks = [" % \
                 (FullBox.__str__(self), self.entry_count, self.entry_count)
        for i in range(self.entry_count):
            logstr += "\n\t\t\t\t\t%08ld. %s" % (i, self.sample_chunks[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
