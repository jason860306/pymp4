#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '5/5/2016 17:59:16'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"

# '$Source$'


from box import *


class ParameterSet(object):
    """
    unsigned int(16) sequenceParameterSetLength ;
    bit(8*sequenceParameterSetLength) sequenceParameterSetNALUnit;

    unsigned int(16) pictureParameterSetLength;
    bit(8*pictureParameterSetLength) pictureParameterSetNALUnit;
    """

    def __init__(self):
        self.ps_len = 0
        self.ps_nalu = ''

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm
        self.ps_len = file_strm.read_uint16()
        self.ps_nalu = file_strm.read_byte(self.ps_len)

        return file_strm

    def Size(self):
        size = 0
        size += UInt16ByteLen
        size += UInt8ByteLen * self.ps_len
        return size

    def dump(self):
        dump_info = {}
        dump_info['ps_len'] = self.ps_len
        dump_info['ps_nalu'] = repr(self.ps_nalu)
        return dump_info

    def __str__(self):
        logstr = "ps_len = %08ld(0x%016lx), ps_nalu = %08s(0x%016s)" % \
                 (self.ps_len, self.ps_len, repr(self.ps_nalu), repr(self.ps_nalu))
        return logstr


class SequenceParameterSet(object, ParameterSet):
    """
    unsigned int(16) sequenceParameterSetLength ;
    bit(8*sequenceParameterSetLength) sequenceParameterSetNALUnit;
    """

    def __init__(self):
        ParameterSet.__init__(self)

    def decode(self, file_strm):
        return ParameterSet.decode(self, file_strm)


class PictureParameterSet(object, ParameterSet):
    """
    unsigned int(16) pictureParameterSetLength;
    bit(8*pictureParameterSetLength) pictureParameterSetNALUnit;
    """

    def __init__(self):
        ParameterSet.__init__(self)

    def decode(self, file_strm):
        return ParameterSet.decode(self, file_strm)


class SequenceParameterSetExt(object, ParameterSet):
    """
    unsigned int(16) sequenceParameterSetExtLength;
    bit(8*sequenceParameterSetExtLength) sequenceParameterSetExtNALUnit;
    """

    def __init__(self):
        ParameterSet.__init__(self)

    def decode(self, file_strm):
        return ParameterSet.decode(self, file_strm)


