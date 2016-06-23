#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '5/10/0010 19:09:09'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from sample_entry import *


class AudioSampleEntry(SampeEntry):
    """
    class AudioSampleEntry(codingname) extends SampleEntry (codingname){
        const unsigned int(32)[2] reserved = 0;
        template unsigned int(16) channelcount = 2;
        template unsigned int(16) samplesize = 16;
        unsigned int(16) pre_defined = 0;
        const unsigned int(16) reserved = 0 ;
        template unsigned int(32) samplerate = { default samplerate of media}<<16;
        ChannelLayout();
        // we permit any number of DownMix or DRC boxes:
        DownMixInstructions() [];
        DRCCoefficientsBasic() [];
        DRCInstructionsBasic() [];
        DRCCoefficientsUniDRC() [];
        DRCInstructionsUniDRC() [];
        Box (); // further boxes as needed
    }

    12.2.3.3 Semantics
    ChannelCount - is the number of channels such as 1 (mono) or 2 (stereo)
    SampleSize - is in bits, and takes the default value of 16
    SampleRate - when a SamplingRateBox is absent is the sampling rate; when a SamplingRateBox is
                 present, is a suitable integer multiple or division of the actual sampling rate.
                 This 32‐bit field is expressed as a 16.16 fixed‐point number (hi.lo)
    sampling_rate - is the actual sampling rate of the audio media, expressed as a 32‐bit integer
    """

    def __init__(self, offset=0, box=None):
        SampeEntry.__init__(self, offset, box)

        self.reserved = [0 for i in range(2)]
        self.channelcount = 2
        self.samplesize = 16
        self.pre_defined = 0
        self.reserved1 = 0
        self.samplerate = 0

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = SampeEntry.decode(self, file_strm)

        for i in range(len(self.reserved)):
            reserved_ = file_strm.read_uint32()
            self.reserved[i] = reserved_
            self.offset += UInt32ByteLen

        self.channelcount = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.samplesize = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.pre_defined = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.reserved1 = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.samplerate = file_strm.read_uint32()
        self.offset += UInt16ByteLen

        # tmp_size = self.offset - self.box_offset
        # if tmp_size != self.Size():
        #     file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = SampeEntry.dump(self)
        dump_info['reserved'] = self.reserved
        dump_info['channelcount'] = self.channelcount
        dump_info['samplesize'] = self.samplesize
        dump_info['pre_defined'] = self.pre_defined
        dump_info['reserved1'] = self.reserved1
        dump_info['samplerate'] = self.samplerate
        return dump_info

    def __str__(self):
        logstr = "\t\t\t\t\t\t%s\n\t\t\t\t\t\treserved = [" % (SampeEntry.__str__(self))
        for i in range(len(self.reserved)):
            logstr += "%08ld(0x%016lx), " % (self.reserved[i], self.reserved[i])
        logstr += "]\n\t\t\t\t\t\tchannelcount = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tsamplesize = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tpre_defined = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\treserved1 = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tsamplerate = %08ld(0x%016lx)\n" % \
                  (self.channelcount, self.channelcount, self.samplesize,
                   self.samplesize, self.pre_defined, self.pre_defined,
                   self.reserved1, self.reserved1, self.samplerate,
                   self.samplerate)
        return logstr
