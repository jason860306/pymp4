#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 16:21:48'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class DecoderSpecificInfo(BaseDescriptor, object):
    """
    7.2.6.7.1 Syntax
    abstract class DecoderSpecificInfo extends BaseDescriptor
        : bit(8) tag=DecSpecificInfoTag
    {
        // empty. To be filled by classes extending this class.
    }
    7.2.6.7.2 Semantics
    The decoder specific information constitutes an opaque container with
    information for a specific media decoder. The existence and semantics
    of decoder specific information depends on the values of
    DecoderConfigDescriptor.streamType and DecoderConfigDescriptor.objectTypeIndication.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to
    streams complying with ISO/IEC 14496-2 the syntax and semantics of decoder
    specific information are defined in Annex K of that part.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to
    streams complying with ISO/IEC 14496-3 the syntax and semantics of decoder
    specific information are defined in subpart 1, subclause 1.6 of that part.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to scene
    description streams the semantics of decoder specific information is defined
    in ISO/IEC 14496-11.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to streams
    complying with ISO/IEC 13818-7 the decoder specific information consists of
    an „adif_header()“ and an access unit is a „raw_data_block()“ as defined in
    ISO/IEC 13818-7.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to streams
    complying with ISO/IEC 11172-3 or ISO/IEC 13818-3 the decoder specific information
    is empty since all necessary data is contained in the bitstream frames itself.
    The access units in this case are the „frame()“ bitstream element as is defined
    in ISO/IEC 11172-3
    """

    def __init__(self, offset=0, descr_tag=DescrTag_DecSpecificInfoTag):
        super(DecoderSpecificInfo, self).__init__(offset, descr_tag)

        self.opaque_data = ''

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

        file_strm = super(DecoderSpecificInfo, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm
        self.opaque_data = file_strm.read_byte(self.size())
        self.offset += self.size()

        return file_strm

    def size(self):
        return super(DecoderSpecificInfo, self).size()

    def dump(self):
        dump_info = super(DecoderSpecificInfo, self).dump()
        return dump_info

    def __str__(self):
        log_str = super(DecoderSpecificInfo, self).__str__()
        return log_str
