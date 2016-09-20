#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '2016-09-13 上午11:04'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# from bitstream import BitStream
from aot import *
from audio_channel import AudioChannel
from sample_rate import SampleRate


# from descr import (decspecinfo, descrtagdef)


class GASpecificConfig(object):
    """
    + -----------------------------------------------------------------------------------------
    +                         Table 4.1 – Syntax of GASpecificConfig()
    + -----------------------------------------------------------------------------------------
    + Syntax                                                          No. of bits     Mnemonic
    + -----------------------------------------------------------------------------------------
    + GASpecificConfig (samplingFrequencyIndex,
    +                   channelConfiguration, audioObjectType)
    + {
    +     frameLengthFlag;                                              1               bslbf
    +     dependsOnCoreCoder;                                           1               bslbf
    +     if (dependsOnCoreCoder) {
    +         coreCoderDelay;                                           14              uimsbf
    +     }
    +     extensionFlag;                                                1               bslbf
    +     if (! channelConfiguration) {
    +         program_config_element ();
    +     }
    +     if ((audioObjectType == 6) || (audioObjectType == 20)) {
    +         layerNr;                                                  3               uimsbf
    +     }
    +     if (extensionFlag) {
    +         if (audioObjectType == 22) {
    +             numOfSubFrame;                                        5               bslbf
    +             layer_length;                                         11              bslbf
    +         }
    +         if (audioObjectType == 17 || audioObjectType == 19 ||
    +         audioObjectType == 20 || audioObjectType == 23) {
    +             aacSectionDataResilienceFlag;                         1               bslbf
    +             aacScalefactorDataResilienceFlag;                     1               bslbf
    +             aacSpectralDataResilienceFlag;                        1               bslbf
    +         }
    +         extensionFlag3;                                           1               bslbf
    +         if (extensionFlag3) {
    +             /* tbd in version 3 */
    +         }
    +     }
    + }
    + -----------------------------------------------------------------------------------------
    """

    def __init__(self):
        self.frameLengthFlag = 0
        self.dependsOnCoreCoder = 0
        self.extensionFlag = 0

    def decode(self, bit_strm):
        if bit_strm is None:
            return bit_strm
        self.frameLengthFlag = bit_strm.read(1).int
        self.dependsOnCoreCoder = bit_strm.read(1).int
        self.extensionFlag = bit_strm.read(1).int
        return bit_strm

    def dump(self):
        dump_info = dict()
        dump_info['frameLengthFlag'] = str(self.frameLengthFlag)
        dump_info['dependsOnCoreCoder'] = str(self.dependsOnCoreCoder)
        dump_info['extensionFlag'] = str(self.extensionFlag)
        return dump_info

    def __str__(self):
        logstr = "\n\t\t\t\t\t\t\t\t\t\t\tframeLengthFlag = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\t\tdependsOnCoreCoder = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\t\textensionFlag = %08ld(0x%016lx)" % \
                 (self.frameLengthFlag, self.frameLengthFlag, self.dependsOnCoreCoder,
                  self.dependsOnCoreCoder, self.extensionFlag, self.extensionFlag)
        return logstr


