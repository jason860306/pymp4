#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 14:32:47'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from deccfgdescr import *
from extslcfgdescr import *
from ipidescr import *
from mp4descr import *
from odproflevelindicdef import *


class ESDescriptor(BaseDescriptor, object):
    """
    7.2.6.5.1 Syntax
    class ES_Descriptor extends BaseDescriptor
        : bit(8) tag=ES_DescrTag {
        bit(16) ES_ID;
        bit(1) streamDependenceFlag;
        bit(1) URL_Flag;
        bit(1) OCRstreamFlag;
        bit(5) streamPriority;
        if (streamDependenceFlag)
            bit(16) dependsOn_ES_ID;
        if (URL_Flag) {
            bit(8) URLlength;
            bit(8) URLstring[URLlength];
        }
        if (OCRstreamFlag)
            bit(16) OCR_ES_Id;
        DecoderConfigDescriptor decConfigDescr;
        if (ODProfileLevelIndication==0x01) //no SL extension.
        {
            SLConfigDescriptor slConfigDescr;
        }
        else // SL extension is possible.
        {
            SLConfigDescriptor slConfigDescr;
        }
        IPI_DescrPointer ipiPtr[0 .. 1];
        IP_IdentificationDataSet ipIDS[0 .. 255];
        IPMP_DescriptorPointer ipmpDescrPtr[0 .. 255];
        LanguageDescriptor langDescr[0 .. 255];
        QoS_Descriptor qosDescr[0 .. 1];
        RegistrationDescriptor regDescr[0 .. 1];
        ExtensionDescriptor extDescr[0 .. 255];
    }

    7.2.6.5.2 Semantics
    The ES_Descriptor conveys all information related to a particular elementary
    stream and has three major parts.

    The first part consists of the ES_ID which is a unique reference to the
    elementary stream within its name scope (see 7.2.7.2.4), a mechanism to
    describe dependencies of elementary streams within the scope of the parent
    object descriptor and an optional URL string. Dependencies and usage of URLs
    are specified in 7.2.7.

    The second part consists of the component descriptors which convey the
    parameters and requirements of the elementary stream.

    The third part is a set of optional extension descriptors that support the
    inclusion of future extensions as well as the transport of private data in
    a backward compatible way.

    ES_ID – This syntax element provides a unique label for each elementary
    stream within its name scope. The values 0 and 0xFFFF are reserved.
    streamDependenceFlag – If set to one indicates that a dependsOn_ES_ID will follow.
    URL_Flag – if set to 1 indicates that a URLstring will follow.
    OCRstreamFlag – indicates that an OCR_ES_ID syntax element will follow.
                    streamPriority – indicates a relative measure for the priority
                    of this elementary stream. An elementary stream with a higher
                    streamPriority is more important than one with a lower
                    streamPriority. The absolute values of streamPriority are not
                    normatively defined.
    dependsOn_ES_ID – is the ES_ID of another elementary stream on which this
                      elementary stream depends. The stream with dependsOn_ES_ID
                      shall also be associated to the same object descriptor as the
                      current ES_Descriptor.
    URLlength – the length of the subsequent URLstring in bytes.
    URLstring[] – contains a UTF-8 (ISO/IEC 10646-1) encoded URL that shall point to
                  the location of an SLpacketized stream by name. The parameters of
                  the SL-packetized stream that is retrieved from the URL are
                  fully specified in this ES_Descriptor.
                  See also 7.2.7.3.3. Permissible URLs may be constrained by profile
                  and levels as well as by specific delivery layers.
    OCR_ES_ID – indicates the ES_ID of the elementary stream within the name scope
                (see 7.2.7.2.4) from which the time base for this elementary stream
                is derived. Circular references between elementary streams are not
                permitted.
    decConfigDescr – is a DecoderConfigDescriptor as specified in 7.2.6.6.
    slConfigDescr – is an SLConfigDescriptor as specified in 7.2.6.8. If
                    ODProfileLevelIndication is different from 0x01, it may be an
                    extension of SLConfigDescriptor (i.e. and extended class) as
                    defined in 7.2.6.8.
    ipiPtr[] – an array of zero or one IPI_DescrPointer as specified in 7.2.6.12.
    ipIDS[] – an array of zero or more IP_IdentificationDataSet as specified in 7.2.6.9.
              Each ES_Descriptor shall have either one IPI_DescrPointer or zero up to 255
              IP_IdentificationDataSet elements. This allows to unambiguously associate
              an IP Identification to each elementary stream.
    ipmpDescrPtr[] – an array of IPMP_DescriptorPointer, as defined in 7.2.6.13, that
                     points to the IPMP_Descriptors related to the elementary stream
                     described by this ES_Descriptor. The array shall have any number
                     of zero up to 255 elements.
    langDescr[] – an array of zero or one LanguageDescriptor structures as specified
                  in 7.2.6.18.6. It indicates the language attributed to this elementary
                  stream.
    NOTE — Multichannel audio streams may be treated as one elementary stream with one
           ES_Descriptor by ISO/IEC 14496. In that case different languages present
           in different channels of the multichannel stream are not identifyable with
           a LanguageDescriptor.
    qosDescr[] – an array of zero or one QoS_Descriptor as specified in 7.2.6.15.
    extDescr[] – an array of ExtensionDescriptor structures as specified in 7.2.6.16.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_ES_DescrTag,
                 odprof_levelindic=OdProfLevelIndic_ReservedISONoSLExtension):
        BaseDescriptor.__init__(self, offset, descr_tag)
        self.ES_ID = 0
        self.strmDependceFlag = 0
        self.urlFlag = 0
        self.OCRStrmFlag = 0
        self.strmPriority = 0
        self.dependsOn_ES_ID = 0  # if strmDependceFlag
        self.urlLen = 0  # if urlFlag
        self.url = ''  # if urlFlag
        self.OCR_ES_ID = 0  # if OCRStrmFlag
        self.decConfigDescr = None
        self.slCfgDescr = None  # if (ODProfileLevelIndication==0x01)
        self.ipiPtr = []
        self.ipIDS = []
        self.ipmpDescrPtr = []
        self.langDescr = []
        self.qosDescr = []
        self.regDescr = []
        self.extDescr = []

        self.odProfLevelIndic = odprof_levelindic

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
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        strm_pos = file_strm.tell()

        file_strm = super(ESDescriptor, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        self.ES_ID = file_strm.read_int16()
        self.offset += UInt16ByteLen

        tmp_byte = file_strm.read_int8()
        self.strmDependceFlag = tmp_byte >> 7
        self.urlFlag = (tmp_byte >> 6) & 0x01
        self.OCRStrmFlag = (tmp_byte >> 5) & 0x01
        self.strmPriority = tmp_byte & 0x1F
        self.offset += UInt8ByteLen

        if self.strmDependceFlag != 0:
            self.dependsOn_ES_ID = file_strm.read_int16()
            self.offset += UInt16ByteLen
        if self.urlFlag != 0:
            self.urlLen = file_strm.read_int8()
            self.url = file_strm.read_byte(self.urlLen)
            self.offset += UInt8ByteLen + self.urlLen
        if self.OCRStrmFlag != 0:
            self.OCR_ES_ID = file_strm.read_int16()
            self.offset += UInt16ByteLen

        tmpDecCfgDescr = DecoderConfigDescriptor(self.offset)
        file_strm = tmpDecCfgDescr.decode(file_strm)
        if file_strm is None:
            return file_strm
        self.decConfigDescr = tmpDecCfgDescr
        self.offset += self.decConfigDescr.size()

        tmpSLCfgDescr = None
        if self.odProfLevelIndic == OdProfLevelIndic_ReservedISONoSLExtension:
            tmpSLCfgDescr = SLConfigDescriptor(self.offset)
        else:
            tmpSLCfgDescr = ExtendedSLConfigDescriptor(self.offset)
        file_strm = tmpSLCfgDescr.decode(file_strm)
        if file_strm is None:
            return file_strm
        self.slCfgDescr = tmpSLCfgDescr
        self.offset += self.slCfgDescr.size()

        left_size = self.size() - (self.offset - self.descr_offset)
        while left_size > 0:
            tmp_descr = BaseDescriptor(self.offset)
            if tmp_descr.peek(file_strm) is None:
                return file_strm
            tmp_descr = create_descr(self.offset, tmp_descr.descr_tag)
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
        if DescrTag_IPI_DescrPointerTag == tmp_descr.descr_tag:
            self.ipiPtr.append(descr)
        elif DescrTag_ContentIdentDescrTag == tmp_descr.descr_tag:
            self.ipIDS.append(descr)
        elif DescrTag_SupplContentIdentDescrTag == tmp_descr.descr_tag:
            self.ipIDS.append(descr)
        elif DescrTag_IPMP_DescrPointerTag == tmp_descr.descr_tag:
            self.ipmpDescrPtr.append(descr)
        elif DescrTag_LanguageDescrTag == tmp_descr.descr_tag:
            self.langDescr.append(descr)
        elif DescrTag_QoS_DescrTag == tmp_descr.descr_tag:
            self.qosDescr.append(descr)
        elif DescrTag_RegistrationDescrTag == tmp_descr.descr_tag:
            self.regDescr.append(descr)
        elif DescrTag_ExtensionProfileLevelDescrTag == tmp_descr.descr_tag:
            self.extDescr.append(descr)

    def size(self):
        return super(ESDescriptor, self).size()

    def dump(self):
        dump_info = super(ESDescriptor, self).dump()
        return dump_info

    def __str__(self):
        log_str = super(ESDescriptor, self).__str__()
        return log_str
