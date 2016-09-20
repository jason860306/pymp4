#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 15:11:13'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


import mp4descr
from extprofleveldescr import *


class DecoderConfigDescriptor(BaseDescriptor, object):
    """
    7.2.6.6.1 Syntax
    class DecoderConfigDescriptor extends BaseDescriptor
        : bit(8) tag=DecoderConfigDescrTag {
        bit(8) objectTypeIndication;
        bit(6) streamType;
        bit(1) upStream;
        const bit(1) reserved=1;
        bit(24) bufferSizeDB;
        bit(32) maxBitrate;
        bit(32) avgBitrate;
        DecoderSpecificInfo decSpecificInfo[0 .. 1];
        profileLevelIndicationIndexDescriptor profileLevelIndicationIndexDescr[0..255];
    }

    7.2.6.6.2 Semantics
    The DecoderConfigDescriptor provides information about the decoder type and
    the required decoder resources needed for the associated elementary stream.
    This is needed at the receiving terminal to determine whether it is able to
    decode the elementary stream. A stream type identifies the category of the
    stream while the optional decoder specific information descriptor contains
    stream specific information for the set up of the decoder in a stream specific
    format that is opaque to this layer.
    ObjectTypeIndication – an indication of the object or scene description type
                           that needs to be supported by the decoder for this
                           elementary stream as per Table 5.

    When the objectTypeIndication value is 0x6C (Visual ISO/IEC 10918-1, which is JPEG)
    the stream may contain one or more Access Units, where one Access Unit is defined
    to be a complete JPEG (as defined in Visual ISO/IEC 10918-1). Note, that timing and
    other Access Unit and packetization information is to be carried in the transport
    layer such as the MPEG-4 Sync Layer.

    When the objectTypeIndication value is 0x6E (Visual ISO/IEC 15444-1, which is
    JPEG 2000) the stream may contain one or more Access Units, where one Access
    Unit is defined to be a complete JPEG 2000 (as defined in Visual ISO/IEC
    15444-1). Note, that timing and other Access Unit and packetization information
    is to be carried in the transport layer such as the MPEG-4 Sync Layer.

    NOTE The format defined in ISO/IEC 15444-3 is preferred for the storage of JPEG
    2000 sequences in file format of the ISO/IEC 14496-12 family, including MP4.

    streamType – conveys the type of this elementary stream as per Table 6.
    upStream – indicates that this stream is used for upstream information.
    bufferSizeDB – is the size of the decoding buffer for this elementary stream in byte.
    maxBitrate – is the maximum bitrate in bits per second of this elementary stream
                 in any time window of one second duration.
    avgBitrate – is the average bitrate in bits per second of this elementary stream.
                 For streams with variable bitrate this value shall be set to zero.
    decSpecificInfo[] – an array of zero or one decoder specific information classes
                        as specified in 7.2.6.7.
    ProfileLevelIndicationIndexDescr [0..255] – an array of unique identifiers for
                                                a set of profile and level indications
                                                as carried in the ExtensionProfileLevelDescr
                                                defined in 7.2.6.19.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_DecoderConfigDescrTag):
        super(DecoderConfigDescriptor, self).__init__(offset, descr_tag)

        self.objectTypeIndication = 0
        self.streamType = 0
        self.upStream = 0
        self.reserved = 0x1
        self.bufferSizeDB = 0
        self.maxBitrate = 0
        self.avgBitrate = 0
        self.decSpecificInfo = []  # DecoderSpecificInfo
        self.profileLevelIndicationIndexDescr = []  # ExtensionProfileLevelDescriptor

    def decode(self, file_strm):
        """
        :detail layout of esds refer from
         http://www.geocities.com/xhelmboyx/quicktime/formats/mp4-layout.txt

          * 8+ bytes vers. 2 ES Descriptor box
              = long unsigned offset + long ASCII text string 'esds'
           - if encoded to ISO/IEC 14496-10 AVC standards then optionally use:
              = long unsigned offset + long ASCII text string 'm4ds'

            -> 4 bytes version/flags = 8-bit hex version + 24-bit hex flags
                (current = 0)

            -> 1 byte ES descriptor type tag = 8-bit hex value 0x03
            -> 3 bytes extended descriptor type tag string = 3 * 8-bit hex value
              - types are Start = 0x80 ; End = 0xFE
              - NOTE: the extended start tags may be left out
            -> 1 byte descriptor type length = 8-bit unsigned length

              -> 2 bytes ES ID = 16-bit unsigned value
              -> 1 byte stream priority = 8-bit unsigned value
                - Defaults to 16 and ranges from 0 through to 31

                -> 1 byte decoder config descriptor type tag = 8-bit hex value 0x04
                -> 3 bytes extended descriptor type tag string = 3 * 8-bit hex value
                  - types are Start = 0x80 ; End = 0xFE
                  - NOTE: the extended start tags may be left out
                -> 1 byte descriptor type length = 8-bit unsigned length

                  -> 1 byte object type ID = 8-bit unsigned value
                    - type IDs are system v1 = 1 ; system v2 = 2
                    - type IDs are MPEG-4 video = 32 ; MPEG-4 AVC SPS = 33
                    - type IDs are MPEG-4 AVC PPS = 34 ; MPEG-4 audio = 64
                    - type IDs are MPEG-2 simple video = 96
                    - type IDs are MPEG-2 main video = 97
                    - type IDs are MPEG-2 SNR video = 98
                    - type IDs are MPEG-2 spatial video = 99
                    - type IDs are MPEG-2 high video = 100
                    - type IDs are MPEG-2 4:2:2 video = 101
                    - type IDs are MPEG-4 ADTS main = 102
                    - type IDs are MPEG-4 ADTS Low Complexity = 103
                    - type IDs are MPEG-4 ADTS Scalable Sampling Rate = 104
                    - type IDs are MPEG-2 ADTS = 105 ; MPEG-1 video = 106
                    - type IDs are MPEG-1 ADTS = 107 ; JPEG video = 108
                    - type IDs are private audio = 192 ; private video = 208
                    - type IDs are 16-bit PCM LE audio = 224 ; vorbis audio = 225
                    - type IDs are dolby v3 (AC3) audio = 226 ; alaw audio = 227
                    - type IDs are mulaw audio = 228 ; G723 ADPCM audio = 229
                    - type IDs are 16-bit PCM Big Endian audio = 230
                    - type IDs are Y'CbCr 4:2:0 (YV12) video = 240 ; H264 video = 241
                    - type IDs are H263 video = 242 ; H261 video = 243
                  -> 6 bits stream type = 3/4 byte hex value
                    - type IDs are object descript. = 1 ; clock ref. = 2
                    - type IDs are scene descript. = 4 ; visual = 4
                    - type IDs are audio = 5 ; MPEG-7 = 6 ; IPMP = 7
                    - type IDs are OCI = 8 ; MPEG Java = 9
                    - type IDs are user private = 32
                  -> 1 bit upstream flag = 1/8 byte hex value
                  -> 1 bit reserved flag = 1/8 byte hex value set to 1
                  -> 3 bytes buffer size = 24-bit unsigned value
                  -> 4 bytes maximum bit rate = 32-bit unsigned value
                  -> 4 bytes average bit rate = 32-bit unsigned value

                    -> 1 byte decoder specific descriptor type tag
                        = 8-bit hex value 0x05
                    -> 3 bytes extended descriptor type tag string
                        = 3 * 8-bit hex value
                      - types are Start = 0x80 ; End = 0xFE
                      - NOTE: the extended start tags may be left out
                    -> 1 byte descriptor type length
                        = 8-bit unsigned length

                      -> ES header start codes = hex dump

                -> 1 byte SL config descriptor type tag = 8-bit hex value 0x06
                -> 3 bytes extended descriptor type tag string = 3 * 8-bit hex value
                  - types are Start = 0x80 ; End = 0xFE
                  - NOTE: the extended start tags may be left out
                -> 1 byte descriptor type length = 8-bit unsigned length

                  -> 1 byte SL value = 8-bit hex value set to 0x02

            00 00 00 27 65 73 64 73 00 00 00 00 03 19 00 02 ; ...'esds........
            00 04 11 40 15 00 06 00 00 01 F4 00 00 01 F4 00 ; ...@............
            05 02 12 10 06 01 02                            ; .......
            Atom Box:
            00 00 00 27 (box size) 65 73 64 73 ('esds') 00 00 00 00 (version + flag)
            ES descriptor:
            03 (tag) 19 (tag size) 00 02 (track_id) 00 (flag)
            DecoderConfig descriptor:
            04 (tag) 11 (tag size) 40 (MPEG-4 audio) 15 (audio stream)
            00 06 00 (Buffersize DB)  00 01 F4 00 (max bitrate 128000)
            00 01 F4 00 (avg bitrate 128000)
            DecoderSpecific info descriptor
            05 (tag) 02 (tag size) 12 10 (Audio Specific Config)
            Audio Specific Config:
            5 bits: object type
            4 bits: frequency index
            4 bits: channel configuration
            1 bit: frame length flag
            1 bit: dependsOnCoreCoder
            1 bit: extensionFlag
            Audio Object Types
            MPEG-4 Audio Object Types:
            0: Null
            1: AAC Main
            2: AAC LC (Low Complexity)
            3: AAC SSR (Scalable Sample Rate)
            4: ...
            Sampling Frequencies
            0: 96000 Hz
            1: 88200 Hz
            2: 64000 Hz
            3: 48000 Hz
            4: 44100 Hz
            5: ...
            Channel Configurations
            0: Defined in AOT Specifc Config
            1: 1 channel: front-center
            2: 2 channels: front-left, front-right
            3: 3 channels: front-center, front-left, front-right
            4: ...
            frame length flag:
            0: Each packet contains 1024 samples
            1: Each packet contains 960 samples
            Example:
            1210h = 00010010 00010000b = 00010(AAC LC)  010 0 (44100Hz)
            0010 (strero) 0 (1024 samples) 00 ( ? )
            SL descriptor
            06 (tag) 01 (tag size) 02 (always 2 refer from mov_write_esds_tag);

            Reference:
            ffmpeg-2.7/libavformat/movenc.c  mov_write_esds_tag
            http://wiki.multimedia.cx/?title=Understanding_AAC
            http://wiki.multimedia.cx/index.php?title=MPEG-4_Audio

        :param file_strm:
        :return:
        """

        file_strm = super(DecoderConfigDescriptor, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        self.objectTypeIndication = file_strm.read_uint8()
        self.offset += UInt8ByteLen

        tmp_byte = file_strm.read_uint8()
        self.streamType = tmp_byte & 0xFC >> 2
        self.upStream = tmp_byte & 0x02 >> 1
        self.reserved = tmp_byte & 0x01  # 0x1
        self.offset += UInt8ByteLen

        self.bufferSizeDB = file_strm.read_byte(3)
        self.offset += 3
        # self.bufferSizeDB = int(self.bufferSizeDB, base=16)

        self.maxBitrate = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        self.avgBitrate = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        left_size = self.size() - (self.offset - self.descr_offset)
        while left_size > 0:
            tmp_descr = BaseDescriptor(self.offset)
            if tmp_descr.peek(file_strm) is None:
                return file_strm
            tmp_descr = mp4descr.create_descr(self.offset, tmp_descr.descr_tag)
            file_strm = tmp_descr.decode(file_strm)
            if file_strm is None:
                print "file_strm is None"
                return file_strm
            self.offset += tmp_descr.size()
            self._add_desc(tmp_descr)

            left_size = self.size() - (self.offset - self.descr_offset)

        return file_strm

    def _add_desc(self, tmp_descr):
        """
        :brief add a descriptor, source code from gpac(be famous as mp4box)
        :detail:
            GF_Err AddDescriptorToESD(GF_ESD *esd, GF_Descriptor *desc)
            {
                if (!esd || !desc) return GF_BAD_PARAM;

                switch (desc->tag) {
                case GF_ODF_DCD_TAG:
                    if (esd->decoderConfig) return GF_ODF_INVALID_DESCRIPTOR;
                    esd->decoderConfig = (GF_DecoderConfig *) desc;
                    break;

                case GF_ODF_SLC_TAG:
                    if (esd->slConfig) return GF_ODF_INVALID_DESCRIPTOR;
                    esd->slConfig = (GF_SLConfig *) desc;
                    break;

                case GF_ODF_MUXINFO_TAG:
                    gf_list_add(esd->extensionDescriptors, desc);
                    break;

                case GF_ODF_LANG_TAG:
                    if (esd->langDesc) return GF_ODF_INVALID_DESCRIPTOR;
                    esd->langDesc = (GF_Language *) desc;
                    break;

            #ifndef GPAC_MINIMAL_ODF
                //the GF_ODF_ISOM_IPI_PTR_TAG is only used in the file format and replaces GF_ODF_IPI_PTR_TAG...
                case GF_ODF_ISOM_IPI_PTR_TAG:
                case GF_ODF_IPI_PTR_TAG:
                    if (esd->ipiPtr) return GF_ODF_INVALID_DESCRIPTOR;
                    esd->ipiPtr = (GF_IPIPtr *) desc;
                    break;

                case GF_ODF_QOS_TAG:
                    if (esd->qos) return GF_ODF_INVALID_DESCRIPTOR;
                    esd->qos  =(GF_QoS_Descriptor *) desc;
                    break;

                case GF_ODF_CI_TAG:
                case GF_ODF_SCI_TAG:
                    return gf_list_add(esd->IPIDataSet, desc);

                //we use the same struct for v1 and v2 IPMP DPs
                case GF_ODF_IPMP_PTR_TAG:
                    return gf_list_add(esd->IPMPDescriptorPointers, desc);

                case GF_ODF_REG_TAG:
                    if (esd->RegDescriptor) return GF_ODF_INVALID_DESCRIPTOR;
                    esd->RegDescriptor =(GF_Registration *) desc;
                    break;
            #endif

                default:
                    if ( (desc->tag >= GF_ODF_EXT_BEGIN_TAG) &&
                            (desc->tag <= GF_ODF_EXT_END_TAG) ) {
                        return gf_list_add(esd->extensionDescriptors, desc);
                    }
                    gf_odf_delete_descriptor(desc);
                    return GF_OK;
                }

                return GF_OK;
            }
        :param tmp_descr:
        :return:
        """

        if DescrTag_DecSpecificInfoTag == tmp_descr.descr_tag:
            self.decSpecificInfo.append(tmp_descr)
        elif DescrTag_profileLevelIndicationIndexDescrTag == tmp_descr.descr_tag:
            self.profileLevelIndicationIndexDescr.append(tmp_descr)

    def size(self):
        return super(DecoderConfigDescriptor, self).size()

    def dump(self):
        dump_info = super(DecoderConfigDescriptor, self).dump()
        dump_info['objectTypeIndication'] = str(self.objectTypeIndication)
        dump_info['streamType'] = str(self.streamType)
        dump_info['upStream'] = str(self.upStream)
        dump_info['reserved'] = str(self.reserved)
        dump_info['bufferSizeDB'] = repr(self.bufferSizeDB)
        dump_info['maxBitrate'] = str(self.maxBitrate)
        dump_info['avgBitrate'] = str(self.avgBitrate)
        if self.decSpecificInfo is not None:
            decSpecInfo = dict()
            for i in xrange(len(self.decSpecificInfo)):
                decSpecInfo["decSpecificInfo_{0}".format(i)] = self.decSpecificInfo[i].dump()
            dump_info['decSpecificInfo'] = decSpecInfo

        if self.profileLevelIndicationIndexDescr is not None:
            profLevelIndicIdxDescr = dict()
            for i in xrange(len(self.profileLevelIndicationIndexDescr)):
                profLevelIndicIdxDescr["profileLevelIndicationIndexDescr_{0}".format(i)] = \
                    self.profileLevelIndicationIndexDescr[i].dump()
            dump_info['profileLevelIndicationIndexDescr'] = profLevelIndicIdxDescr

        return dump_info

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t\t\t\t" \
                 "objectTypeIndication = %08ld(0x%016lx)\n\t\t\t\t\t\t\t\t" \
                 "streamType = %08ld(0x%016lx)\n\t\t\t\t\t\t\t\t" \
                 "upStream = %08ld(0x%016lx)\n\t\t\t\t\t\t\t\t" \
                 "reserved = %08ld(0x%016lx)\n\t\t\t\t\t\t\t\t" \
                 "bufferSizeDB = %s\n\t\t\t\t\t\t\t\t" \
                 "maxBitrate = %08ld(0x%016lx)\n\t\t\t\t\t\t\t\t" \
                 "avgBitrate = %08ld(0x%016lx)\n\t\t\t\t\t\t\t\t" \
                 % (str(super(DecoderConfigDescriptor, self)), self.objectTypeIndication,
                    self.objectTypeIndication, self.streamType, self.streamType,
                    self.upStream, self.upStream, self.reserved, self.reserved,
                    repr(self.bufferSizeDB), self.maxBitrate, self.maxBitrate,
                    self.avgBitrate, self.avgBitrate)
        for i in xrange(len(self.decSpecificInfo)):
            logstr += 'decSpecificInfo_%d: %s\n\t\t\t\t\t\t\t\t' % (i, str(self.decSpecificInfo[i]))
        for i in xrange(len(self.profileLevelIndicationIndexDescr)):
            logstr += 'profileLevelIndicationIndexDescr_%d: %s\n\t\t\t\t\t\t\t\t' % \
                      (i, str(self.profileLevelIndicationIndexDescr[i]))
        return logstr