class AudioSpecificConfig(object):
    """
    AudioSpecificConfig() extends the abstract class DecoderSpecificInfo, as defined in ISO/IEC 14496-1, when
    DecoderConfigDescriptor.objectTypeIndication refers to streams complying with ISO/IEC 14496-3. In this case the
    existence of AudioSpecificConfig() is mandatory.
    ---------------------------------------------------------------------------------------------------
                            Table 1.15 – Syntax of AudioSpecificConfig()
    ---------------------------------------------------------------------------------------------------
    Syntax                                                                  No. of bits     Mnemonic
    ---------------------------------------------------------------------------------------------------
    AudioSpecificConfig ()
    {
        audioObjectType = GetAudioObjectType();
        samplingFrequencyIndex;                                             4               bslbf
        if ( samplingFrequencyIndex == 0xf ) {
            samplingFrequency;                                              24              uimsbf
        }
        channelConfiguration;                                               4               bslbf
        sbrPresentFlag = -1;
        psPresentFlag = -1;
        if ( audioObjectType == 5 ||
        audioObjectType == 29 ) {
        extensionAudioObjectType = 5;
        sbrPresentFlag = 1;
        if ( audioObjectType == 29 ) {
            psPresentFlag = 1;
        }
        extensionSamplingFrequencyIndex;                                    4               uimsbf
        if ( extensionSamplingFrequencyIndex == 0xf )
            extensionSamplingFrequency;                                     24              uimsbf
        audioObjectType = GetAudioObjectType();
        if ( audioObjectType == 22 )
            extensionChannelConfiguration;                                  4               uimsbf
        }
        else {
            extensionAudioObjectType = 0;
        }
        switch (audioObjectType) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 6:
            case 7:
            case 17:
            case 19:
            case 20:
            case 21:
            case 22:
            case 23:
                GASpecificConfig();
                break:
            case 8:
                CelpSpecificConfig();
                break;
            case 9:
                HvxcSpecificConfig();
                break:
            case 12:
                TTSSpecificConfig();
                break;
            case 13:
            case 14:
            case 15:
            case 16:
                StructuredAudioSpecificConfig();
                break;
            case 24:
                ErrorResilientCelpSpecificConfig();
                break;
            case 25:
                ErrorResilientHvxcSpecificConfig();
                break;
            case 26:
            case 27:
                ParametricSpecificConfig();
                break;
            case 28:
                SSCSpecificConfig();
                break;
            case 30:
                sacPayloadEmbedding;                                        1               uimsbf
                SpatialSpecificConfig();
                break;
            case 32:
            case 33:
            case 34:
                MPEG_1_2_SpecificConfig();
                break;
            case 35:
                DSTSpecificConfig();
                break;
            case 36:
                fillBits;                                                   5               bslbf
                ALSSpecificConfig();
                break;
            case 37:
            case 38:
                SLSSpecificConfig();
                break;
            case 39:
                ELDSpecificConfig(channelConfiguration);
                break:
            case 40:
            case 41:
                SymbolicMusicSpecificConfig();
                break;
            default:
                /* reserved */
        }
        switch (audioObjectType) {
            case 17:
            case 19:
            case 20:
            case 21:
            case 22:
            case 23:
            case 24:
            case 25:
            case 26:
            case 27:
            case 39:
                epConfig;                                                   2               bslbf
                if ( epConfig == 2 || epConfig == 3 ) {
                    ErrorProtectionSpecificConfig();
                }
                if ( epConfig == 3 ) {
                    directMapping;                                          1               bslbf
                    if ( ! directMapping ) {
                        /* tbd */
                    }
                }
        }
        if ( extensionAudioObjectType != 5 && bits_to_decode() >= 16 ) {
            syncExtensionType;                                              11              bslbf
            if (syncExtensionType == 0x2b7) {
                extensionAudioObjectType = GetAudioObjectType();
                if ( extensionAudioObjectType == 5 ) {
                    sbrPresentFlag;                                         1               uimsbf
                    if (sbrPresentFlag == 1) {
                        extensionSamplingFrequencyIndex;                    4               uimsbf
                        if ( extensionSamplingFrequencyIndex == 0xf ) {
                            extensionSamplingFrequency;                     24              uimsbf
                        }
                        if ( bits_to_decode() >= 12 ) {
                            syncExtensionType;                              11              bslbf
                            if (syncExtesionType == 0x548) {
                                psPresentFlag;                              1               uimsbf
                            }
                        }
                    }
                }
                if ( extensionAudioObjectType == 22 ) {
                    sbrPresentFlag;                                         1               uimsbf
                    if (sbrPresentFlag == 1) {
                        extensionSamplingFrequencyIndex;                    4               uimsbf
                        if ( extensionSamplingFrequencyIndex == 0xf ) {
                            extensionSamplingFrequency;                     24              uimsbf
                        }
                    }
                    extensionChannelConfiguration;                          4               uimsbf
                }
            }
        }
    }

    ---------------------------------------------------------------------------------------------------
                        Table 1.16 – Syntax of GetAudioObjectType()
    ---------------------------------------------------------------------------------------------------
    Syntax                                                                  No. of bits     Mnemonic
    ---------------------------------------------------------------------------------------------------
    GetAudioObjectType()
    {
        audioObjectType;                                                    5               uimsbf
        if (audioObjectType == 31) {
            audioObjectType = 32 + audioObjectTypeExt;                      6               uimsbf
        }
        return audioObjectType;
    }
    ---------------------------------------------------------------------------------------------------
    The classes defined in subclauses 1.6.2.1.1 to 1.6.2.1.9 do not extend the BaseDescriptor class (see ISO/IEC
    14496-1) and consequently their length shall be derived by difference from the length of AudioSpecificConfig()
    """

    @staticmethod
    def GetAudioObjectType(bit_strm):
        """
        a snipplet from ffmpeg:

        static inline int get_object_type(GetBitContext *gb)
        {
            int object_type = get_bits(gb, 5);
            if (object_type == AOT_ESCAPE)
                object_type = 32 + get_bits(gb, 6);
            return object_type;
        }
        :param bit_strm:
        :return:
        """
        if bit_strm is None:
            return AOT_NULL, bit_strm

        aot = bit_strm.read(5).int
        if aot == AOT_Escape:
            aot_ext = bit_strm.read(6).int
            aot = 32 + aot_ext
        return aot, bit_strm

    @staticmethod
    def GetSampleRate(bit_strm):
        """
        a snipplet from ffmpeg:

        static inline int get_sample_rate(GetBitContext *gb, int *index)
        {
            *index = get_bits(gb, 4);
            return *index == 0x0f ? get_bits(gb, 24) :
                avpriv_mpeg4audio_sample_rates[*index];
        }
        :param bit_strm:
        :return:
        """
        if bit_strm is None:
            return 0, 0, bit_strm

        sample_rate = 0
        index = bit_strm.read(4).int
        if 0x0f == index:
            sampling_frequency = bit_strm.read(32).uint
            sample_rate = sampling_frequency
        else:
            sample_rate = SampleRate[index]

        return index, sample_rate, bit_strm

    def __init__(self, offset=0):
        """
        a snipplet from ffmpeg

        typedef struct MPEG4AudioConfig {
            int object_type;
            int sampling_index;
            int sample_rate;
            int chan_config;
            int sbr; ///< -1 implicit, 1 presence
            int ext_object_type;
            int ext_sampling_index;
            int ext_sample_rate;
            int ext_chan_config;
            int channels;
            int ps;  ///< -1 implicit, 1 presence
            int frame_length_short;
        } MPEG4AudioConfig;
        """
        self.offset = offset

        self.object_type = 0
        self.sampling_index = 0
        self.sample_rate = 0
        self.chan_config = 0
        self.channels = 0
        self.sbr = 0
        self.ps = 0
        self.ga_spec_conf = None
        self.ext_object_type = 0
        self.ext_sampling_index = 0
        self.ext_sample_rate = 0
        self.ext_chan_config = 0
        self.frame_length_short = 0

    def decode(self, bit_strm):
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
        if bit_strm is None:
            return bit_strm

        self.object_type, bit_strm = AudioSpecificConfig.GetAudioObjectType(bit_strm)
        self.sampling_index, self.sample_rate, bit_strm = \
            AudioSpecificConfig.GetSampleRate(bit_strm)
        self.chan_config = bit_strm.read(4).int
        if self.chan_config < len(AudioChannel):
            self.channels = AudioChannel[self.chan_config]
        self.ps = -1
        self.sbr = -1

        # switch (audioObjectType) {
        #     case 1:
        #     case 2:
        #     case 3:
        #     case 4:
        #     case 6:
        #     case 7:
        #     case 17:
        #     case 19:
        #     case 20:
        #     case 21:
        #     case 22:
        #     case 23:
        #         GASpecificConfig();
        #         break:
        # }
        gaspecaot = (AOT_AAC_MAIN, AOT_AAC_LC, AOT_AAC_SSR, AOT_AAC_LTP,
                     AOT_AAC_Scalable, AOT_TwinVQ, AOT_ER_AAC_LC,
                     AOT_ER_AAC_LTP, AOT_ER_AAC_Scalable, AOT_ER_Twin_VQ,
                     AOT_ER_BSAC, AOT_ER_AAC_LD)
        if self.object_type not in gaspecaot:
            return

        self.ga_spec_conf = GASpecificConfig()
        bit_strm = self.ga_spec_conf.decode(bit_strm)

        # self.ext_object_type = 0
        # self.ext_sampling_index = 0
        # self.ext_sample_rate = 0
        # self.ext_chan_config = 0
        # self.frame_length_short = 0

        return bit_strm

    def dump(self):
        dump_info = dict()
        dump_info['offset'] = str(self.offset)
        dump_info['object_type'] = str(self.object_type)
        dump_info['sampling_index'] = str(self.sampling_index)
        dump_info['sample_rate'] = str(self.sample_rate)
        dump_info['chan_config'] = str(self.chan_config)
        dump_info['channels'] = str(self.channels)
        dump_info['sbr'] = str(self.sbr)
        dump_info['ps'] = str(self.ps)
        if self.ga_spec_conf is not None:
            dump_info['ga_spec_conf'] = self.ga_spec_conf.dump()
        dump_info['ext_object_type'] = str(self.ext_object_type)
        dump_info['ext_sampling_index'] = str(self.ext_sampling_index)
        dump_info['ext_sample_rate'] = str(self.ext_sample_rate)
        dump_info['ext_chan_config'] = str(self.ext_chan_config)
        dump_info['frame_length_short'] = str(self.frame_length_short)
        return dump_info

    def __str__(self):
        logstr = "\n\t\t\t\t\t\t\t\t\t\toffset = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tobject_type = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tsampling_index = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tsample_rate = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tchan_config = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tchannels = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tsbr = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tps = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tga_spec_conf = %s" \
                 "\n\t\t\t\t\t\t\t\t\t\text_object_type = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\text_sampling_index = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\text_sample_rate = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\text_chan_config = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tframe_length_short = %08ld(0x%016lx)" \
                 % (self.offset, self.offset, self.object_type, self.object_type,
                    self.sampling_index, self.sampling_index, self.sample_rate,
                    self.sample_rate, self.chan_config, self.chan_config, self.channels,
                    self.channels, self.sbr, self.sbr, self.ps, self.ps, self.ga_spec_conf,
                    self.ext_object_type, self.ext_object_type, self.ext_sampling_index,
                    self.ext_sampling_index, self.ext_sample_rate, self.ext_sample_rate,
                    self.ext_chan_config, self.ext_chan_config, self.frame_length_short,
                    self.frame_length_short)
        return logstr