class AVCDecoderConfigurationRecord(object):
    """
    aligned(8) class AVCDecoderConfigurationRecord {
        unsigned int(8) configurationVersion = 1;
        unsigned int(8) AVCProfileIndication;
        unsigned int(8) profile_compatibility;
        unsigned int(8) AVCLevelIndication;
        bit(6) reserved = ‘111111’b;
        unsigned int(2) lengthSizeMinusOne;
        bit(3) reserved = ‘111’b;
        unsigned int(5) numOfSequenceParameterSets;
        for (i=0; i< numOfSequenceParameterSets; i++) {
            unsigned int(16) sequenceParameterSetLength ;
            bit(8*sequenceParameterSetLength) sequenceParameterSetNALUnit;
        }
        unsigned int(8) numOfPictureParameterSets;
        for (i=0; i< numOfPictureParameterSets; i++) {
            unsigned int(16) pictureParameterSetLength;
            bit(8*pictureParameterSetLength) pictureParameterSetNALUnit;
        }
        if( profile_idc == 100 || profile_idc == 110 ||
        profile_idc == 122 || profile_idc == 144 )
        {
            bit(6) reserved = ‘111111’b;
            unsigned int(2) chroma_format;
            bit(5) reserved = ‘11111’b;
            unsigned int(3) bit_depth_luma_minus8;
            bit(5) reserved = ‘11111’b;
            unsigned int(3) bit_depth_chroma_minus8;
            unsigned int(8) numOfSequenceParameterSetExt;
            for (i=0; i< numOfSequenceParameterSetExt; i++) {
                unsigned int(16) sequenceParameterSetExtLength;
                bit(8*sequenceParameterSetExtLength) sequenceParameterSetExtNALUnit;
            }
        }
    }

    5.2.4.1.2 Semantics
    AVCProfileIndication - contains the profile code as defined in ISO/IEC 14496-10.
    profile_compatibility - is a byte defined exactly the same as the byte which occurs
                            between the profile_IDC and level_IDC in a sequence parameter
                            set (SPS), as defined in ISO/IEC 14496-10.
    AVCLevelIndication - contains the level code as defined in ISO/IEC 14496-10.
    lengthSizeMinusOne - indicates the length in bytes of the NALUnitLength field in an AVC video
                         sample or AVC parameter set sample of the associated stream minus one.
                         For example, a size of one byte is indicated with a value of 0.
                         The value of this field shall be one of 0, 1, or 3 corresponding to a
                         length encoded with 1, 2, or 4 bytes, respectively.
    numOfSequenceParameterSets - indicates the number of SPSs that are used as the initial set
                                 of SPSs for decoding the AVC elementary stream.
    sequenceParameterSetLength - indicates the length in bytes of the SPS NAL unit as defined in
                                 ISO/IEC 14496-10.
    sequenceParameterSetNALUnit - contains a SPS NAL unit, as specified in ISO/IEC 14496-10. SPSs
                                  shall occur in order of ascending parameter set identifier with
                                  gaps being allowed.
    numOfPictureParameterSets - indicates the number of picture parameter sets (PPSs) that are used
                                as the initial set of PPSs for decoding the AVC elementary stream.
    pictureParameterSetLength - indicates the length in bytes of the PPS NAL unit as defined in
                                ISO/IEC 14496-10.
    pictureParameterSetNALUnit - contains a PPS NAL unit, as specified in ISO/IEC 14496-10. PPSs
                                 shall occur in order of ascending parameter set identifier with
                                 gaps being allowed.
    chroma_format - contains the chroma_format indicator as defined by the chroma_format_idc
                    parameter in ISO/IEC 14496-10.
    bit_depth_luma_minus8 - indicates the bit depth of the samples in the Luma arrays.
                            For example, a bit depth of 8 is indicated with a value of zero
                            (BitDepth = 8 + bit_depth_luma_minus8). The value of this field
                            shall be in the range of 0 to 4, inclusive.
    bit_depth_chroma_minus8 - indicates the bit depth of the samples in the Chroma arrays.
                              For example, a bit depth of 8 is indicated with a value of zero
                              (BitDepth = 8 + bit_depth_luma_minus8). The value of this field
                              shall be in the range of 0 to 4, inclusive.
    numOfSequenceParameterSetExt - indicates the number of Sequence Parameter Set Extensions that
                                   are used for decoding the AVC elementary stream.
    sequenceParameterSetExtLength - indicates the length in bytes of the SPS Extension NAL unit as
                                    defined in ISO/IEC 14496-10.
    sequenceParameterSetExtNALUnit - contains a SPS Extension NAL unit, as specified in
                                     ISO/IEC 14496-10.
    """

    class SequenceParameterSetExt(object):
        """
        if( profile_idc == 100 || profile_idc == 110 ||
        profile_idc == 122 || profile_idc == 144 )
        {
            bit(6) reserved = ‘111111’b;
            unsigned int(2) chroma_format;
            bit(5) reserved = ‘11111’b;
            unsigned int(3) bit_depth_luma_minus8;
            bit(5) reserved = ‘11111’b;
            unsigned int(3) bit_depth_chroma_minus8;
            unsigned int(8) numOfSequenceParameterSetExt;
            for (i=0; i< numOfSequenceParameterSetExt; i++) {
                unsigned int(16) sequenceParameterSetExtLength;
                bit(8*sequenceParameterSetExtLength) sequenceParameterSetExtNALUnit;
            }
        }
        """

        def __init__(self, offset=0):
            self.box_offset = offset
            self.offset = offset

            self.reserved1 = 0
            self.chroma_format = 0
            self.reserved2 = 0
            self.bit_depth_luma_minus8 = 0
            self.reserved3 = 0
            self.bit_depth_chroma_minus8 = 0
            self.num_spse = 0
            self.spse = []

        def decode(self, file_strm):
            if file_strm is None:
                print "file_strm is None"
                return file_strm

            tmp_byte = file_strm.read_uint8()
            self.reserved1 = ((tmp_byte & 0xFC) >> 2)
            self.chroma_format = (tmp_byte & 0x03)
            self.offset += UInt8ByteLen

            tmp_byte = file_strm.read_uint8()
            self.reserved2 = ((tmp_byte & 0xF8) >> 3)
            self.bit_depth_luma_minus8 = (tmp_byte & 0x07)
            self.offset += UInt8ByteLen

            tmp_byte = file_strm.read_uint8()
            self.reserved3 = ((tmp_byte & 0xF8) >> 3)
            self.bit_depth_chroma_minus8 = (tmp_byte & 0x07)
            self.offset += UInt8ByteLen

            self.num_spse = file_strm.read_uint8()
            self.offset += UInt8ByteLen
            for i in range(self.num_spse):
                tmp_spse = SequenceParameterSetExt()
                file_strm = tmp_spse.decode(file_strm)
                self.spse.append(tmp_spse)
                self.offset += tmp_spse.Size()

            return file_strm

        def dump(self):
            dump_info = {}
            dump_info['box_offset'] = self.box_offset
            dump_info['offset'] = self.offset
            dump_info['reserved1'] = self.reserved1
            dump_info['chroma_format'] = self.chroma_format
            dump_info['reserved2'] = self.reserved2
            dump_info['bit_depth_luma_minus8'] = self.bit_depth_luma_minus8
            dump_info['reserved3'] = self.reserved3
            dump_info['bit_depth_chroma_minus8'] = self.bit_depth_chroma_minus8
            dump_info['num_spse'] = self.num_spse
            if self.num_spse > 0 and self.spse != None:
                spsees = {}
                for i in range(len(self.spse)):
                    sps_ = self.spse[i]
                    spsees['spse_%d' % i] = sps_[i].dump()
                dump_info['spse'] = spsees
            return dump_info

        def __str__(self):
            logstr = "\t\t\t\t\t\t\t\t\t\tbox_offset = %08ld(0x%016lx)" \
                     "\n\t\t\t\t\t\t\t\t\t\toffset = %08ld(0x%016lx)" \
                     "\n\t\t\t\t\t\t\t\t\t\treserved1 = %08ld(0x%016lx)" \
                     "\n\t\t\t\t\t\t\t\t\t\tchroma_format = %08ld(0x%016lx)" \
                     "\n\t\t\t\t\t\t\t\t\t\treserved2 = %08ld(0x%016lx)" \
                     "\n\t\t\t\t\t\t\t\t\t\tbit_depth_luma_minus8 = %08ld(0x%016lx)" \
                     "\n\t\t\t\t\t\t\t\t\t\treserved3 = %08ld(0x%016lx)" \
                     "\n\t\t\t\t\t\t\t\t\t\tbit_depth_chroma_minus8 = %08ld(0x%016lx)" \
                     "\n\t\t\t\t\t\t\t\t\t\tnum_spse = %08ld(0x%016lx), spse = [" % \
                     (self.box_offset, self.box_offset, self.offset, self.offset,
                      self.reserved1, self.reserved1, self.chroma_format, self.chroma_format,
                      self.reserved2, self.reserved2, self.bit_depth_luma_minus8,
                      self.bit_depth_luma_minus8, self.reserved3, self.reserved3,
                      self.bit_depth_chroma_minus8, self.bit_depth_chroma_minus8,
                      self.num_spse, self.num_spse)
            for i in range(len(self.spse)):
                logstr += "\n\t\t\t\t\t\t\t\t\t\t\t%08ld. %s" % (i, self.spse[i])
            logstr += "\n\t\t\t\t\t\t\t\t\t\t]\n"
            return logstr

    def __init__(self, offset=0):
        self.box_offset = offset
        self.offset = offset

        self.conf_version = 0
        self.avc_profile_indication = 0
        self.profile_compatibility = 0
        self.avc_level_indication = 0
        self.reserved1 = 0
        self.length_size_nalu = 0
        self.reserved2 = 0
        self.num_sps = 0
        self.sps = []
        self.num_pps = 0
        self.pps = []
        self.reserved3 = 0
        self.chroma_format = 0
        self.reserved4 = 0
        self.bit_depth_luma_minus8 = 0
        self.reserved5 = 0
        self.bit_depth_chroma_minus8 = 0
        self.num_spse = 0
        self.spse = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        self.conf_version = file_strm.read_uint8()
        self.offset += UInt8ByteLen

        self.avc_profile_indication = file_strm.read_uint8()
        self.offset += UInt8ByteLen

        self.profile_compatibility = file_strm.read_uint8()
        self.offset += UInt8ByteLen

        self.avc_level_indication = file_strm.read_uint8()
        self.offset += UInt8ByteLen

        tmp_byte = file_strm.read_uint8()
        self.reserved1 = ((tmp_byte & 0xFC) >> 2)
        self.length_size_nalu = (tmp_byte & 0x03)
        self.offset += UInt8ByteLen

        tmp_byte = file_strm.read_uint8()
        self.reserved2 = ((tmp_byte & 0x07) >> 5)
        self.num_sps = (tmp_byte & 0x1F)
        self.offset += UInt8ByteLen

        for i in range(self.num_sps):
            tmp_sps = SequenceParameterSet()
            file_strm = tmp_sps.decode(file_strm)
            self.sps.append(tmp_sps)
            self.offset += tmp_sps.Size()

        self.num_pps = file_strm.read_uint8()
        self.offset += UInt8ByteLen

        for i in range(self.num_pps):
            tmp_pps = PictureParameterSet()
            file_strm = tmp_pps.decode(file_strm)
            self.pps.append(tmp_pps)
            self.offset += tmp_pps.Size()

        # TODO: to debug profile_idc
        # if( profile_idc == 100 || profile_idc == 110 ||
        #     profile_idc == 122 || profile_idc == 144 )
        #
        # if self.avc_profile_indication in [100, 110, 122, 144]:
        #     tmp_byte = file_strm.read_uint8()
        #     self.reserved3 = ((tmp_byte & 0xFC) >> 2)
        #     self.chroma_format = (tmp_byte & 0x03)
        #     self.offset += UInt8ByteLen
        #
        #     tmp_byte = file_strm.read_uint8()
        #     self.reserved4 = ((tmp_byte & 0xF8) >> 3)
        #     self.bit_depth_luma_minus8 = (tmp_byte & 0x07)
        #     self.offset += UInt8ByteLen
        #
        #     tmp_byte = file_strm.read_uint8()
        #     self.reserved5 = ((tmp_byte & 0xF8) >> 3)
        #     self.bit_depth_chroma_minus8 = (tmp_byte & 0x07)
        #     self.offset += UInt8ByteLen
        #
        #     self.num_spse = file_strm.read_uint8()
        #     self.offset += UInt8ByteLen
        #
        #     for i in range(self.num_spse):
        #         self.spse = SequenceParameterSetExt()
        #         file_strm = self.spse.decode(file_strm)
        #         self.offset += self.spse.Size()

        return file_strm

    def get_nal_len_size(self):
        return self.length_size_nalu + 1

    def dump(self):
        dump_info = {}
        dump_info['box_offset'] = self.box_offset
        dump_info['offset'] = self.offset
        dump_info['conf_version'] = self.conf_version
        dump_info['avc_profile_indication'] = self.avc_profile_indication
        dump_info['profile_compatibility'] = self.profile_compatibility
        dump_info['avc_level_indication'] = self.avc_level_indication
        dump_info['reserved1'] = self.reserved1
        dump_info['length_size_nalu'] = self.length_size_nalu
        dump_info['reserved2'] = self.reserved2
        dump_info['num_sps'] = self.num_sps
        if self.num_sps > 0 and self.sps != None:
            spses = {}
            for i in range(len(self.sps)):
                spses['sps_%d' % i] = self.sps[i].dump()
            dump_info['sps'] = spses
        dump_info['num_pps'] = self.num_pps
        if self.num_pps > 0 and self.pps != None:
            ppses = {}
            for i in range(len(self.pps)):
                ppses['pps_%d' % i] = self.pps[i].dump()
            dump_info['pps'] = ppses
        dump_info['reserved3'] = self.reserved3
        dump_info['chroma_format'] = self.chroma_format
        dump_info['reserved4'] = self.reserved4
        dump_info['bit_depth_luma_minus8'] = self.bit_depth_luma_minus8
        dump_info['reserved5'] = self.reserved5
        dump_info['bit_depth_chroma_minus8'] = self.bit_depth_chroma_minus8
        dump_info['num_spse'] = self.num_spse
        if self.num_spse > 0 and self.spse != None:
            spse_dict = {}
            for i in range(len(self.spse)):
                spse_dict['spse_%d' % i] = self.spse[i].dump()
            dump_info['spse'] = spse_dict
        return dump_info

    def __str__(self):
        logstr = "\n\t\t\t\t\t\tbox_offset = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\toffset = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\tconf_version = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\tavc_profile_indication = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\tprofile_compatibility = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\tavc_level_indication = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\treserved1 = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\tlength_size_nalu = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\treserved2 = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\tnum_sps = %08ld(0x%016lx), sps = [" % \
                 (self.box_offset, self.box_offset, self.offset, self.offset,
                  self.conf_version, self.conf_version, self.avc_profile_indication,
                  self.avc_profile_indication, self.profile_compatibility,
                  self.profile_compatibility, self.avc_level_indication, self.avc_level_indication,
                  self.reserved1, self.reserved1, self.length_size_nalu, self.length_size_nalu,
                  self.reserved2, self.reserved2, self.num_sps, self.num_sps)
        for i in range(len(self.sps)):
            logstr += "\n\t\t\t\t\t\t\t%08ld. %s" % (i, self.sps[i])
        logstr += "\n\t\t\t\t\t\t]\n\t\t\t\t\t\tnum_pps = %08ld(0x%016lx), " \
                  "pps = [" % (self.num_pps, self.num_pps)
        for i in range(len(self.pps)):
            logstr += "\n\t\t\t\t\t\t\t%08ld. %s" % (i, self.pps[i])
        logstr += "\n\t\t\t\t\t\t]"
        logstr += "\n\t\t\t\t\t\treserved3 = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tchroma_format = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\treserved4 = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tbit_depth_luma_minus8 = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\treserved5 = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tbit_depth_chroma_minus8 = %08ld(0x%016lx)" \
                  "\n\t\t\t\t\t\tnum_spse = %08ld(0x%016lx), spse = [" % \
                  (self.reserved3, self.reserved3, self.chroma_format,
                   self.chroma_format, self.reserved4, self.reserved4,
                   self.bit_depth_luma_minus8, self.bit_depth_luma_minus8,
                   self.reserved5, self.reserved5, self.bit_depth_chroma_minus8,
                   self.bit_depth_chroma_minus8, self.num_spse, self.num_spse)
        for i in range(len(self.spse)):
            logstr += "\n\t\t\t\t\t\t\t%08ld. %s" % (i, self.spse[i])
        logstr += "\n\t\t\t\t\t\t]"
        return logstr


