#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 16:48:59'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# Table 12 — TextProfileLevelIndication Values
# -----------------------------------------------------------
# Value     | Profile                               | Level
# -----------------------------------------------------------
# 0x00      | Reserved for ISO use                  | -
# 0x01      | Simple Text profile                   | L1
# 0x02      | Simple Text profile                   | L2
# 0x03      | Simple Text profile                   | L3
# 0x04      | Advanced Simple Text profile          | L1
# 0x05      | Advanced Simple Text profile          | L2
# 0x06      | Advanced Simple Text profile          | L3
# 0x07      | Main Text profile                     | L1
# 0x08      | Main Text profile                     | L2
# 0x09      | Main Text profile                     | L3
# 0x0A-0x7F | reserved for ISO use                  | -
# 0x80-0xFD | user private                          | -
# 0xFE      | no Text profile specified             | -
# 0xFF      | no text rendering capability required | -
# -----------------------------------------------------------
# Note: Usage of the value 0xFE may indicate that the
# content described by this descriptor does not comply
# to any conformance point specified in ISO/IEC 14496-18.

TPLI_ISOReserved00 = 0x00
TPLI_SimpleTextProfileL1 = 0x01
TPLI_SimpleTextProfileL2 = 0x02
TPLI_SimpleTextProfileL3 = 0x03
TPLI_AdvancedSimpleTextProfileL1 = 0x04
TPLI_AdvancedSimpleTextProfileL2 = 0x05
TPLI_AdvancedSimpleTextProfileL3 = 0x06
TPLI_MainTextProfileL1 = 0x07
TPLI_MainTextProfileL2 = 0x08
TPLI_MainTextProfileL3 = 0x09
TPLI_ISOReserved0A = 0x0A
TPLI_ISOReserved7F = 0x7F
TPLI_UserPrivate80 = 0x80
TPLI_UserPrivateFD = 0xFD
TPLI_NoTextProfileSpecified = 0xFE
TPLI_NoTextRenderingCapabilityRequired = 0xFF
