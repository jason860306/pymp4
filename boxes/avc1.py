#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '5/10/0010 19:25:29'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import mp4boxes
from visual_sample_entry import *


class Avc1(object, VisualSampleEntry):
    """
    class AvcC extends Box(‘avcC’) {
        AVCDecoderConfigurationRecord() AVCConfig;
    }
    class MPEG4BitRateBox extends Box(‘btrt’){
        unsigned int(32) bufferSizeDB;
        unsigned int(32) maxBitrate;
        unsigned int(32) avgBitrate;
    }
    class MPEG4ExtensionDescriptorsBox extends Box(‘m4ds’) {
        Descriptor Descr[0 .. 255];
    }
    class AVCSampleEntry() extends VisualSampleEntry (‘avc1’){
        AVCConfigurationBox config;
        MPEG4BitRateBox (); // optional
        MPEG4ExtensionDescriptorsBox (); // optional
    }

    5.3.4.1.3 Semantics
    Compressorname - in the base class VisualSampleEntry indicates the name of the compressor used
                     with the value "\012AVC Coding" being recommended (\012 is 10, the length of
                     the string as a byte).
    config - is defined in 5.2.4. If a separate parameter set stream is used,
             numOfSequenceParameterSets and numOfPictureParameterSets must both be zero.
    Descr - is a descriptor which should be placed in the ElementaryStreamDescriptor when
            this stream is used in an MPEG-4 systems context. This does not include
            SLConfigDescriptor or DecoderConfigDescriptor, but includes the other descriptors
            in order to be placed after the SLConfigDescriptor.
    """

    def __init__(self, offset=0, box=None):
        VisualSampleEntry.__init__(self, offset, box)

        self.avcC = None
        self.btrt = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = VisualSampleEntry.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)

            if tmp_box.type == FourCCMp4AvcC:
                self.avcC = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.avcC.decode(file_strm)
                self.offset += self.avcC.Size()
            elif tmp_box.type == FourCCMp4Btrt:
                self.btrt = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.btrt.decode(file_strm)
                self.offset += self.btrt.Size()
            else:
                file_strm.seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def get_sps(self):
        return None if (self.avcC is None) else self.avcC.get_sps()

    def get_pps(self):
        return None if (self.avcC is None) else self.avcC.get_pps()

    def get_spse(self):
        return None if (self.avcC is None) else self.avcC.get_spse()

    def get_nal_len_size(self):
        return 0 if (self.avcC is None) else self.avcC.get_nal_len_size()

    def dump(self):
        dump_info = VisualSampleEntry.dump(self)
        if self.avcC is not None:
            dump_info[self.avcC.type] = self.avcC.dump()
        if self.btrt is not None:
            dump_info[self.btrt.type] = self.btrt.dump()
        return dump_info

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t%s\n\t\t\t\t\t%s" % \
                 (VisualSampleEntry.__str__(self), self.avcC, self.btrt)
        return logstr
