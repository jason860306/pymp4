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


from bitstring import (BitArray, ConstBitStream, BitStream)

from asc import AudioSpecificConfig


class Adts(object):
    """
    ---------------------------------------------------------------------------------------------------
    6.2 Audio Data Transport Stream, ADTS

    ---------------------------------------------------------------------------------------------------
    Table 4 — Syntax of adts_sequence()
    ---------------------------------------------------------------------------------------------------
    Syntax                                                                  No. of bits     Mnemonic
    ---------------------------------------------------------------------------------------------------
    adts_sequence()
    {
        while (nextbits() == syncword) {
            adts_frame();
        }
    }

    ---------------------------------------------------------------------------------------------------
    Table 5 — Syntax of adts_frame()
    ---------------------------------------------------------------------------------------------------
    Syntax                                                                  No. of bits     Mnemonic
    ---------------------------------------------------------------------------------------------------
    adts_frame()
    {
        adts_fixed_header();
        adts_variable_header();
        if (number_of_raw_data_blocks_in_frame == 0) {
            adts_error_check();
            raw_data_block();
        }
        else {
            adts_header_error_check();
            for (i = 0; i <= number_of_raw_data_blocks_in_frame;
                i++) {
                raw_data_block();
                adts_raw_data_block_error_check();
            }
        }
    }

    ---------------------------------------------------------------------------------------------------
    Table 6 — Syntax of adts_header_error_check()
    ---------------------------------------------------------------------------------------------------
    Syntax                                                                  No. of bits     Mnemonic
    ---------------------------------------------------------------------------------------------------
    adts_header_error_check ()
    {
        if (protection_absent == ‘0’) {
            for (i = 1; i <= number_of_raw_data_blocks_in_frame; i++) {
                raw_data_block_position[i];                                 16              uimsfb
            }
            crc_check;                                                      16              rpchof
        }
    }

    ---------------------------------------------------------------------------------------------------
    Table 7 — Syntax of adts_raw_data_block_error_check()
    ---------------------------------------------------------------------------------------------------
    Syntax                                                                  No. of bits     Mnemonic
    ---------------------------------------------------------------------------------------------------
    adts_raw_data_block_error_check()
    {
        if (protection_absent == ‘0’)
            crc_check;                                                      16              rpchof
    }

    ---------------------------------------------------------------------------------------------------
    6.2.1 Fixed Header of ADTS

    ---------------------------------------------------------------------------------------------------
    Table 8 — Syntax of adts_fixed_header()
    ---------------------------------------------------------------------------------------------------
    Syntax                                                                  No. of bits     Mnemonic
    ---------------------------------------------------------------------------------------------------
    adts_fixed_header()
    {
        syncword;                                                           12              bslbf
        ID;                                                                 1               bslbf
        layer;                                                              2               uimsbf
        protection_absent;                                                  1               bslbf
        profile;                                                            2               uimsbf
        sampling_index;                                                     4               uimsbf
        private_bit;                                                        1               bslbf
        chan_config;                                                        3               uimsbf
        original_copy;                                                      1               bslbf
        home;                                                               1               bslbf
    }

    ---------------------------------------------------------------------------------------------------
    6.2.2 Variable Header of ADTS

    ---------------------------------------------------------------------------------------------------
    Table 9 — Syntax of adts_variable_header()
    ---------------------------------------------------------------------------------------------------
    Syntax                                                                  No. of bits     Mnemonic
    ---------------------------------------------------------------------------------------------------
    adts_variable_header()
    {
        copyright_id_bit;                                                   1               bslbf
        copyright_id_start;                                                 1               bslbf
        aac_frame_length;                                                   13              bslbf
        adts_buffer_fullness;                                               11              bslbf
        number_of_raw_data_blocks_in_frame;                                 2               uimsfb
    }

    ---------------------------------------------------------------------------------------------------
    6.2.3 Error Detection

    ---------------------------------------------------------------------------------------------------
    Table 10 — Syntax of adts_error_check()
    ---------------------------------------------------------------------------------------------------
    Syntax                                                                  No. of bits     Mnemonic
    ---------------------------------------------------------------------------------------------------
    adts_error_check()
    {
        if (protection_absent == ‘0’)
            crc_check;                                                      16              rpchof
    }
    ---------------------------------------------------------------------------------------------------
    """

    ADTS_SYNC_WORD = 0xFFF
    ADTS_HEADER_SIZE = \
        (
            # adts_fixed_header()
            12  # syncword                            12 bit
            + 1  # ID                                  1  bit
            + 2  # layer                               2  bit
            + 1  # protection_absent                   1  bit
            + 2  # profile                             2  bit
            + 4  # sampling_index                      4  bit
            + 1  # private_bit                         1  bit
            + 3  # chan_config                         3  bit
            + 1  # original_copy                       1  bit
            + 1  # home                                1  bit
            # adts_variable_header()
            + 1  # copyright_id_bit                    1  bit
            + 1  # copyright_id_start                  1  bit
            + 13  # aac_frame_length                    13 bit
            + 11  # adts_buffer_fullness                11 bit
            + 2  # number_of_raw_data_blocks_in_frame  2  bit
        ) / 8
    ADTS_FULLNESS_FLAG = 0x7FF

    @staticmethod
    def asc2adts(asc_data, raw_data_len):
        if asc_data is None or raw_data_len == 0:
            return None

        asc = None
        if isinstance(asc_data, AudioSpecificConfig):
            asc = asc_data
        elif isinstance(asc_data, basestring):
            bit_strm = ConstBitStream(bytes=asc_data)
            asc = AudioSpecificConfig()
            bit_strm = asc.decode(bit_strm)
            if bit_strm is None:
                return None
        elif isinstance(asc_data, ConstBitStream):
            bit_strm = asc_data
            asc = AudioSpecificConfig()
            bit_strm = asc.decode(bit_strm)
            if bit_strm is None:
                return None
        else:
            return None

        adts = Adts()
        adts.ID = 0
        adts.layer = 0
        adts.protection_absent = 0
        adts.profile = 1
        adts.sampling_index = asc.sampling_index
        adts.private_bit = 0
        adts.chan_config = asc.chan_config
        adts.original_copy = 0
        adts.home = 0
        adts.copyright_id_bit = 0
        adts.copyright_id_start = 0
        adts.aac_frame_length = Adts.ADTS_HEADER_SIZE + raw_data_len
        adts.adts_buffer_fullness = Adts.ADTS_FULLNESS_FLAG
        adts.number_of_raw_data_blocks_in_frame = 0
        return adts

    def __init__(self):
        """
        """

        # adts_fixed_header()
        # {
        #     syncword;                 12 bslbf
        #     ID;                       1  bslbf
        #     layer;                    2  uimsbf
        #     protection_absent;        1  bslbf
        #     profile;                  2  uimsbf
        #     sampling_index;           4  uimsbf
        #     private_bit;              1  bslbf
        #     chan_config;              3  uimsbf
        #     original_copy;            1  bslbf
        #     home;                     1  bslbf
        # }
        self.syncword = Adts.ADTS_SYNC_WORD
        self.ID = 0
        self.layer = 0
        self.protection_absent = 0
        self.profile = 0
        self.sampling_index = 0
        self.private_bit = 0
        self.chan_config = 0
        self.original_copy = 0
        self.home = 0

        # adts_variable_header()
        # {
        #     copyright_id_bit;                   1  bslbf
        #     copyright_id_start;                 1  bslbf
        #     aac_frame_length;                   13 bslbf
        #     adts_buffer_fullness;               11 bslbf
        #     number_of_raw_data_blocks_in_frame; 2  uimsfb
        # }
        self.copyright_id_bit = 0
        self.copyright_id_start = 0
        self.aac_frame_length = 0
        self.adts_buffer_fullness = 0
        self.number_of_raw_data_blocks_in_frame = 0

    def encode(self, bit_strm=None, offset=0):
        if bit_strm is None:
            bit_strm = BitStream()

        if not isinstance(bit_strm, BitStream):
            return None

        bit_strm.append(BitArray(uint=self.syncword, length=12))
        bit_strm.append(BitArray(int=self.ID, length=1))
        bit_strm.append(BitArray(int=self.layer, length=2))
        bit_strm.append(BitArray(int=self.protection_absent, length=1))
        bit_strm.append(BitArray(int=self.profile, length=2))
        bit_strm.append(BitArray(int=self.sampling_index, length=4))
        bit_strm.append(BitArray(int=self.private_bit, length=1))
        bit_strm.append(BitArray(int=self.chan_config, length=3))
        bit_strm.append(BitArray(int=self.original_copy, length=1))
        bit_strm.append(BitArray(int=self.home, length=1))
        bit_strm.append(BitArray(int=self.copyright_id_bit, length=1))
        bit_strm.append(BitArray(int=self.copyright_id_start, length=1))
        bit_strm.append(BitArray(uint=self.aac_frame_length, length=13))
        bit_strm.append(BitArray(uint=self.adts_buffer_fullness, length=11))
        bit_strm.append(BitArray(int=self.number_of_raw_data_blocks_in_frame, length=2))
        bit_strm.byteswap()

        return bit_strm

    def dump(self):
        dump_info = dict()
        dump_info['syncword'] = str(self.syncword)
        dump_info['ID'] = str(self.ID)
        dump_info['layer'] = str(self.layer)
        dump_info['protection_absent'] = str(self.protection_absent)
        dump_info['profile'] = str(self.profile)
        dump_info['sampling_index'] = str(self.sampling_index)
        dump_info['private_bit'] = str(self.private_bit)
        dump_info['chan_config'] = str(self.chan_config)
        dump_info['original_copy'] = str(self.original_copy)
        dump_info['home'] = str(self.home)
        dump_info['copyright_id_bit'] = str(self.copyright_id_bit)
        dump_info['copyright_id_start'] = str(self.copyright_id_start)
        dump_info['aac_frame_length'] = str(self.aac_frame_length)
        dump_info['adts_buffer_fullness'] = str(self.adts_buffer_fullness)
        dump_info['number_of_raw_data_blocks_in_frame'] = str(self.number_of_raw_data_blocks_in_frame)
        return dump_info

    def __str__(self):
        logstr = "\n\t\t\t\t\t\t\t\t\t\tsyncword = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tID = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tlayer = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tprotection_absent = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tprofile = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tsampling_index = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tprivate_bit = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tchan_config = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\toriginal_copy = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\thome = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tcopyright_id_bit = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tcopyright_id_start = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\taac_frame_length = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tadts_buffer_fullness = %08ld(0x%016lx)" \
                 "\n\t\t\t\t\t\t\t\t\t\tnumber_of_raw_data_blocks_in_frame = %08ld(0x%016lx)" \
                 % (self.syncword, self.syncword, self.ID, self.ID,
                    self.layer, self.layer, self.protection_absent,
                    self.protection_absent, self.profile, self.profile, self.sampling_index,
                    self.sampling_index, self.private_bit, self.private_bit, self.chan_config,
                    self.chan_config, self.original_copy, self.original_copy,
                    self.home, self.home, self.copyright_id_bit,
                    self.copyright_id_bit, self.copyright_id_start, self.copyright_id_start,
                    self.aac_frame_length, self.aac_frame_length, self.adts_buffer_fullness,
                    self.adts_buffer_fullness, self.number_of_raw_data_blocks_in_frame,
                    self.number_of_raw_data_blocks_in_frame)
        return logstr