class AvcC(object, Box):
    """
    // Visual Sequences
    class AvcC extends Box(‘avcC’) {
        AVCDecoderConfigurationRecord() AVCConfig;
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        self.avcCRecord = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)
        self.avcCRecord = AVCDecoderConfigurationRecord(self.offset)
        file_strm = self.avcCRecord.decode(file_strm)

        # tmp_size = self.offset - self.box_offset
        # if tmp_size != self.Size():
        #     file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def get_sps(self):
        return None if (self.avcCRecord is None) else \
            [sps.ps_nalu for sps in self.avcCRecord.sps]

    def get_pps(self):
        return None if (self.avcCRecord is None) else \
            [pps.ps_nalu for pps in self.avcCRecord.pps]

    def get_spse(self):
        return None if (self.avcCRecord is None) else \
            [spse.ps_nalu for spse in self.avcCRecord.spse]

    def get_nal_len_size(self):
        return 0 if (self.avcCRecord is None) else \
            self.avcCRecord.get_nal_len_size()

    def dump(self):
        dump_info = Box.dump(self)
        if self.avcCRecord != None:
            dump_info['avcCRecord'] = self.avcCRecord.dump()
        return dump_info

    def __str__(self):
        logstr = "%s%s\n" % \
                 (Box.__str__(self), self.avcCRecord)
        return logstr
