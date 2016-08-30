#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-06 17:11:16'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# Table 13 — Overview of predefined SLConfigDescriptor values
# ------------------------------------------------------------
# Predefined field value | Description
# ------------------------------------------------------------
# 0x00                   | Custom
# 0x01                   | null SL packet header
# 0x02                   | Reserved for use in MP4 files
# 0x03 – 0xFF            | Reserved for ISO use
# ------------------------------------------------------------

SLCfgDescrPredef_Custom = 0x00
SLCfgDescrPredef_NULL_SLPktHdr = 0x01
SLCfgDescrPredef_MP4Reserved = 0x02
SLCfgDescrPredef_ISOReserved03 = 0x03
SLCfgDescrPredef_ISOReservedFF = 0xFF

# Table 14 — Detailed predefined SLConfigDescriptor values
# ------------------------------------------------------------
# Predefined field value    | 0x01 | 0x02
# ------------------------------------------------------------
# UseAccessUnitStartFlag    | 0    | 0
# UseAccessUnitEndFlag      | 0    | 0
# UseRandomAccessPointFlag  | 0    | 0
# UsePaddingFlag            | 0    | 0
# UseTimeStampsFlag         | 0    | 1
# UseIdleFlag               | 0    | 0
# DurationFlag              | 0    | 0
# TimeStampResolution       | 1000 | -
# OCRResolution             | -    | -
# TimeStampLength           | 32   | 0
# OCRlength                 | -    | 0
# AU_length                 | 0    | 0
# InstantBitrateLength      | -    | 0
# DegradationPriorityLength | 0    | 0
# AU_seqNumLength           | 0    | 0
# PacketSeqNumLength        | 0    | 0
# ------------------------------------------------------------
