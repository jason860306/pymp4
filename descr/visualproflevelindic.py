#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 18:44:56'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# Table 4 — visualProfileLevelIndication Values
# -----------------------------------------------------------
# Value     | Profile                                | Level
# -----------------------------------------------------------
# 0x00-0x7E | defined in ISO/IEC 14496-2 Annex G     | -
# 0x7F      | ISO/IEC 14496-10 Advanced Video Coding | -
# 0x80-0xFD | defined in ISO/IEC 14496-2 Annex G     | -
# 0xFE      | no visual profile specified            | -
# 0xFF      | no visual capability required          |
# -----------------------------------------------------------
#
# NOTE 1 Usage of the value 0x7F indicates the use of any profile
# and level of ISO/IEC 14496-10 AVC. For the real profile and
# level numbers for ISO/IEC 14496-10 refer to the DecoderSpecificInfo.
#
# NOTE 2 Usage of the value 0xFE indicates that the content described
# by this InitialObjectDescriptor does not comply to any visual profile
# specified in ISO/IEC 14496-2 or -10. Usage of the value 0xFF indicates
# that none of the visual profile capabilities are required for this content.

VPLI_14496_2_Annex_G_00 = 0x00
VPLI_14496_2_Annex_G_7E = 0x7E
VPLI_14496_10_AVC = 0x7F
VPLI_14496_2_Annex_G_80 = 0x80
VPLI_14496_2_Annex_G_FD = 0xFD
VPLI_NoVisualProfileSpecified = 0xFE
VPLI_NoVisualCapabilityRequired = 0xFF
