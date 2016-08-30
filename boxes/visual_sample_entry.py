#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '5/10/0010 19:08:59'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from sample_entry import *


class VisualSampleEntry(object, SampeEntry):
    """
    class VisualSampleEntry(codingname) extends SampleEntry (codingname){
        unsigned int(16) pre_defined = 0;
        const unsigned int(16) reserved = 0;
        unsigned int(32)[3] pre_defined = 0;
        unsigned int(16) width;
        unsigned int(16) height;
        template unsigned int(32) horizresolution = 0x00480000; // 72 dpi
        template unsigned int(32) vertresolution = 0x00480000; // 72 dpi
        const unsigned int(32) reserved = 0;
        template unsigned int(16) frame_count = 1;
        string[32] compressorname;
        template unsigned int(16) depth = 0x0018;
        int(16) pre_defined = -1;
        // other boxes from derived specifications
        CleanApertureBox clap; // optional
        PixelAspectRatioBox pasp; // optional
    }
    12.1.3.3 Semantics
    resolution - fields give the resolution of the image in pixels‐per‐inch, as a fixed 16.16 number
    frame_count - indicates how many frames of compressed video are stored in each sample. The
                  default is 1, for one frame per sample; it may be more than 1 for multiple
                  frames per sample
    compressorname - is a name, for informative purposes. It is formatted in a fixed 32‐byte field,
                     with the first byte set to the number of bytes to be displayed, followed by
                     that number of bytes of displayable data, and then padding to complete 32
                     bytes total (including the size byte). The field may be set to 0.
    depth - takes one of the following values
            0x0018 – images are in colour with no alpha
    width and height - are the maximum visual width and height of the stream described by this
                       sample description, in pixels
    """

    def __init__(self, offset=0, box=None):
        SampeEntry.__init__(self, offset, box)

        self.pre_defined = 0
        self.reserved1 = 0
        self.pre_defined1 = [0 for i in range(3)]
        self.width = 0
        self.height = 0
        self.horizresolution = 0x00480000  # 72 dpi
        self.vertresolution = 0x00480000  # 72 dpi
        self.reserved2 = 0
        self.frame_count = 1
        self.compressorname = 'a' * 32
        self.depth = 0x0018
        self.pre_defined2 = -1
        # other boxes from derived specifications
        self.clap = None  # optional
        self.pasp = None  # optional

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = SampeEntry.decode(self, file_strm)

        self.pre_defined = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.reserved1 = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        for i in range(len(self.pre_defined1)):
            pre_defined_ = file_strm.read_uint32()
            self.pre_defined1[i] = pre_defined_
            self.offset += UInt32ByteLen

        self.width = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.height = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.horizresolution = file_strm.read_uint32()  # 0x00480000 # 72 dpi
        self.offset += UInt32ByteLen

        self.vertresolution = file_strm.read_uint32()  # 0x00480000 # 72 dpi
        self.offset += UInt32ByteLen

        self.reserved2 = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        self.frame_count = file_strm.read_uint16()
        self.offset += UInt16ByteLen

        self.compressorname = file_strm.read_byte(len(self.compressorname))
        self.offset += UInt8ByteLen * len(self.compressorname)

        self.depth = file_strm.read_uint16()  # 0x0018
        self.offset += UInt16ByteLen

        self.pre_defined2 = file_strm.read_int16()  # -1
        self.offset += UInt16ByteLen

        # tmp_size = self.offset - self.box_offset
        # if tmp_size != self.Size():
        #     file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def GetLength(self):
        size_ = self.offset - self.box_offset
        return size_

    def dump(self):
        dump_info = SampeEntry.dump(self)
        dump_info['pre_defined'] = self.pre_defined
        dump_info['reserved1'] = self.reserved1
        dump_info['pre_defined1'] = self.pre_defined1
        dump_info['width'] = self.width
        dump_info['height'] = self.height
        dump_info['horizresolution'] = self.horizresolution
        dump_info['vertresolution'] = self.vertresolution
        dump_info['reserved2'] = self.reserved2
        dump_info['frame_count'] = self.frame_count
        dump_info['compressorname'] = repr(self.compressorname)
        dump_info['depth'] = self.depth
        dump_info['pre_defined2'] = self.pre_defined2
        return dump_info

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t\tpre_defined = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\treserved1 = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\tpre_defined1 = [" % \
                 (SampeEntry.__str__(self), self.pre_defined, self.pre_defined,
                  self.reserved1, self.reserved1)
        for i in range(len(self.pre_defined1)):
            logstr += "%08ld(0x%016lx), " % (self.pre_defined1[i], self.pre_defined1[i])
        logstr += "]\n\t\t\t\t\t\twidth = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\theight = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\thorizresolution = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tvertresolution = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\treserved2 = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tframe_count = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tcompressorname = %s" \
                  "\n\t\t\t\t\t\tdepth = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tpre_defined2 = %08ld(0x%016lx)\n" % \
                  (self.width, self.width, self.height, self.height, self.horizresolution,
                   self.horizresolution, self.vertresolution, self.vertresolution,
                   self.reserved2, self.reserved2, self.frame_count, self.frame_count,
                   self.compressorname, self.depth, self.depth, self.pre_defined2,
                   self.pre_defined2)
        return logstr
